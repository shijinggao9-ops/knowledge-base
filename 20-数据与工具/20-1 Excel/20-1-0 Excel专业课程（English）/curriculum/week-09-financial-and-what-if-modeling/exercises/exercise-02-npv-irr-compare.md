# Exercise 2 — Compare Projects With NPV/IRR

**Goal:** Use `NPV` and `IRR` to evaluate two capital projects Crunch Manufacturing is considering funding with cash freed up by the equipment loan, and recommend one.

**Estimated time:** 90 minutes.

## Setup

On the `Investments` tab, build an assumptions block:

```
      A                     B
1   Discount Rate         10.00%    <- name "DiscountRate"
```

Below it, enter the two projects' cash flows, one per column, year 0 through year 5:

```
      A          B            C
1   Year      Project A    Project B
2     0       -120000      -40000
3     1         38000       14000
4     2         38000       14000
5     3         38000       14000
6     4         38000       14000
7     5         38000       14000
```

*(Project A is the bigger bet — three times the upfront cost of Project B — but also returns more in absolute dollars every year. Neither is obviously better just by eyeballing it: bigger isn't automatically better, and this exercise is exactly about learning to tell the difference between "creates more total value" and "uses capital more efficiently.")*

## Tasks

1. **Project A's NPV.** In a labeled cell, write the `NPV` formula for Project A. Remember Lecture 1, Section 5: year 0's cash flow is **not** inside the `NPV(...)` call. *(`=NPV(DiscountRate, B3:B7) + B2`)*

2. **Project B's NPV.** Same pattern, referencing column C. *(`=NPV(DiscountRate, C3:C7) + C2`)*

3. **Project A's IRR.** Write the `IRR` formula for Project A. This time year 0 **is** inside the range — `IRR` needs the full cash-flow timeline. *(`=IRR(B2:B7)`)*

4. **Project B's IRR.** Same pattern for column C.

5. **Sanity-check the NPV/IRR relationship.** For each project, confirm: if `NPV` is positive at the 10% discount rate, `IRR` is above 10%. If this doesn't hold for either project, you have a sign or range error to find before continuing.

6. **The recommendation.** In a `Recommendation` cell, write a formula that picks the project with the higher NPV: `=IF(NPV_A > NPV_B, "Project A", "Project B")`, referencing your actual NPV cells.

7. **A one-sentence justification.** In a text cell (or a `notes.md` alongside the workbook), state which project you'd recommend and why — NPV tells you the *dollar* value created; IRR tells you the *rate of return*; when they disagree on which project "wins" (which can happen when projects have very different sizes), which one should drive the decision, and why?

## Expected results (spot checks)

- Project A NPV (at 10%) ≈ **$24,050**.
- Project B NPV (at 10%) ≈ **$13,071**.
- Project A IRR ≈ **17.6%**.
- Project B IRR ≈ **22.1%**.
- Note the classic conflict: Project A has the **higher NPV** (more total dollar value, because it's a bigger project committing more capital) but Project B has the **higher IRR** (a better rate of return per dollar invested). Your justification in Task 7 should address this directly, not ignore it.

## Done when…

- [ ] Both NPV formulas correctly exclude year 0 from inside `NPV(...)` and add it back separately.
- [ ] Both IRR formulas correctly include year 0 inside the range.
- [ ] The NPV/IRR sanity check (Task 5) holds for both projects.
- [ ] Your recommendation cell is a formula, not a typed answer.
- [ ] Your written justification directly addresses the NPV-vs-IRR conflict, not just "the numbers are bigger."

## Stretch

- Recompute both projects' NPV at a 15% discount rate instead of 10% (just change `DiscountRate` — everything should ripple). Does the recommendation change? What does that tell you about how sensitive this decision is to the discount rate you assume?
- If Crunch's cash flows actually land on irregular dates rather than clean annual marks, rebuild Project A using `XNPV`/`XIRR` with a real date column (invent five plausible dates that aren't exactly one year apart) and compare the result to the plain `NPV`/`IRR` version.

## Submission

Commit the `Investments` tab (plus `notes.md` if used) to your portfolio under `c41-week-09/exercise-02/`.
