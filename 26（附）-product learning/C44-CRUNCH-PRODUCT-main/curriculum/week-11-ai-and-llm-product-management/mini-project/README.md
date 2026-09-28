# Mini-Project — Spec Loopline Copilot End to End

> Take everything this week built in pieces — the fit checklist, the human-in-the-loop design, the eval set, the guardrail plan — and assemble it into one coherent spec for **Loopline Copilot**, the kind of document you'd actually bring into a launch-readiness review. One feature, specced completely, one clean deliverable.

**Estimated time:** 2.5–3 hours, best done Saturday after the lectures, exercises, and challenges.

This is the week's capstone, and it's different in shape from earlier mini-projects: instead of answering 15–20 independent questions, you're producing **one integrated artifact** — because that's how AI feature specs actually get reviewed. A launch-readiness meeting doesn't ask "did you write an eval set?" and "did you think about cost?" as separate checkboxes; it asks "is this feature safe, good, and affordable to ship, and can you prove it?" This mini-project is your answer to that question, in writing.

---

## Deliverable

A directory in your portfolio `c44-week-11/mini-project/` containing:

1. `spec.md` — the full feature spec (structure below).
2. `eval-set.sql` — your golden eval set as real `CREATE TABLE` / `INSERT` statements, plus the queries you used to evaluate it.
3. `usage-guardrails.sql` — your cost/safety guardrail queries against usage data.
4. `notes.md` — a short reflection (see the end).

You may reuse and extend the `eval_cases`/`eval_runs`/`eval_results` tables from Lecture 2 and the `ai_usage_log` table from Lecture 3 rather than inventing new schemas from scratch — the point this week is applying the tables well, not reinventing them for the fourth time.

---

## Part 1 — Scope (`spec.md`, Section 1)

Write the feature scope for Loopline Copilot as if this were the actual PRD:

1. **The user problem**, in one sentence, with no mention of "AI" — what does a Loopline user actually need that they don't have today?
2. **The five-question fit checklist** (Lecture 1), answered in full for Copilot specifically — you can draw on the worked example in Lecture 1 Section 6, but write it in your own words with your own reasoning, not copied verbatim.
3. **The bounded task** the model performs, stated precisely (input → output shape).
4. **Model tier and volume estimate**, with reasoning (Lecture 1, Section 5).
5. **Build-vs-buy pick** (Lecture 1, Section 4) with one sentence of justification.

## Part 2 — Human-in-the-loop design (`spec.md`, Section 2)

1. State the HITL pattern (Lecture 3, Section 2) Copilot ships with, and why.
2. Describe the **exact user flow**: what the user sees when they click "break this down," what they can edit before anything is created, and what the explicit confirming action is.
3. Describe the **deterministic fallback**: what happens if the model call fails, times out, or the feature is disabled — a real, usable path, not an error message with a dead end.

## Part 3 — Eval set (`eval-set.sql` + `spec.md` Section 3)

1. Build a golden eval set of **at least 12 cases** across all four categories (happy_path, edge_case, adversarial, out_of_scope) — you may reuse Lecture 2's 14 seed cases as a base, but add **at least 2 new cases of your own invention** covering a scenario the lecture's set doesn't (state which ones are new and why you added them).
2. Run — meaning grade by hand, exactly as Lecture 2's `v1`/`v2` runs did — at least **two prompt or model versions**, either reusing Lecture 2's `v1`/`v2` grading or inventing your own second version with its own grades and notes.
3. In `spec.md` Section 3, paste the output of: (a) pass rate by category per run, (b) the regression-detection query between your two runs, and write 2–3 sentences interpreting what the numbers say about whether the feature is ready to ship.

## Part 4 — Guardrail plan (`usage-guardrails.sql` + `spec.md` Section 4)

1. Reuse or extend the `ai_usage_log` seed data from Lecture 3.
2. Write and run a query that would catch a cost/abuse anomaly (you can reuse the workspace-41 detection query from the lecture or Exercise 3, or invent a new anomaly scenario in fresh seed rows).
3. Write the full guardrail table (failure mode / guardrail / where it lives) from Lecture 3 Section 6, covering **at minimum**: one hallucination guardrail, one cost guardrail, and one safety guardrail — each tied to something concrete and testable (an eval case, a SQL query, an architectural decision), not a vague monitoring promise.

## Part 5 — Acceptance criteria (`spec.md`, Section 5)

Write the feature's acceptance criteria as a short checklist a launch-readiness reviewer could actually check off — each item should be verifiable against something you built in Parts 3–4 (e.g., "adversarial category pass rate ≥ 90% on the golden eval set," "no workspace can exceed N calls per T minutes without triggering a rate-limit response," "on model-call failure, user sees the manual fallback flow, never a dead-end error"). This section is where you prove the feature is genuinely ready, not just described.

---

## Milestones

- **Milestone 1 (45 min):** Part 1 — scope and fit checklist.
- **Milestone 2 (30 min):** Part 2 — HITL design and fallback.
- **Milestone 3 (60 min):** Part 3 — eval set, grading, and SQL queries.
- **Milestone 4 (45 min):** Parts 4–5 — guardrail plan and acceptance criteria.

---

## Rules

- **No spreadsheets.** The eval set and the usage log are both real SQL tables with real `INSERT`s — exactly like every dataset this week.
- **Every acceptance criterion in Part 5 must be verifiable** against something you actually produced in Parts 3–4 — a criterion nothing in your spec can check off is not a real acceptance criterion.
- **State your assumptions.** Volume estimates, model-tier choice, and the rate-limit threshold all involve a judgment call — name the assumption behind each one explicitly, the same discipline Week 1's mini-project asked of you.
- **The two new eval cases in Part 3 must test something the existing 14 don't** — not a close paraphrase of an existing case.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Scope & fit checklist | 20% | Five-question checklist reasoned through specifically for Copilot, not copy-pasted from the lecture |
| HITL design | 15% | A concrete, walkable user flow with a real fallback — not a description of "human review" in the abstract |
| Eval set & queries | 25% | 12+ well-categorized cases with specific rubrics, 2 genuinely novel cases, working category-breakdown and regression queries with real output |
| Guardrail plan | 25% | Guardrail table ties every risk to something concrete and testable; anomaly-detection query actually runs and returns a sensible result |
| Acceptance criteria | 15% | Every item is verifiable against Parts 3–4's actual artifacts |

---

## Reflection (`notes.md`, ~200 words)

1. Which part of this spec was hardest to make concrete — the fit checklist, the eval rubrics, or the guardrails — and why?
2. If you had to cut this mini-project's scope in half to ship in one real sprint, what would you cut first, and what would you refuse to cut no matter the deadline pressure?
3. Name one place where your own judgment call (a volume estimate, a rate-limit number, a rubric threshold) could plausibly be wrong, and what evidence in production would tell you.
4. How is specing this feature different from specing a deterministic one back in Week 4 — what did you have to do this week that Week 4's PRD template never asked for?

---

## Why this matters

Almost every product category now has an "AI feature" pressure exactly like the one that opened this week — and almost every team that ships one badly does it by skipping straight from "let's use AI" to a demo, with no fit check, no eval set, and no guardrail plan in between. The team that does this well isn't smarter about prompting — they're the team that treats a probabilistic feature with the same rigor a deterministic one gets by default, using exactly the three tools this mini-project makes you assemble: a real decision about whether the tool fits, a real measurement of whether it's good, and a real plan for when it isn't.

When done: push, then take the [quiz](../quiz.md) and move on to [Week 12 — Capstone: zero to one](../../week-12-capstone-zero-to-one/), where this spec-writing discipline gets applied to an entire product, not just one feature.
