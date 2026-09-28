# Week 1 — Homework

A practice set to tie the week together. Spread this across the week rather than doing it all in one sitting — spaced repetition on the shortcuts and formatting habits is exactly what makes them automatic. Budget roughly 5 hours total.

## How to use this

Each task below is short (10–30 minutes) and targets a specific skill from the lectures. Do them in a fresh area of your workbook (a new sheet per task, or a dedicated `Homework` sheet split into labeled blocks) so nothing collides with the exercises, challenges, or mini-project.

## Part A — Data types and entry (≈1 hour)

1. In a fresh block, deliberately try to break each data type and observe what happens, then explain it in a one-line comment next to the cell:
   - Type `01/04` into an empty cell. What did it become? Fix it so it displays as the fraction one-quarter instead.
   - Type `007` into an empty cell. What did it become? Fix it so it stays as literal text `007`.
   - Type `50%` into an empty cell, then check the Name Box / formula bar to see the actual stored value. What is it?
   - Type `=TRUE` — Excel/Sheets treat this differently from typing `TRUE` directly in some contexts; check whether your app shows it as a formula or a literal boolean, and note which.
2. Enter today's date three different ways in three cells (`3/4/2026`, `March 4, 2026`, `2026-03-04`) and confirm all three are recognized as the *same* underlying serial number by subtracting one from another in a nearby cell (`=B1-A1` should be `0`). *(You haven't formally learned formulas yet — this one early peek is fine, just type the formula shown.)*

## Part B — Navigation drills (≈1 hour)

3. Build a data block at least 40 rows tall with one intentional gap (like Exercise 2). Practice jumping to the top, bottom, and across the gap using only `Ctrl/Cmd+Arrow` until you can do it without looking at your hands.
4. Time yourself selecting a 20×5 range three different ways: (a) click-and-drag, (b) Name Box typed range, (c) keyboard navigate + `Shift+Ctrl/Cmd+Arrow`. Which was fastest? Which will scale best to a 10,000-row sheet, and why?
5. Create 5 sheets, rename each to a real month name, color each a different color, then reorder them into calendar order using only drag (or the keyboard-accessible move dialog if your app has one).

## Part C — Formatting reps (≈1.5 hours)

6. Take any 4-column, 10-row numeric block and apply, on separate copies of it: General format, Number format (2 decimals), Currency format, Accounting format, and a custom format code of your own devising. Compare all five visually side by side — write one sentence on when you'd actually choose Accounting over Currency in real work.
7. Build a small table (any 3 columns, 6 rows) and apply three different conditional formatting rule types to three different columns: a Highlight Cells rule, a Color Scale, and (Excel only, if available) a Data Bar or Icon Set. If your app is Sheets and lacks a direct data-bar equivalent, substitute a second Color Scale on a different column and note the substitution.
8. Practice the freeze-panes decision: build a sheet with both a header row **and** a header column you want fixed (like a small crosstab — rows are products, columns are months). Freeze both simultaneously (Lecture 2, section 4 covers freezing rows; research how to freeze a row *and* a column at once — hint: it's about which cell you select before freezing).

## Part D — Reflection (≈30 min)

9. In a few sentences: which of this week's shortcuts do you predict will be hardest to keep using once the pressure of "homework" is gone? What's your plan to keep using it anyway?
10. Open a workbook you've made in the past (school, work, personal) — or, if you have none, a template from your app's gallery. Spend 10 minutes finding at least 3 things you'd now fix, using only this week's skills (formatting consistency, frozen panes, sheet naming). Write down what you found.

## Submission

Keep your homework work in a `Homework` area of your workbook (or a separate file) — no formal submission format required, but be ready to reference specific tasks if asked in review.
