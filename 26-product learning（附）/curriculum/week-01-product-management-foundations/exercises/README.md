# Week 1 Exercises

Three exercises, meant to be done in order. Each is a guided rep against a real artifact — a real product you use, or a real (small, seeded) dataset — not a thought experiment. Budget ~1–1.5 hours each.

| # | Exercise | Practices | Dataset |
|--:|----------|-----------|---------|
| 1 | [Map a Product's Users and Value](exercise-01-map-a-products-users-and-value.md) | Segments, personas, JTBD, value proposition (Lecture 2) | None — a real product of your choosing |
| 2 | [Classify Features by the VVF Lens](exercise-02-classify-features-by-vvf-lens.md) | VVF+U scoring, defensible trade-off calls (Lecture 3) | Loopline feature backlog (SQL, seeded in the exercise) |
| 3 | [Infer Strategy from a Product's Metrics](exercise-03-infer-strategy-from-metrics.md) | Lifecycle diagnosis, reading metrics honestly (Lecture 3) | Loopline 12-week metrics (SQL, seeded in the exercise) |

## How to work them

1. Read the linked lecture first — each exercise assumes you've done the reading, not just skimmed it.
2. For Exercises 2 and 3, you'll create a small SQLite or PostgreSQL database — the `CREATE TABLE` / `INSERT` statements are inside each exercise, ready to paste. You do **not** need prior SQL experience; every query you need to run is given to you. Your job is the product judgment on top of the output, not writing the SQL from scratch (that skill is built starting Week 6).
3. Deliverables are plain Markdown files. Keep them tight — a strong answer here is precise and evidenced, not long.
4. Commit each exercise's output to your portfolio, in a folder named for the exercise (see the **Submission** section at the bottom of each file).

## Why data lives in SQL here, not a spreadsheet

Every dataset this week — and every week after it — is stored and queried as a real table (SQLite or PostgreSQL), never a spreadsheet standing in as a database. This isn't a stylistic preference: a spreadsheet silently breaks the moment two people sort it differently, and it has no real way to enforce "activation rate is always between 0 and 100." A table with a schema does. Spreadsheets have a place — as a presentation or export surface — and that's taught on its own in [C41 Crunch Excel](../../../../C41-CRUNCH-EXCEL/). In this course, if it's a system of record, it's SQL.
