---
name: repo-practical-maintenance
description: Use when TaF asks for practical repo maintenance across their active checkouts, especially CI failures, failing tests, PR reviews, changelogs, docs updates, release prep, deployment workflow fixes, debugging evidence, package visibility, or focused triage in Microbot, GameOverlay.NET, ModernOverlay, LegionLabs, or related local repos.
metadata:
  short-description: Practical repo maintenance for TaF
---

# Repo Practical Maintenance

## Default Shape

Use this skill for practical repo work where the user wants the current checkout handled directly.

1. Start with the narrow repo surface the user named.
2. Check current state before assuming memory is current: `git status --short`, relevant files, logs, failing commands, or CI metadata.
3. Keep the work repo-native. Prefer existing scripts, workflows, docs, test projects, and helper APIs over new process.
4. Preserve the full requested end state. Do not close on a smaller local slice unless the user explicitly narrows scope.
5. Verify the touched contract with the smallest meaningful compile, test, build, or direct evidence pass.
6. Report concrete outcomes and commands. Use numbered lists for decisions, recommendations, review findings, and next actions.

## Repeated Workflows

### CI or Test Triage

1. Identify the failing job, command, test, and recent relevant change.
2. Reproduce the smallest local command when practical.
3. If behavior changed, rebuild before trusting `--no-build` test runs.
4. Fix the test contract or implementation in the same pass when the failure is local and scoped.
5. End with the rerun command and result.

### Release or Deploy Prep

1. Inspect workflow files and artifact-producing project tasks first.
2. Confirm the artifact path or publishing command against the repo build output.
3. Keep workflow edits functional and narrow.
4. On Windows PowerShell, quote Gradle `-P...` property arguments.
5. If the user says "push it", commit and push the narrow fix without extra ceremony.

### PR Review

1. Lead with findings, ordered by severity.
2. Ground each issue in file and line references.
3. Prioritize bugs, regressions, risk, and missing tests over style.
4. If there are no findings, say so and name any residual test gap.

### Changelog or Docs Update

1. Confirm the live docs location before editing.
2. Patch current repo docs instead of stale root notes.
3. Keep release-readiness language aligned with the user's stated bar.
4. Prefer exact, practical wording over broad product claims.

### Debugging Evidence

1. Decode the exact local symptom first.
2. Add structured evidence that helps solve the immediate issue.
3. Avoid generic logs when the user asks for actionable debugging output.
4. Keep diagnostic scope tight to the named subsystem.

## Repo Notes

- Microbot Gradle wrapper tasks should be serialized on this machine because parallel wrapper runs can collide on `gradle-8.8-all.zip.lck`.
- Microbot walker work should begin at the named surface: `DoorHandler`, `DefaultWalkStateMachine`, `ShortestPathScript`, `ShortestPathPanel`, `InteractionRegistry`, migration specs, or TODO files.
- GameOverlay.NET and ModernOverlay decisions should default to hobbyist MVP/alpha language unless the user asks for a production bar.
- GameOverlay.NET timing work should compare `FrameRateLimit.Unlimited` with `PresentMode.Immediate` and inspect `PresentDuration`.
- LegionLabs overlay recommendations should stay compact and directive-style: concrete build/send/hold calls, target waves, and explicit `needs_enemy_scan` uncertainty.

## Delegation Template

When the user explicitly asks for a custom subagent or parallel investigation, use `references/bounded-investigator-subagent.md` as the prompt template for a spawned explorer or worker. Keep the subagent's scope bounded and do non-overlapping work locally while it runs.
