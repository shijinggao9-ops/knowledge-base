# Week 5 — Homework

A practice set to tie the week together. Spread this across the week rather than doing it all in one sitting — the audit-then-clean sequence only becomes automatic through repetition on data you haven't seen the "answer" for yet. Budget roughly 5 hours total.

## How to use this

Each task below is short (10–30 minutes) and targets a specific skill from the lectures. Do them in a fresh area of your workbook (a new sheet per task, or a dedicated `Homework` sheet split into labeled blocks) so nothing collides with the exercises, challenges, or mini-project.

## Part A — Auditing drills (≈1 hour)

1. Build a 15-row block of any fictional data (your choice of subject — books, recipes, playlists) and **deliberately** introduce: 2 exact duplicate rows, 1 near-duplicate (differing only by casing), 1 blank row, and 1 whitespace-only "blank" row (a cell containing just a space). Then write the four audit formulas from Lecture 1 (exact-duplicate flag, near-duplicate normalized-key flag, `COUNTA`-based blank flag, `TRIM`-based whitespace flag) and confirm each one correctly catches what it's supposed to catch — and, just as important, confirm the `COUNTA` one *fails* to catch the whitespace-only row, so you've proven to yourself why the stricter check exists.

2. Take any column of at least 10 category-like values (real or invented) and deliberately type 3 casing/spelling variants of at least 2 of the categories. Run the `UNIQUE` + `COUNTIF` frequency-count audit from Lecture 1 and confirm it correctly reveals the fragmentation before you fix anything.

## Part B — Cleaning technique reps (≈1.5 hours)

3. Take a column of 10 names with inconsistent spacing (some double spaces, some leading/trailing spaces) and clean it with `TRIM`. Then deliberately add one cell with a line break baked into it (in most apps: `Alt+Enter` inside a cell) and confirm `TRIM` alone does **not** remove it, but `TRIM(CLEAN(...))` does.

4. Practice the "formula, verify, paste-as-values, delete helper" cycle explicitly: build any cleaning formula, verify it against 3 spot-checked rows by eye, paste-as-values over the original, and delete the now-redundant helper column. Do this twice on two different problems (e.g., once for a `PROPER()` casing fix, once for a `SUBSTITUTE`-based text fix) until the four-step sequence feels automatic rather than something you have to consciously recall.

5. Try Flash Fill (Excel) or Split-to-columns (Sheets) on a column of `"Last, First"` names, reshaping to two separate `First` and `Last` columns. Then do the **same task** with a formula (`LEFT`/`FIND`/`MID` from Week 4) instead. Write two sentences: which was faster to set up, and which would survive the source column changing later.

6. Build a small "wide" table with one row per person and three separate `Score1`/`Score2`/`Score3` columns (any fictional scores). Manually unpivot it (Lecture 2, Section 6) into a tidy two-column `Person, Score` table with one row per score. Confirm your unpivoted row count equals (original row count) × 3.

## Part C — Validation and drop-down reps (≈1.5 hours)

7. Build a single-cell List validation sourced from a 5-item range of your choosing. Add an Input Message and set the Error Alert to Warning (not Stop). Test that you *can* override it with a value not on the list, and confirm the warning actually appeared before you did.

8. Write a custom-formula validation rule (in your own domain — anything with a sensible business rule) that rejects entries failing **two** conditions at once (an `AND` of two checks), similar to Lecture 3's email-validation example. Test it with three inputs: one that should pass, and two that should each fail one of the two conditions separately.

9. Build one dependent drop-down pair from scratch, in a completely different domain than the lecture's Category → Subcategory example (e.g., Country → City, or Genre → Book Title). Use the `FILTER`-based technique (or `INDIRECT` fallback) and confirm the second list correctly updates when the first changes.

10. Add a conditional-formatting rule to any column of numbers that flags values more than 2x the column's average — write the formula using `AVERAGE()` over an absolute-referenced range compared against the current cell (relative reference), the same relative/absolute pairing pattern from Week 2.

## Part D — Reflection (≈30 min)

11. In a few sentences: of everything covered this week, which technique do you predict you'll use most often in real spreadsheets you build after this course — audit formulas, Remove Duplicates, Find & Replace, Data Validation, dependent drop-downs, or conditional-formatting flags? Why?
12. Open a spreadsheet you've built in the past (school, work, personal) that has **no** validation or cleaning applied to it. Spend 10 minutes identifying 3 specific places where this week's techniques would have prevented a real mistake you remember making (or could make) in that file. Write down what you found.

## Submission

Keep your homework work in a `Homework` area of your workbook (or a separate file) — no formal submission format required, but be ready to reference specific tasks if asked in review.
