# Exercise 3 — Merge Two Data Sources

**Goal:** Enrich the North warehouse's orders with `Category` and `Supplier` columns pulled from the `Products.csv` lookup table, using a Power Query Merge — no `XLOOKUP` involved.

**Estimated time:** 1–1.5 hours.

## Setup

Confirm `North_Week1.csv` and `Products.csv` both exist in your `crunch-wholesale` folder, exactly as specified in the week README.

## Tasks

1. **Import both sources as connections only.** For each file: `Data → Get Data → From File → From Text/CSV` → select the file → **Transform Data** → (nothing to clean — both files are already tidy) → `Home → Close & Load To…` → **Only Create Connection**. You should end up with two entries in the Queries pane, `North_Week1` and `Products`, neither loaded to a sheet.

2. **Start the merge.** With either query open in the editor (or from the Queries pane, right-click `North_Week1` → **Merge**), `Home → Combine → Merge Queries → Merge Queries as New`.

3. **Configure the join.** Top table: `North_Week1`. Bottom table: `Products`. Click the `SKU` column header in each table's preview to set it as the matching key on both sides. Confirm **Join Kind** is **Left Outer** (the default).

4. **Inspect before expanding.** Click OK and look at the result: the original 6 `North_Week1` columns, plus one new column named `Products`, each cell holding a small `Table` value (not yet expanded). *(Expected: 5 rows, unchanged from `North_Week1` — Left Outer keeps every top-table row.)*

5. **Expand the matched columns.** Click the expand icon (⤢) on the `Products` column header. Uncheck `SKU` (you already have it), leave `Category` and `Supplier` checked, uncheck "Use original column name as prefix" for cleaner headers. Confirm.

6. **Rename and load.** Rename the query itself (right-click in the Queries pane → Rename) to `NorthEnriched`. `Home → Close & Load`, as a Table.

## Expected result (spot checks)

- 5 rows, 8 columns (the original 6, plus `Category` and `Supplier`).
- SKU-104 (Camp Stove) row: `Category` = `Gear`, `Supplier` = `Summit Gear Partners`.
- SKU-101 (Hiking Boots) row: `Category` = `Footwear`, `Supplier` = `TrailWorks Inc.`
- Sum of `Qty × UnitCost` across all 5 rows is still **1949.00** — a Merge never changes the numeric facts, only adds descriptive columns.

## Done when…

- [ ] `Category` and `Supplier` are two flat, real columns — not a nested `Table` value still waiting to be expanded.
- [ ] Every row has a `Category`/`Supplier` value (no blanks) — proof every `SKU` in `North_Week1` has a match in `Products`.
- [ ] The checksum (1949.00) is unchanged from before the merge.
- [ ] You can state, in one sentence, why **Left Outer** was the correct join kind here rather than **Inner**.

## Stretch

- Temporarily edit `North_Week1.csv` outside Excel, changing one row's `SKU` to a value that doesn't exist in `Products.csv` (e.g., `SKU-999`), save, and Refresh `NorthEnriched`. *(Expected: that row's `Category`/`Supplier` come back blank, not an error — this is Left Outer's defined behavior for a non-match.)* Then redo the merge as **Left Anti** instead of **Left Outer** and confirm it isolates exactly that one orphaned row — this is the data-quality check Lecture 3, Section 3 described. Revert the CSV back to `SKU-104` when done.
- Build the same enrichment a second way, entirely in a worksheet with `XLOOKUP` (Week 3) against the loaded `North_Week1` and `Products` Tables, and compare: how many formulas did the `XLOOKUP` approach need versus how many clicks the Merge approach needed, to pull in both `Category` and `Supplier`?

## Submission

Commit the workbook to your portfolio under `c41-week-11/exercise-03/`.
