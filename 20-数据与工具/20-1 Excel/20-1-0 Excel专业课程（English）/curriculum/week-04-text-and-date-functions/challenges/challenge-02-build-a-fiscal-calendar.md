# Challenge 2 — Build a Fiscal-Period Calendar

**Time:** ~60 minutes. **Difficulty:** Medium.

## The scenario

Crunch's finance team runs on a **fiscal year starting July 1**, not January 1 (a genuinely common corporate convention — plenty of real companies, universities, and governments run non-calendar fiscal years). Every report needs to show which fiscal year, fiscal quarter, and fiscal period (month-within-fiscal-year) a given transaction date falls into — and none of that lines up with `YEAR()`/`MONTH()` in the obvious way, because those two functions only know about the *calendar* year.

## Build the data

Add a new sheet, `Challenge 2`. Type this exactly as shown:

| TransactionDate |
|---|
| 2026-01-15 |
| 2026-06-30 |
| 2026-07-01 |
| 2026-07-15 |
| 2026-09-30 |
| 2026-10-01 |
| 2026-12-31 |
| 2027-03-15 |

Row 1 is your header (`TransactionDate`).

## Fiscal calendar rules (given — do not deviate)

- **Fiscal Year (FY)** runs July 1 → June 30. It's named for the calendar year it **ends** in — so July 1, 2026 through June 30, 2027 is **"FY2027,"** not FY2026 and not FY2026-27.
- **Fiscal Quarter (FQ)** — FQ1 is July–September, FQ2 is October–December, FQ3 is January–March, FQ4 is April–June (each fiscal quarter is 3 calendar months, just offset from the calendar quarter by 2 months).
- **Fiscal Period (FP)** — a simple 1–12 count of months since the fiscal year started: July = FP1, August = FP2, … June = FP12.

## Your task

Build four formula-driven columns: `FiscalYear`, `FiscalQuarter`, `FiscalPeriod`, and `FiscalYearEnd`.

### Step 1 — FiscalYear

Think through the logic before writing the formula: if the transaction's calendar month is July (7) or later, the fiscal year it belongs to **ends** the *following* calendar year. If the calendar month is January–June, the fiscal year ends in the *same* calendar year. Build this with `IF` and `YEAR`/`MONTH`:

```
=IF(MONTH(A2) >= 7, YEAR(A2) + 1, YEAR(A2))
```

Fill down through row 9. Spot check: `2026-07-01` (July) → `FY2027`. `2026-06-30` (June, one day earlier) → `FY2026`. `2027-03-15` → `FY2027` (January–June counts toward the fiscal year that *started* the previous July).

### Step 2 — FiscalQuarter

The core trick: shift the calendar month by the same 6-month offset before doing the usual "which quarter" math, wrapping months 1–6 around to 7–12 first. One clean approach:

```
=INT((MOD(MONTH(A2) + 5, 12)) / 3) + 1
```

Walk through this by hand for `MONTH = 7` (July): `MOD(7+5, 12) = MOD(12, 12) = 0`; `INT(0/3) = 0`; `+1 = 1` → **FQ1**. Correct. Now walk it by hand for `MONTH = 1` (January): `MOD(1+5, 12) = MOD(6, 12) = 6`; `INT(6/3) = 2`; `+1 = 3` → **FQ3**. Correct — January is fiscal Q3 per the rules above.

Fill this formula down through row 9, and hand-verify at least 2 rows yourself the same way before trusting it on the rest — this formula is dense enough that a typo is easy to miss without checking.

### Step 3 — FiscalPeriod

Similar month-shifting idea, but without the divide-by-3 — you want the raw 1–12 count, not a quarter bucket:

```
=MOD(MONTH(A2) + 5, 12) + 1
```

Fill down through row 9. `MONTH = 7` → `MOD(12,12)+1 = 0+1 = 1` (FP1, correct — July is the first fiscal period). `MONTH = 6` → `MOD(11,12)+1 = 11+1 = 12` (FP12, correct — June is the last fiscal period, the end of the fiscal year).

### Step 4 — FiscalYearEnd

Using your `FiscalYear` column, compute the actual calendar date the fiscal year ends on (always June 30 of the `FiscalYear` number):

```
=DATE(D2, 6, 30)
```

(assuming `FiscalYear` is column `D` — adjust the column letter to match your own layout). Fill down through row 9.

## Verification table

Check every row against this before submitting:

| TransactionDate | FiscalYear | FiscalQuarter | FiscalPeriod |
|---|---|---|---|
| 2026-01-15 | FY2026 | FQ3 | FP7 |
| 2026-06-30 | FY2026 | FQ4 | FP12 |
| 2026-07-01 | FY2027 | FQ1 | FP1 |
| 2026-07-15 | FY2027 | FQ1 | FP1 |
| 2026-09-30 | FY2027 | FQ1 | FP3 |
| 2026-10-01 | FY2027 | FQ2 | FP4 |
| 2026-12-31 | FY2027 | FQ2 | FP6 |
| 2027-03-15 | FY2027 | FQ3 | FP9 |

If any of your rows disagree with this table, your formula logic has a bug — trace it back through Steps 1–3 by hand for that specific row before assuming the table is wrong.

## Stretch

- Add an `IsYearEndMonth` column that flags `TRUE` for any transaction in the last fiscal period (FP12 — June) of its fiscal year, using your `FiscalPeriod` column and a simple `IF`.
- Build a single-cell formula (using `TEXT`/`&`) that produces a label like `"FY2027-Q1"` directly from `TransactionDate`, without needing the three helper columns — a genuinely harder version of the same problem, useful once you're comfortable with the underlying logic.
- Generalize: rewrite all three core formulas so the fiscal year start month (currently hard-coded as `7`) is instead read from a single cell, so the whole calendar could be repointed to an April-start or October-start fiscal year by changing one input.

## Submission

Keep the `Challenge 2` sheet, with all four formula columns, in your workbook.
