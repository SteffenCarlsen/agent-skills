# Agent Skills

Private snapshot of the 121 agent skills active on this workstation on 2026-07-15.

## Contents

- `skills/local/`: 104 user-managed Codex skills.
- `skills/system/`: 5 skills bundled with Codex 0.144.4.
- `skills/plugins/`: 12 skills from the active Browser, Visualize, GitHub, and Ponytail plugins. Each plugin version is preserved in its path and its `plugin.json` is included when available.
- `SOURCES.md`: upstream repositories, versions, licenses, and locally authored exceptions.

## Restore

Copy the children of `skills/local/` into `~/.codex/skills/`.

Do not copy `skills/system/` or `skills/plugins/` into that folder unless you deliberately want to override app-managed content. Codex and the plugin manager normally restore those.

## Snapshot policy

The files are copied verbatim from the installed skill directories. Upstream links document where external skills came from; this repository remains the exact snapshot if an upstream later changes or disappears.
