---
name: improve-codebase-architecture
description: Review a codebase for architectural friction and deepening opportunities, then present evidence-backed candidates in a visual HTML report and pressure-test the selected design. Use when asked to improve architecture, simplify shallow modules, clarify seams and adapters, increase locality or leverage, or plan a substantial refactor before implementation.
---

# Improve Codebase Architecture

Find refactors that turn shallow modules into deep modules. Optimize for testability, locality, leverage, and ease of codebase navigation.

## Use the shared vocabulary

- **module**: code that hides related decisions behind an interface.
- **interface**: the surface callers must understand.
- **implementation**: complexity hidden behind the interface.
- **depth**: useful implementation complexity divided by interface complexity.
- **deep**: a small interface hides substantial implementation complexity.
- **shallow**: the interface is nearly as complex as the implementation.
- **seam**: a place where behavior can vary independently.
- **adapter**: one concrete implementation behind a seam.
- **leverage**: one focused change benefits many call sites.
- **locality**: related knowledge and behavior live together.

Use these terms precisely. Prefer `module`, `interface`, and `seam` over vague substitutes such as `component`, `service`, `API`, or `boundary` when the architecture concept is what matters.

Apply these rules:

- **Deletion test**: deleting a shallow module should concentrate complexity, not merely move it elsewhere.
- **Interface is the test surface**: prefer tests through stable behavior over tests coupled to implementation details.
- **Adapter threshold**: one adapter is a hypothetical seam; two adapters demonstrate a real seam.

## Workflow

### 1. Establish context

1. Inspect the worktree and the closest repository instructions before analysis.
2. Read `CONTEXT.md` and relevant ADRs when present. Treat domain terms in `CONTEXT.md` as canonical.
3. Trace actual production paths and their tests. Separate confirmed facts from inferences.
4. Keep this phase read-only. Do not implement a refactor before the user selects and approves a candidate.

If subagents are available and current instructions allow them, use them only for bounded, read-only exploration by subsystem. Do not run parallel edits. Otherwise, explore locally.

### 2. Explore architectural friction

Explore organically rather than scoring files by a rigid heuristic. Look for:

- concepts that require bouncing among many small modules;
- shallow modules whose interface nearly matches their implementation;
- pure functions extracted only for testability while call-site behavior remains untested;
- decisions that leak across a seam;
- duplicated coordination logic;
- tests that require implementation knowledge or excessive setup;
- interfaces with only one adapter and no demonstrated variation;
- low locality or low leverage in frequently changed paths.

For each suspected opportunity:

1. Trace callers, dependencies, tests, and ownership.
2. Apply the deletion test.
3. Explain which complexity would move behind the deeper interface.
4. Reject candidates that only rename, rearrange, or add speculative abstraction.
5. Respect ADRs. Surface a conflicting candidate only when observed friction justifies reopening the decision, and name the conflict explicitly.

Do not design exact interfaces yet. Describe candidate changes in plain English until the user chooses one.

### 3. Present candidates in an HTML report

Read [HTML-REPORT.md](HTML-REPORT.md) before generating the report.

Write one standalone HTML file outside the repository:

- Resolve the temporary directory from `$TMPDIR`, `/tmp`, or `%TEMP%`, as appropriate.
- Name it `architecture-review-<timestamp>.html` so every run is fresh.
- Use Tailwind and Mermaid through the CDN links in the scaffold.
- Open the file with the platform command when desktop interaction is available.
- Tell the user the absolute path.

Each candidate card must include:

- files and modules involved;
- the observed problem;
- the proposed deepening in plain English;
- benefits stated as locality, leverage, interface, or test-surface gains;
- a before/after visualization;
- recommendation strength: `Strong`, `Worth exploring`, or `Speculative`;
- an ADR warning when applicable.

End with one top recommendation and the concrete evidence that makes it first. Keep prose sparse and let the diagrams carry the structure.

After presenting the report, ask: **Which of these would you like to explore?**

### 4. Pressure-test the selected candidate

Once the user chooses a candidate, work through one decision cluster at a time:

1. Clarify the desired behavior and constraints.
2. Trace every caller and adapter affected by the proposed seam.
3. Identify what belongs behind the deepened interface and what must remain outside.
4. Compare at least two concrete designs when the interface shape is uncertain.
5. Decide which existing tests survive, which become unnecessary, and which behavior needs new proof.
6. Map a narrow migration that preserves behavior and allows intermediate validation.
7. Record unresolved risks and rejected alternatives.

Update `CONTEXT.md` only when a durable domain term is introduced or sharpened. Create it lazily if needed. If the user rejects a candidate for a durable, load-bearing reason, offer to record an ADR so future reviews do not repeat it; do not offer for temporary prioritization decisions.

Do not implement until the user explicitly approves implementation.

## Quality bar

- Tie every candidate to real files, callers, tests, and observed friction.
- Prefer deletion and consolidation over new abstraction.
- Do not introduce a seam without demonstrated variation or a concrete second adapter.
- Preserve domain language and existing architectural decisions unless evidence justifies revisiting them.
- State what was inspected, what remains uncertain, and what validation a future refactor would need.
