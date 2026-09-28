# Week 9 — Resources

Free, official, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Tools (you already have these from Week 1)

- **Excel** (365, 2021, or Excel for the web) — <https://www.microsoft.com/microsoft-365/excel>
- **Google Sheets** — <https://sheets.google.com> (free with any Google account)

Nothing new to install this week — you're using the same workbook tool, writing a different category of formula in it. Note again: **Data Tables and Scenario Manager are Excel-only** — Sheets users rely on the manual filled-formula and dropdown-switcher patterns from Lecture 3.

## Required reading (this week's core)

- **Microsoft — PMT function:** <https://support.microsoft.com/en-us/office/pmt-function-0214da64-9a63-4996-bc20-214433fa6441>
  *Why: the canonical reference for the fixed-payment function this entire week is built on.*
- **Microsoft — IPMT function:** <https://support.microsoft.com/en-us/office/ipmt-function-5cce0ad6-8402-4a41-8d29-61a0b054cb6f>
  *Why: the interest-split half of the amortization schedule from Lecture 1.*
- **Microsoft — PPMT function:** <https://support.microsoft.com/en-us/office/ppmt-function-c370d9e3-7749-4ca4-beea-b06c6ac95e1b>
  *Why: the principal-split half of the same schedule.*
- **Microsoft — NPV function:** <https://support.microsoft.com/en-us/office/npv-function-8672cb67-2576-4d07-b67b-ac28acf2a568>
  *Why: the exact, official rules on argument timing that Lecture 1, Section 5's "biggest mistake" section is based on.*
- **Microsoft — IRR function:** <https://support.microsoft.com/en-us/office/irr-function-64925eaa-9988-495b-b290-3ad0c163c1bc>
  *Why: the official reference on the iterative solve and the `guess` argument.*
- **Microsoft — What-If Analysis overview:** <https://support.microsoft.com/en-us/office/introduction-to-what-if-analysis-22bffa5f-e891-4acc-bbd1-4d251458570f>
  *Why: the one-page map of Data Tables, Goal Seek, and Scenario Manager that Lecture 3 expands into full walkthroughs.*
- **Corporate Finance Institute — Financial Modeling Best Practices:** <https://corporatefinanceinstitute.com/resources/financial-modeling/financial-modeling-best-practices/>
  *Why: the industry-standard inputs/calculations/outputs convention Lecture 2 teaches, from a professional finance training source.*

## Reference (keep in tabs)

- **Microsoft — XNPV function:** <https://support.microsoft.com/en-us/office/xnpv-function-1b42bbf6-370f-4532-a0eb-d67c16b664b7>
- **Microsoft — XIRR function:** <https://support.microsoft.com/en-us/office/xirr-function-de1242ec-6477-445b-b11b-a303ad9adc9d>
- **Microsoft — NPER function:** <https://support.microsoft.com/en-us/office/nper-function-240535b5-6653-4d2d-bfcf-b6a38151d815>
- **Microsoft — RATE function:** <https://support.microsoft.com/en-us/office/rate-function-9f665657-4a7e-4bb7-a030-83fc59e748ce>
- **Microsoft — PV function:** <https://support.microsoft.com/en-us/office/pv-function-23879d31-0e02-4321-be01-da16e8168cbd>
- **Microsoft — FV function:** <https://support.microsoft.com/en-us/office/fv-function-2eef9f44-a084-4c61-bdd8-4fe4bb1b71b3>
- **Microsoft — Calculate multiple results with a Data Table:** <https://support.microsoft.com/en-us/office/calculate-multiple-results-by-using-a-data-table-e95e2487-6ca6-4413-ad12-77542a5ea50b>
- **Microsoft — Use Goal Seek to find a result by adjusting an input:** <https://support.microsoft.com/en-us/office/use-goal-seek-to-find-the-result-you-want-by-adjusting-an-input-value-320131d2-f599-4211-8f8f-b95d0b0a6a37>
- **Microsoft — Define and analyze a what-if scenario (Scenario Manager):** <https://support.microsoft.com/en-us/office/define-and-analyze-a-what-if-scenario-3d61a8b1-fdfe-4c9b-869d-cad2ab13f866>
- **Google — Goal Seek in Sheets:** <https://support.google.com/docs/answer/9088656>
- **Google — Data validation (for a scenario-switcher dropdown):** <https://support.google.com/docs/answer/186103>
- **Google — Named ranges in Google Sheets:** <https://support.google.com/docs/answer/63175>
- **Google — Financial functions in Sheets:** <https://support.google.com/docs/table/25273#financial>

## Practice beyond this week's exercises

- **Corporate Finance Institute — Free courses on financial modeling fundamentals:** <https://corporatefinanceinstitute.com/resources/financial-modeling/>
  *Why: more depth on how professional analysts structure loan and investment models, if this week's pace left you wanting more.*
- **Investopedia — Net Present Value (NPV):** <https://www.investopedia.com/terms/n/npv.asp>
  *Why: a clear, non-spreadsheet explanation of what NPV means conceptually, useful if the mechanics clicked before the intuition did.*
- **Investopedia — Internal Rate of Return (IRR):** <https://www.investopedia.com/terms/i/irr.asp>
  *Why: the same, for IRR — including the classic pitfalls with multiple sign changes this lecture only touched on briefly.*

## Glossary

| Term | Definition |
|------|------------|
| **Time value of money** | The principle that a dollar today is worth more than a dollar in the future, because today's dollar could be invested and grow. |
| **Amortization** | The process of paying off a loan through fixed periodic payments that each contain a shrinking interest portion and a growing principal portion. |
| **Present value (PV)** | A future cash flow's worth expressed in today's dollars, after discounting. |
| **Future value (FV)** | A present cash flow's worth at some future date, after compounding. |
| **Discount rate / hurdle rate** | The minimum rate of return required to make an investment worthwhile, used to discount future cash flows back to present value. |
| **NPV (Net Present Value)** | The present-value total of a stream of cash flows, minus the initial investment; positive means the investment creates value above the discount rate. |
| **IRR (Internal Rate of Return)** | The discount rate at which a project's NPV equals exactly zero — the project's own effective rate of return. |
| **XNPV / XIRR** | Date-aware versions of NPV/IRR that discount by the exact number of days between real calendar dates rather than assuming even periods. |
| **Input cell** | A cell holding a typed assumption — never a formula — that the rest of a model references. |
| **Named range** | A plain-English name assigned to a cell, usable in formulas in place of its raw address. |
| **Check cell** | A formula reducing to `TRUE`/`FALSE` (or a value that should be zero) that verifies a model's internal consistency. |
| **Data table** | A what-if tool that recalculates a formula's result across a whole range of one or two varying inputs at once. |
| **Goal Seek** | A what-if tool that runs a formula backwards: given a target output, it finds the single input value that produces it. |
| **Scenario Manager** | An Excel tool for saving and comparing named sets of multiple input values (e.g., Best/Base/Worst) with one click. |
| **Scenario switcher** | The Google Sheets workaround for Scenario Manager: a dropdown plus `INDEX`/`MATCH` "active" rows driving the rest of the model. |

---

*Broken link? Open an issue or PR.*
