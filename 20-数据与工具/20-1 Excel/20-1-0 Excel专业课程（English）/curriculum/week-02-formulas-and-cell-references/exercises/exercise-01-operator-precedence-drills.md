# Exercise 1 — Operator & Precedence Drills

**Goal:** Get order of operations and the five core aggregate functions into your fingers, so reading and predicting a formula's result stops requiring conscious effort.

**Estimated time:** 45–60 minutes.

## Setup

In your workbook, create (or rename) a sheet tab called `Ex1`. You'll work in two parts: a prediction drill (no data needed) and a function drill (build a small table).

## Part A — Predict, then check (10 formulas)

For each formula below: **write your predicted result on paper or in a `Notes` column first**, then type the formula into a cell exactly as shown and compare. If you're wrong, work out on paper exactly which operator ran first before moving to the next one.

Type each into its own cell, e.g. `A1` through `A10`, and put your prediction in the cell next to it (`B1` through `B10`) *before* typing the formula in `A`.

1. `=6+2*3`
2. `=(6+2)*3`
3. `=20-4/2`
4. `=(20-4)/2`
5. `=2^3+1`
6. `=2^(3+1)`
7. `=10-2-3` *(watch left-to-right on tied precedence)*
8. `=100/10/2` *(same — left-to-right)*
9. `=3+4*2^2-1`
10. `=(3+4)*(2^2-1)`

## Part B — The five aggregate functions

Build this table starting at `A15`:

```
      A            B
15  Product      Units Sold
16  Notebook     120
17  Pen          340
18  Folder       (leave blank)
19  Marker       85
20  Binder       "discontinued"
```

Type the word `discontinued` as literal text into `B20` — not a formula.

Write these formulas in cells `D16` through `D22` (one per row), labeling each in column `C`:

11. `=SUM(B16:B20)` — label it `Total`.
12. `=AVERAGE(B16:B20)` — label it `Average`. *(Predict: how many cells does the denominator actually count?)*
13. `=COUNT(B16:B20)` — label it `Count (numeric)`.
14. `=COUNTA(B16:B20)` — label it `CountA (non-blank)`.
15. `=COUNTBLANK(B16:B20)` — label it `Blank count`.
16. `=MIN(B16:B20)` — label it `Minimum`.
17. `=MAX(B16:B20)` — label it `Maximum`.

## Expected results (spot checks)

- Part A, #1 → `12` (not `24`).
- Part A, #7 → `5` (not `11` — left to right: `10-2=8`, `8-3=5`).
- Part A, #9 → `18` (order: `2^2=4`, `4*4=16`, `3+16=19`, `19-1=18` — walk through it yourself if this doesn't match your prediction).
- Part B, #12 (`AVERAGE`) → `181.67` (rounded), from 3 numeric values (`120+340+85=545`, `545/3≈181.67`) — **not** divided by 5.
- Part B, #13 (`COUNT`) → `3`. Part B, #14 (`COUNTA`) → `4`. Part B, #15 (`COUNTBLANK`) → `1`.

## Done when…

- [ ] All 10 Part A formulas are typed and your predictions column shows where you were right vs. wrong.
- [ ] All 7 Part B formulas are correctly labeled and match the spot checks above.
- [ ] You can explain out loud, without looking, why `COUNT` and `COUNTA` returned different numbers on the exact same range.
- [ ] For any Part A formula you predicted wrong, you've written one sentence in a `Notes` cell explaining which operator you underestimated.

## Stretch

- Write one formula combining all five functions' *results* into a sentence using `&`: e.g. `="Total: "&SUM(B16:B20)&", Average: "&ROUND(AVERAGE(B16:B20),1)`. Confirm it displays as readable text, not an error.
- Add a sixth product with a **negative** number of units (a return). Re-check which of the seven B-column formulas are affected and which aren't.

## Submission

Keep the `Ex1` sheet in your `crunch-week2` workbook — you'll build on the same file for Exercises 2 and 3.
