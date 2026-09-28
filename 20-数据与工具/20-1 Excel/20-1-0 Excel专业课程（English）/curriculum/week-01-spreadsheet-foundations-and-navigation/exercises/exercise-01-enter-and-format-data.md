# Exercise 1 — Enter & Format a Data Block

**Goal:** Get real data into the grid correctly, then apply the formatting from Lecture 3 so it reads like a finished mini-report — not a wall of "General"-formatted numbers.

**Estimated time:** 45 minutes.

## Setup

In your `crunch-week1` workbook, add a new sheet and rename it `Exercise 1`.

## Part A — Enter the data

Starting at `A1`, type this data **exactly as shown**, one value per cell, using `Tab` to move right across a row and `Enter` to drop to the next row (see Lecture 2, section 1). Do not paste it — the point is entering it by hand so the type-guessing behavior from Lecture 1 is something you actually watch happen.

| Item | Category | Unit Price | Qty | Restock Date | In Stock |
|---|---|---|---|---|---|
| Notebook | Office | 3.5 | 120 | 1/15/2026 | TRUE |
| USB-C Cable | Electronics | 8.99 | 45 | 2/1/2026 | TRUE |
| Desk Lamp | Furniture | 22 | 0 | 1/28/2026 | FALSE |
| Stapler | Office | 6.25 | 60 | 3/10/2026 | TRUE |
| Monitor Stand | Furniture | 34.5 | 12 | 2/14/2026 | TRUE |
| Whiteboard Marker | Office | 1.75 | 300 | 1/20/2026 | TRUE |
| Webcam | Electronics | 45 | 0 | 3/1/2026 | FALSE |

Row 1 is your header row.

## Part B — Verify the types landed correctly

Before formatting, check that each column was interpreted the way you expect:

1. Click any cell in the **Unit Price** column. Look at the Name Box and the alignment — it should be **right-aligned** (a number).
2. Click any cell in the **Restock Date** column. It should also be right-aligned (dates are numbers underneath — Lecture 1, section 3).
3. Click any cell in the **In Stock** column. `TRUE`/`FALSE` should be centered.
4. Click any cell in **Item**, **Category**. They should be left-aligned (text).

If any numeric or date column came in left-aligned, that value was likely parsed as text — fix it now: re-type it, or select the cell, set the format explicitly to Number/Date first, then re-enter the value.

## Part C — Format it

Apply, in this order:

1. **Header row (row 1):** bold, with a bottom border (Lecture 3, section 3).
2. **Unit Price column:** Currency format, 2 decimal places (`$3.50`, `$8.99`, etc.).
3. **Restock Date column:** ISO date format, `YYYY-MM-DD` (Lecture 3, section 1) — so `1/15/2026` displays as `2026-01-15`.
4. **Qty column:** plain Number format, 0 decimal places (whole units, no decimal point).
5. **Auto-fit every column** so nothing is truncated or shows `#####`.
6. **Freeze the header row** (Lecture 2, section 4) — scroll down a few rows and confirm row 1 stays visible.
7. **Conditional formatting:** apply a rule that highlights any row where **Qty is 0** (the out-of-stock items) — a light red/pink fill on the Qty cell is enough for this exercise; highlighting the whole row is a nice stretch (hint: you'll need this technique again later in the course once formulas exist, so a simple single-cell rule is completely fine for now).

## Expected result

- 7 data rows + 1 header row, all readable at a glance without zooming or widening manually.
- Unit Price shows dollar signs and exactly 2 decimals.
- Restock Date reads `2026-01-15` style, not `1/15/2026`.
- Qty has no decimal point.
- Row 1 stays frozen and visible when you scroll.
- The two rows with `Qty = 0` (Desk Lamp, Webcam) are visually flagged by your conditional formatting rule.

## Done when…

- [ ] All 7 rows are entered with the correct data type per column (verified in Part B).
- [ ] Header row is bold with a bottom border.
- [ ] Unit Price is Currency, Restock Date is ISO, Qty is whole-number.
- [ ] No column shows `#####` or truncated text.
- [ ] Header row is frozen.
- [ ] The 2 out-of-stock rows are conditionally highlighted.

## Stretch

- Add an 8th row for a new item of your choice, and confirm the conditional formatting rule automatically applies to it too (a well-built range-based rule should, without you touching the rule again).
- Try the **Center Across Selection** technique (Lecture 3, section 2) on a merged-looking title above your header row, without actually merging cells.

## Submission

Keep this sheet in your workbook — you'll reference the same layout style in the mini-project this week.
