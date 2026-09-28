# Mini-Project — 15 Product Questions from the Loopline Event Tables

> Answer 15 real product questions about Loopline using **only** `users`, `events`, and the SQL (plus optional pandas) you learned this week. Funnels, cohorts, activation, DAU/MAU — then write the one-paragraph health summary a real product team would ship in their weekly review.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it mirrors exactly what a PM analytics review actually looks like: a stakeholder doesn't hand you a dashboard, they hand you *questions*, and your job is turning each into a correct query, running it, and reporting the answer in plain English — then, at the end, synthesizing fifteen individual answers into one coherent verdict on product health. That last step is the one junior PMs skip and senior PMs are hired for.

---

## Deliverable

A directory in your portfolio `c44-week-06/mini-project/` containing:

1. `answers.sql` — all 15 queries, each under a `-- Q<n>: <the question>` comment.
2. `report.md` — for each question: the answer (the actual number/rows), and one sentence of interpretation ("Loopline's overall visitor-to-activated-task rate is 17.3%, meaning roughly 1 in 6 people who ever load the landing page eventually complete a task").
3. `health-summary.md` — the capstone: a single paragraph (150–250 words) summarizing Loopline's current product health, written as if for the founding team's weekly review (see the end of this file for the exact bar).

Everything runs against the seed tables from the [week README](../README.md). Works on PostgreSQL or SQLite; note which you used. The dataset's as-of date is **2025-03-16**.

---

## The 15 questions

Group A and B build the funnel and cohort picture; C is activation; D is DAU/MAU and the synthesis. Write one query per question unless noted.

### A. Funnel (Lecture 2)

1. How many distinct visitors landed on Loopline in total, and how many of those distinct visitors eventually completed at least one task (i.e., made it through the entire 6-step funnel)? Report both numbers and the overall conversion rate.
2. Compare the `signup_started → signup_completed` conversion rate to the `workspace_created → task_created` conversion rate (both step-to-step, per Lecture 2 §3). Which is weaker?
3. Which single step-to-step transition loses the **largest number of users in absolute terms** (not percentage)? Is that the same step you'd flag if you only looked at percentages?
4. Compute the `workspace_created → task_created` conversion rate for each of the 8 cohort weeks (Lecture 2 §6). Excluding the one week that's an outlier, what is the typical range for the other 7 weeks?

### B. Cohorts and retention (Lecture 3)

5. Build week-1 retention for all 8 cohorts. Which cohort has the highest **observable** week-1 retention, and what's its cohort size? (Watch for right-censoring — Lecture 3 §3.)
6. List every (cohort_week, week_number) cell from week 0 through week 4 that is **not yet observable** as of the dataset's as-of date, 2025-03-16.
7. Compare week-1 retention for the `2025-01-06` cohort against the `2025-01-20` cohort. State the percentage-point gap, then state — given both cohorts' sizes — whether you'd act on that gap or call it noise.
8. For the `2025-01-06` cohort (the one with enough history to observe 8+ weeks), compute its retention percentage for every week from week 1 through week 8. Does it flatten into a "retained core," or does it decay all the way toward zero? State which, with the numbers.

### C. Activation (Lecture 3)

9. Using the course's activation definition (≥3 tasks completed within 7 days of `signup_completed`), how many of the 59 registered users are Activated? What percentage of registered users is that?
10. Reproduce the Lecture 3 §4 comparison: what's the week-3/4 retention rate for Activated users versus everyone else? State both percentages.
11. List the `user_id` and `signup_date` of every Activated user, sorted by signup date.

### D. DAU/MAU and synthesis

12. Find the single busiest day in the dataset by DAU (engaged events only — Lecture 3 §5). Report the date, and DAU/WAU/MAU for that day.
13. Compute the DAU/MAU stickiness ratio for that busiest day. In one sentence, characterize what that ratio suggests about how habitual Loopline is for its monthly-active users — and say what a *different* stickiness number (e.g. 60%) would suggest instead, for contrast.
14. How many distinct users, across the whole dataset, ever fired at least one "engaged" event? What percentage of the 59 registered users does that represent, and what does the gap tell you about the group who signed up but never really used the product?
15. **Synthesis.** This is the write-up, not a query. Pull together your answers to Q1 (funnel), Q9 (activation), and Q13 (stickiness) into `health-summary.md` — see the bar below.

---

## Milestones

Pace yourself; don't try to do all 15 in one sitting.

- **Milestone 1 (45 min):** Questions 1–4. Funnel fluency, cohort-by-week practice.
- **Milestone 2 (45 min):** Questions 5–8. Retention cohort table, right-censoring judgment calls.
- **Milestone 3 (30 min):** Questions 9–11. Activation, reusing Lecture 3's exact query pattern.
- **Milestone 4 (45 min):** Questions 12–14. DAU/WAU/MAU, the engaged-events filter.
- **Milestone 5 (30 min):** Question 15. Write the health summary last, after every number is in front of you.

---

## Rules

- **Every question is answerable from `users` and `events` alone.** No external data, no invented numbers.
- **Name your columns and alias computed ones.** No naked `SELECT *` in the final answers.
- **Handle right-censoring deliberately** (Q5, Q6, Q7) — a cell that isn't observable yet is not the same thing as a cell that measured zero, and reporting it as zero is a real mistake, not a rounding nuance.
- **Every judgment-call question** (Q3's "same step?", Q7's "noise or signal?", Q8's "flatten or decay?") gets a one- or two-sentence stated reasoning in `report.md`, not just a bare number.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness | 35% | All 15 answers are right; the funnel/cohort/activation/DAU-MAU numbers are internally consistent with each other |
| Right-censoring handling | 15% | Q5–Q7 correctly separate "not yet observable" from "measured and low" |
| Interpretation | 20% | `report.md` states the answer *in words*, with the judgment calls reasoned through, not just a number |
| Health summary | 20% | `health-summary.md` reads like a real weekly product-health paragraph, cites specific numbers, and ends with a concrete next step |
| SQL craft | 10% | Readable queries — CTEs named for what they hold, no repeated boilerplate that should have been a CTE |

---

## The health-summary bar

`health-summary.md` is 150–250 words, written for people who will *not* read your SQL. It must:

1. State the overall funnel conversion rate and name the weakest step.
2. State the activation rate and what threshold defines "activated."
3. State the DAU/MAU stickiness number for the busiest observed day, with one sentence of context for what that number means for a work tool (not a social app).
4. End with **one specific, actionable recommendation** — not "improve engagement," but something like "investigate the `workspace_created → task_created` step specifically for the week-of-Feb-10 cohort, since that's the single largest outlier in the entire funnel."

A summary that lists four disconnected facts with no throughline, or that ends with a vague platitude instead of a specific next step, does not meet the bar — rewrite it until it does.

---

## Reflection (add to the bottom of `health-summary.md`, ~150 words)

1. Which of the 15 questions took the longest to get right, and what was the SQL mistake you made before you got there?
2. Where did right-censoring almost trip you up?
3. If you had one more event type tracked in this dataset that you don't currently have, what would it be, and what question would it let you answer that you can't answer today?

---

## Why this matters

This mini-project is the shape of real product analytics work: someone asks fifteen specific questions, and you return fifteen trustworthy answers plus one synthesized verdict. Do this once for real and the skill transfers directly — the SQL patterns here (funnel-by-cohort, retention triangle, activation threshold, DAU/MAU) are close to universal across every consumer and B2B product with an events pipeline. Keep `answers.sql`; the pattern (not the specific numbers) is what you'll reuse for the rest of your career.

When done: push, then take the [quiz](../quiz.md) and start [Week 7 — Experimentation: A/B design, sample size, significance](../../week-07-experimentation-ab-testing/).
