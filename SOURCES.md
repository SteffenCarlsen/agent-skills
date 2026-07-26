# Sources

Snapshot date: 2026-07-26.

## User-managed skills

| Snapshot | Origin | Notes |
| --- | --- | --- |
| All `skills/local/*` not named below | [dotnet/skills](https://github.com/dotnet/skills/tree/main/plugins) | 92 skills imported from `plugins/*/skills/*`; MIT. |
| `animation-vocabulary`, `emil-design-eng`, `find-animation-opportunities`, `improve-animations`, `review-animations` | [emilkowalski/skills](https://github.com/emilkowalski/skills/tree/main/skills) | Imported together, excluding `apple-design`; MIT. |
| `grill-me`, `to-prd`, `to-issues` | [Matt Pocock skills](https://github.com/mattpocock/skills) and the [AI Hero article](https://www.aihero.dev/5-agent-skills-i-use-every-day) | Rewritten locally as standalone Codex-compatible skills; MIT upstream. |
| `improve-codebase-architecture` | [Original skill](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) | Normalized locally to remove unsupported metadata and sibling-skill dependencies; MIT upstream. |
| `goal` | [kingbootoshi/goal-ledger](https://github.com/kingbootoshi/goal-ledger/tree/main/plugins/goal-ledger/skills/goal) | Goal Ledger skill; MIT. |
| `orchestrate-work` | [Original workflow post](https://x.com/cjzafir/status/2076347110417678502) | Adapted into a concise standalone Codex skill. |
| `repo-practical-maintenance` | Local | Authored locally from recurring repository-maintenance workflows; no external upstream. |

The first row is intentionally the fallback: the other 12 user-managed skills are listed explicitly, leaving exactly the 92 imported .NET skills.

## Codex system skills

`skills/system/` contains six app-managed skills shipped with the locally installed `codex-cli 0.144.4`: `imagegen`, `openai-docs`, `plugin-creator`, `review-agent`, `skill-creator`, and `skill-installer`. The local distribution did not record separate upstream URLs, so the exact bundled files are retained here. `review-agent` is Local/unknown for upstream and license.

## Plugin skills

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
