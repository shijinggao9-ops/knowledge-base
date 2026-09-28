# Exercise 3 — Wire a One-Click Refresh Button

**Goal:** combine Exercises 1 and 2 into a single entry-point routine — one button (Excel) or one menu item (Sheets) that runs a multi-step refresh chain, formats the result, stamps a timestamp, and reports success or failure. This is a smaller rehearsal of exactly what the mini-project needs at full scale.

**Estimated time:** 90 minutes. **Pick one platform** (Excel or Sheets) to build fully; do the other if time allows — the mini-project lets you choose one for the graded deliverable, but understanding both is expected for the quiz.

## Setup

Use your Exercise 1 (`.xlsm`) or Exercise 2 (Sheet) file, or start fresh with the same `Sales_Data` shape from those exercises. Add a second sheet named `Dashboard` with:

- `A1`: label `"Total Revenue"`, `B2`: a formula summing `Units * Unit Price` across `Sales_Data` (e.g. `=SUMPRODUCT(Sales_Data!E2:E6, Sales_Data!F2:F6)` in Excel, or `=SUMPRODUCT(Sales_Data!E2:E6, Sales_Data!F2:F6)` in Sheets — same formula, both engines).
- `A2`: label `"Last Refreshed"`, `B2`... wait — use `C1`/`C2` for the timestamp label/value so it doesn't collide with revenue. Final layout: `A1:"Total Revenue" B1:(formula)`, `A2:"Last Refreshed" B2:(blank, filled by your macro/script)`.

## Excel track

Write one macro, `RefreshDashboard`, that does all of the following **in order**, with error handling wrapping the whole thing:

1. Calls `FormatSalesHeader` (from Exercise 1) if you kept it in this workbook, or inline the header formatting.
2. Calls a new helper `FlagLowStock` that loops `Sales_Data` and writes `"REORDER"` into column G for any row with `Units < 10` (same logic as Exercise 2's Apps Script version, written in VBA this time — use the `For i = 2 To lastRow` loop pattern from lecture 01).
3. Forces recalculation with `Application.CalculateFull`.
4. Writes a timestamp into `Dashboard!B2`: `"Refreshed " & Format(Now, "mmm d, h:mm AM/PM")`.
5. Shows a `MsgBox` confirming success — or, in the error handler, a `MsgBox` naming what failed.

Assign `RefreshDashboard` to a Form Control button on the `Dashboard` sheet, captioned "Refresh Dashboard."

## Sheets track

Write one function, `refreshDashboard`, that does all of the following **in order**, wrapped in `try`/`catch`:

1. Calls `boldHeaderRow` (from Exercise 2) if kept in this project, or inlines the formatting.
2. Calls `flagLowStock` (from Exercise 2, batch-read/batch-write version).
3. Calls `SpreadsheetApp.flush()` to force recalculation.
4. Writes a timestamp into `Dashboard!B2` using `Utilities.formatDate`.
5. Shows `SpreadsheetApp.getActiveSpreadsheet().toast(...)` confirming success — or, in the `catch`, an alert naming what failed.

Add `refreshDashboard` as a **Refresh Now** item in the `Crunch Tools` menu from Exercise 2's `onOpen()`.

## A deliberate break — test your error handling

Before you call this exercise done, **break it on purpose**: rename the `Sales_Data` sheet to `Sales_Data_OLD` temporarily, then click your refresh button/menu item. It should fail *gracefully* — a clear message naming the problem (a `Worksheets("Sales_Data")`/`getSheetByName('Sales_Data')` call returning nothing), not a raw runtime error dialog with a line number and nothing else. Fix your error handler if it doesn't. Then rename the sheet back.

## Expected result

- Clicking the button/menu item once refreshes formatting, flags low-stock rows, updates the timestamp, and confirms success — in that order, from one click.
- Deliberately breaking the sheet reference produces a readable, specific failure message, not a raw crash.
- Running it twice in a row produces the same correct result both times (idempotent — no row gets double-flagged, no timestamp format breaks on the second run).

## Done when…

- [ ] One function/macro is the single entry point; every other routine is a private helper it calls.
- [ ] The deliberate-break test produces a graceful, specific error message.
- [ ] The timestamp updates correctly on every run, in a consistent format.
- [ ] You can point to the exact line where your code would fail if the source sheet were missing, and explain why your error handler catches it there instead of crashing.

## Submission

Commit your exported macro (`.bas`) or `Code.gs`, plus a one-paragraph write-up of what you broke and how the error handling responded, to `c41-week-12/exercise-03/`.
