# Mini-Project — Build a Repeatable ETL Pipeline for Crunch Wholesale

> Assemble every technique from this week into one connected pipeline: import a full folder of warehouse exports, clean a messy raw file, unpivot a monthly report, merge in product data, append it all together, and load one final, analysis-ready Table — then prove the entire pipeline survives a new week's data with a single click of Refresh.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it deliberately mirrors the job this week has been building toward: a weekly reporting cycle where new files land, and the job is to get from "raw exports in a folder" to "one trustworthy Table" without redoing any manual work. You already built every individual piece — Exercise 1's cleaning, Exercise 2's unpivot, Exercise 3's merge, Challenge 1's folder combine — this project's job is wiring them into **one dependency chain** that refreshes as a unit.

---

## Deliverable

A single workbook, `crunch-week11-pipeline.xlsx`, containing:

1. A **Queries pane** with a clear, sensible set of named queries forming one dependency chain (see Requirements below) — no orphaned or duplicate queries left over from earlier experiments.
2. A final loaded Table, `WeeklyOrdersFinal`, that is the pipeline's single consumer-ready output — every other query in the chain should be **Only Create Connection**.
3. A `Summary` sheet with at least 3 `SUMIFS`/pivot-based figures computed **against** `WeeklyOrdersFinal` (Week 6/7 skills, applied to this week's output) — proof the final Table is genuinely usable, not just technically correct.
4. A `pipeline-notes.md` (or a `Notes` sheet) documenting your query dependency chain, in plain English, and the results of your refresh test (see Requirements, Part 4).

---

## Requirements

### Part 1 — Import and clean (30–40 min)

Import `Orders_Raw_Export.csv` (from Lecture 2 / Exercise 1) and apply the full cleaning sequence: remove junk header rows, promote headers, fix the trapped-as-text `Qty` value, trim `ProductName`, set correct types. Load this as **Only Create Connection**, named `NorthCleaned`.

### Part 2 — Combine the folder (30–40 min)

Using `From Folder` (Challenge 1's technique), combine every file in `warehouse-exports` (`North_Week1.csv`, `South_Week1.csv`, `West_Week1.csv` — and your Midwest file from Challenge 1, if you completed it) into one query, correctly typed, with a source-file column retained. Load as **Only Create Connection**, named `AllWarehousesCombined`.

You now have two independently-cleaned views of North's data (`NorthCleaned` from the raw messy export, and North's rows inside `AllWarehousesCombined` from the already-clean file) — this is intentional. In `pipeline-notes.md`, note explicitly which one you're using downstream and why (hint: `AllWarehousesCombined` already contains North correctly, making `NorthCleaned` a demonstration query rather than one that needs to feed the final pipeline — but defend your own reasoning either way).

### Part 3 — Merge in product data (30–40 min)

Import `Products.csv` as **Only Create Connection**, named `Products`. Merge it (Left Outer, matched on `SKU`) against your chosen combined-orders query from Part 2, expanding `Category` and `Supplier`. Load the result as **Only Create Connection**, named `OrdersEnriched`.

### Part 4 — Finalize and test refresh (40–50 min)

Rename (or re-point) your final output to `WeeklyOrdersFinal`, loaded as a real Table this time (not connection-only — this is the pipeline's end point). Build the `Summary` sheet: at minimum, total `Qty × UnitCost` by `Category` (SUMIFS or a small pivot), total order count by warehouse/source, and average `UnitCost` by `Supplier`.

**The refresh test — this is the actual point of the project:**

1. Note your `WeeklyOrdersFinal` row count and its `Qty × UnitCost` grand total right now.
2. Outside Excel, add a new row to `West_Week1.csv` (any invented SKU that exists in `Products.csv`, any realistic `Qty`/`UnitCost`). Save the file.
3. In Excel, click **Data → Refresh All** — do not open any query editor, do not touch a single step.
4. Confirm: the row count in `WeeklyOrdersFinal` increased by exactly 1, the grand total updated by exactly `Qty × UnitCost` of your new row, the `Summary` sheet's figures updated automatically (since they reference the Table, Week 6-style), and no error appeared anywhere in the chain.
5. Document the before/after numbers in `pipeline-notes.md`.

---

## Milestones

- **Milestone 1 (40 min):** `NorthCleaned` built and verified against the 1949.00 checksum.
- **Milestone 2 (40 min):** `AllWarehousesCombined` built via `From Folder`, verified against the 6934.50 checksum (or the adjusted total if your Challenge 1 Midwest file is included).
- **Milestone 3 (40 min):** `Products` imported, `OrdersEnriched` merge built and verified (spot-check at least 2 rows' `Category`/`Supplier`).
- **Milestone 4 (30 min):** `WeeklyOrdersFinal` loaded as a Table; `Summary` sheet built with all 3 required figures.
- **Milestone 5 (30–40 min):** Refresh test executed end-to-end, results documented in `pipeline-notes.md`.

---

## Rules

- **Only `WeeklyOrdersFinal` loads to a visible Table.** Every other query in the chain must be **Only Create Connection** — a workbook cluttered with five loaded Tables when only one is meant to be consumed is a sign the Load-vs-Connection distinction (Lecture 1, Section 7) wasn't applied.
- **The refresh test must be real.** Adding the row, saving the file, clicking Refresh, and recording the actual before/after numbers — not asserting what "should" happen.
- **No manual formula patch-ups.** If a number looks wrong, fix the Power Query step that produced it, not a worksheet formula layered on top to compensate.
- **`Summary` sheet formulas must reference the Table**, the way Week 6 taught (`WeeklyOrdersFinal[Category]`, etc.), not a hard-coded range — so that adding rows via Refresh keeps `Summary` correct with zero edits there either.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|---------------------|
| Cleaning correctness | 20% | `NorthCleaned` checksum-verified; junk rows/types fully handled |
| Folder combine | 20% | `AllWarehousesCombined` correctly built via `From Folder`, checksum-verified |
| Merge correctness | 20% | `OrdersEnriched` has zero blank `Category`/`Supplier` cells, correct join kind used |
| Pipeline hygiene | 15% | Only the final query loads to a Table; every step sensibly named |
| Refresh test | 15% | New row actually added, Refresh actually clicked, before/after numbers documented and correct |
| Summary sheet | 10% | All 3 required figures present, built from structured references, and correctly updated by the refresh test |

---

## Reflection (`pipeline-notes.md`, ~200 words)

1. Which part of this pipeline took the longest to get right, and was the difficulty in Power Query mechanics or in figuring out the right *sequence* of operations?
2. You had two valid paths to North's clean data in Part 2 (`NorthCleaned` vs. `AllWarehousesCombined`). Which did you use downstream, and why?
3. If Crunch Wholesale added a fifth warehouse next month, list the exact steps you'd need to take to include it — be specific about which files change, which queries (if any) need editing, and which don't.
4. Compare this project's refresh test to Week 6's Table auto-expansion test. What's structurally the same about "prove it survives new data" in both weeks, and what's genuinely new about doing it across multiple files and sources instead of one Table?

---

## Why this matters

This mini-project is the complete arc of Week 11 in one workbook: pull data from wherever it actually lives — a messy single file, a whole folder, a lookup table — shape and combine it once, and end with a pipeline that treats "new data arrived" as a non-event. That's the difference between a spreadsheet that's correct *today* and one that stays correct *every week*, which is exactly the foundation Week 12's automation (macros/VBA or Apps Script wrapping a one-click "refresh everything and re-send the report" button) builds directly on top of.

When done: push/save your work, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-11-power-query-and-data-connections/quiz.md) and start [Week 12 — Capstone: automation + dashboard](../../week-12-capstone-automation-and-dashboard/).
