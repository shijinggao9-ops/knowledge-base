# Week 9 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hands-on formula-writing, a written explanation, and a build-your-own-model task. Keep each in its own tab within a `crunch-week9-homework` workbook.

---

## Problem 1 — Twenty financial-function warm-ups (75 min)

Write and check each formula in a `Warmups` tab, one per row, with the formula text visible alongside its result (toggle formula view, or add a label cell).

1. `=PMT(0.05/12, 36, 20000)` — a 3-year, 5% car loan on $20,000. Predict the sign before checking.
2. `=PMT(0.05/12, 36, 20000)*-1` — the same result displayed as a positive number for a report.
3. `=IPMT(0.05/12, 1, 36, 20000)` — interest in month 1 of that loan.
4. `=PPMT(0.05/12, 1, 36, 20000)` — principal in month 1. Confirm `IPMT + PPMT` from #3 and #4 equals #1.
5. `=IPMT(0.05/12, 36, 36, 20000)` — interest in the *final* month. Compare its magnitude to #3 and explain the difference in one sentence.
6. Build a 6-row cash-flow list: `-50000, 12000, 14000, 13000, 15000, 16000` (year 0 through 5). Write `=NPV(0.08, [years 1-5]) + [year 0]`.
7. Same cash flows: `=IRR([all 6 values, including year 0])`.
8. Confirm the NPV/IRR sign relationship: is #7's IRR above or below 8%, and does that match #6's NPV being positive or negative?
9. `=NPV(0.12, [same years 1-5])+[year 0]` — recompute #6 at a higher discount rate. Did NPV go up or down? Explain why higher discount rates always push NPV in that direction.
10. Build a 4-row dated cash flow: dates `2026-01-01`, `2026-07-15`, `2027-02-28`, `2027-09-10`, values `-30000, 9000, 11000, 14000`. Write `=XNPV(0.09, values, dates)`.
11. Same dated flows: `=XIRR(values, dates)`.
12. Compare #10/#11 to what plain `NPV`/`IRR` would give treating the same four values as evenly-spaced annual flows. Are they close or meaningfully different? What does that tell you about how irregular these particular dates are?
13. `=NPER(0.06/12, -500, 10000)` — how many monthly $500 payments pay off a $10,000 balance at 6% annual interest? *(Note the negative on the payment — `NPER` uses the same sign convention as `PMT`.)*
14. `=RATE(60, -500, 25000)` — what monthly rate makes a $500/month payment for 60 months pay off a $25,000 loan? Multiply by 12 for the approximate annual rate.
15. `=FV(0.07/12, 12*10, -200)` — the future value of saving $200/month for 10 years at 7% annual, compounding monthly.
16. Build a check formula confirming `ROUND(final amortization balance, 2) = 0` for any 5-year, $100,000, 5% loan schedule you build for this problem alone (12 rows minimum, or the full 60 if you prefer).
17. Write a formula combining `PMT` and `*12*[years]` to compute total amount repaid over the life of a $150,000, 4.5%, 15-year loan.
18. Subtract the original principal from #17's result to get total interest paid. Sanity-check: is it larger or smaller than the principal itself, and does that match your intuition for a 15-year loan?
19. `=PV(0.06/12, 36, -500)` — what loan amount could you afford today if you can pay $500/month for 3 years at 6%?
20. Write one sentence connecting #19 back to `PMT`: if you plug #19's result into `=PMT(0.06/12, 36, [that PV])`, what should you get back, and why does that round-trip make sense?

---

## Problem 2 — Sign convention identification (25 min)

In a `Signs` tab, for each scenario, state whether the value passed to a financial function should be **positive** or **negative**, and one sentence why:

1. The `pv` argument when you're the one *receiving* a loan.
2. The `pv` argument when you're the one *making* an investment (money leaving you today).
3. The `pmt` argument in a monthly savings-contribution `FV` formula (money leaving you each month).
4. The first cash flow inside an `IRR` array, for a typical new project.
5. A cash flow inside `NPV`'s argument list that represents a customer refund (money leaving the business).

---

## Problem 3 — Explain the model-structure discipline (45 min)

In `structure-writeup.md`, answer in prose (no more than 450 words total):

1. A coworker hands you a workbook where every formula has rates and terms typed directly inside it, with no separate input cells anywhere. Explain, concretely, what goes wrong the first time that workbook needs an assumption updated — not in the abstract, walk through what actually happens.
2. What's the difference between a **named range** and a plain cell reference (`$B$2`), in terms of what a formula communicates to a reader who has never seen the sheet before?
3. Why does a "check cell" that reduces to `TRUE`/`FALSE` catch more real errors than trusting your eyes to notice something looks off in a wall of numbers?
4. Give one example from this week's own models (loan, investment, or scenarios) where you decomposed a formula into more steps than strictly necessary, purely for auditability — and explain what a reviewer gains from that extra step.

---

## Problem 4 — Build a savings-goal model (75 min)

In a `SavingsGoal` tab, build a model answering: "How much do I need to save monthly to reach $50,000 in 8 years, at an assumed 6% annual return?"

1. An **Assumptions** block: `TargetAmount` ($50,000), `Years` (8), `AnnualReturn` (6.00%) — all named.
2. A `Required Monthly Savings` calculation using `PMT` (solving for the payment that grows to a target `fv`, with `pv = 0`).
3. A **Check** row: plug your computed monthly payment back into `FV(...)` and confirm it returns (within a cent) the original `TargetAmount`.
4. Use Goal Seek to answer a follow-up question without changing your `PMT` formula: if the saver can only contribute $400/month, what `AnnualReturn` would they need to still hit $50,000 in 8 years? Record the Goal Seek result and whether that required return seems realistic for a typical investment.

**Deliver** the working tab plus one sentence on what Task 4's answer implies about the plan if the saver truly can only afford $400/month.

---

## Problem 5 — Two-way sensitivity, different variables (60 min)

Build a new two-variable data table (Excel: a real Data Table; Sheets: the manual filled-formula pattern) answering a *different* question than Challenge 1's rate×term grid: for a **fixed** $250,000, 6%, 5-year loan, show `Total Interest Paid` (not monthly payment) across a grid varying:

- Rows: `AnnualRate` at 4.5%, 5.5%, 6.5%, 7.5%
- Columns: `TermYears` at 3, 5, 7, 10

**Deliver** the completed grid plus one sentence identifying the single most expensive combination (highest total interest) and the single cheapest, and whether that matches your intuition about how rate and term each drive total interest paid.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 75 min |
| 2 | 25 min |
| 3 | 45 min |
| 4 | 75 min |
| 5 | 60 min |
| **Total** | **~4.7 h** |

After homework, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/quiz.md) and ship the [mini-project](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/mini-project/README.md).
