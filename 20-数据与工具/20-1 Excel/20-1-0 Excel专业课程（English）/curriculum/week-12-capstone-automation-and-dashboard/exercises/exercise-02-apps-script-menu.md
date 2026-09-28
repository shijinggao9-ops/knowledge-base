# Exercise 2 — Add a Custom Menu in Apps Script

**Goal:** write your first Apps Script functions from scratch (no recorder exists for Sheets), wire them into a custom menu via `onOpen()`, and practice the batch read/write pattern instead of a cell-by-cell loop.

**Estimated time:** 60 minutes.

## Setup

Create a new Google Sheet named `Week 12 Exercise 2 — Crunch Outfitters`. On `Sheet1` (rename it `Sales_Data`), enter:

| Order ID | Date | Region | Category | Units | Unit Price |
|---|---|---|---|---|---|
| 1001 | 1/4/2026 | North | Footwear | 3 | 89.99 |
| 1002 | 1/5/2026 | South | Apparel | 12 | 34.50 |
| 1003 | 1/6/2026 | East | Camping | 1 | 249.00 |
| 1004 | 1/7/2026 | West | Accessories | 25 | 12.75 |
| 1005 | 1/8/2026 | North | Footwear | 5 | 89.99 |

Add an empty `Reorder Flag` header in `G1`. Open `Extensions → Apps Script`, delete the placeholder `myFunction`, and save the project as `Week 12 Exercise 2`.

## Tasks

### 1. `onOpen()` and a custom menu

Write `onOpen()` that adds a menu titled **Crunch Tools** with three items: "Flag Low Stock," "Bold Header Row," and "About This Sheet" (with a separator before the last one), calling three functions you'll write next.

```javascript
function onOpen() {
  // your code here — see lecture 02, section 3
}
```

Save, **reload the spreadsheet tab** (menus only appear after a reload, not just a script save), and confirm **Crunch Tools** appears in the menu bar.

### 2. `flagLowStock()` — batch read, batch write

Write a function that reads the `Units` column (`E2:E6`) in **one** `getValues()` call, computes for each row whether `Units < 10`, and writes `"REORDER"` or `""` into the matching row of column `G` with **one** `setValues()` call. No `getRange` inside a loop.

```javascript
function flagLowStock() {
  const sheet = SpreadsheetApp.getActive().getSheetByName('Sales_Data');
  // read once, compute in memory, write once — see lecture 02, section 5
}
```

Run it from the menu. Expected: rows for Order 1001 (3 units) and 1003 (1 unit) get `REORDER`; the rest are blank.

### 3. `boldHeaderRow()`

A short one — bold `A1:G1` and set a light gray background, referencing the range directly (no `.getRange().activate()` or anything selection-based — Apps Script doesn't record macros, but it's just as possible to write clunky selection-chasing code by habit).

### 4. `showAbout()`

Use `SpreadsheetApp.getUi().alert(...)` to show a short message naming the sheet and today's date (`new Date()`).

## Expected result

- The **Crunch Tools** menu appears on reload with 3 items and a separator before "About This Sheet."
- Running "Flag Low Stock" writes `REORDER` into `G2` and `G4` only.
- Running "Bold Header Row" bolds and shades `A1:G1`.
- "About This Sheet" pops an alert dialog.

## Done when…

- [ ] All four functions exist and are wired into the menu — clicking each menu item runs the right function (not the wrong one; double-check the string names in `addItem` match your function names exactly, since Apps Script won't catch a typo there until you click it).
- [ ] `flagLowStock()` contains exactly one `getValues()` call and one `setValues()` call — no `getRange(...).getValue()` inside a loop.
- [ ] You can explain why the menu doesn't appear until the spreadsheet tab is reloaded, even though the script saved successfully.

## Stretch

- Add a fourth menu item, "Clear Reorder Flags," that blanks `G2:G6` in one call.
- Make `flagLowStock()` dynamic instead of hardcoded to `E2:E6`: find the last row with `sheet.getLastRow()` and size the range to match, so it still works if rows are added later.

## Submission

Copy the full contents of `Code.gs` into a file named `Code.gs` and commit it to your portfolio under `c41-week-12/exercise-02/`, along with a one-paragraph note on what `getLastRow()` returns and why it matters for the stretch goal.
