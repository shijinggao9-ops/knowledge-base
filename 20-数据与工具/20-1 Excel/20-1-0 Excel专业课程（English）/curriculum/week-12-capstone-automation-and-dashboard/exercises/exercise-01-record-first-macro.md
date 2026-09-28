# Exercise 1 — Record & Edit Your First Macro

**Goal:** record a macro, read the VBA it generates line by line, then hand-edit it into something you'd be comfortable running on someone else's workbook. By the end, `.Select`/`Selection` should look like a code smell to you, not normal VBA.

**Estimated time:** 60 minutes.

## Setup

Open Excel, enable the Developer tab (see the [week README setup](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/README.md#setup--enable-what-youll-need) if you haven't), and set macro security to **Disable all macros with notification**.

Build a small sheet named `Sales_Data` with this shape (or reuse your Week 11 workbook's cleaned Table if you have one):

| Order ID | Date | Region | Category | Units | Unit Price |
|---|---|---|---|---|---|
| 1001 | 2026-01-04 | North | Footwear | 3 | 89.99 |
| 1002 | 2026-01-05 | South | Apparel | 12 | 34.50 |
| 1003 | 2026-01-06 | East | Camping | 1 | 249.00 |
| 1004 | 2026-01-07 | West | Accessories | 25 | 12.75 |
| 1005 | 2026-01-08 | North | Footwear | 5 | 89.99 |

Save the file as `week12-exercise01.xlsm` **now**, before recording anything.

## Part A — Record

1. `Developer → Record Macro`. Name it `FormatSalesHeader`, store it in **This Workbook**, click OK.
2. Select `A1:F1` (the header row). Bold it. Fill it with a light blue (`Fill Color → light blue swatch`). Widen all six columns to fit their content (`Home → Format → AutoFit Column Width`, or double-click a column border).
3. Select `E2:E6` (the Units column). Apply a number format with no decimals (`Home → Number Format → Number`, 0 decimal places).
4. `Developer → Stop Recording`.

## Part B — Read

Open the VBA editor (`Alt+F11`), find `Module1` (or wherever the recorder put it) under `VBAProject → Modules`, and read `FormatSalesHeader` line by line. In a text file `notes.txt`, answer:

1. How many `.Select` / `Selection.___` pairs appear? List them.
2. What raw numeric value did Excel record for your fill color? (Something like `.Color = 15921906` — the exact number depends on your exact swatch.)
3. Does the `AutoFit` line select anything first, or act directly on `Columns(...)`? What does that tell you about which recorded actions need selection and which don't?

## Part C — Edit

Rewrite `FormatSalesHeader` from scratch (don't just delete `.Select` lines — some subsequent lines reference `Selection` and need converting to reference the range directly) so that it:

- Uses **no** `.Select` or `Selection` anywhere.
- Replaces the raw color number with `RGB(r, g, b)` using approximately the same blue you picked (close enough is fine — the point is readability, not pixel-matching).
- Uses one `With Range("A1:F1") ... End With` block for the header formatting.
- Sets the Units column's number format with `Range("E2:E6").NumberFormat = "0"`.
- Ends with `Range("A:F").EntireColumn.AutoFit`.

Run your rewritten version (delete the header formatting first so you can see it reapply, or just run it on a fresh copy of the sheet) and confirm it produces the same visual result as the recording did.

## Expected result

- Header row `A1:F1`: bold, light blue fill.
- `E2:E6`: whole numbers, no decimals.
- All six columns auto-fit to content width.
- Your hand-written `FormatSalesHeader` has zero occurrences of the word `Select` or `Selection`.

## Done when…

- [ ] `notes.txt` answers all three Part B questions.
- [ ] The hand-edited `FormatSalesHeader` runs successfully and produces the same formatting as the recorded version.
- [ ] You can explain, out loud, why acting on `Range("A1:F1")` directly is safer than `Range("A1:F1").Select` followed by `Selection.___` — specifically, what could go wrong with the selection-based version that can't go wrong with the direct version.

## Stretch

- Add a second macro, `HighlightHighUnits`, that loops `E2:E6` with a `For Each c In Range("E2:E6")` and colors any cell with `Units > 10` a light green — no recording, write it directly using the loop pattern from the lecture.
- Assign `FormatSalesHeader` to a Form Control button on the sheet, styled with the text "Format Header," and confirm clicking it (not the VBA editor's Run button) works.

## Submission

Export the module (`File → Export File...` in the VBA editor, saves a `.bas` file) and commit both `notes.txt` and the exported `.bas` to your portfolio under `c41-week-12/exercise-01/`.
