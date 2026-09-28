# Week 11 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of writing, structured judgment, and one SQL problem set. Commit each.

---

## Problem 1 — Ten "let's add AI" requests, ten fit-checklist verdicts (75 min)

Fluency comes from reps, and the five-question checklist (Lecture 1, Section 3) only becomes fast with practice. For each request below, run the full five-question checklist (yes/no + one clause each) and give a verdict: LLM, rules/classic ML, or "not enough problem definition yet to build anything."

1. "Auto-translate task titles into the viewer's language."
2. "Detect duplicate tasks before a user creates one."
3. "Write release notes from a list of merged pull request titles."
4. "Flag tasks that have been 'in progress' for suspiciously long with no update."
5. "Let users ask 'what did I work on last week?' in plain English."
6. "Auto-fill a task's priority based on its title and description."
7. "Generate a project status report a manager can forward to their boss with zero edits."
8. "Suggest which teammate should be assigned a new task based on their current workload."
9. "Warn a user before they archive a workspace that still has active tasks."
10. "Draft a reply to a customer's feature request, explaining our roadmap stance."

**Deliver** `fit-checklist-drills.md` — 10 requests, each with a full five-question walkthrough and a verdict.

---

## Problem 2 — Rewrite three vague AI briefs as real feature scopes (60 min)

Each brief below has the same problem this week's opening scenario did: it names a technology, not a job. For each, write (a) a one-sentence user-problem restatement with no "AI"/model-technology words in it, and (b) a bounded task description (input → output shape) the way Lecture 1 and Exercise 1 modeled.

1. "We need AI-powered search."
2. "Add a chatbot to the help center."
3. "Use AI to make onboarding smarter."

**Deliver** `brief-rewrites.md`.

---

## Problem 3 — Extend the eval set and find the gap (75 min)

Reuse the `eval_cases` / `eval_runs` / `eval_results` tables from Lecture 2. In `eval-extension.sql`:

1. Write `INSERT` statements adding **3 new eval cases** to `eval_cases` (case_ids 15–17), one each in `happy_path`, `edge_case`, and `adversarial`, testing something the original 14 don't (state what, in a comment above each).
2. Write a **third run** (`run_id = 3`) representing a hypothetical `v3` prompt, and grade all 17 cases (the original 14 plus your 3 new ones) with plausible scores — assume `v3` fixes one specific new weakness you invent but introduces one small regression somewhere else (state both in a comment).
3. Write the regression-detection query (Lecture 2, Section 6) comparing `run_id = 2` to `run_id = 3` and confirm it correctly surfaces your invented regression.
4. Then **undo the additions** cleanly: delete the rows you added for cases 15–17 and run 3, and confirm you're back to the original 14/2/28 row counts from Lecture 2.

**Deliver** `eval-extension.sql` (inserts, regression query with output, and the cleanup) plus one sentence on what your invented `v3` regression would mean for a real ship decision.

---

## Problem 4 — Cost-control speed drills (45 min)

For each scenario, name which cost control from Lecture 3, Section 4 (rate limit, retry-cap, spend cap + alert, caching, kill switch) is the *primary* fix — not "all of them," pick the one that most directly addresses the described failure — and one clause of reasoning:

1. A client-side bug causes the same request to be retried 40 times in 10 seconds after a timeout.
2. A single power-user workspace generates 200 Copilot calls a day, all legitimate, and monthly spend is now 3x the original estimate.
3. Two different users in the same workspace submit the identical goal text within a minute of each other, each generating a fresh (and identical) model call.
4. Copilot's underlying model provider raises per-token pricing overnight with no warning, and this month's actual spend is about to blow past budget with two weeks still left in the month.
5. A newly discovered prompt-injection technique is being used against Copilot in the wild, and you need it stopped **immediately** while you investigate and patch the prompt.

**Deliver** `cost-control-drills.md` — 5 scenarios × primary control × one-clause reasoning.

---

## Problem 5 — Compare two real AI product launches (60 min)

Pick two real, publicly documented AI features from products you or people you know actually use (not hypothetical — find real ones, e.g., via release notes, product blog posts, or press coverage). For each, answer in `product-comparisons.md`:

1. What's the bounded task, as best you can tell from public information?
2. What human-in-the-loop pattern does it appear to use (suggest-only, confirm-to-act, confidence-gated, full autonomy)? What's your evidence?
3. Can you find any public evidence of a guardrail (a stated limitation, a "may make mistakes" disclosure, a rate limit, an opt-out)? Quote or describe what you found.
4. One sentence: based on everything above, would you say this feature was scoped with this week's discipline, or does it show signs of having skipped straight from "let's add AI" to shipping?

**Deliver** `product-comparisons.md` — two products, four answers each.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 75 min |
| 2 | 60 min |
| 3 | 75 min |
| 4 | 45 min |
| 5 | 60 min |
| **Total** | **~5.25 h** |

After homework, take the [quiz](26-product%20learning（附）/curriculum/week-11-ai-and-llm-product-management/quiz.md) and ship the [mini-project](26-product%20learning（附）/curriculum/week-11-ai-and-llm-product-management/mini-project/README.md).
