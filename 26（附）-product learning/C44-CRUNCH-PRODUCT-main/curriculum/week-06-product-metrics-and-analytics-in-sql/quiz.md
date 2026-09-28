# Week 6 — Quiz

Fifteen questions. Lectures closed. Aim for 12/15 before starting Week 7. A mix of multiple-choice and short "what would this query return" — the answer key explains the *why*, not just the letter.

---

**Q1.** Which of these is the strongest North Star Metric candidate for a team task-management app?

- A) Total registered users (cumulative)
- B) Weekly Engaged Users (distinct users completing ≥1 task in a trailing 7-day window)
- C) App store downloads this month
- D) Monthly recurring revenue

<details>
<summary>Answer</summary>

**B** — Weekly Engaged Users reflects delivered customer value (a completed task), is a leading indicator, and is a single trackable number. Registered users only grows; downloads measure curiosity; MRR is a real but lagging metric, not a value signal on its own.

</details>

---

**Q2.** A metric is a **vanity metric** if:

- A) It's measured in dollars
- B) It requires SQL to compute
- C) It goes up almost no matter what you do, and tells you nothing actionable when it moves
- D) It's reported to executives

<details>
<summary>Answer</summary>

**C** — the defining test of a vanity metric is "if this goes up, do you know what to do differently?" If it just goes up regardless, it's vanity.

</details>

---

**Q3.** A team is evaluated on "tasks created per user" and responds by auto-creating a task for every calendar event synced, with no user request. This is an example of:

- A) A leading indicator
- B) A gameable metric being gamed
- C) A vanity metric
- D) A properly designed guardrail

<details>
<summary>Answer</summary>

**B** — this is a gameable metric being gamed: the volume metric moves, but the change is one a reasonable person would call a regression (unwanted auto-created tasks), not real value delivered.

</details>

---

**Q4.** In Loopline's `events` table, why does `user_id` have **no** foreign key relationship to `users`?

- A) It's a schema bug that should be fixed
- B) `events` tracks every visitor from their first landing-page view, most of whom never finish signing up and so never get a `users` row
- C) `users` is populated before `events`
- D) SQLite doesn't support foreign keys

<details>
<summary>Answer</summary>

**B** — `users` only holds people who *finished* signing up; `events` tracks everyone from their first landing-page touch, so most `user_id`s in `events` never appear in `users` at all. That's intentional, not a bug.

</details>

---

**Q5.** `SELECT event_name, COUNT(*) FROM events GROUP BY event_name;` for the funnel step `task_completed` will, on Loopline's data, return a number that is:

- A) Exactly equal to `COUNT(DISTINCT user_id)` for that step, always
- B) Larger than or equal to `COUNT(DISTINCT user_id)` for that step, because some users complete more than one task
- C) Always smaller than `COUNT(DISTINCT user_id)`
- D) Meaningless for funnel analysis, in every case

<details>
<summary>Answer</summary>

**B** — `task_completed` can fire multiple times per user (they complete more than one task), so `COUNT(*)` (events) is greater than or equal to `COUNT(DISTINCT user_id)` (people).

</details>

---

**Q6.** `ROW_NUMBER() OVER (PARTITION BY user_id, event_name ORDER BY event_time ASC)` assigns `1` to:

- A) The most recent event of each type, per user
- B) The earliest event of each type, per user
- C) A random event per user
- D) The event with the lowest `event_id`, regardless of time

<details>
<summary>Answer</summary>

**B** — `ORDER BY event_time ASC` inside the window means the earliest row in each partition gets `rn = 1`.

</details>

---

**Q7.** A funnel query joins `events` to `users` as its **very first step**, before counting `landing_page_view`. What does this actually compute?

- A) The correct total visitor count
- B) Landing-page views by people who eventually registered — a smaller, different number than total visitors
- C) An error, because the join is invalid
- D) The same number as not joining at all

<details>
<summary>Answer</summary>

**B** — joining to `users` before counting `landing_page_view` silently restricts the count to people who eventually registered, throwing away the majority of the top-of-funnel who never converted. That's a materially different, smaller number than "total visitors."

</details>

---

**Q8.** A retention cohort table's newest cohort (the most recent signup week) typically shows the **weakest** retention numbers in the later weeks/columns of the grid mainly because:

- A) Newer users are inherently less engaged
- B) Not enough time has passed for that cohort to reach those later weeks yet — the cells are right-censored, not truly zero
- C) The product got worse right before that cohort signed up
- D) Cohort tables always trend downward by design

<details>
<summary>Answer</summary>

**B** — right-censoring: the newest cohort hasn't had enough elapsed time to reach the later weeks of the observation window, so those cells reflect incomplete data, not confirmed poor retention.

</details>

---

**Q9.** Which SQL fix correctly addresses right-censoring in a retention report?

- A) Reporting every cell's raw percentage with no distinction
- B) Deleting the newest cohort from the report entirely
- C) Computing an "is this cell observable as of today" flag, and excluding or greying out unobservable cells rather than showing them as a measured zero
- D) Rounding all percentages to the nearest 10%

<details>
<summary>Answer</summary>

**C** — compute an explicit observability flag per cell and treat unobservable cells differently from measured, low, cells. Deleting the cohort or rounding doesn't solve the underlying misread.

</details>

---

**Q10.** Loopline's activation threshold (≥3 tasks completed within 7 days of signup) was chosen because:

- A) It's a round, easy-to-remember number
- B) A retention-lift comparison showed users crossing that threshold retained at a substantially higher rate weeks later than users who didn't
- C) It matches a number used by a well-known competitor
- D) It was the median number of tasks completed across all users

<details>
<summary>Answer</summary>

**B** — the threshold came from evidence: a real (if small-sample) retention-lift comparison showing 3+ tasks in week 1 correlated with much higher week-3/4 retention, not from a round-number guess or a competitor's number.

</details>

---

**Q11.** DAU/MAU should generally be computed using:

- A) Every event in the table, including `landing_page_view`, for the widest possible reach
- B) Only in-product "engaged" events (e.g. `login`, `task_created`, `task_completed`), excluding pre-signup marketing touches
- C) Only `signup_completed` events
- D) Only events from paying (`pro` plan) users

<details>
<summary>Answer</summary>

**B** — DAU/MAU should count genuine in-product engagement events, not pre-signup marketing/landing-page traffic, which would inflate the denominator with people who never really used the product.

</details>

---

**Q12.** If DAU/MAU stickiness is calculated by mistakenly **including** `landing_page_view` events, and a blog post drives a traffic spike, the resulting effect on the reported ratio is:

- A) No effect — pageviews don't count toward either DAU or MAU
- B) The ratio would appear to **improve** (go up), correctly reflecting better engagement
- C) MAU balloons with one-time visitors who never engage further, making the stickiness ratio look **worse** even though nothing about actual product usage changed
- D) DAU and MAU would move by exactly the same amount, leaving the ratio unchanged

<details>
<summary>Answer</summary>

**C** — including `landing_page_view` inflates MAU with one-time visitors who took no further action, which drags stickiness *down* (worse-looking), even during a period when the traffic itself might be a marketing win — a classic case of a wrong-events bug producing a misleading, not just imprecise, number.

</details>

---

**Q13.** A DAU/MAU stickiness ratio of roughly 20% for a work task-management tool most reasonably suggests:

- A) The product is failing and near abandonment
- B) Users open it on average a few times a week, not daily — plausible and not alarming for a work tool
- C) The product has a daily-habit usage pattern, like a messaging app
- D) The number is meaningless without comparing it to a spreadsheet

<details>
<summary>Answer</summary>

**B** — roughly 20% stickiness (about 1 day in 5) reads as a several-times-a-week habit, which is normal and healthy for a work tool — it would be a concerning number for a messaging or social app, where daily habitual use is the expectation.

</details>

---

**Q14.** In Loopline's growth-accounting metric-tree identity, `WEU (this week) = New + Retained + Resurrected − Churned`, "Resurrected" refers to:

- A) Users engaged this week who were also engaged last week
- B) Users engaged this week for the very first time ever
- C) Users engaged this week, not engaged last week, but engaged at some earlier point in the past
- D) Users who canceled their subscription

<details>
<summary>Answer</summary>

**C** — Resurrected users returned this week after a gap; New users have never engaged before at all; Retained users were active in both the current and prior week.

</details>

---

**Q15.** Why does this course teach funnel/cohort/activation/DAU-MAU analysis in SQL and pandas, and explicitly never in a spreadsheet?

- A) Spreadsheets can't open CSV files
- B) A retention cohort grid needs cell-by-cell manual formulas that silently produce wrong right-censoring judgments at scale, while the SQL version is a dozen lines and correct at any size
- C) Spreadsheets don't support numbers over 1,000
- D) SQL is required by law for product analytics

<details>
<summary>Answer</summary>

**B** — a retention cohort grid at scale needs correct, consistent right-censoring logic across every cell; a spreadsheet's manual, copy-pasted formulas make that error-prone and don't verify or scale the way a parameterized SQL query does.

</details>

**Scoring:** 12+ → start Week 7. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; the concepts compound fast next week, when you start measuring whether a *change* caused a metric to move.

---
