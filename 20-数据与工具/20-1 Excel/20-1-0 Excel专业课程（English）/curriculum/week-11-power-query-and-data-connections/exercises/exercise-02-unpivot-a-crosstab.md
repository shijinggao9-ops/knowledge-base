# Exercise 2 — Unpivot a Cross-Tab

**Goal:** Reshape the wide `Monthly_Sales_Report.csv` (one row per product, one column per month) into a tidy long table (`Product`, `Month`, `Sales`) using Power Query's Unpivot step, ready to feed a pivot table or `SUMIFS` formulas.

**Estimated time:** 1–1.5 hours.

## Setup

Confirm `Monthly_Sales_Report.csv` exists in `crunch-wholesale` with the exact content from Lecture 2, Section 7 — six products, three month columns (`Jan`, `Feb`, `Mar`).

## Tasks

1. **Import.** `Data → Get Data → From File → From Text/CSV` → select `Monthly_Sales_Report.csv` → **Transform Data**. Confirm the preview shows 4 columns (`Product`, `Jan`, `Feb`, `Mar`) and 6 data rows — the wide shape, untouched.

2. **Select the column to keep as-is.** Click the `Product` column header to select only it.

3. **Unpivot everything else.** `Transform → Unpivot Columns → Unpivot Other Columns`. *(Expected: the result is 3 columns — `Product`, `Attribute`, `Value` — and 18 rows, 6 products × 3 months each.)*

4. **Rename for clarity.** Double-click each new column header: `Attribute` → `Month`, `Value` → `Sales`.

5. **Set correct types.** Confirm `Month` is `Text` and `Sales` is a numeric type (`Whole Number` or `Decimal Number` — either is acceptable here since all values are whole numbers).

6. **Sort for readability (optional but recommended).** `Home → Sort` or click the column header's sort arrow: sort by `Product` ascending, then `Month`. *(This doesn't change any value — it's purely for a human reading the result. Confirm the checksum below is unaffected by whether you sort.)*

7. **Load.** `Home → Close & Load`, as a Table, renamed `MonthlySalesLong`.

## Expected result (spot checks)

- 18 rows total, 3 columns (`Product`, `Month`, `Sales`).
- Trail Backpack's three rows sum to **4250** (1200 + 1450 + 1600).
- Hiking Boots' three rows sum to **6530** (2200 + 1980 + 2350).
- Sum of the entire `Sales` column across all 18 rows = **19810**, matching the checksum from Lecture 2.

## Done when…

- [ ] The wide 4-column, 6-row source is now a long 3-column, 18-row table.
- [ ] Column names are `Product`, `Month`, `Sales` — not the auto-generated `Attribute`/`Value`.
- [ ] The checksum (19810) matches exactly.
- [ ] You can explain, in one sentence, why `Unpivot Other Columns` was used instead of manually selecting `Jan`, `Feb`, and `Mar` to unpivot.

## Stretch

- Build a quick pivot table (Week 7) directly against `MonthlySalesLong`, with `Month` in Columns and `Product` in Rows, summing `Sales`. Confirm it reconstructs the *exact* original wide crosstab — proof that unpivoting is a lossless reshape, not a data-destroying one.
- Add a fourth month column, `Apr`, with any 6 values you invent, directly in `Monthly_Sales_Report.csv` outside Excel. Refresh your query. *(Expected: no step needs editing — the row count jumps to 24 automatically, because `Unpivot Other Columns` re-evaluates "everything except `Product`" fresh on every refresh.)* This is the exact behavior a hard-coded `Unpivot Columns` (selecting `Jan`/`Feb`/`Mar` by name) would **not** give you — try switching to that variant and confirm `Apr` gets silently left out, then switch back.

## Submission

Commit the workbook to your portfolio under `c41-week-11/exercise-02/`.
