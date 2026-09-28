# Week 10 Exercises

Three exercises, meant to be done in order. Each is a guided rep against a real artifact — a pricing table you design from scratch, or a real (small, seeded) dataset — not a thought experiment. Budget ~1.5 hours each.

| # | Exercise | Practices | Dataset |
|--:|----------|-----------|---------|
| 1 | [Design a Three-Tier Pricing Table](exercise-01-design-a-pricing-tier.md) | Packaging, value-metric gating, anchoring, willingness-to-pay (Lecture 1) | None — your own design, plus a small Van Westendorp drill |
| 2 | [Map and Instrument a Growth Loop](exercise-02-map-a-growth-loop.md) | Loop diagramming, k-factor, cycle time (Lecture 2) | Loopline `referral_events` (SQL, seeded in Lecture 2) |
| 3 | [Model a Pricing Change in SQL](exercise-03-model-a-pricing-change.md) | Tier migration, risk-adjusted revenue modeling (Lecture 3) | Loopline `subscriptions` (SQL, seeded in Lecture 3) |

## How to work them

1. Read the linked lecture first — each exercise assumes you've done the reading, not just skimmed it.
2. For Exercises 2 and 3, you're querying tables you already seeded while reading Lectures 2 and 3 — if you skipped straight to the exercises, go back and run the `CREATE TABLE`/`INSERT` blocks first.
3. Exercise 1 has no fixed answer key — it's your own packaging design, judged on reasoning, not on matching a specific price point. Exercises 2 and 3 are SQL-scored: your queries against the seeded data should produce the same numbers shown in the lecture, because everyone is working from the same seed.
4. Deliverables are plain Markdown/SQL files. Keep them tight — a strong answer here is precise and evidenced, not long.
5. Commit each exercise's output to your portfolio, in a folder named for the exercise (see the **Submission** section at the bottom of each file).

## Why this week's models live in SQL and pandas, not a spreadsheet

A pricing model and a growth-loop projection are exactly the kind of structured, queryable, testable data this course insists on keeping in a real database or a real dataframe — never a spreadsheet standing in as the system of record. The tier-migration model in Exercise 3 has real relationships (an account has one segment, one seat count, one resulting tier, one resulting price) that a schema enforces and a spreadsheet does not; the risk-adjustment logic is a `CASE` expression you can read and re-run, not a cell formula that silently breaks the moment someone inserts a row above it. Spreadsheets have a place — as a presentation or export surface — and that's taught on its own in [C41 Crunch Excel](../../../../C41-CRUNCH-EXCEL/). In this course, if it's a system of record, it's SQL and/or Python.
