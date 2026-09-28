# Exercise 3 — Find Break-Even With Goal Seek

**Goal:** Build a simple profit model for a new Crunch product, then use Goal Seek to find the exact unit volume where the product stops losing money and starts making it.

**Estimated time:** 60 minutes.

## Setup

On the `WhatIf` tab, build this profit model:

```
      A                      B
1   ASSUMPTIONS
2   Unit Price               45.00
3   Variable Cost/Unit       27.00
4   Fixed Costs           95000.00
5   Units Sold              3000     <- this is the cell Goal Seek will change
6
7   CALCULATIONS
8   Revenue               =B2*B5
9   Total Variable Cost   =B3*B5
10  Contribution Margin   =B8-B9
11  Profit                =B10-B4
```

Name `B2` `UnitPrice`, `B3` `VariableCost`, `B4` `FixedCosts`, `B5` `UnitsSold` — then rewrite rows 8–11 to use the names instead of raw cell addresses:

```
8   Revenue               =UnitPrice*UnitsSold
9   Total Variable Cost   =VariableCost*UnitsSold
10  Contribution Margin   =B8-B9
11  Profit                =B10-FixedCosts
```

At `UnitsSold = 3000`, confirm `Profit` shows **-$41,000** — the product is currently losing money at this volume.

## Tasks

1. **Do the algebra first, by hand, before touching Goal Seek.** Contribution margin per unit is `UnitPrice - VariableCost = 45 - 27 = 18`. Break-even units = `FixedCosts / (UnitPrice - VariableCost) = 95000 / 18 ≈ 5,277.8`. Write this prediction down — you'll check Goal Seek against it in Task 3.

2. **Run Goal Seek.**
   - **Excel:** **Data → What-If Analysis → Goal Seek** → **Set cell:** the `Profit` cell → **To value:** `0` → **By changing cell:** the `UnitsSold` cell → **OK**.
   - **Google Sheets:** **Tools → Goal Seek** → same three fields → **OK**.

3. **Compare Goal Seek's answer to your hand calculation from Task 1.** They should match (within a fraction of a unit — Goal Seek finds the exact break-even, which isn't a whole number since you can't literally sell 0.8 of a unit in reality; round up to the next whole unit for a real business decision, and explain why rounding up, not down, is the correct direction).

4. **Confirm the mechanics.** After Goal Seek runs, check that `UnitsSold` (`B5`) has actually been overwritten with the new value, and `Profit` now reads `$0.00` (or extremely close, within rounding).

5. **Reset and re-target.** Change `UnitsSold` back to `3000` by hand. Now run Goal Seek again, this time targeting a **profit of $50,000** instead of `0` (same Set cell, same By changing cell, **To value** = `50000`). What unit volume does that require?

6. **A pricing question.** Reset `UnitsSold` to `3000` one more time. This time, run Goal Seek with **Set cell** = `Profit`, **To value** = `0`, but **By changing cell** = `UnitPrice` instead of `UnitsSold` — i.e., holding volume fixed at 3,000 units, what price would Crunch need to charge to break even?

## Expected results (spot checks)

- Hand-calculated break-even: **≈ 5,278 units** (5,277.78 exactly).
- Goal Seek's answer for Task 2/3 should match within rounding.
- Task 5 (profit target of $50,000): required units ≈ **8,056** *(`(95000 + 50000) / 18 = 8,055.6`)*.
- Task 6 (break-even price at 3,000 units): required price ≈ **$58.67** *(`FixedCosts/UnitsSold + VariableCost = 95000/3000 + 27 = 31.67 + 27 = 58.67`)*.

## Done when…

- [ ] Your hand-calculated break-even (Task 1) matches Goal Seek's result (Task 2–3) within rounding.
- [ ] You can explain, in one sentence, why the real-world break-even volume should be rounded **up**, not down or to the nearest whole number.
- [ ] You've run Goal Seek three separate times (Tasks 2, 5, 6) with three different **Set cell**/**By changing cell** combinations and gotten sensible results for each.
- [ ] `UnitsSold` and `UnitPrice` are back to their original values (`3000` and `45.00`) after you finish, unless you intentionally kept a Goal Seek result — note in a comment which state you left the sheet in.

## Stretch

- Goal Seek can only solve for one input at a time. Without running it again, use plain algebra to answer: if Crunch cuts `VariableCost` from $27 to $24 (a supplier discount), what's the new break-even unit volume at the original $45 price? Verify your algebra by plugging the new `VariableCost` into the model directly (not through Goal Seek) and confirming `Profit` at 5,278 units is now positive.
- Build a one-variable data table (Lecture 3, Section 2) showing `Profit` at unit volumes from 2,000 to 9,000 in steps of 1,000, so the break-even point is visible as the row where the sign flips from negative to positive — a visual cross-check on the exact number Goal Seek gave you.

## Submission

Commit the `WhatIf` tab to your portfolio under `c41-week-09/exercise-03/`.
