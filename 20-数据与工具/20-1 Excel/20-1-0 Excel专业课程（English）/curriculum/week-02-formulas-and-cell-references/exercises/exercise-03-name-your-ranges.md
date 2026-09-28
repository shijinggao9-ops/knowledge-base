# Exercise 3 — Name Ranges for Readability

**Goal:** Take a working sheet full of cryptic `$`-locked cell addresses and rewrite it using named ranges — proving the formulas still compute identically, while becoming genuinely readable to a stranger.

**Estimated time:** 45 minutes.

## Setup

Create (or rename) a sheet tab called `Ex3`. Build this small commission-calculator table exactly:

```
      A            B          C
1   Rep          Sales      Commission
2   Priya        18000
3   Omar         9500
4   Tanvi         26000
5   Leo           4200
```

Off to the side, two shared constants:

```
      F                    G
1   Commission Rate      0.06
2   Bonus Threshold      15000
3   Bonus Amount         250
```

The rule: every rep earns `Sales * Commission Rate`. Any rep whose `Sales` is **at or above** `Bonus Threshold` also gets a flat `Bonus Amount` added on top.

## Tasks

1. **Build it first with raw absolute references.** In `C2`, write a formula computing total commission (base commission plus bonus if earned) using `$G$1`, `$G$2`, `$G$3` directly — no `IF` needed if you'd rather write two helper columns first (a `Base` column and a `Bonus` column), but a single formula using `IF` is the cleaner target: `=B2*$G$1 + IF(B2>=$G$2, $G$3, 0)`. Fill down through `C5`. Confirm it works — you haven't learned `IF` formally yet (that's Week 3), but reading this one should be followable from context: "if sales meets the threshold, add the bonus, otherwise add zero."

2. **Name the three constants.** Using the Name Box (Excel) or Data → Named ranges (Sheets), name:
   - `G1` → `CommissionRate`
   - `G2` → `BonusThreshold`
   - `G3` → `BonusAmount`

3. **Rewrite the formula using the names.** In a new column `D`, label `D1`: `Commission (named)`. In `D2`, rewrite the exact same logic from Task 1, but replace every `$G$1`/`$G$2`/`$G$3` with its name: `CommissionRate`, `BonusThreshold`, `BonusAmount`. Fill down through `D5`.

4. **Prove equivalence.** In `E2`, write `=C2=D2` (a simple equality check) and fill down through `E5`. Every cell should show `TRUE` — the named-range version and the raw-address version must compute identical results; only the *readability* changed.

5. **Break a name on purpose, then fix it.** Temporarily rename `CommissionRate` to `CommRate` using the Name Manager / Named ranges panel (rename the *name*, not the cell). Watch what happens to the formulas in column `D` that still say `CommissionRate` — they should now show `#NAME?`. Fix it by either renaming back to `CommissionRate`, or updating the formulas to use `CommRate`. Write one sentence in a `Notes` cell about which repair you chose and why.

## Expected results (spot checks)

- Priya (`18000` sales, meets threshold) → `18000*0.06 + 250 = 1330`.
- Omar (`9500` sales, below threshold) → `9500*0.06 + 0 = 570`.
- Tanvi (`26000` sales, meets threshold) → `26000*0.06 + 250 = 1810`.
- Leo (`4200` sales, below threshold) → `4200*0.06 + 0 = 252`.
- Every cell in column `E` → `TRUE`.

## Done when…

- [ ] Columns `C` and `D` are numerically identical for all four reps (verified by the `TRUE`s in column `E`).
- [ ] Column `D`'s formulas contain zero raw `$G$` addresses — every constant is referenced by name.
- [ ] You deliberately broke a name, saw `#NAME?`, and fixed it — and can explain in one sentence what caused the error.
- [ ] You can read `D2`'s formula out loud and it sounds like an English sentence describing the business rule, without needing to check what any cell contains.

## Stretch

- Name the whole `B2:B5` range `AllSales` and write `=SUM(AllSales)` and `=AVERAGE(AllSales)` beside the table.
- Open the Name Manager (Excel: `Ctrl+F3`) or Named ranges panel (Sheets) and delete one name you no longer need (e.g., a leftover from the rename step). Confirm any formula that referenced it now shows `#NAME?`, then decide whether to restore it or rewrite the formula.

## Submission

Keep the `Ex3` sheet in your `crunch-week2` workbook alongside `Ex1` and `Ex2`. This workbook — all three exercise sheets together — is what you'll draw on conceptually for this week's challenges.
