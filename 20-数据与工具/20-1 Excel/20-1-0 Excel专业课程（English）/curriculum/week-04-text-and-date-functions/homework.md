# Week 4 — Homework

A practice set to tie the week together. Spread this across the week rather than doing it all in one sitting — text and date functions only really stick once you've hit a handful of different messy shapes and worked out the fix each time. Budget roughly 5 hours total.

## How to use this

Each task below is short (10–30 minutes) and targets a specific skill from the lectures. Do them in a fresh area of your workbook (a new sheet per part, or a dedicated `Homework` sheet split into labeled blocks) so nothing collides with the exercises, challenges, or mini-project.

## Part A — Parsing reps (≈1 hour)

1. Build a column of 8 product SKUs shaped like `"WIDGET-BLUE-042-XL"` (category-color-serial-size, dash-separated, variable-length pieces). Extract each of the four pieces into its own column using `TEXTSPLIT`. Then redo just the `category` extraction using `FIND`+`LEFT` instead, and confirm both approaches agree.
2. Build a column of 6 values shaped like `"Q1-2026-Actual"` and `"Q3-2026-Forecast"` (quarter-year-type). Use `MID` and `FIND` to pull out the quarter number (as an actual number, `1`–`4`, not text `"Q1"`) and the year (as an actual number). Confirm with `ISNUMBER()` that both extracted columns are real numbers, not text that merely looks numeric.
3. Take a single cell containing `"Total: $12,450.75 (paid)"` and extract just the numeric amount (`12450.75`, as a real number usable in `SUM`) using a combination of `FIND`, `MID`, and `SUBSTITUTE` to strip the `$` and `,`. *(Hint: `VALUE()` from Lecture 2/3 converts the cleaned text into a real number at the end.)*

## Part B — Cleaning reps (≈1.5 hours)

4. Build a 10-row column of company names with deliberately inconsistent casing and spacing (mix `ALL CAPS`, `all lowercase`, extra internal spaces, leading/trailing spaces). Clean all 10 with one formula pattern (`PROPER(TRIM(CLEAN(...)))`), then write a `=LEN()` check column confirming no row still has extra whitespace.
5. Build a 6-row column of email addresses where 2 rows have a trailing space, 2 rows have inconsistent casing, and 2 rows are already clean. Write a single cleaning formula, then write a **duplicate-detection** formula using `COUNTIF` against your *cleaned* column that would catch two rows that are the same email but were originally formatted differently (e.g., `"Ana@Crunch.io "` and `"ana@crunch.io"`) — confirm it correctly flags them as duplicates only *after* cleaning, and would have missed them if you'd checked the raw column instead.
6. Take a column of 8 full names and build a `TEXTJOIN`-based "Initials" column (e.g., `"Grace Hopper"` → `"GH"`) using `LEFT` on each split name piece.

## Part C — Date math reps (≈1.5 hours)

7. Build a column of 10 hire dates spanning several different years, including at least one leap year (2024, 2028, etc. — a year divisible by 4). For each, compute: age of employment in complete years (`DATEDIF`, unit `"Y"`), and the exact number of days employed (`TODAY() - HireDate`). Confirm the leap-year row's day count is 1 higher than a non-leap-year row with the identical month/day span — explain in one sentence why.
8. Build a small table of 5 project start dates and 5 project durations (in calendar days). Compute each project's end date with simple addition (`StartDate + Duration`), then compute the **last business day on or before** that end date using `WORKDAY` (the sibling function to `NETWORKDAYS` — look up its signature in [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-04-text-and-date-functions/resources.md) if you haven't seen it yet; it's a short jump from what Lecture 3 covered).
9. Using `EOMONTH`, build a 12-row column listing the last day of every month in 2026 (January through December), starting from a single seed date of `2026-01-01` and one filled-down formula — do not type 12 separate dates by hand.

## Part D — Reflection (≈30 min)

10. In a few sentences: of the three lectures this week (parsing, cleaning, dates), which felt most naturally like "real work" you can already picture doing on an actual messy file you own? Name the specific file/dataset if you have one in mind.
11. You now know two different ways to fix "dates stored as text" — `DATEVALUE` (Lecture 3) and manually rebuilding with `DATE`+`LEFT`/`MID`/`VALUE` (used in the mini-project for the ambiguous `MM/DD/YYYY` case). Write one sentence on when you'd reach for each.

## Submission

Keep your homework work in a `Homework` area of your workbook (or a separate file) — no formal submission format required, but be ready to reference specific tasks if asked in review.
