# Challenge 1 — Build a Self-Growing Tracker

**Time:** ~60 minutes. **Difficulty:** Medium. **You design the dataset.**

## The scenario

Every real tracker — a personal budget, a habit log, a project's task list, a small business's expense sheet — starts small and grows for months or years. The test of whether you actually learned this week's material isn't whether you can build a Table that looks right *today*; it's whether the Table you build today is still correct after fifty more rows get added by someone who has never read this course.

## Your task

Design and build a **self-growing tracker** from a blank sheet — your choice of subject (a personal weekly expense log, a workout log with sets/reps/weight, a reading log with book/pages/date-finished, a freelance time log with client/hours/rate — anything with at least 4-5 columns and a natural "one new row per event" shape).

### Requirements

1. **At least 15 seed rows** of your own invented data, entered as a Table from the start (`Ctrl+T` on a plain range first, then rename it — you may not skip the "why tables" step, even though it's your own design).
2. **At least one computed column** using a structured-reference formula referencing `[@Column]` names — e.g., a `Total` = `[@Quantity] * [@UnitCost]`, or a `Duration` = `[@EndTime] - [@StartTime]`. It must auto-fill down the column and auto-fill into new rows without you touching it after the first row.
3. **A Total Row** with the correct aggregate function per column (Sum where it makes sense, Average or Count where it doesn't).
4. **A summary section** (same sheet or a new one) with **at least 3 `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` formulas**, each filtering by at least one criterion, all built from structured references — no hard-coded ranges.
5. **The growth test:** after everything above is built and verified correct, add **5 new rows** to the Table, one at a time, with realistic new data. After each one, confirm (and note in `challenge-01.md`) that:
   - The Table's border/banding/Total Row extended automatically.
   - Your computed column's formula filled into the new row without being re-typed.
   - Every summary formula's numbers changed to reflect the new data, with zero formula edits.

## What "self-growing" actually means here

A tracker fails this challenge if any of the following is true after you add the 5 test rows:

- A summary number didn't change when it should have.
- You had to select-and-fill-down a formula manually to get it into a new row.
- Any cell shows `#REF!`, `#VALUE!`, or a stale number that doesn't match a hand-recomputed check.

If any of those happen, that's not a failure of the challenge — it's data. Diagnose *why* (usually: a formula somewhere used an A1-style range instead of a structured reference, or a criterion referenced a cell outside the Table that didn't get included). Fix it, and note what you found in `challenge-01.md` — a bug you found and fixed is worth more than a tracker that happened to work by luck.

## Constraints

- No downloaded template — build the structure yourself, the way you built `Orders` in the week README.
- At least one `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` formula must use **two or more criteria**, not just one.
- The computed column must genuinely compute something from at least two other columns — not just copy a value.

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Table setup | Data typed as a plain range, never converted | A real, renamed Table with a style and Total Row |
| Structured references | Summary formulas reference `A2:A16` | Every formula uses `Table[Column]`/`[@Column]` |
| Growth test | Claimed to work, never actually tested | 5 real rows added, each confirmed, documented |
| Debugging | A broken formula left unexplained | A found-and-fixed bug, explained in `challenge-01.md` |

## Submission

Commit the workbook plus `challenge-01.md` (your design notes, the growth-test log for each of the 5 added rows, and anything you had to fix) to your portfolio under `c41-week-06/challenge-01/`.
