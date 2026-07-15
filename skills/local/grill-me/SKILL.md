---
name: grill-me
description: Relentlessly interview the user to sharpen a plan, feature idea, design, or technical approach before implementation. Use when the user invokes grill-me, asks to pressure-test an idea, wants clarifying questions, or needs decisions walked through before code is written.
---

# Grill Me

Run a focused design interview before implementation.

## Process

1. Identify the current plan, goal, or decision being tested.
2. Ask concrete questions that expose missing requirements, constraints, risks, dependencies, and tradeoffs.
3. Follow each decision branch until it reaches either a clear answer, an explicit deferral, or a codebase fact that can be inspected.
4. If the answer can be discovered from files, commands, docs, or repo state, inspect that source instead of asking the user.
5. Continue until the plan is specific enough to implement or the remaining uncertainty is intentionally accepted.

## Output

Keep questions grouped and numbered. Prefer short batches when answers will change the next questions.

When enough is known, summarize:

1. Confirmed decisions
2. Open decisions
3. Implementation implications
