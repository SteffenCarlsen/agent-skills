# Roadborne 3D concept-to-Godot pipeline

Use this reference for models, materials, textures, rigs, animations, collision, navigation, LOD,
or GLB/glTF delivery. A render proves appearance only.

## Gate before DCC work

Read outstanding_questions.md ART-Q01 through ART-Q05. ART-Q03 currently owns the Blender version,
units, axes, editable-source convention, deterministic export, collision, and navigation rules.
When it is Paused or Unresolved, concepts and source inspection may continue only within explicit
task authority; do not represent a production Blender-to-Godot export contract as selected.

Derive the active Godot SDK version from Roadborne.Client.csproj. Use the matching version of the
official Godot import documentation and test the exact installed engine. Do not hardcode 4.6 or
4.7 in an asset recipe.

## Pipeline

1. Record the owner-authorized gameplay role, camera distance, silhouette requirement, scale,
   pivot, collision role, animation need, and any selected budgets. Mark missing values Unknown.
2. Treat orthographic, turnaround, and generated images as geometric references, not meshes.
3. Preserve an editable DCC source. Inspect evaluated topology, normals, UVs, texel density,
   transforms, material slots, armature, weights, actions, external files, and licenses.
4. Give the asset a gameplay-meaningful origin. Keep render geometry, simple collision proxies,
   navigation geometry, sockets, and LODs distinct where their roles differ.
5. Use PBR inputs and color spaces the effective Godot importer supports. Read the existing
   ASSET_PROVENANCE.md before reusing Roadborne's packed ARM/ORM or material conventions.
6. Export to a new artifact path; never overwrite the only source. GLB/glTF is the recorded
   direction, but exact Blender export settings remain owned by ART-Q03 until selected.
7. Run a fresh Godot import in the real Roadborne checkout. Verify scale, axes, hierarchy,
   materials, normals, bounds, animation clips, collision correspondence, and missing dependencies.
8. Capture the asset through the actual gameplay/review camera and inspect it at representative
   on-screen size. Measure runtime cost when the task includes performance.

## Required gates

- silhouette remains readable at gameplay distance and through LOD transitions;
- evaluated geometry has no unintended internal faces, inverted normals, degenerates, loose
  residue, or non-manifold defects inconsistent with the asset;
- transforms, dimensions, origin, forward/up orientation, and names match the selected contract;
- UVs, texture color spaces, channel packing, texel density, and material count are intentional;
- deformation, root/in-place motion, action names, and extreme poses survive export and import;
- collision and navigation proxies match their gameplay purpose without inheriting render detail;
- the exact Godot import and raw runtime capture pass; a Blender viewport render is insufficient;
- provenance and checksums cover every retained source, dependency, license, and export.

## Generated 3D caution

Apply the same gates to generated meshes. A preview cannot establish topology, UVs, rigging,
licensing, animation, material efficiency, or visual acceptance. Record the generator, version,
inputs, and modifications, and retain Candidate status until Roadborne approval.

## Primary references

- Khronos glTF registry: https://registry.khronos.org/glTF/
- Godot versioned 3D import docs:
  https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/index.html
- Roadborne authority: TECHNICAL_DIRECTION.md, WorldDesign.md, WORLD_PREVIEW.md,
  outstanding_questions.md, and the existing ASSET_PROVENANCE.md.
