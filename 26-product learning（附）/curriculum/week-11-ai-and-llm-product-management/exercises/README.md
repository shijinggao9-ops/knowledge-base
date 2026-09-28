# Week 11 Exercises

Three exercises, meant to be done in order — each builds on the artifact the last one produced. Budget ~1.5 hours each.

| # | Exercise | Practices | Dataset |
|--:|----------|-----------|---------|
| 1 | [Scope an AI Feature and Its Fallback](exercise-01-scope-an-ai-feature.md) | The fit checklist, human-in-the-loop design, deterministic fallback (Lecture 1) | None — Loopline Copilot, scoped from scratch |
| 2 | [Build an Eval Set for an LLM Feature](exercise-02-build-an-eval-set.md) | Golden set design, grading, SQL quality tracking (Lecture 2) | `eval_cases` / `eval_runs` / `eval_results` (SQL, seeded in the exercise) |
| 3 | [Design Guardrails for Failure and Cost](exercise-03-design-guardrails.md) | Human-in-the-loop tiers, cost caps, safety guardrails (Lecture 3) | `ai_usage_log` (SQL, seeded in the exercise) |

## How to work them

1. Read the linked lecture first — each exercise assumes you've done the reading, not just skimmed it.
2. Exercises 2 and 3 build a small SQLite or PostgreSQL database — the `CREATE TABLE` / `INSERT` statements are inside each exercise, ready to paste. You do not need prior data-engineering experience; the SQL you need is either given directly or is a light variation on a query from the matching lecture.
3. Deliverables are plain Markdown (and one `.sql` file in Exercises 2–3). Keep them tight — a strong answer here is precise and evidenced, not long.
4. Commit each exercise's output to your portfolio, in a folder named for the exercise (see the **Submission** section at the bottom of each file).

## Why data lives in SQL here, not a spreadsheet

An eval set and a usage log are exactly the kind of data this course insists stays in SQL, not a spreadsheet: rows with real relationships (a result belongs to a run, a run belongs to a case), values you'll filter and aggregate by category or by day, and a history you need to trust wasn't hand-edited after the fact. A spreadsheet "eval tracker" a teammate updates by typing over old numbers has no audit trail and no way to enforce that every result actually references a real case. A table with a schema does both for free. Spreadsheets are a presentation surface, taught on their own in [C41 Crunch Excel](../../../../C41-CRUNCH-EXCEL/); in this course, a system of record is SQL.
