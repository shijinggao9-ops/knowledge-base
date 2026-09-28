# Exercise 1 — Import & Clean With Power Query

**Goal:** Turn the deliberately messy `Orders_Raw_Export.csv` into a clean, correctly-typed Table, using only Power Query steps — no manual worksheet formulas, no hand-editing the CSV.

**Estimated time:** 1 hour.

## Setup

Confirm `Orders_Raw_Export.csv` exists in your `crunch-wholesale` folder with the exact content from Lecture 2, Section 1 (three metadata lines, a blank line, the real header, five data rows including `"8 units"` and `" Camp Stove "`). Do not edit the file directly — every fix happens as a Power Query step.

## Tasks

1. **Import.** `Data → Get Data → From File → From Text/CSV` → select `Orders_Raw_Export.csv` → **Transform Data**. Confirm the preview shows the raw junk (metadata rows as `Column1`, no real headers detected yet) before you touch anything.

2. **Remove the junk rows.** Use `Home → Remove Rows → Remove Top Rows` to strip everything above and including the blank line, landing exactly on the real header row as the new top row. *(Expected: after this step, the very first visible row in the preview is `OrderID, OrderDate, SKU, ProductName, Qty, UnitCost` as plain text — not yet promoted to headers.)*

3. **Promote headers.** `Home → Use First Row as Headers`. *(Expected: column headers are now `OrderID`, `OrderDate`, `SKU`, `ProductName`, `Qty`, `UnitCost`, and a `Changed Type` step auto-appends.)*

4. **Fix the trapped text value.** Confirm `Qty`'s column type shows as `Text` (or check by trying to convert it to `Whole Number` and watching an error appear on the `"8 units"` row). Use `Replace Values` on that one cell (or the whole column, with *Value To Find* `" units"` and *Replace With* blank, which is the more general fix if more rows had unit suffixes) to leave a plain numeric string, then set the column's type to **Whole Number**.

5. **Trim the text column.** Select `ProductName` → `Transform → Format → Trim`. *(Expected: the SKU-104 row now shows `Camp Stove` with no leading/trailing spaces, matching every other row's formatting.)*

6. **Confirm types are all correct.** `OrderID`/`SKU`/`ProductName` should show the `ABC` text icon, `OrderDate` the calendar icon, `Qty` the `#` whole-number icon, `UnitCost` the `1.2` decimal-number icon. Fix any that auto-detected wrong.

7. **Load.** `Home → Close & Load` (default: new sheet, Table). Rename the resulting Table `OrdersClean` (Table Design → Table Name).

## Expected result (spot checks)

- 5 data rows, 6 columns, zero blank or error rows.
- SKU-104's `Qty` = **8** (a real number, not text), `ProductName` = `Camp Stove` (no stray spaces).
- Sum of `Qty × UnitCost` across all 5 rows = **1949.00** — the North-warehouse checksum from the week README.

## Done when…

- [ ] The Applied Steps pane shows a clear, sensibly-named sequence (at minimum: `Source`, a row-removal step, `Promoted Headers`, a fixed-`Qty` step, a `Trim` step, a type-conversion step).
- [ ] Every column has the correct data-type icon — no column is still `Text` that should be numeric or date.
- [ ] The checksum (1949.00) matches exactly.
- [ ] Clicking `Refresh` on the loaded Table re-runs without error.

## Stretch

- Click back through your Applied Steps one at a time, from `Source` to the final step, narrating out loud (or in a comment) what changed at each click — this is the exact debugging skill Challenge 1 and the mini-project require when a folder-combine query breaks on an unexpected file.
- Deliberately break your own query: edit `Orders_Raw_Export.csv` outside Excel, changing `"8 units"` to `"eight"` (unparseable as any number), save, and Refresh. Read the resulting error message carefully, then fix the step that broke — practice reading Power Query's own error output before you need to under real time pressure.

## Submission

Commit the workbook to your portfolio under `c41-week-11/exercise-01/`.
