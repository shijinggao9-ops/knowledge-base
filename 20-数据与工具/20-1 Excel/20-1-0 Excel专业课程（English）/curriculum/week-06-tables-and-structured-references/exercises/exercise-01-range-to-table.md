# Exercise 1 — Convert a Range to a Table

**Goal:** Turn the flat `Orders` range into a real Table, rename it, style it, add a Total Row, and prove — with your own eyes — that it auto-expands.

**Estimated time:** 1 hour.

## Setup

Open your Week 6 workbook. Confirm the `Orders` sheet has the flat range `A1:I25` from the README, with `Total` still **typed numbers** (you convert this to a formula in Exercise 2, not here). Confirm `SUM(I2:I25)` reads **5240.60** in a scratch cell before starting.

## Tasks

1. **Convert to a Table.** Click any cell inside the data, `Ctrl+T` (Excel) or select `A1:I25` then **Insert → Tables** (Sheets). Confirm the detected range is `A1:I25` and headers are recognized before confirming.

2. **Rename it.** Excel: **Table Design** tab → Table Name box → `Orders`. Sheets: Table's dropdown/name chip → Rename → `Orders`. *(Expected: any structured-reference formula you type from now on shows `Orders[...]` autocomplete suggestions, not `Table1[...]`.)*

3. **Apply a style.** Pick any built-in Table style (Excel: Table Design → style gallery; Sheets: Table's color theme picker). Turn **on** Banded Rows if it isn't already.

4. **Add a Total Row.** Excel: Table Design → check **Total Row**; set the `Qty` column's total to **Sum**, and the `Total` column's total to **Sum**. Sheets: Table menu → toggle the totals/summary row; set the same two columns to **Sum**. *(Expected: the `Total` column's Total Row cell reads **5240.60**, matching the checksum.)*

5. **Prove auto-expansion — add a row.** Click the cell directly below the Table's last data row (not the Total Row — one row *above* it, where a new data row inserts) and type a 25th order: `1025`, `2026-02-27`, `J. Alvarez`, `South`, `Desk Lamp`, `Furniture`, `1`, `39.00`, `39.00`. *(Expected: the Table's border, banding, and Total Row all extend/recalculate immediately — the Total Row's `Total` cell now reads **5279.60**. If it doesn't move, you typed into a cell outside the Table's expansion trigger — undo, and try again by typing directly adjacent to the last existing row.)*

6. **Prove auto-expansion — add a column.** In the column immediately to the right of `Total` (currently blank), type a header `Notes` in the header row. *(Expected: the new column instantly inherits the Table's border and banding — it's now part of the Table, addressable as `Orders[Notes]`.)*

7. **Test the filter arrows.** Click the `Region` header's dropdown, uncheck everything except `East`, and confirm the Total Row's `Total` figure changes to reflect only the visible (East) rows. Clear the filter afterward so all rows show again.

8. **Clean up.** Delete the test row (`1025`) and the `Notes` column you added in Tasks 5–6 — the rest of this week's exercises assume exactly 24 data rows. Confirm the Total Row's `Total` cell is back to **5240.60**.

## Expected result (spot checks)

- After Task 4: Total Row `Total` = 5240.60.
- After Task 5: Total Row `Total` = 5279.60 (temporarily).
- After Task 8 (cleanup): Total Row `Total` = 5240.60 again, exactly 24 data rows, no extra column.

## Done when…

- [ ] The Table is named `Orders`, not `Table1`.
- [ ] A style with banded rows is applied.
- [ ] The Total Row is enabled with `Sum` on both `Qty` and `Total`.
- [ ] You watched the border/banding/Total Row extend automatically when you typed a new row — not by re-applying anything manually.
- [ ] The workbook is back to exactly 24 data rows and the original 9 columns before you move to Exercise 2.

## Stretch

- Turn **off** Banded Rows and turn **on** First Column styling instead — notice how the visual emphasis shifts from "scan across a row" to "the leftmost column is the label."
- In Excel, open **Table Design → Resize Table** and manually shrink the range by one row, then immediately re-expand it back — this is the manual equivalent of what auto-expansion does for you, useful to understand when a Table's boundary ever needs a deliberate fix (e.g., after deleting rows from the *middle* rather than typing new ones at the edge).

## Submission

Commit the workbook to your portfolio under `c41-week-06/exercise-01/`.
