# Week 7 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hand calculation, Python analysis, and applied writing. Commit each.

Problems 1–3 use the seed dataset from the [README](./README.md) (`stuck_alert_experiment`) and the Exercise 2 daily dataset (Quick Add button). Problems 4–5 are new scenarios.

---

## Problem 1 — Hypotheses for five Loopline feature ideas (45 min)

Loopline's backlog has five loosely-defined feature ideas. For each, write a proper if/then/because hypothesis (Lecture 1 §1) with **one** primary metric and **one** plausible guardrail metric. Where the idea is too vague to hypothesize about as written, say so and state the one clarifying question you'd ask before you could write a real hypothesis.

1. "Add dark mode."
2. "Let users @-mention teammates in task comments."
3. "Show a weekly digest email summarizing team activity."
4. "Add a 'duplicate task' button."
5. "Redesign the task list to show due dates more prominently."

**Deliver** `hypotheses.md` with all five, each following the template, each with a named unit of randomization (user, team, or "cannot cleanly randomize — see Challenge 2's approach").

---

## Problem 2 — Sample size sensitivity table (60 min)

Using the sample-size formula and `statsmodels`, build a table showing required n-per-arm for a metric with baseline **p₁ = 0.15**, across a grid of:

- MDE: 1pp, 2pp, 3pp, 5pp, 10pp
- Power: 0.70, 0.80, 0.90

That's a 5×3 = 15-cell table. Write the Python loop that generates it (don't hand-type 15 numbers) and save the output as `sensitivity-table.md` (a markdown table) plus `sensitivity.py` (the code).

Then answer in 3–4 sentences: looking at the table, is it more expensive (in required sample) to tighten the MDE from 3pp to 1pp, or to raise the power from 0.80 to 0.90 at a fixed 3pp MDE? Which lever would you pull first if a stakeholder wanted "more confidence" in a result?

---

## Problem 3 — Reanalyze the Stuck Task Alerts guardrail with a different lens (45 min)

The mini-project's Analysis A found no significant guardrail violation on overall task completion rate (p ≈ 0.18). In `guardrail-deep-dive.md`:

1. Compute the 95% confidence interval of the difference in `task_completion_rate` between arms (control vs. treatment), using the same team-level approach as the primary metric.
2. State the interval and, in your own words, what range of true guardrail effects is consistent with this data.
3. Suppose Loopline's tolerance (from a design doc written before the test) was "we will not ship if the guardrail interval's lower bound shows more than a 5-point drop." Does this result clear that bar? Show the arithmetic, don't just assert it.

---

## Problem 4 — Peeking, quantified (60 min)

Lecture 3 §1 shows a real (seeded) null-effect dataset where daily peeking crossed p < 0.05 on 3 of 14 days by chance. In `peeking-simulation.py`:

1. Write a Python simulation: two arms, **true underlying rate 0.20 for both** (no real effect), ~140 sessions/arm/day, run for 30 simulated days, computing the cumulative two-proportion p-value after each day.
2. Run the simulation **500 times** (500 independent 30-day null experiments). For each run, record whether **any** day's cumulative p-value dropped below 0.05 at some point during the 30 days ("would a peeking PM have declared a false win in this run?").
3. Report: out of 500 runs, what percentage had at least one day cross p < 0.05, even though the true effect was always zero? Compare that percentage to the nominal 5% significance level.
4. Write 2–3 sentences on what this number tells you about the real-world false-positive rate of "check every day, stop at the first significant-looking result."

**Deliver** `peeking-simulation.py` and your written answer to Task 4.

---

## Problem 5 — Design brief for a real (or realistic) experiment (75 min)

Pick a product you personally use (an app on your phone, a website you visit often) and a change you think it should test — something you've genuinely wondered about, not a made-up example. In `real-world-design-brief.md`, write a full mini design doc:

1. The product and the change.
2. Hypothesis (if/then/because), primary metric, one guardrail.
3. Unit of randomization, with a one-paragraph justification referencing SUTVA/contamination risk specific to this product.
4. A rough, stated-assumption estimate of baseline rate and a reasonable MDE (you won't have the company's real data — estimate it plausibly and say you're estimating).
5. Using your estimated baseline and MDE, compute a required sample size with `statsmodels`.
6. One paragraph: given what you know (or can guess) about this product's traffic, is that sample size realistic in a reasonable timeframe? If not, what would you change about the test design?

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 45 min |
| 2 | 60 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 75 min |
| **Total** | **~4.75 h** |

After homework, take the [quiz](./quiz.md) and ship the [mini-project](./mini-project/README.md).
