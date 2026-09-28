# Mini-Project — Design and Analyze the Stuck Task Alerts Experiment

> Write the full experiment design for a feature hypothesis, then analyze real (seeded) results from a 3-week rollout in Python and SQL, and deliver a ship/no-ship recommendation you'd defend in a roadmap review. This is the week's capstone — everything from Lecture 1's hypothesis template through Lecture 2's significance math through Lecture 3's traps comes together in one deliverable.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

## The brief

You are the PM for Loopline's **Stuck Task Alerts** feature (specced in Week 4, shipped behind a flag). Before rolling it out to all teams, Loopline's leadership ran a 3-week randomized experiment across 40 teams, following the design you'd have written in Lecture 1: 20 control teams (no alerts), 20 treatment teams (alerts on), randomized by **team** because the Slack alert posts to a shared channel (Lecture 1 §3 explains why individual-user randomization would contaminate here).

The data is loaded (see the [week README](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/README.md)) as `stuck_alert_experiment`, one row per team: how many times a task crossed the 48-hour stuck threshold during the window (`incidents_logged`), how many of those got a status update within 24 hours of the alert threshold (`incidents_unstuck_24h` — the primary metric), and a guardrail (`task_completion_rate`, the team's overall completion rate during the window).

Your job: write the design doc this test *should have had* (even though it already ran — writing it retroactively is still the right exercise, and you'll need it to interpret the result correctly), then analyze the actual data two ways, and recommend what Loopline does next.

## Deliverable

A directory in your portfolio `c44-week-07/mini-project/` containing:

1. `design-doc.md` — the experiment design (Part 1 below).
2. `analysis.py` (or `.ipynb`) — all the analysis code (Part 2 below), runnable end to end.
3. `report.md` — the results, both analyses' numbers, and your ship/no-ship recommendation (Part 3 below).
4. `notes.md` — a short reflection (see the end).

Everything runs against the seed table from the [week README](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/README.md). Works on PostgreSQL or SQLite; note which you used for the SQL portion.

---

## Part 1 — Write the design doc (before touching the data)

Even though this test already ran, write the design doc as if you were writing it the week before launch — this forces you to commit to interpretation choices *before* you look at results, which is the whole discipline of Lecture 1.

In `design-doc.md`, include:

1. **Hypothesis** — the if/then/because sentence (Lecture 1 §1). Use the mechanism actually described in the Week 4 PRD: the alert removes the need for a manager to remember to check a view.
2. **Primary metric** — defined precisely: "% of stuck incidents (tasks crossing the 48-hour threshold) that receive a status update within 24 hours of the alert." State the exact SQL that would compute it from a raw incidents table.
3. **Guardrail metric(s)** — at minimum, overall task completion rate (already in the seed data). Name at least one more you'd want if you were designing this for real (e.g., Slack channel mute/leave rate) and explain why, even though it's not in this week's dataset.
4. **Unit of randomization** — team, and a two-sentence justification referencing SUTVA/contamination (Lecture 1 §3).
5. **MDE and required sample size** — the test targeted an 8-point lift (from the Week 4 PRD's promise). Using Lecture 2's formula (treating each team's rate as one independent unit, since that's the unit of randomization here — not the incident count), what team-level effect size would an 8-point lift on a ~28% baseline with roughly the sd you'll observe in the data represent, and does 20 teams per arm look, on paper, like enough? (You'll confirm this precisely in Part 2 — this is your *before-the-fact* estimate.)

## Part 2 — Analyze the seed data two ways

In `analysis.py`, do **both** of the following analyses, and make sure your code clearly separates them — you'll compare them directly in your report.

### Analysis A — Correct: team-level analysis (matches the unit of randomization)

1. Load `stuck_alert_experiment` (via SQL query or a CSV export — your choice) into a DataFrame or two arrays.
2. Compute each team's individual unstuck-rate: `incidents_unstuck_24h / incidents_logged`.
3. Compute the mean and standard deviation of that rate, separately for control and treatment (n=20 each).
4. Run a **Welch's t-test** (`scipy.stats.ttest_ind(..., equal_var=False)`) comparing the two arms' team-level rates.
5. Compute the 95% confidence interval of the difference in means.
6. Compute the **achieved statistical power** of this test at its actual sample size and observed effect size (`statsmodels.stats.power.TTestIndPower`).
7. Analyze the **guardrail metric** (`task_completion_rate`) the same way — is there a significant difference that should worry you?

### Analysis B — Incorrect (for comparison only): naive pooled incident-level analysis

1. Sum `incidents_logged` and `incidents_unstuck_24h` across all teams in each arm, ignoring which team each incident came from.
2. Run a two-proportion z-test (`statsmodels.stats.proportion.proportions_ztest`) on these pooled totals.
3. **Do not use this result to make a decision** — the point of running it is to see, side by side, how differently it answers the same question compared to Analysis A, and to understand *why* (Lecture 2 §4: pseudoreplication).

### Also, in SQL

Write the SQL query (Postgres or SQLite) that produces the team-level rates used in Analysis A directly from `stuck_alert_experiment` — the `GROUP BY`-free, one-row-per-team aggregation, plus a second query that produces the pooled Analysis B totals with `GROUP BY arm` and `SUM(...)`. Include both in `analysis.py` as comments or in a `queries.sql` alongside it.

## Part 3 — Write the report and recommendation

In `report.md`:

1. **Results table** — both analyses' means, test statistics, and p-values, side by side.
2. **Which analysis is correct, and why** — reference Lecture 2 §4 directly.
3. **Achieved power** — state it plainly, and what it means for how much weight this result can bear.
4. **Guardrail check** — did the guardrail metric raise any concern?
5. **Ship/no-ship recommendation** — this is the section your VP actually reads. Do not write "it's inconclusive, more data needed" as your entire answer — that's true but incomplete. Give a real recommendation: ship to everyone now, ship to a larger rollout while continuing to measure, hold and extend the test, or kill it — and defend your choice against the two most obvious alternatives. (There is a genuinely defensible case for more than one answer here; the rubric rewards the *reasoning*, not a specific choice.)
6. **One paragraph**: if you were rerunning this experiment from scratch, what would you change about its design, sized correctly this time?

---

## Milestones

- **Milestone 1 (30 min):** Write `design-doc.md` — Part 1, all five sections.
- **Milestone 2 (60 min):** Analysis A — team-level t-test, CI, achieved power, guardrail check.
- **Milestone 3 (30 min):** Analysis B — naive pooled comparison, plus the two SQL queries.
- **Milestone 4 (45 min):** `report.md` — results table through recommendation.
- **Milestone 5 (15 min):** `notes.md` reflection.

---

## Rules

- **Team-level rates are the unit of analysis for Analysis A** — do not average or sum across teams in a way that hides the per-team variance (that's the whole point of Analysis A vs. B).
- **State every assumption** — the MDE-to-sample-size back-of-envelope in Part 1, Step 5, and the recommendation's threshold in Part 3, Step 5, both require a judgment call. Write it down.
- **Report the CI, not just the p-value**, everywhere you report a significance test.
- **Run Analysis B, but do not base your recommendation on it.** Its only job in this deliverable is the comparison in Part 3, Step 2.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Design doc completeness | 15% | All five sections present, hypothesis is falsifiable, MDE reasoning shown |
| Analysis A correctness | 25% | Correct team-level t-test, CI, and achieved-power calculation, matching the expected spot-checks |
| Analysis B + comparison | 15% | Naive pooled result computed correctly, and the pseudoreplication difference is explained, not just shown |
| Guardrail check | 10% | Guardrail analyzed with the same rigor as the primary metric |
| Recommendation quality | 25% | A real, defended recommendation — not "more data needed" alone; alternatives named and argued against |
| SQL queries | 10% | Both queries (team-level and pooled) run and produce the same numbers as the Python analysis |

---

## Expected results (spot checks)

- Analysis A: control mean ≈ **0.277**, treatment mean ≈ **0.334**, Welch's t ≈ **0.78**, p ≈ **0.44** — not significant.
- Analysis A guardrail: control ≈ **0.709**, treatment ≈ **0.729**, p ≈ **0.18** — no guardrail violation.
- Analysis A achieved power at this sample size and effect: well under the 0.80 target — this test could not reliably have detected an effect this size even if it were real.
- Analysis B (naive, do not use for the decision): pooled control ≈ **24.5%** (36/147), pooled treatment ≈ **35.7%** (60/168), z ≈ **2.16**, p ≈ **0.031** — *looks* significant, and is wrong to trust, because it pretends 147 and 168 independent samples exist when only 20 and 20 do.

If your Analysis A numbers don't match, double check you're computing **one rate per team** (20 numbers per arm) and not accidentally pooling first.

---

## Reflection (`notes.md`, ~200 words)

1. Before you ran Analysis B, did you expect it to agree with Analysis A? What does the gap between them teach you about analyzing clustered/team-level data?
2. Which was harder to write honestly: the statistical analysis, or the recommendation? Why?
3. If your VP had asked for this analysis with a one-day turnaround instead of the 3-week test window, what would you have told them was and wasn't possible?
4. This test's real result — directionally positive, not statistically significant, guardrails clean — is extremely common in real experimentation. What's the risk of a team's *default* response to results like this always being "no clear win, don't ship"?

---

## Why this matters

Most real A/B tests do not come back with the clean, obviously-significant win a case study shows you. They come back looking like this one — a plausible positive direction, wide uncertainty, and a business deadline that doesn't care how wide your confidence interval is. The skill this week actually builds isn't running a z-test; it's holding two things at once: rigorous honesty about what the data does and doesn't prove, and a real, defensible recommendation anyway. That's the job.

When done: push, then take the [quiz](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/quiz.md).
