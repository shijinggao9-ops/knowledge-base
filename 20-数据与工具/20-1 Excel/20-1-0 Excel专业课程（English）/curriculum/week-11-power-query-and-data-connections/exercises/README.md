# Week 11 — Exercises

Three guided exercises, ~1–1.5 hours each. **Do every step yourself, inside the Power Query editor** — reading about a transform step and clicking through it in your own workbook are not the same skill, and the Applied Steps pane only becomes a debugging tool once you've watched it build up, break, and get fixed at least a few times.

1. **[Exercise 1 — Import & clean with Power Query](exercise-01-import-and-clean.md)** — take the deliberately messy `Orders_Raw_Export.csv` and turn it into a clean, typed Table using only Power Query steps, no manual formula cleanup.
2. **[Exercise 2 — Unpivot a cross-tab](exercise-02-unpivot-a-crosstab.md)** — reshape the wide `Monthly_Sales_Report.csv` into a tidy long table ready for a pivot table or a `SUMIFS` formula.
3. **[Exercise 3 — Merge two data sources](exercise-03-merge-two-sources.md)** — enrich the North warehouse's orders with category and supplier data from the `Products` lookup table.

## Before you start

- You've completed all three lectures.
- The four seed files from the week README exist in your `crunch-wholesale` folder: `warehouse-exports/North_Week1.csv`, `warehouse-exports/South_Week1.csv`, `warehouse-exports/West_Week1.csv`, and `Products.csv`.
- You've built `Orders_Raw_Export.csv` and `Monthly_Sales_Report.csv` from Lecture 2 — both exercises 1 and 2 reuse them exactly as specified there.
- Excel 365, Excel 2016+, or Excel with the Power Query add-in installed (Excel 2010–2013).

## Suggested workflow

- Do each step in order — later exercises assume queries built in earlier ones (or the equivalent files) already exist.
- After every transform step, check the data preview against the exercise's stated expected result **before** moving to the next step. Power Query's Applied Steps pane makes it cheap to catch a mistake immediately — much more expensive to notice five steps later that step two was wrong.
- Rename your steps as you go (right-click → Rename in the Applied Steps pane) rather than leaving everything as `Changed Type1`, `Changed Type2` — the mini-project reuses these query patterns, and a self-documenting step list will save you real time then.
- Keep every workbook and CSV from these exercises; the challenges and mini-project build directly on top of them.
