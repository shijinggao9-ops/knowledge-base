# Week 6 — Exercises

Three guided exercises, ~1–1.5 hours each. **Do every step yourself, in the actual app** — don't just read the formulas. The auto-expansion and auto-fill behaviors this week teaches are things you have to *watch happen* to trust them.

1. **[Exercise 1 — Convert a range to a Table](exercise-01-range-to-table.md)** — turn the `Orders` range into a real Table, rename it, style it, add a Total Row, and prove it auto-expands.
2. **[Exercise 2 — Rewrite formulas as structured refs](exercise-02-structured-ref-formulas.md)** — replace A1-style formulas with `[@Column]`/`Table[Column]` syntax and stress-test them against inserted rows and columns.
3. **[Exercise 3 — Summarize with SUMIFS/COUNTIFS](exercise-03-sumifs-summary.md)** — build the Region × Category summary matrix from Lecture 3 on your own, from a blank sheet.

## Before you start

- You've completed all three lectures.
- You have the `Orders` range from the week README loaded (`A1:I25`, checksum `SUM` = **5240.60**).
- Excel 365/2021/web, or Google Sheets with the Tables feature available (**Insert → Tables**). If your Sheets version doesn't show that menu item, do Exercises 1–3 in Excel and read Challenge 2 for the named-range fallback pattern.

## Suggested workflow

- Do each step in order — later exercises assume the Table from Exercise 1 already exists and is named `Orders`.
- After every structural change (insert row, insert column, add a new record), **re-check the checksum** (`SUM(Orders[Total])` should read `5240.60` before you add anything new, and the correct new total after you do). If it doesn't match, something broke — find it before moving on.
- Keep the workbook from this exercise set; the mini-project builds directly on top of it.
