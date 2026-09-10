---
name: test-gap-analysis
description: "Performs pseudo-mutation analysis on .NET production code to find gaps in existing test suites. Use when the user asks to find weak tests, discover untested edge cases, check if tests would catch a bug, or evaluate test effectiveness through mutation-style reasoning. Analyzes production code for mutation points (boundary conditions, boolean flips, null returns, exception removal, arithmetic changes) and checks whether existing tests would detect each mutation. Works with MSTest, xUnit, NUnit, and TUnit. DO NOT USE FOR: writing new tests (use writing-mstest-tests), detecting test anti-patterns (use test-anti-patterns), measuring assertion diversity (use assertion-quality), or running actual mutation testing tools."
license: MIT
---

# Test Gap Analysis via Pseudo-Mutation

Analyze .NET production code by reasoning about hypothetical mutations and checking whether existing tests would catch them. This reveals blind spots where tests pass but would continue to pass even if the code were broken.

## Why Pseudo-Mutation Matters

Code coverage tells you what code ran during tests. It does **not** tell you whether tests would fail if that code were wrong. A method can have 100% line coverage but zero tests that would catch a sign flip, an off-by-one error, or a removed null check.

Pseudo-mutation analysis asks: _"If this plausible defect changed relevant behavior, would an existing test fail?"_ An expected survivor is a candidate gap, not an automatic demand for another test.

| Coverage Metric | What It Measures | What It Misses |
|----------------|-----------------|----------------|
| Line coverage | Which lines executed | Whether assertions verify those lines' behavior |
| Branch coverage | Which branches taken | Whether both branches produce different asserted outcomes |
| **Executed mutation score** | Which generated mutations tests detected | Real-world relevance, equivalent mutations, and defects outside the mutation set |

This skill performs **static pseudo-mutation**: verdicts are reasoned expectations, not executed results or a measured mutation score. Keep analysis read-only unless implementation is requested. There is no coverage percentage or mutation-count target; stop when the scoped meaningful risks have been assessed.

## When to Use

- User asks "would my tests catch a bug in this code?"
- User wants to find weak or shallow tests
- User wants to evaluate test effectiveness beyond coverage
- User asks for mutation testing or mutation analysis
- User asks "where are my tests blind?"
- User wants to prioritize which tests to strengthen

## When Not to Use

- User wants to write new tests from scratch (use `writing-mstest-tests`)
- User wants to detect test anti-patterns like flakiness or poor naming (use `test-anti-patterns`)
- User wants to measure assertion variety (use `assertion-quality`)
- User wants to run an actual mutation testing framework like Stryker (help them directly)
- User only wants code coverage numbers (out of scope)

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| Production code | Yes | The source files to analyze for mutation points |
| Test code | Yes | The test files that cover the production code |
| Focus area | No | A specific mutation category or code region to focus on |

## Workflow

### Step 1: Gather production and test code

Read the production code, relevant callers, input/data flows, and corresponding tests. If the user points to a directory, use naming conventions to find candidates, then confirm the actual calls rather than assuming a filename proves coverage. Choose the scope from the request and relevant risks; do not default to an exhaustive repository audit.

Establish which production methods are exercised by which test methods — trace this through method calls in test code, setup, and helper methods.

### Step 2: Identify mutation points

Select mutations that model plausible regressions in meaningful production behavior: domain rules, observed bugs, reachable boundaries, or consequential trust-boundary and dependency failures. The catalog below is a menu, not a requirement to enumerate every operator or method. Skip invented states that supported flows cannot reach; rare reachable security/error cases can still matter.

#### Boundary Mutations

| Original | Mutation | What it tests |
|----------|----------|---------------|
| `<` | `<=` | Off-by-one at upper bound |
| `>` | `>=` | Off-by-one at lower bound |
| `<=` | `<` | Boundary inclusion |
| `>=` | `>` | Boundary inclusion |
| `== 0` | `== 1` or `<= 0` | Zero-boundary handling |
| `i < length` | `i < length - 1` or `i <= length` | Loop boundary |
| `index + 1` | `index` or `index + 2` | Index arithmetic |

#### Boolean and Logic Mutations

| Original | Mutation | What it tests |
|----------|----------|---------------|
| `&&` | `\|\|` | Condition independence |
| `\|\|` | `&&` | Condition necessity |
| `!condition` | `condition` | Negation correctness |
| `if (x)` | `if (!x)` | Branch selection |
| `true` (constant) | `false` | Hardcoded assumption |
| `flag \|\| other` | `other` | Short-circuit first operand |

#### Return Value Mutations

| Original | Mutation | What it tests |
|----------|----------|---------------|
| `return result` | `return null` | Null handling downstream |
| `return result` | `return default` | Default value handling |
| `return true` | `return false` | Boolean return verification |
| `return list` | `return new List<T>()` | Empty collection handling |
| `return count` | `return 0` or `return count + 1` | Numeric return verification |
| `return string` | `return ""` or `return null` | String return verification |

#### Exception Removal Mutations

| Original | Mutation | What it tests |
|----------|----------|---------------|
| `throw new ArgumentNullException(...)` | _(remove entire throw)_ | Guard clause verification |
| `throw new InvalidOperationException(...)` | _(remove entire throw)_ | State validation testing |
| `if (x == null) throw ...` | _(remove entire guard)_ | Null guard testing |
| `if (!IsValid()) throw ...` | _(remove entire check)_ | Validation testing |

#### Arithmetic Mutations

| Original | Mutation | What it tests |
|----------|----------|---------------|
| `a + b` | `a - b` | Addition correctness |
| `a - b` | `a + b` | Subtraction correctness |
| `a * b` | `a / b` | Multiplication correctness |
| `a / b` | `a * b` | Division correctness |
| `a % b` | `a / b` | Modulo correctness |
| `x++` | `x--` | Increment direction |
| `-value` | `value` | Sign flip |

#### Null-Check Removal Mutations

| Original | Mutation | What it tests |
|----------|----------|---------------|
| `if (x == null) return ...` | _(remove null check)_ | Null path coverage |
| `if (x != null) { ... }` | _(always enter block)_ | Null guard necessity |
| `x ?? defaultValue` | `x` | Null coalescing coverage |
| `x?.Method()` | `x.Method()` | Null-conditional coverage |

### Step 3: Evaluate each mutation against tests

For each identified mutation point, reason about whether existing tests would detect the change:

1. **Find covering tests** — Which test methods exercise the mutated line? Follow call chains through helpers and setup methods.
2. **Check assertion relevance** — Do those tests assert something that would change if the mutation were applied? A test that calls the method but only asserts an unrelated property would NOT catch the mutation.
3. **Classify the mutation** as:

| Verdict | Meaning | Action |
|---------|---------|--------|
| **Expected killed** | A traced test executes the relevant production path and asserts an outcome the mutation would change | Explain the assertion supporting this inference |
| **Expected survived** | The inspected tests reach the path but appear to miss the changed behavior | Recommend improvement only if the behavior and risk justify it |
| **No test path found** | No exercising test was found within the inspected scope | State the search scope; assess relevance rather than assuming severity |
| **Equivalent** | The mutation preserves relevant observable behavior under the established contract | Skip; state the constraint supporting equivalence |
| **Unknown** | Inputs, call paths, assertions, or runtime behavior cannot be established sufficiently | State what evidence would resolve it; do not count it as a gap or success |

### Step 4: Calibrate findings

Before reporting, apply these calibration rules:

- **Don't flag trivial code.** Simple property getters (`return _name;`), auto-properties, and boilerplate don't need mutation analysis. Focus on logic, conditions, calculations, and error handling.
- **Consider defensive depth and reachability.** Establish whether callers prevent the input and whether an external trust boundary still requires the guard. Do not create an impossible scenario solely to test a defensive branch.
- **Equivalent mutations are not gaps.** If changing `>=` to `>` doesn't alter behavior because the `==` case is impossible given the domain, mark it Equivalent and skip.
- **Private methods reached through public API are valid targets.** Trace through the call chain — a private method called from a tested public method may still have expected survivors if the test doesn't assert the specific behavior affected.
- **Rate by relevant behavior and consequence, not count.** Explain the plausible input or regression and its observable effect. Unexecuted logging code is not automatically a higher priority than weakly asserted domain logic.
- **Check what is really tested.** A test of a mock's configured return value or a copied implementation does not protect the production behavior. Recommend executing the real code, using mocks only for useful dependency isolation; meaningful unit tests do not require live services.

### Step 5: Report findings

Keep the report proportional to the request:

1. **Scope and conclusion** — State what was inspected, the important risks, and that verdicts are static expectations. Do not report a measured mutation score. Provide counts only if requested, labeled as counts of inspected hypotheses.

2. **Relevant candidate gaps** — For each consequential expected survivor or missing test path, report:
   - **Location**: File, method, line
   - **Mutation category**: Boundary / Boolean / Return value / Exception / Arithmetic / Null-check
   - **Original code**: The current code
   - **Hypothetical mutation**: What would change
   - **Real scenario and consequence**: How supported inputs or a plausible regression expose the changed behavior
   - **Evidence and verdict**: Which tests exercise the real code and why their assertions appear to miss it; label uncertainty
   - **Recommended check**: The smallest useful assertion or case that protects this behavior, reusing existing tests where practical

   Group by the demonstrated consequence in this project, with the most relevant risks first.

3. **Existing protection and limits** — Briefly note strong assertions, equivalent changes, unknowns, and material limits. No need to enumerate every expected killed mutation.

4. **Recommendations** — Prioritize relevant checks by risk and combine cases that protect the same behavior. Do not prescribe tests for every mutation, all public methods, or a target percentage. Stop after the scoped risks are addressed; no automatic test-writing or infrastructure work follows a review.

## Validation

- [ ] Reported verdicts are labeled as expected, equivalent, no test path found, or unknown; no executed mutation result is implied
- [ ] Each recommended gap includes a reachable scenario or plausible regression, its consequence, and the evidence that existing assertions miss it
- [ ] Each recommendation is a focused check of actual production behavior, not a test for its own sake
- [ ] Equivalent or irrelevant mutations are excluded from recommendations
- [ ] Trivial code (simple getters, auto-properties) is excluded from analysis
- [ ] Findings are prioritized by risk, not just listed in source order
- [ ] Report notes existing protection and material uncertainties where relevant
- [ ] Mutation categories are correctly labeled

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Analyzing trivial code | Skip auto-properties, simple getters, and boilerplate — focus on logic |
| Reporting equivalent mutations as gaps | If the mutation doesn't change behavior, it's not a gap — mark Equivalent |
| Ignoring call chains | A private helper called from a tested public method is reachable — trace the chain |
| Over-counting mutations in generated code | Skip auto-generated code, designer files, and migration files |
| Recommending a new test for every expected survivor | Several mutations may share one meaningful missing check; low-value or unreachable cases may need none |
| Ignoring production context | Prioritize the consequence and reachable flow, not the method name; formatting may matter when it defines a persisted or external contract |
| Claiming 100% kill rate is required | Some mutations in low-risk code are acceptable to leave — acknowledge this in the report |
| Treating static reasoning as execution evidence | Use expected/unknown verdicts and say what was inspected; executing ordinary tests would still not prove a mutation was killed |
