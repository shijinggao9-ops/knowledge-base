# Week 9 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 10. A mix of multiple-choice and short "what does this return?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** You take out a loan and write `=PMT(rate, nper, pv)` with `pv` as a positive number. Why does the result come back negative?

- A) It's a bug — wrap it in `ABS()`.
- B) Money received is positive; money paid out (the payment) is negative, by convention.
- C) `PMT` always returns negative for loans under $500,000.
- D) The rate was entered as a decimal instead of a percentage.

<details>
<summary>Answer</summary>

**B** — Excel/Sheets financial functions use a strict cash-flow-direction convention: money received is positive, money paid out is negative. The negative payment is correct, not a bug.

</details>

---

**Q2.** For a loan with a 6% annual rate paid monthly, which is the correct `rate` argument to `PMT`?

- A) `0.06`
- B) `6`
- C) `0.06/12`
- D) `0.06*12`

<details>
<summary>Answer</summary>

**C** — the rate must match the payment frequency. An annual rate divided by 12 gives the monthly rate needed for monthly payments.

</details>

---

**Q3.** What identity must hold between `IPMT`, `PPMT`, and `PMT` for the same period?

- A) `IPMT × PPMT = PMT`
- B) `IPMT + PPMT = PMT`
- C) `IPMT - PPMT = PMT`
- D) There is no fixed relationship between them.

<details>
<summary>Answer</summary>

**B** — `IPMT + PPMT` always equals `PMT` for the same period; this is the built-in sanity check for any amortization schedule.

</details>

---

**Q4.** Across the life of a fixed-payment amortizing loan, what happens to the interest and principal portions of each payment?

- A) Both stay exactly constant every period.
- B) Interest grows, principal shrinks.
- C) Interest shrinks, principal grows — even though the total payment stays fixed.
- D) Both shrink at the same rate.

<details>
<summary>Answer</summary>

**C** — interest each period is the rate times the *remaining* balance, which shrinks over time; since total payment is fixed, principal must grow to compensate.

</details>

---

**Q5.** In `=NPV(rate, value1, value2, ...) + initialInvestment`, where does the initial investment (happening today, at time 0) belong?

- A) As `value1` inside the `NPV(...)` call.
- B) Added or subtracted separately, outside the `NPV(...)` call.
- C) It should be ignored entirely.
- D) Divided by `rate` before being added.

<details>
<summary>Answer</summary>

**B** — `NPV`'s first argument is assumed to occur at the end of period 1, not today. The time-0 cash flow is added/subtracted separately, at face value (no discounting needed since it's already "today").

</details>

---

**Q6.** Why does `IRR` include the initial investment **inside** its values array, unlike `NPV`?

- A) It's an arbitrary difference with no real reason.
- B) `IRR` solves for the rate using the entire cash-flow timeline including time 0, while `NPV`'s formula structure already assumes `value1` occurs at the end of period 1.
- C) `NPV` cannot accept negative numbers.
- D) `IRR` ignores the first value in the array automatically.

<details>
<summary>Answer</summary>

**B** — `IRR` needs the complete cash-flow timeline, including time 0, to solve for the single rate that zeroes out the whole sequence; `NPV`'s structure already reserves time 0 for the separate add-back.

</details>

---

**Q7.** If a project's `NPV` at your 10% hurdle rate is positive, what do you already know about its `IRR` without calculating it?

- A) IRR must be below 10%.
- B) IRR must be above 10%.
- C) IRR must be exactly 10%.
- D) Nothing — NPV and IRR are unrelated.

<details>
<summary>Answer</summary>

**B** — a positive NPV at a given rate means the project's actual return (its IRR) exceeds that rate; NPV and IRR always agree on direction.

</details>

---

**Q8.** When should you reach for `XNPV`/`XIRR` instead of `NPV`/`IRR`?

- A) Never — they're older, deprecated functions.
- B) Only when all cash flows are exactly evenly spaced.
- C) When cash flows land on real, irregular calendar dates rather than clean, even periods.
- D) Only for loans, never for investments.

<details>
<summary>Answer</summary>

**C** — `XNPV`/`XIRR` discount by the exact number of days between real dates, which matters the moment cash flows aren't evenly spaced; for evenly-spaced annual flows they give nearly the same answer as `NPV`/`IRR`.

</details>

---

**Q9.** In a well-structured financial model, where should a rate or term that might change ever be typed as a literal number inside a formula?

- A) Anywhere it's needed, for speed.
- B) Nowhere — it should live in exactly one labeled input cell that every formula references.
- C) Once per sheet tab.
- D) Only in the first formula that uses it; later formulas can hardcode it.

<details>
<summary>Answer</summary>

**B** — every changeable assumption should live in exactly one labeled input cell, referenced everywhere else, so updating it in one place updates the whole model correctly.

</details>

---

**Q10.** What's the main advantage of `=PMT(AnnualRate/12, TermYears*12, LoanAmount)` over `=PMT(0.06/12, 60, 250000)`?

- A) It calculates faster.
- B) It's self-documenting and updates everywhere automatically if an assumption changes — no functional difference in the math itself.
- C) It uses less memory.
- D) It only works in Excel, not Sheets.

<details>
<summary>Answer</summary>

**B** — the named-range version computes the identical result but communicates its meaning to a reader and updates automatically wherever it's used if the input cell changes; it has no mathematical advantage, only structural/readability ones.

</details>

---

**Q11.** In an Excel two-variable data table, what must occupy the top-left corner cell of the selected range?

- A) A blank cell.
- B) The text label for the table.
- C) A formula reference to the output being swept (e.g., `=Loan!$B$10`).
- D) The first row-input value.

<details>
<summary>Answer</summary>

**C** — the corner cell must hold a formula reference to the output being swept; without it, the Data Table has nothing to recalculate against each row/column combination.

</details>

---

**Q12.** What does Goal Seek actually do to the "By changing cell" once it finishes?

- A) Nothing — it only displays a suggested value.
- B) It overwrites that cell with the value it found.
- C) It creates a new sheet with the result.
- D) It deletes the formula in the "Set cell."

<details>
<summary>Answer</summary>

**B** — Goal Seek writes its found value directly into the "By changing cell," overwriting whatever was there before.

</details>

---

**Q13.** Why can't Goal Seek answer "what rate *or* term should I change to hit this payment target"?

- A) Goal Seek only solves for exactly one changing cell at a time.
- B) Goal Seek doesn't work with `PMT`.
- C) Goal Seek requires the target value to be zero.
- D) Goal Seek can only change cells containing text.

<details>
<summary>Answer</summary>

**A** — Goal Seek is fundamentally a single-input, single-output backward solver; it cannot simultaneously solve for two unknowns.

</details>

---

**Q14.** Google Sheets has no native Scenario Manager. What's the standard workaround this week's lecture teaches?

- A) It's simply not possible in Sheets.
- B) A dropdown (data validation) selecting a scenario name, combined with `INDEX`/`MATCH` "active" rows that feed the rest of the model.
- C) Manually retyping every input each time you want to check a scenario, with no saved record.
- D) Using `IMPORTRANGE` to pull scenarios from a different file.

<details>
<summary>Answer</summary>

**B** — a data-validation dropdown selecting the active scenario name, with `INDEX`/`MATCH` pulling that scenario's stored values into "active" rows the rest of the model references.

</details>

---

**Q15.** A model's "check cell" reads `ROUND(FinalBalance, 2) = 0`. What is this cell actually verifying?

- A) That the loan has been fully paid off — the amortization schedule is internally consistent.
- B) That the interest rate was entered correctly.
- C) That the workbook has no spelling errors.
- D) That the loan amount matches the invoice.

<details>
<summary>Answer</summary>

**A** — it confirms the amortization schedule's math is internally consistent — the loan actually reaches a zero balance by its final period, catching a whole category of reference or argument errors elsewhere in the schedule.

</details>

**Scoring:** 13+ → start Week 10. 10–12 → re-read the lecture sections behind your misses. <10 → re-read all three lectures from the top; this week's concepts compound directly into the mini-project and the rest of the course's modeling weeks.

---
