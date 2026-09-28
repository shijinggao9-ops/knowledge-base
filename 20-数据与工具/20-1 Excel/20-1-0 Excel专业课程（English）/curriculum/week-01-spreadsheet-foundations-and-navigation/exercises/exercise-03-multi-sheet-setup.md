# Exercise 3 — Set Up a Multi-Sheet Workbook

**Goal:** Build a workbook with more than one sheet, laid out the way real workbooks should be — raw data separated from summary/notes — with clean naming, color-coding, and cross-sheet references. This is the structural convention (Lecture 2, section 5) you'll reuse every week for the rest of the course.

**Estimated time:** 45 minutes.

## Setup

You'll build **three sheets** in this order, in your `crunch-week1` workbook.

## Part A — `Raw Data` sheet

1. Create a new sheet. Rename it exactly `Raw Data`.
2. Right-click the tab → set its color to **blue** (this week's convention: blue = source data, never edited by hand after entry).
3. Enter this small dataset starting at `A1`:

| Region | Rep | Units Sold | Unit Price |
|---|---|---|---|
| East | Alvarez | 42 | 19.99 |
| East | Byrne | 31 | 19.99 |
| West | Chen | 58 | 21.5 |
| West | Diallo | 27 | 21.5 |
| North | Evans | 19 | 18.75 |

4. Format: bold header row with bottom border, Currency on Unit Price, plain Number on Units Sold, auto-fit all columns, freeze row 1.

## Part B — `Notes` sheet

1. Create a second new sheet. Rename it `Notes`.
2. Color its tab **gray** (convention: gray = documentation, not data).
3. In `A1`, type a title: `Workbook Notes`. In `A3`, type: `Source: Raw Data sheet, entered manually for C41 Week 1 Exercise 3.` In `A4`, type: `Last updated:` and in `B4` type today's date (let it auto-format as a date).
4. Bold `A1` and increase its font size to 14pt.

## Part C — `Summary` sheet with cross-sheet references

1. Create a third sheet. Rename it `Summary`. Color its tab **green** (convention: green = calculated/summary output).
2. **Reorder the tabs** (Lecture 2, section 5) so they read left to right: `Raw Data`, `Summary`, `Notes` — summary sits next to its source, notes trails at the end.
3. In the `Summary` sheet, `A1`, type `Region`. In `B1`, type `Rep`. In `C1`, type `Units Sold`.
4. In `A2`, type an **equals sign followed by a cross-sheet reference** to pull East's first rep's region from Raw Data — type exactly:
   ```
   ='Raw Data'!A2
   ```
   Press Enter. This isn't a lesson in formulas yet (that's Week 2) — it's a lesson in the **sheet-name-plus-exclamation-mark** addressing syntax from Lecture 1, section 2. Confirm the cell now displays `East`, pulled live from `Raw Data`.
5. Do the same for `B2` (`='Raw Data'!B2`) and `C2` (`='Raw Data'!C2`). Confirm you get `Alvarez` and `42`.
6. Now go back to `Raw Data` and change Alvarez's Units Sold from `42` to `50`. Return to `Summary` — `C2` should now read `50` automatically. This is the payoff of the "raw data separate from summary" convention: the summary always reflects the current source, with zero manual re-typing.
7. Bold the `Summary` header row, freeze it, and auto-fit columns.

## Expected result

- Three sheets, correctly named and colored: `Raw Data` (blue), `Summary` (green), `Notes` (gray), in that left-to-right order.
- `Raw Data` holds the only hand-typed sales numbers in the workbook.
- `Summary!A2:C2` displays `East`, `Alvarez`, `50` — live-pulled from `Raw Data`, not retyped.
- Editing a value on `Raw Data` updates `Summary` without you touching `Summary` at all.

## Done when…

- [ ] All three sheets exist, correctly named (exact spelling/casing matters — `Raw Data`, `Summary`, `Notes`).
- [ ] Tab colors match the convention: blue / green / gray.
- [ ] Tabs are ordered `Raw Data`, `Summary`, `Notes` left to right.
- [ ] `Summary!A2:C2` uses live `='Raw Data'!...` references, not typed-in values.
- [ ] You verified the live link by editing `Raw Data` and watching `Summary` update.

## Stretch

- Add two more cross-sheet reference rows to `Summary` (for Byrne and Chen), pulling from `Raw Data` rows 3 and 4 the same way.
- On the `Notes` sheet, add a **hyperlink** (Excel: `Ctrl+K`; Sheets: `Ctrl+K` also) in `A6` that jumps to the `Summary` sheet when clicked — a nice navigation touch for a workbook that will grow.

## Submission

Keep all three sheets in your workbook — this exact `Raw Data` / `Summary` / `Notes` pattern is the layout convention the mini-project builds on.
