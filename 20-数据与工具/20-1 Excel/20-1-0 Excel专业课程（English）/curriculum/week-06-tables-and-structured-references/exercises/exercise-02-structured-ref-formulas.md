# Exercise 2 — Rewrite Formulas as Structured References

**Goal:** Replace typed `Total` values and any A1-style formula with structured references, then stress-test them against inserted rows and columns — the exact scenarios that break plain-range formulas.

**Estimated time:** 1.5 hours.

## Setup

Continue in the `Orders` Table from Exercise 1 — exactly 24 data rows, `Total` still typed numbers, Total Row enabled. Add a new sheet tab called `Checks` if you don't already have one from the lectures — you'll put scratch formulas there.

## Tasks

1. **Convert `Total` to a structured-reference formula.** Click the `Total` column's first data cell and replace the typed `45.00` with `=[@Qty]*[@UnitPrice]`. *(Expected: it still shows 45, and the formula fills down the entire column automatically — verify by clicking a few other rows in `Total` and confirming each shows `=[@Qty]*[@UnitPrice]`, not a typed number.)* Confirm the Total Row still reads **5240.60** — a formula-driven column should produce identical numbers to the typed values it replaced.

2. **Build three whole-column aggregates on `Checks`.** Using `Table[Column]` syntax (no `@`):
   - `=SUM(Orders[Total])` → expect **5240.60**
   - `=AVERAGE(Orders[UnitPrice])` → expect **76.43** (rounded to 2 decimals; unrounded ≈76.4346…)
   - `=MAX(Orders[Total])` → expect **1745.00**

3. **Reference the Total Row explicitly.** Write `=Orders[[#Totals],[Total]]` on `Checks`. *(Expected: identical value to Task 2's `SUM`, but this formula is reading the Table's own Total Row rather than recomputing the sum independently — if you ever change the Total Row's function to something other than Sum, this formula's result changes with it, while your Task 2 `SUM` formula would not.)*

4. **Insert a column and confirm nothing breaks.** Right-click the `Category` column header inside the Table → **Insert → Table Column to the Left**. Rename the new blank column `Subcategory` (leave it empty otherwise). *(Expected: your `[@Qty]*[@UnitPrice]` formula in `Total` is completely unaffected — check two or three rows to confirm. Your three `Checks` formulas from Task 2 are also unaffected.)*

5. **Insert a row in the middle and confirm nothing breaks.** Right-click any data row around the middle of the Table (e.g., the row for order `1012`) → **Insert → Table Rows Above**. Leave the new blank row's `OrderID` through `UnitPrice` empty for now — just confirm the `Total` column's structured-reference formula is *already present* in that new blank row (it should show `0` or blank, computing `[@Qty]*[@UnitPrice]` against two currently-empty cells). *(Expected: `SUM(Orders[Total])` on `Checks` is unaffected — an empty row contributes 0.)*

6. **Fill in the inserted row and re-check.** Give the new row real values: `OrderID` `1013b`, `OrderDate` `2026-02-12`, `Rep` `M. Chen`, `Region` `East`, `Product` `Desk Organizer`, `Category` (blank — no subcategory), `Qty` `2`, `UnitPrice` `15.00`. *(Expected: `Total` for this row auto-computes `30.00`; `SUM(Orders[Total])` on `Checks` now reads **5270.60** — the original 5240.60 plus this new row's 30.00.)*

7. **Delete the temporary column.** Remove the `Subcategory` column you added in Task 4 (right-click its header → Delete → Table Columns). *(Expected: no `#REF!` anywhere — the `Total` formula never referenced that column, so removing it is harmless. This is the payoff: a formula that only names the columns it actually uses is immune to unrelated columns being added or removed.)*

## Expected result (spot checks)

- Task 1 → Total Row still 5240.60 after switching to formulas.
- Task 2 → SUM 5240.60, AVERAGE ≈73.87, MAX 1745.00.
- Task 6 → SUM becomes 5270.60 after the mid-Table insert is filled in.
- Task 7 → zero errors after deleting the unused column.

## Done when…

- [ ] Every `Total` cell is a `[@Qty]*[@UnitPrice]` formula, not a typed number.
- [ ] You have working `SUM`, `AVERAGE`, `MAX`, and `[#Totals]` structured-reference formulas on `Checks`.
- [ ] You've personally watched a mid-Table row insert and a column insert/delete leave every formula intact.
- [ ] Your final `SUM(Orders[Total])` reads **5270.60** (24 original rows + the one you added in Task 6).

## Stretch

- Delete the row you added in Task 6 (right-click → Delete → Table Rows) and confirm `SUM(Orders[Total])` returns to exactly **5240.60** — a clean round-trip, no residue.
- Write a formula that counts how many columns the Table currently has, without hard-coding the number: `=COLUMNS(Orders[#All])`. Compare it to `=COLUMNS(Orders[#Headers])` — same answer, different reasoning path — and explain in one sentence why both work.

## Submission

Commit the workbook to your portfolio under `c41-week-06/exercise-02/`.
