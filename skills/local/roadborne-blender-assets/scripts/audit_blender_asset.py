#!/usr/bin/env python3
"""Audit the open Blender scene and emit a machine-readable JSON report.

Run with Blender, not the system Python:
  blender --background asset.blend --python audit_blender_asset.py -- --output report.json

Triangle and topology counts use dependency-graph evaluated meshes, so modifiers and Geometry
Nodes are included. The report is a mechanical audit, not Godot import or visual acceptance.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path

import bpy
import bmesh


def script_args() -> list[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write JSON to this path; stdout when omitted")
    parser.add_argument("--max-triangles", type=int, default=None)
    parser.add_argument("--require-uv", action="store_true")
    parser.add_argument("--require-applied-scale", action="store_true")
    parser.add_argument("--fail-on-warnings", action="store_true")
    return parser.parse_args(script_args())


def rounded(values) -> list[float]:
    return [round(float(value), 6) for value in values]


def source_triangle_count(mesh: bpy.types.Mesh) -> int:
    mesh.calc_loop_triangles()
    return len(mesh.loop_triangles)


def mesh_report(obj: bpy.types.Object, depsgraph: bpy.types.Depsgraph) -> dict:
    source_mesh = obj.data
    evaluated_object = obj.evaluated_get(depsgraph)
    evaluated_mesh = evaluated_object.to_mesh()
    if evaluated_mesh is None:
        raise RuntimeError(f"{obj.name}: Blender did not produce an evaluated mesh")

    try:
        evaluated_mesh.calc_loop_triangles()
        bm = bmesh.new()
        try:
            bm.from_mesh(evaluated_mesh)
            non_manifold_edges = sum(1 for edge in bm.edges if not edge.is_manifold)
            loose_vertices = sum(1 for vertex in bm.verts if not vertex.link_edges)
        finally:
            bm.free()

        return {
            "name": obj.name,
            "evaluated": True,
            "source_triangles": source_triangle_count(source_mesh),
            "vertices": len(evaluated_mesh.vertices),
            "edges": len(evaluated_mesh.edges),
            "faces": len(evaluated_mesh.polygons),
            "triangles": len(evaluated_mesh.loop_triangles),
            "uv_layers": [layer.name for layer in evaluated_mesh.uv_layers],
            "material_slots": len(evaluated_object.material_slots),
            "dimensions": rounded(evaluated_object.dimensions),
            "location": rounded(evaluated_object.location),
            "rotation_euler": rounded(evaluated_object.rotation_euler),
            "scale": rounded(evaluated_object.scale),
            "non_manifold_edges": non_manifold_edges,
            "loose_vertices": loose_vertices,
            "modifiers": [{"name": mod.name, "type": mod.type} for mod in obj.modifiers],
        }
    finally:
        evaluated_object.to_mesh_clear()


def missing_external_files() -> list[dict[str, str]]:
    missing: list[dict[str, str]] = []
    for image in bpy.data.images:
        if not image.filepath or image.packed_file:
            continue
        resolved = bpy.path.abspath(image.filepath)
        if not os.path.exists(resolved):
            missing.append({"kind": "image", "name": image.name, "path": resolved})

    for library in bpy.data.libraries:
        if not library.filepath:
            continue
        resolved = bpy.path.abspath(library.filepath)
        if not os.path.exists(resolved):
            missing.append({"kind": "library", "name": library.name, "path": resolved})
    return missing


def main() -> int:
    args = parse_args()
    if args.max_triangles is not None and args.max_triangles < 0:
        raise ValueError("--max-triangles must be zero or greater")

    depsgraph = bpy.context.evaluated_depsgraph_get()
    meshes = [
        mesh_report(obj, depsgraph)
        for obj in bpy.context.scene.objects
        if obj.type == "MESH"
    ]
    total_triangles = sum(item["triangles"] for item in meshes)
    warnings: list[str] = []
    failures: list[str] = []

    for item in meshes:
        if item["non_manifold_edges"]:
            warnings.append(f"{item['name']}: {item['non_manifold_edges']} non-manifold edges")
        if item["loose_vertices"]:
            warnings.append(f"{item['name']}: {item['loose_vertices']} loose vertices")
        if args.require_uv and not item["uv_layers"]:
            failures.append(f"{item['name']}: missing UV map")
        if args.require_applied_scale and any(
            not math.isclose(value, 1.0, abs_tol=1e-5) for value in item["scale"]
        ):
            failures.append(f"{item['name']}: scale is not applied ({item['scale']})")

    if args.max_triangles is not None and total_triangles > args.max_triangles:
        failures.append(f"evaluated triangle budget exceeded: {total_triangles} > {args.max_triangles}")

    missing_files = missing_external_files()
    if missing_files:
        failures.append(f"{len(missing_files)} external file(s) are missing")

    armatures = [
        {"name": obj.name, "bones": len(obj.data.bones)}
        for obj in bpy.context.scene.objects
        if obj.type == "ARMATURE"
    ]

    report = {
        "schema_version": 2,
        "blender_version": bpy.app.version_string,
        "source_file": bpy.data.filepath or None,
        "scene": bpy.context.scene.name,
        "geometry_basis": "dependency_graph_evaluated",
        "units": {
            "system": bpy.context.scene.unit_settings.system,
            "scale_length": bpy.context.scene.unit_settings.scale_length,
        },
        "summary": {
            "objects": len(bpy.context.scene.objects),
            "mesh_objects": len(meshes),
            "evaluated_triangles": total_triangles,
            "materials": len(bpy.data.materials),
            "images": len(bpy.data.images),
            "armatures": len(armatures),
            "actions": len(bpy.data.actions),
        },
        "meshes": meshes,
        "armatures": armatures,
        "actions": [action.name for action in bpy.data.actions],
        "missing_files": missing_files,
        "warnings": warnings,
        "failures": failures,
        "passed": not failures and not (args.fail_on_warnings and warnings),
    }

    payload = json.dumps(report, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0 if report["passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
