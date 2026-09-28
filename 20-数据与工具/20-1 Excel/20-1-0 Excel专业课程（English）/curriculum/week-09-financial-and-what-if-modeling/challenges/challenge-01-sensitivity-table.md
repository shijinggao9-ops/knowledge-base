# Challenge 1 — Build a Two-Variable Sensitivity Table

**Time:** ~60–90 minutes. **Difficulty:** Medium.

## The scenario

Crunch Manufacturing hasn't signed the equipment loan yet. The bank has offered a range of possible rates depending on final credit review (**5.0% to 7.0%**), and Crunch itself hasn't committed to a term (**4 to 7 years**). Before signing anything, the CFO wants to see the monthly payment across **every combination** of rate and term — one screen, one grid, no guessing.

This is exactly the two-variable data table from Lecture 3, Section 3, applied to the loan you've already built.

## Your task

1. **Build the grid** on a new area of your `Loan` tab (or a fresh `Sensitivity` tab):
   - Column headers (across the top): loan terms **4, 5, 6, 7** years.
   - Row headers (down the left): interest rates **5.00%, 5.50%, 6.00%, 6.50%, 7.00%**.
   - The body of the grid: the monthly payment for that row's rate crossed with that column's term.

2. **Excel path:** use a real Data Table (**Data → What-If Analysis → Data Table**) with the `PMT` formula referenced in the grid's top-left corner, **Row input cell** = your term input, **Column input cell** = your rate input, exactly as walked through in Lecture 3, Section 3.

3. **Google Sheets path:** build the manual equivalent — one `PMT` formula in the top-left body cell using correctly mixed references to the row and column headers, then fill it across and down to complete the grid, exactly as walked through in Lecture 3, Section 3.

4. **Verify at least three cells by hand** — pick three (rate, term) combinations from your grid and independently compute `=PMT(rate/12, term*12, 250000)` in a scratch cell elsewhere on the sheet to confirm the grid's value matches. Write down which three you checked.

5. **Highlight the affordability threshold.** Crunch's CFO has said any payment **above $5,500/month** is not viable. Apply conditional formatting (Week 1/8 skill) to highlight every cell in your grid exceeding $5,500 in red. *(Payments are negative numbers — set your conditional formatting rule using the correct comparison direction for negative currency: "less than -5500," not "greater than 5500.")*

6. **Write a one-paragraph recommendation** (in a `notes.md` or a text cell) stating which rate/term combinations stay under the $5,500 threshold, and which single combination you'd recommend Crunch pursue, and why.

## Spot-check values (verify your own grid lands here)

| Rate ↓ / Term → | 4 yrs | 5 yrs | 6 yrs | 7 yrs |
|---|---:|---:|---:|---:|
| 5.00% | -$5,757.32 | -$4,717.81 | -$4,026.23 | -$3,533.48 |
| 6.00% | -$5,871.26 | -$4,833.20 | -$4,143.22 | -$3,652.14 |
| 7.00% | -$5,986.56 | -$4,950.30 | -$4,262.25 | -$3,773.17 |

(5.5% and 6.5% rows are yours to compute and verify — they follow the same pattern between the rows shown above.)

## Constraints

- The grid must be produced by **one formula setup** (a real Data Table in Excel, or one filled formula in Sheets) — not 20 individually typed `PMT` calls. If a grader can't find a single formula (or a single Data Table definition) responsible for the whole grid, the challenge isn't complete regardless of whether the numbers are right.
- Your grid's numbers must exactly match (to the cent) the values a direct `PMT` call would produce for the same rate/term pair — that's what Task 4's spot-check is for.
- Conditional formatting must apply automatically across the whole grid, not be manually colored cell-by-cell.

## Hints

<details>
<summary>On the Excel Data Table "phantom" corner cell</summary>

The top-left cell of a Data Table looks wrong when you first build it — it's a plain formula reference (`=PMT(...)` or a reference to your existing Monthly Payment cell), sitting in a spot that will *display* as a header once the table is built. This is normal and required; a Data Table with no formula reference in that corner produces an error or a blank grid.

</details>

<details>
<summary>On the Sheets mixed-reference pattern</summary>

In the top-left body cell of your grid (say it's `B2`, with rates down column `A` starting at `A2` and terms across row `1` starting at `B1`), the formula should reference the row's rate with the column locked (`$A2`) and the column's term with the row locked (`B$1`): `=PMT($A2/12, B$1*12, 250000)`. Get this one cell right, then fill it across and down — the locks make every other cell in the grid pick up the correct row/column pairing automatically.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Grid mechanics | Grid built from typed-in individual formulas | Grid built from one Data Table (Excel) or one filled mixed-reference formula (Sheets) |
| Accuracy | Values don't match a direct `PMT` spot-check | All spot-checked cells match to the cent |
| Conditional formatting | Manually colored, or comparison direction wrong (misses negative-number cells) | Rule applies automatically and correctly across the whole grid |
| Recommendation | No stated reasoning | Clear one-paragraph justification referencing specific grid values |

## Submission

Commit your `Loan`/`Sensitivity` tab and `notes.md` to your portfolio under `c41-week-09/challenge-01/`.
