# Week 11 — Homework

A practice set to tie the week together. Spread this across the week rather than doing it all in one sitting — Power Query fluency comes from watching the Applied Steps pane respond to your own experiments, on data you built yourself, not from re-reading someone else's finished query. Budget roughly 5 hours total.

## How to use this

Each task below is short (10–40 minutes) and targets a specific skill from the lectures. Do them in a fresh workbook or a dedicated `Homework` section (separate from the exercises, challenges, and mini-project — those need their own untouched files) so nothing collides.

## Part A — Editor fluency drills (≈1 hour)

1. Import any one seed file from this week (`North_Week1.csv` is fine) and, without applying any transform, click through **View → Advanced Editor**. Read the auto-generated M code top to bottom. You won't understand every token, but identify at least the `let`/`in` structure and the fact that each line assigns a name to the result of the previous line — the same Applied Steps pane, just as literal code.
2. Rename every auto-generated step in a fresh import (`Source`, `Promoted Headers`, `Changed Type`) to a plain-English description of what it does. Then delete the renamed `Changed Type` step and observe exactly what breaks in the preview (if anything) — confirm you understand why removing a type-conversion step does or doesn't cascade an error to steps after it.
3. Build one query with at least 5 steps, then use **Insert Step After** (not "append to the end") to insert a new step in the *middle* of the sequence. Confirm whether the steps after your insertion still work correctly, and if any needed adjustment, document exactly why.

## Part B — Transform reps (≈1.5 hours)

4. Take any text column from one of this week's files (`ProductName` works) and split it two different ways: once **By Delimiter** on a space (splitting "Trail Backpack" into "Trail" and "Backpack"), once **By Number of Characters** at position 5. Compare the two results and write one sentence on when each split mode is the right tool.
5. Build a brand-new wide crosstab from scratch — any subject you choose (weekly hours worked per employee, monthly rainfall per city, quarterly scores per team) — at least 4 rows and 4 "wide" columns. Import it and unpivot it with `Unpivot Other Columns`. Confirm your unpivoted row count equals (original row count) × (number of wide columns).
6. On your unpivoted result from Task 5, use `Group By` to collapse back to one row per original "row" label, summing the value column. Confirm the sum for each group matches what you'd get by manually adding across that row in the original wide version.
7. Take the `Monthly_Sales_Report.csv` unpivoted result from Exercise 2 and use `Group By` with **two** aggregate columns at once (e.g., `Sum of Sales` and `Count of Rows` in the same Group By dialog) grouped by `Product`. Confirm the Count column reads exactly 3 for every product (one row per month).

## Part C — Combine reps (≈1.5 hours)

8. Build two small, unrelated queries by hand (invent any two datasets with at least one shared key column, 4–5 rows each) and merge them with **Inner** join instead of Left Outer. Compare the resulting row count to what a Left Outer join on the same two sources would produce, and explain the difference in one sentence.
9. Build three small queries with identical column structure (any subject, invented data, 3–4 rows each) and append all three with **Append Queries as New**, choosing "Three or more tables." Confirm the resulting row count is the exact sum of the three sources.
10. Revisit Challenge 1's `AllWarehousesCombined` query (or rebuild a small version if you skipped the challenge) and deliberately place a file with a **different column name** (rename one column, e.g. `Qty` → `Quantity`, in a duplicate copy of one CSV, dropped into the same folder) into the source folder. Refresh and observe exactly what happens to that column in the combined result. Document it, then remove the mismatched file and confirm the pipeline returns to its correct 14-row baseline.

## Part D — Reflection (≈1 hour)

11. In a few sentences: of everything covered this week — import, transform, unpivot, merge, append, folder-combine, refresh — which technique do you predict you'll use most often in real spreadsheet work after this course, and why?
12. Think of a repetitive data-cleanup task you've done by hand before (in this course or in real life) — copying values from multiple files into one sheet, reformatting a report every week, deduping an export. Write 3–4 sentences on exactly how you'd rebuild that task as a Power Query pipeline now, naming which techniques from this week apply.
13. Compare Power Query's Applied Steps pane to Google Sheets' `IMPORTHTML`/`IMPORTRANGE` approach (Lecture 3, Section 7) one more time, in your own words: what's the single biggest practical difference for someone maintaining the pipeline six months from now, after the original builder has moved on?

## Submission

Keep your homework work in a `Homework` area of your workbook (or a separate file) — no formal submission format required, but be ready to reference specific tasks if asked in review.
