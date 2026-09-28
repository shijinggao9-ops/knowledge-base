# Mini-Project — A Loan + Investment Model With Scenarios

> Build one complete, auditable workbook for Crunch Manufacturing: a structured equipment-loan amortization schedule, an investment evaluation with NPV/IRR, and a Best/Base/Worst scenario comparison — all built on Lecture 2's inputs/calculations/outputs discipline, so a stranger could open it and understand it in five minutes.

**Estimated time:** 3–3.5 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it's designed to be the single most "real" deliverable in the course so far — the kind of workbook an actual finance or operations analyst builds before a capital-spending decision. You've already built every individual piece across the exercises and challenges this week; the mini-project's job is to combine them into one coherent, well-structured model instead of three disconnected exercises.

---

## The brief

Crunch Manufacturing is borrowing **$250,000** to fund new equipment, and using the operating capacity that equipment unlocks to pursue a **$120,000** capital project expected to return **$38,000/year** for 5 years under normal conditions. The board wants one workbook answering three questions:

1. What does the loan actually cost, month by month, and in total?
2. Is the investment worth making, in today's dollars, and at what rate of return?
3. How does the investment decision hold up if conditions are better or worse than expected?

---

## Deliverable

A single workbook, `crunch-week9-mini-project.xlsx` (or the Sheets equivalent), containing four tabs, plus a `notes.md` reflection.

### Tab 1 — `Loan`

- An **Assumptions** block: `LoanAmount` ($250,000), `AnnualRate` (6.00%), `TermYears` (5) — all named cells.
- A full 60-month amortization schedule (Period, Payment, Interest, Principal, Balance) using `PMT`, `IPMT`, `PPMT`, exactly as built in Exercise 1.
- A **Check** cell confirming the final balance rounds to `$0.00`.
- A summary block: Monthly Payment, Total Paid, Total Interest Paid.

### Tab 2 — `Investment`

- An **Assumptions** block: `InitialInvestment` ($120,000), `AnnualCashFlow` ($38,000), `ProjectYears` (5), `DiscountRate` (10.00%) — all named cells.
- `NPV` and `IRR` calculations, correctly handling the year-0 cash flow (Lecture 1, Section 5–6).
- A **Check** cell confirming the NPV-positive/IRR-above-hurdle relationship holds (Lecture 2, Section 7).

### Tab 3 — `Scenarios`

- Best/Base/Worst scenarios varying `AnnualCashFlow` and `DiscountRate` together (use Challenge 2's values, or your own defensible set — state which if you deviate).
- Excel: a real Scenario Manager with a generated Summary report. Sheets: a dropdown-driven scenario switcher plus a captured three-row comparison table.
- All three scenarios' NPV and IRR visible together in one place on this tab.

### Tab 4 — `Summary`

- A clean, decision-maker-facing rollup, referencing the other three tabs with simple formulas — **no new calculations on this tab**, only references:
  - Monthly Loan Payment
  - Total Interest Paid Over Life of Loan
  - Investment NPV and IRR (Base case)
  - Best/Base/Worst NPV comparison (one line each)
  - A one-cell, formula-driven **recommendation**: proceed or don't, based on whatever rule you define (state the rule in `notes.md` — e.g., "proceed if Base-case NPV is positive and Worst-case NPV loss is less than 15% of the initial investment").

### `notes.md` (~250–300 words)

1. State your recommendation in one sentence, then justify it referencing specific numbers from your `Summary` tab.
2. Explain, specifically, how the `Investment` tab's discount rate relates to the loan's interest rate — are they the same number, and should they be? *(Hint: think about what each rate actually represents — cost of borrowing vs. required return on invested capital — and whether a company should demand a return higher than what it's paying to borrow.)*
3. Which single input, if the board challenged it, are you least confident in — and what would you want to research or confirm before presenting this model for real?

---

## Required behaviors (test these yourself before submitting)

- [ ] Change `AnnualRate` on the `Loan` tab from 6.00% to 6.50%. The Monthly Payment, the entire schedule, and the `Summary` tab's Monthly Payment figure all update — nowhere in the workbook should you need to manually re-type a number to make this propagate.
- [ ] Change `DiscountRate` on the `Investment` tab. NPV, IRR, and the `Summary` tab's investment figures all update; the `Scenarios` tab's **Base** scenario should reflect this too if — and only if — you've wired the scenario system to read from the same source rather than storing a disconnected duplicate rate. *(If Base's discount rate is hardcoded separately inside Scenario Manager/your switcher table, note that as an intentional design choice in `notes.md` — Scenario Manager and switcher tables commonly do store their own copies on purpose, precisely so a scenario stays fixed even if the "live" assumption changes. Either choice is acceptable; an unexplained inconsistency is not.)*
- [ ] Every scenario in `Scenarios` produces a different NPV/IRR pair when selected/shown — if two scenarios produce identical output, an input didn't actually change between them.
- [ ] The `Loan` tab's Check cell reads `TRUE` (or `$0.00`) and the `Investment` tab's Check cell reads `TRUE`.
- [ ] Every number on the `Summary` tab is a formula referencing another tab — not a typed, static copy.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness | 30% | Amortization schedule pays off exactly; NPV/IRR calculated correctly (year-0 handling right); scenario numbers match the required-behaviors test |
| Model structure | 25% | Every tab follows the Assumptions/Calculations/Outputs shape from Lecture 2; every changeable number is a single named cell referenced everywhere else |
| What-if mechanics | 20% | Real Scenario Manager or a genuinely working Sheets switcher; all three scenarios distinct and verifiable |
| Auditability | 15% | A stranger could open `Summary` and understand the recommendation without reading a single underlying formula |
| Reflection | 10% | `notes.md` engages specifically with the discount-rate-vs-loan-rate question, not just restates the numbers |

## Stretch goals

- Add a two-variable data table (Challenge 1's technique) to the `Loan` tab showing monthly payment sensitivity to rate × term, and reference the single most favorable cell from that grid directly in your `Summary` recommendation.
- Add a Goal Seek-derived figure to `Summary`: "the maximum interest rate Crunch could accept and still have the Base-case investment clear a 15% IRR hurdle" — run Goal Seek to find it, then paste the resulting number as a static, labeled fact (since Goal Seek's result isn't a live formula) with a note on what you solved for.
- Extend the amortization schedule with an extra-payment column: what if Crunch pays an additional $500/month toward principal? Rebuild the schedule to show how many months earlier the loan pays off and how much total interest that saves. *(This requires a schedule that recalculates the balance each period based on actual remaining principal rather than assuming the original `nper` — a genuinely harder version of Exercise 1's structure.)*

## Why this matters

This is the shape of real financial analysis: not one formula, but a small system of formulas — a loan, an investment, a set of what-ifs, and a summary someone who's never opened your workbook can trust. Every dashboard you built in Week 8 answered "what happened." This model answers "what should we do" — a fundamentally different, higher-stakes question, and one you can now answer with a spreadsheet instead of a gut feeling.

When done: push/save your work, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/quiz.md), and start [Week 10 — Dynamic arrays & modern functions](../../week-10-dynamic-arrays-and-modern-functions/).
