# Lecture 1 — Why Tables Change Everything

> **Duration:** ~2 hours. **Outcome:** You can convert a plain range into a real Excel or Google Sheets Table, explain the four concrete behaviors that change the instant you do, apply a Table style, add a Total Row with the right per-column aggregate, and prove to yourself that the Table auto-expands when you type a new row underneath it.

You've spent five weeks writing formulas against ranges you typed the boundaries of by hand: `A2:A25`, `SUM(D2:D25)`, `XLOOKUP(A10, PriceList!$A$2:$A$7, ...)`. Every one of those addresses is a **promise about the size of your data** — a promise that breaks the day someone adds row 26. This lecture replaces the promise with a **Table**: a range that tracks its own size, so your formulas never have to.

## 1. The problem with a plain range

Open your `Orders` sheet from the week README — `A1:I25`, 24 rows of sales data, a bold header row, no Table yet. It *looks* like a table. It behaves like nothing of the kind. Try this:

1. Click into `A26` (the row right after your last order) and type `1025` for `OrderID`, then fill in a plausible row.
2. Look at any formula elsewhere in the workbook that referenced `SUM(I2:I25)` — the checksum from the README setup. **It didn't move.** Row 26 isn't included. The formula's range is a fixed address; it has no idea a new row exists.
3. Notice the new row also has **no formatting** — no currency format on `UnitPrice`/`Total`, no borders, nothing. You typed data into a blank row next to a range, not into the range.

This is the core failure mode of a plain range: **every formula, every format, every filter that touches it has a fixed boundary, and nothing about typing a new row tells that boundary to move.** In a five-row personal budget this is a minor annoyance. In a shared workbook that fifteen people add rows to over a year, it's a silent, compounding source of wrong numbers — a `SUM` that quietly excludes the newest quarter, a chart that stops at last year's last row, a `SUMIFS` that was correct in March and wrong every month since.

Delete row 26 before continuing — you'll re-add data properly once it's a Table.

## 2. Converting a range to a Table

**Excel:**

1. Click any single cell inside your `Orders` data (you don't need to select the whole range — Excel detects the contiguous block automatically).
2. Press **`Ctrl+T`** (or **Insert → Table** on the ribbon).
3. A dialog appears showing the detected range (`$A$1:$I$25`) with **"My table has headers"** checked. Confirm both are correct, click **OK**.

**Google Sheets:**

1. Select the range `A1:I25` (Sheets' Tables feature needs the range selected first, unlike Excel's auto-detect).
2. **Insert → Tables** (or the Tables icon in the toolbar).
3. Sheets shows a preview with the header row detected; confirm the range, click **Create table** (or the checkmark).

Both apps immediately change the range's appearance — banded row shading, a bold header row with filter/sort arrows, and (in Excel) a solid border around the whole block. That visual change is the smallest part of what just happened.

## 3. What actually changed — four things

### a) The range now has a name

Excel names it `Table1` by default; rename it immediately — a named Table is the entire point of next lecture. Click any cell inside the Table, then:

- **Excel:** **Table Design** tab (appears only while a Table cell is selected) → **Table Name** box, top-left → type `Orders` → **Enter**.
- **Google Sheets:** click the Table's name chip (appears above the Table when selected, or via the Table's dropdown menu) → **Rename table** → `Orders`.

From this point on, every structured-reference formula in Lecture 2 refers to this Table as `Orders`, not `Table1`.

### b) It auto-expands when you type below or beside it

Click the cell directly below your last row (now `A26`, just outside the Table's bottom-left corner) and type `1025`, `2026-02-27`, `J. Alvarez`, `South`, `Desk Lamp`, `Furniture`, `1`, `39.00`, `39.00`. The moment you press **Enter** or **Tab** into that row, **the Table's border, banding, and filter arrows extend to include it automatically** — you didn't tell it to; typing adjacent to the Table is the trigger. Any formula that references the Table as a whole (next lecture) now includes this new row too, with no edit required. The same happens if you type a value into the column immediately to the right of the Table's last column — a new column joins the Table and inherits its formatting.

This is the single behavior that makes the rest of this week possible: **a formula built against a Table today keeps working correctly on data that doesn't exist yet.**

### c) A new row copies the formulas and formatting above it

Once `Total` becomes a formula (you'll build this in Lecture 2 — `[@Qty] * [@UnitPrice]`), typing a new row into the Table **automatically fills that formula down into the new row's `Total` cell** — you never re-type or drag-fill it. Number formats (currency on `UnitPrice`/`Total`, date on `OrderDate`) also copy down to new rows automatically. Compare this to the plain-range test at the start of this lecture, where the new row got neither formula nor formatting — this is the concrete fix.

### d) Filter and sort arrows appear on every header, for free

Click the dropdown arrow on the `Region` header and uncheck everything except `East`. The Table filters in place — other rows hide, row numbers on the left show gaps where hidden rows are, and any Total Row (next section) recalculates against only the visible rows. Clear the filter (dropdown → **Clear Filter From "Region"**, or **Select All**) to restore every row. This is the same filtering experience as `AutoFilter` on a plain range, except it's bound permanently to the Table rather than something you re-apply after every structural change.

```mermaid
flowchart TD
  A["Convert range to Table"] --> B["Gets a name (Orders)"]
  A --> C["Auto-expands on new row or column"]
  A --> D["New rows inherit formulas and formatting"]
  A --> E["Filter and sort arrows on every header"]
```

*The four concrete behaviors that change the instant a range becomes a Table.*

## 4. Table styles

**Excel:** with a Table cell selected, the **Table Design** tab shows a gallery of built-in styles (Light/Medium/Dark, various color families) — click one to reformat instantly. The **Table Style Options** checkboxes next to the gallery control which visual features are on: **Header Row**, **Total Row** (next section), **Banded Rows**, **First/Last Column** (bold the edges), **Banded Columns**. Turn off **Banded Rows** and on **First Column** to see a style built for a Table where the leftmost column is the primary label, for example.

**Google Sheets:** the Table's own formatting panel (accessible via the Table's dropdown or right-click → **View table**) offers a smaller set of built-in color themes plus manual banding control. Sheets Tables lean more on **column type** (see below) than on style variety.

Pick any built-in style for `Orders` now — the specific choice doesn't matter for the rest of the week, but get in the habit: a styled Table reads faster than an unstyled one, and it costs one click.

## 5. Column types (Google Sheets' extra feature)

Google Sheets Tables add something Excel Tables don't have natively: **per-column data types**, enforced with light validation. Click a column header's dropdown inside the Table (e.g., `Category`) and Sheets may suggest a type — **Dropdown** (a fixed list, built automatically from the values already in the column), **Date**, **Currency**, **Number**, or plain **Text**. Try it on `Category`: Sheets detects the four existing values (`Electronics`, `Furniture`, `Office Supplies`, `Software`) and offers to turn the column into a dropdown-restricted list — accept it, and typing a fifth, unlisted category into a new row now shows a validation warning instead of silently accepting a typo. This is functionally close to Excel's **Data Validation → List** feature from Week 5, applied automatically at the column level instead of needing to be set up by hand.

Excel has no equivalent "column type" concept on a Table — you'd still set up Data Validation manually per column, exactly as you learned in Week 5. This is one of the concrete divergences you'll document fully in Challenge 2.

## 6. Adding a Total Row

**Excel:** **Table Design** tab → check **Total Row**. A new row appears at the Table's bottom with `Total` typed under the first column and a `SUM` under the last numeric column by default. Click any cell in that row and a dropdown arrow appears — open it to choose **Sum, Average, Count, Count Numbers, Max, Min, StdDev, Var**, or **None**, per column independently. Set the `Total` row's cell under `Qty` to **Sum**, and under `Total` to **Sum** — confirm the `Total` column's sum reads **5240.60** (plus whatever test row you added and then should now delete, per Section 3b — remove it before continuing so the week's numbers match).

**Google Sheets:** select the Table → its dropdown menu (or right-click) → **Toggle totals row** (naming varies by rollout; look for a totals/summary row toggle in the Table's own menu). Sheets' Total Row offers a smaller function set per column (Sum, Average, Count, Min, Max, custom formula) via a similar per-cell dropdown.

The Total Row is **not** counted as a data row by any structured reference or by the Table's own auto-expansion — it always stays pinned to the bottom, and new data rows insert **above** it automatically. You'll rely on this in the mini-project.

## 7. Check yourself

- Name the four concrete things that change the moment you convert a range to a Table (not counting the visual style).
- You type a new row directly below a Table's last row. What three things happen automatically, without you doing anything else?
- Why did the plain-range test at the start of this lecture fail to include the new row in `SUM(I2:I25)`, but a Table wouldn't have this problem?
- What's the one Table feature Google Sheets has that Excel Tables don't, and what problem does it solve?
- Where does the Total Row sit relative to new data rows typed into the Table, and why does that matter?

If those came quickly, move to Lecture 2 — the formula syntax that makes a Table's column names usable inside `=` expressions.

## Further reading

- **Microsoft — Overview of Excel tables:** <https://support.microsoft.com/en-us/office/overview-of-excel-tables-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c>
- **Microsoft — Create and format an Excel table:** <https://support.microsoft.com/en-us/office/create-and-format-an-excel-table-e81aa349-b006-4f8a-9806-5af9df0ac664>
- **Microsoft — Total the data in an Excel table:** <https://support.microsoft.com/en-us/office/total-the-data-in-an-excel-table-fa749a3c-ab7d-4e10-a1b0-ac1e4bb9e5b3>
- **Google — Use and format tables in Google Sheets:** <https://support.google.com/docs/answer/14471021>
