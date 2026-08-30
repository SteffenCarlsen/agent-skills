# Agent Skills

Private archive of agent skills, last refreshed on 2026-08-31.

The current local inventory contains **90 skills**: 26 user-managed, 6 system,
and 58 plugin skills across 19 cached bundles. Installed or cached does not mean
enabled or available in every task. Older skills and plugin versions are retained.

## Contents

- `skills/local/`: 26 current user-managed skills and 85 retained historical skills.
- `skills/system/`: 6 system skill folders refreshed from the local Codex installation.
- `skills/plugins/`: 58 current plugin skill copies and 26 older copies. Cache-version directories and bundled `plugin.json` metadata are preserved.
- `SOURCES.md`: current inventory, upstream provenance, licenses, and historical records.

## Restore

Copy the desired children of `skills/local/` into `~/.codex/skills/`. Use the
current inventory in `SOURCES.md` to avoid restoring skills no longer installed.

Do not copy `skills/system/` or `skills/plugins/` into that folder unless you deliberately want to override app-managed content. Codex and the plugin manager normally restore those.

## Snapshot policy

Current skill files are copied verbatim, including supporting resources and
available license notices. Git line-ending conversion is disabled for `skills/`.
Generated Python caches and duplicate junction aliases are excluded. Account
configuration, credentials, sessions, plugin runtime data, and cross-agent
duplicate skill directories are not copied.

This is an additive archive: current files replace the same paths, while older
skills, plugin versions, and files absent locally are preserved. Upstream links
record provenance; this refresh does not download newer upstream skill versions.
Skill snapshots do not include the full plugin runtime or prove runtime usability.
Keep this repository private; some bundled content is marked proprietary.
