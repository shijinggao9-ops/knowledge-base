# Exercise 3 — Build the Capstone Metrics Dashboard in SQL

**Goal:** Warm up by re-deriving Lecture 2's five queries against the provided AI Task Summaries dataset, then design and populate your own event schema for your capstone product, and write the queries that measure the PRD's stated success metric — all in SQL, never a spreadsheet.

**Estimated time:** 180 minutes (this is the longest exercise this week — budget for it).

## Setup

Confirm `mvp_users` (18 rows) and `mvp_launch_events` (50 rows) are loaded from the [week README](../README.md). Have `prd.md` from Exercise 2 open — Part B below asks you to measure its stated success metric specifically.

Create `c44-week-12/exercise-03/` with three files: `warmup-queries.sql`, `dashboard-schema.sql`, and `dashboard-queries.sql`.

## Part A — Warm-up on the provided dataset (45 min)

Write each as SQL in `warmup-queries.sql`, under a `-- Task N` comment. Do not copy Lecture 2's queries verbatim — write your own, structurally similar but adapted to the exact question asked.

1. **Trial rate by plan.** Adapt Lecture 2 Section 2.1's query to group by `plan` instead of reporting one overall number. *(Expected: 2 rows. Pro trial rate should come out higher than free — 9 of 10 pro users vs. 7 of 8 free users ever tried it, i.e. 90% vs. 87.5%, a much smaller gap than the week-2 retention gap you'll see next — worth noting in a comment.)*
2. **Day-0 activation by plan.** Same adaptation, for Section 2.2's query. *(Expected: 2 rows. Unlike trial rate, day-0 activation is nearly a tie between plans — free edges out pro slightly (5 of 8 vs. 6 of 10). Don't assume every cut moves in the same direction as the last one; this is the point of checking rather than guessing.)*
3. **The full WASU trend, one query, both weeks side by side** (not two separate queries) — use a single `GROUP BY` with the `CASE WHEN` from Lecture 2 Section 2.3, and add a column computing the week-over-week percentage change. *(Expected: 1 row per week, 2 rows total; week 1 = 16, week 2 = 7, roughly a −56% change.)*
4. **Never-activated users, named.** List the `user_id` and `plan` of every exposed user who never once appears with `event_name = 'summary_generated'`. *(Expected: exactly 2 rows — the two users who only ever logged in.)*
5. **Your own cut.** Pick a segmentation this lecture did NOT run (e.g., "users who activated on day 0 vs. users who activated later — does day-0 activation predict week-2 retention?") and write the query yourself. State your finding in a one-line SQL comment.

## Part B — Design and build your own dashboard (135 min)

1. **Design your event schema.** Using Lecture 2 Section 4's three design questions as your guide, write `CREATE TABLE` statements in `dashboard-schema.sql` for at least two tables: a users/accounts table (with at least one segmentation column, like `mvp_users.plan`) and an events table (with, at minimum, `user_id`, `event_name`, and a timestamp/date column). Name your core-value event and your activation event explicitly in a comment above the schema.
2. **Populate synthetic seed data.** Insert 15–25 users and 40–70 events representing a plausible hypothetical first two weeks of your MVP's usage — mirror the README's `mvp_launch_events` pattern: a mix of power users, regular users, one-and-done users, and at least 1–2 users who never engage with your core-value event at all. Your data should tell an honest, plausible story — it does not need to be a success story (a synthetic dataset showing a real, diagnosable problem, like this week's own AI Task Summaries example, is just as valid as one showing clean success, and often more useful practice).
3. **Write the dashboard queries** in `dashboard-queries.sql`, adapting Lecture 2's five-query pattern to your own schema and your PRD's stated success metric specifically:
   - Exposure and trial rate for your core-value event.
   - Day-0 (or first-session) activation rate.
   - A trend over your observation window (weekly or daily, whichever fits your data) for your chosen North Star.
   - A segmentation cut using your schema's segment column (plan, channel, role — whatever you designed).
   - **A query that directly answers your PRD's stated success metric**, using its exact wording from Exercise 2 as a guide for what to compute.
4. **Write a 150–250 word summary** at the top of `dashboard-queries.sql` (as a block comment), in the style of Lecture 2 Section 3 — one coherent paragraph reading the dashboard as one story, naming what's healthy and what's the actual problem, not five disconnected numbers.

## Expected outcome

A working schema and seed data you could hand to a classmate, who could load it, run your queries, and understand — from the summary paragraph alone — what your hypothetical MVP's first two weeks looked like and where the real risk is.

## Done when…

- [ ] `warmup-queries.sql` has all 5 tasks, each under a `-- Task N` comment, none copy-pasted unchanged from the lecture.
- [ ] Your own schema has a segmentation column and both a core-value event and an activation event, named explicitly.
- [ ] Seed data includes at least one user who never triggers the core-value event (your equivalent of `mvp_users` 17/18) — a dashboard with 100% adoption in synthetic data teaches you nothing about reading a funnel.
- [ ] The dashboard queries include a trend, a segmentation cut, and a query answering the PRD's exact stated success metric.
- [ ] The summary paragraph names both what's healthy and what the real risk is — not just good news, and not just bad news.
- [ ] You can explain, in one sentence, why you chose the North Star you did over at least one plausible alternative, the same way Lecture 2 Section 1 justified WASU over trial rate and total volume.

## Stretch

Write a short Python/pandas script, `dashboard-crosscheck.py`, that loads your seed data (via `sqlite3`/`psycopg2` + `pandas.read_sql`) and reproduces your trend query's result using `groupby` instead of `GROUP BY` — a quick cross-check that your SQL and your pandas logic agree, the same habit Week 6's pandas cross-checks built.

## Submission

Commit `warmup-queries.sql`, `dashboard-schema.sql`, and `dashboard-queries.sql` to your portfolio under `c44-week-12/exercise-03/`.
