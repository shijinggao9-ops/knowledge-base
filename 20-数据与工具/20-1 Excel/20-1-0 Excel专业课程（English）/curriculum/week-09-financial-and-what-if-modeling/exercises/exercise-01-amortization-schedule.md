# Exercise 1 — Build an Amortization Schedule

**Goal:** Turn Lecture 1's `PMT`/`IPMT`/`PPMT` functions into a complete, correct, 60-row amortization schedule for Crunch Manufacturing's equipment loan — the running balance must land on exactly zero at the end.

**Estimated time:** 60 minutes.

## Setup

On the `Loan` tab of `crunch-week9`, build the assumptions block from Lecture 2, Section 3, and name all three cells:

```
      A                  B
1   Loan Amount        250000     <- name "LoanAmount"
2   Annual Rate          6.00%    <- name "AnnualRate"
3   Term (Years)              5   <- name "TermYears"
```

Confirm the names took: click cell `B1` and check the Name Box (Excel) or **Data → Named ranges** (Sheets) shows `LoanAmount`.

## Tasks

1. **Monthly payment.** In a labeled `Monthly Payment` cell (e.g. `B5`), write `=PMT(AnnualRate/12, TermYears*12, LoanAmount)`. *(Expected: approximately `-$4,832.57`.)*

2. **The schedule header.** A few rows below, starting at row 8, build the schedule table header: `Period | Payment | Interest | Principal | Balance`.

3. **Row 0 — the starting balance.** In the `Period` column write `0`; leave `Payment`/`Interest`/`Principal` blank; in `Balance` put `=LoanAmount`.

4. **Row 1 — the first real payment.** `Period` = `1`. `Payment` = a reference to your Monthly Payment cell (e.g. `=$B$5`). `Interest` = `=IPMT(AnnualRate/12, A10, TermYears*12, LoanAmount)` where `A10` is *that row's* Period cell. `Principal` = the matching `PPMT` formula. `Balance` = previous row's balance plus this row's principal.

5. **Fill down 59 more rows.** Select row 1's `Period` through `Balance` cells and fill down through row 60 (period 60). Watch the `Period` column count up `1, 2, 3, …, 60` — if it doesn't, your `Period` formula (or the cell you're filling from) has an absolute reference where it needs a relative one.

6. **Verify the payoff.** The `Balance` in the final row (period 60) must equal `0.00` (or a fraction of a cent — acceptable rounding). If it's off by a large amount, an `IPMT`/`PPMT` argument is referencing the wrong `per` cell, or your `Balance` formula's sign is backwards.

7. **Spot-check the identity.** Pick any single row and confirm `Interest + Principal` for that row equals the `Payment` for that row (Lecture 1, Section 3's identity). *(All three should be negative, and interest + principal should equal payment to the penny.)*

8. **Total interest paid.** Below the schedule, add `Total Interest Paid` = `SUM` of the entire `Interest` column. *(Expected: roughly $39,954 over the 5-year loan — meaning Crunch pays back about $289,954 total on a $250,000 loan.)*

## Expected results (spot checks)

- Monthly Payment ≈ `-$4,832.57`.
- Period 1: Interest ≈ `-$1,250.00`, Principal ≈ `-$3,582.57`.
- Period 60: Balance = `$0.00` (or within a cent).
- Total Interest Paid ≈ `-$39,954` (sign depends on how you summed it — either report the magnitude or wrap with `ABS()` for the summary line).

## Done when…

- [ ] All three assumption cells are named and every formula in the schedule references the names, not raw numbers.
- [ ] The schedule has exactly 60 payment rows (periods 1–60) plus the row-0 starting balance.
- [ ] The final balance is `0.00` (within rounding).
- [ ] `Interest + Principal` matches `Payment` on at least the row you spot-checked.
- [ ] `Total Interest Paid` is computed with a `SUM`, not typed by hand.

## Stretch

- Add a column `Cumulative Principal Paid` — a running total of principal paid to date — and confirm it reaches `LoanAmount` exactly by period 60.
- Change `TermYears` from `5` to `3` and re-fill the schedule (now only 36 rows are meaningful). Confirm the monthly payment goes up but total interest paid goes *down* — and be ready to explain why in one sentence.

## Submission

Commit your `crunch-week9` workbook (or export the `Loan` tab as a standalone file) to your portfolio under `c41-week-09/exercise-01/`.
