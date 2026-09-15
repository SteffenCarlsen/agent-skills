# Sources

Last refresh: 2026-09-15.

## Current local inventory

88 skill copies were found in the user skill directory, system skill directory,
and canonical plugin-cache `skills/` directories: 26 user-managed, 6 system,
and 56 plugin skills in 17 bundles. This is a local installation/cache inventory,
not a claim that every skill is enabled or available in the current task.

### User-managed skills (26)

`analyzing-dotnet-performance`, `code-testing-agent`, `code-testing-extensions`, `deob`, `dotnet-pinvoke`, `dotnet-webapi`, `frontend-design`, `goal`, `grill-me`, `handoff`, `improve-codebase-architecture`, `install-anti-slop`, `mcp-csharp-create`, `microbenchmarking`, `migrate-dotnet10-to-dotnet11`, `migrate-mstest-v3-to-v4`, `msbuild-modernization`, `orchestrate-work`, `performance-optimization`, `repo-practical-maintenance`, `roadborne-blender-assets`, `roadborne-game-assets`, `run-tests`, `technology-selection`, `test-gap-analysis`, `writing-mstest-tests`.

Current files live under `skills/local/<name>/`. Other local skill folders are
historical snapshots retained from earlier refreshes.

### System skills (6)

`imagegen`, `openai-docs`, `plugin-creator`, `review-agent`, `skill-creator`, `skill-installer`.

Copied from the current local `.system` directory. No Codex application version
is inferred from these files. `review-agent` is present locally even though it
is not exposed in the current task's skill catalog.

### Plugin skills (56)

The path preserves the cache directory identifier; it is not always the plugin's
semantic version. The copied `plugin.json` is the authoritative local record for
each current bundle. This refresh did not check upstream for newer versions.

| Snapshot | Marketplace | Skills |
| --- | --- | ---: |
| [i-have-adhd/0.3.0](skills/plugins/i-have-adhd/0.3.0) | i-have-adhd | 1 |
| [computer-use/26.908.40834](skills/plugins/computer-use/26.908.40834) | openai-bundled | 1 |
| [sites/0.1.70](skills/plugins/sites/0.1.70) | openai-bundled | 2 |
| [visualize/1.0.37](skills/plugins/visualize/1.0.37) | openai-bundled | 1 |
| [coderabbit/bd2122cb](skills/plugins/coderabbit/bd2122cb) | openai-curated | 1 |
| [github/bd2122cb](skills/plugins/github/bd2122cb) | openai-curated | 4 |
| [linear/bd2122cb](skills/plugins/linear/bd2122cb) | openai-curated | 1 |
| [nvidia/bd2122cb](skills/plugins/nvidia/bd2122cb) | openai-curated | 11 |
| [openai-templates/0.1.1](skills/plugins/openai-templates/0.1.1) | openai-curated-remote | 20 |
| [plugin-management/0.1.0](skills/plugins/plugin-management/0.1.0) | openai-curated-remote | 1 |
| [documents/26.909.12148](skills/plugins/documents/26.909.12148) | openai-primary-runtime | 1 |
| [pdf/26.909.12148](skills/plugins/pdf/26.909.12148) | openai-primary-runtime | 1 |
| [presentations/26.909.12148](skills/plugins/presentations/26.909.12148) | openai-primary-runtime | 1 |
| [spreadsheets/26.909.12148](skills/plugins/spreadsheets/26.909.12148) | openai-primary-runtime | 2 |
| [template-creator/26.909.12148](skills/plugins/template-creator/26.909.12148) | openai-primary-runtime | 1 |
| [osrs-wiki-mcp/1.1.2](skills/plugins/osrs-wiki-mcp/1.1.2) | osrs-wiki | 1 |
| [ponytail/4.10.0](skills/plugins/ponytail/4.10.0) | ponytail | 6 |

### Previous plugin inventory (2026-08-31)

| Snapshot | Marketplace | Manifest version | Skills | Origin | License recorded |
| --- | --- | --- | ---: | --- | --- |
| [i-have-adhd/0.2.0](skills/plugins/i-have-adhd/0.2.0) | i-have-adhd | 0.2.0 | 1 | [Recorded upstream](https://github.com/ayghri/i-have-adhd) | MIT |
| [browser/26.825.51511](skills/plugins/browser/26.825.51511) | openai-bundled | 26.825.51511 | 1 | [Recorded upstream](https://github.com/openai/openai/tree/master/lib/browser_use/plugin) | Proprietary |
| [chrome/26.825.51511](skills/plugins/chrome/26.825.51511) | openai-bundled | 26.825.51511 | 1 | [Recorded upstream](https://github.com/openai/openai/tree/master/lib/browser_use/plugin) | Proprietary |
| [sites/0.1.46](skills/plugins/sites/0.1.46) | openai-bundled | 0.1.46 | 2 | Not recorded | Proprietary |
| [visualize/1.0.23](skills/plugins/visualize/1.0.23) | openai-bundled | 1.0.23 | 1 | Not recorded | Proprietary |
| [coderabbit/bd2122cb](skills/plugins/coderabbit/bd2122cb) | openai-curated | 1.1.4 | 1 | [Recorded upstream](https://github.com/coderabbitai/codex-plugin) | MIT |
| [github/bd2122cb](skills/plugins/github/bd2122cb) | openai-curated | 0.1.6 | 4 | [Recorded upstream](https://github.com/openai/plugins) | MIT |
| [linear/bd2122cb](skills/plugins/linear/bd2122cb) | openai-curated | 0.0.3 | 1 | [Recorded upstream](https://github.com/openai/plugins) | MIT |
| [nvidia/bd2122cb](skills/plugins/nvidia/bd2122cb) | openai-curated | 1.0.2 | 11 | [Recorded upstream](https://github.com/NVIDIA/skills) | Apache-2.0 AND CC-BY-4.0 |
| [deep-research-work/0.1.14](skills/plugins/deep-research-work/0.1.14) | openai-curated-remote | 0.1.14 | 1 | [Recorded upstream](https://github.com/openai/openai/tree/master/chatgpt/oai-maintained-plugins/plugins/deep-research-work) | Proprietary |
| [openai-templates/0.1.1](skills/plugins/openai-templates/0.1.1) | openai-curated-remote | 0.1.1 | 20 | [Recorded upstream](https://github.com/openai/oai-maintained-plugins/tree/main/plugins/openai-templates) | Proprietary |
| [plugin-management/0.1.0](skills/plugins/plugin-management/0.1.0) | openai-curated-remote | 0.1.0 | 1 | [Recorded upstream](https://github.com/openai/openai/tree/master/chatgpt/oai-maintained-plugins/plugins/plugin-management) | Proprietary |
| [documents/26.826.12353](skills/plugins/documents/26.826.12353) | openai-primary-runtime | 26.826.12353 | 1 | [Recorded upstream](https://github.com/openai/openai) | MIT |
| [pdf/26.826.12353](skills/plugins/pdf/26.826.12353) | openai-primary-runtime | 26.826.12353 | 1 | [Recorded upstream](https://github.com/openai/openai) | MIT |
| [presentations/26.826.12353](skills/plugins/presentations/26.826.12353) | openai-primary-runtime | 26.826.12353 | 1 | [Recorded upstream](https://github.com/openai/openai) | MIT |
| [spreadsheets/26.826.12353](skills/plugins/spreadsheets/26.826.12353) | openai-primary-runtime | 26.826.12353 | 2 | [Recorded upstream](https://github.com/openai/openai) | MIT |
| [template-creator/26.826.12353](skills/plugins/template-creator/26.826.12353) | openai-primary-runtime | 26.826.12353 | 1 | [Recorded upstream](https://github.com/openai/openai) | Proprietary |
| [osrs-wiki-mcp/1.1.2](skills/plugins/osrs-wiki-mcp/1.1.2) | osrs-wiki | 1.1.2 | 1 | [Recorded upstream](https://github.com/SSanderV/osrs-wiki-mcp) | MIT |
| [ponytail/4.9.0](skills/plugins/ponytail/4.9.0) | ponytail | 4.9.0 | 6 | [Recorded upstream](https://github.com/DietrichGebert/ponytail) | MIT |

Only each bundle's `skills/` tree, `plugin.json`, and available root license/notices
are included. The Chrome `latest` junction and cross-agent duplicate folders
such as `.openclaw/skills` and `.cursor/skills` are excluded. Two generated
`__pycache__/*.pyc` files were also excluded.

### Additional user-managed provenance

The historical provenance below still applies to skills present in the original
snapshot. New or locally adapted entries need their own records:

| Skill | Origin evidence | Notes |
| --- | --- | --- |
| `frontend-design` | Bundled `LICENSE.txt` | Apache-2.0 license text retained; no separate upstream URL recorded in the installed folder. |
| `roadborne-blender-assets` | [UPSTREAM.md](skills/local/roadborne-blender-assets/UPSTREAM.md) | Records upstream URL, commit, MIT license, and Roadborne adaptation. |
| `roadborne-game-assets` | [UPSTREAM.md](skills/local/roadborne-game-assets/UPSTREAM.md) | Records upstream URL, commit, Apache-2.0 license, and Roadborne adaptation. |
| `deob`, `handoff`, `install-anti-slop`, `performance-optimization` | Local installed copies | Separate upstream/license provenance not recorded in these installed folders; do not apply the historical .NET fallback to them. |

Existing license metadata is preserved without inventing missing license texts.
Some skills depend on external agents, apps, runtimes, tools, or repository files
not included here; copying their instructions does not supply those dependencies.

### Refresh validation

All 1,075 selected source files matched their snapshot copies by SHA-256. All
90 current `SKILL.md` files parsed as YAML frontmatter with nonempty names and
descriptions. The bundled strict validator accepted 74; 16 retained existing
upstream metadata conventions it rejects (extra keys, angle brackets, or capitalized
names). Those installed files were preserved, not rewritten to satisfy the validator.

## Historical provenance

The following records describe the earlier snapshots, not the current counts.

Snapshot date: 2026-07-26.

### User-managed skills in the original snapshot

| Snapshot | Origin | Notes |
| --- | --- | --- |
| Original-snapshot `skills/local/*` not named below | [dotnet/skills](https://github.com/dotnet/skills/tree/main/plugins) | 92 skills imported from `plugins/*/skills/*`; MIT. Does not cover subsequently added skills. |
| `animation-vocabulary`, `emil-design-eng`, `find-animation-opportunities`, `improve-animations`, `review-animations` | [emilkowalski/skills](https://github.com/emilkowalski/skills/tree/main/skills) | Imported together, excluding `apple-design`; MIT. |
| `grill-me`, `to-prd`, `to-issues` | [Matt Pocock skills](https://github.com/mattpocock/skills) and the [AI Hero article](https://www.aihero.dev/5-agent-skills-i-use-every-day) | Rewritten locally as standalone Codex-compatible skills; MIT upstream. |
| `improve-codebase-architecture` | [Original skill](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) | Normalized locally to remove unsupported metadata and sibling-skill dependencies; MIT upstream. |
| `goal` | [kingbootoshi/goal-ledger](https://github.com/kingbootoshi/goal-ledger/tree/main/plugins/goal-ledger/skills/goal) | Goal Ledger skill; MIT. |
| `orchestrate-work` | [Original workflow post](https://x.com/cjzafir/status/2076347110417678502) | Adapted into a concise standalone Codex skill. |
| `repo-practical-maintenance` | Local | Authored locally from recurring repository-maintenance workflows; no external upstream. |

The first row is intentionally the fallback: the other 12 user-managed skills are listed explicitly, leaving exactly the 92 imported .NET skills.

### Codex system skills in the original snapshot

The original `skills/system/` snapshot recorded six app-managed skills with `codex-cli 0.144.4`: `imagegen`, `openai-docs`, `plugin-creator`, `review-agent`, `skill-creator`, and `skill-installer`. Those paths have since been refreshed; the original files remain in Git history. The local distribution did not record separate upstream URLs. `review-agent` was Local/unknown for upstream and license.

### Historical plugin skill versions

| Snapshot | Version | Origin | License recorded by plugin |
| --- | --- | --- | --- |
| `skills/plugins/browser/` | 26.707.72221 | [OpenAI Browser plugin](https://github.com/openai/openai/tree/master/lib/browser_use/plugin) | Proprietary |
| `skills/plugins/i-have-adhd/` | 0.1.0 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | MIT |
| `skills/plugins/visualize/` | 1.0.11 | [OpenAI](https://openai.com/) | Proprietary |
| `skills/plugins/visualize/` | 1.0.12 | [OpenAI](https://openai.com/) | Proprietary |
| `skills/plugins/github/` | 0.1.8-2841cf9749ae | [openai/plugins](https://github.com/openai/plugins) | MIT |
| `skills/plugins/ponytail/` | 4.8.4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | MIT |
| `skills/plugins/documents/` | 26.715.12143 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/documents/` | 26.723.12215 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/pdf/` | 26.715.12143 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/pdf/` | 26.723.12215 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/presentations/` | 26.715.12143 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/presentations/` | 26.723.12215 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/spreadsheets/` | 26.715.12143 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/spreadsheets/` | 26.723.12215 | [OpenAI repository](https://github.com/openai/openai) | MIT |
| `skills/plugins/template-creator/` | 26.715.12143 | [OpenAI repository](https://github.com/openai/openai) | Proprietary |
| `skills/plugins/template-creator/` | 26.723.12215 | [OpenAI repository](https://github.com/openai/openai) | Proprietary |

The copied `plugin.json` beside each bundle is the authoritative local record of its author, repository, version, and license metadata.
