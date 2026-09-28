# Lecture 3 — What-If Analysis: Data Tables, Goal Seek, and Scenario Manager

> **Duration:** ~2 hours. **Outcome:** You can build a one- and two-variable data table to see a formula's result across a whole grid of assumptions at once, run Goal Seek to answer "what input gets me this target?", and use Scenario Manager (or its Google Sheets equivalent) to save and compare named sets of assumptions.

## 1. Three tools, one underlying question

Every tool in this lecture answers some version of "what happens to my output if my input changes?" — but each is shaped for a different version of that question:

| Tool | Question it answers | Inputs it varies | Outputs it shows |
|---|---|---|---|
| **Data table** | "Show me the result across a whole *range* of one or two inputs, all at once." | 1 or 2 | 1 |
| **Goal Seek** | "What single input gets me *this exact* output?" | 1 | 1 (worked backwards) |
| **Scenario Manager** | "Compare a few *named, curated* combinations of several inputs at once." | Any number | 1 or more |

You already built the structure these tools need — Lecture 2's separated inputs and outputs — so every technique below assumes you know exactly which cell is the input and which cell is the output before you start.

## 2. One-variable data table — sweep one input across a range

Crunch wants to see the monthly loan payment at several different interest rates, without retyping `AnnualRate` five times and writing down five separate answers by hand. A one-variable data table does that sweep automatically.

**Excel:**

1. In one column, list the rates you want to test:

```
      A          B
1              =Loan!$B$10   <- the formula cell (Monthly Payment), referenced here
2    5.00%
3    5.50%
4    6.00%
5    6.50%
6    7.00%
```

Row 1 of column B must contain a **reference to the output formula** you're sweeping — not the formula retyped, an actual reference like `=Loan!$B$10`. Column A holds the candidate input values, starting one row *below* that reference cell.

2. Select the whole block `A1:B6` (input values *and* the formula reference in the corner).
3. **Data → What-If Analysis → Data Table.**
4. Leave **Row input cell** blank (nothing varies across a row here); set **Column input cell** to `AnnualRate` (or its cell address, e.g. `Loan!$B$2`) — the cell your column A values should be substituted into.
5. Click **OK**. Excel fills `B2:B6` with the monthly payment recalculated at each rate — a live table that updates automatically if the loan amount or term changes.

**Google Sheets has no built-in Data Table feature.** Build the same sweep manually, using the fact that a formula can reference values you never actually typed into the "real" input cell — instead, reference the row's own value directly in a self-contained formula:

```
      A          B
1    5.00%     =PMT(A1/12, TermYears*12, LoanAmount)
2    5.50%     =PMT(A2/12, TermYears*12, LoanAmount)
3    6.00%     =PMT(A3/12, TermYears*12, LoanAmount)
4    6.50%     =PMT(A4/12, TermYears*12, LoanAmount)
5    7.00%     =PMT(A5/12, TermYears*12, LoanAmount)
```

This isn't literally a "data table" feature, but it produces the identical result: one formula, filled down, each row substituting a different rate. **This is the Sheets-native workaround you'll use for every data-table task this week** — it's slightly more manual to set up, but once built it fills down and updates exactly like Excel's version.

## 3. Two-variable data table — sweep two inputs at once

The real power shows up with **two** varying inputs at once — say, interest rate *and* loan term, to see the payment across every combination of both.

**Excel:**

```
      A        B          C          D          E
1              4 yrs      5 yrs      6 yrs      7 yrs
2    5.00%
3    5.50%
4    6.00%
5    6.50%
6    7.00%
```

Cell `A1` must hold the reference to the output formula (`=Loan!$B$10`), even though it displays oddly in the corner — that's expected. Row 1 (`B1:E1`) holds the term values; column A (`A2:A6`) holds the rate values.

1. Select the entire block `A1:E6`.
2. **Data → What-If Analysis → Data Table.**
3. **Row input cell** = `TermYears` (because the row headers, B1:E1, are terms). **Column input cell** = `AnnualRate` (because the column headers, A2:A6, are rates).
4. **OK.** Every cell in `B2:E6` now shows the payment for that row's rate crossed with that column's term — a 5×4 grid of payments, all from one setup.

**Google Sheets** — build the same grid with one formula per cell, referencing that cell's own row and column headers directly:

```
B2: =PMT($A2/12, B$1*12, LoanAmount)
```

Fill `B2` right through `E2`, then fill the whole row `B2:E2` down through row 6. The `$A2` (column locked, row floats) and `B$1` (row locked, column floats) are the exact mixed-reference pattern from Week 2 — get them right once in `B2` and the fill handles the rest of the grid correctly in every direction.

## 4. Goal Seek — run a formula backwards

A data table answers "what's the output at *each* of these inputs?" Goal Seek answers a narrower, sharper question: "what **one** input value makes the output hit *exactly* this target?"

Crunch wants to know: what interest rate would bring the monthly payment down to exactly **$4,500**?

**Excel:** **Data → What-If Analysis → Goal Seek.**

- **Set cell:** the output formula cell (Monthly Payment, e.g. `Loan!$B$10`).
- **To value:** `4500` *(type the raw number — note `PMT` itself returns a negative value, so if your Monthly Payment cell displays as negative, target `-4500`, not `4500` — match the sign of what's actually in the cell)*.
- **By changing cell:** the input cell to solve for (`AnnualRate`, e.g. `Loan!$B$2`).
- **OK.** Excel iterates internally and lands on the rate — approximately **4.19%** — that produces a $4,500 payment, and writes that value directly into the rate cell.

**Google Sheets:** **Tools → Goal Seek** *(available in current Sheets; older versions may need Extensions → Add-ons)*. Same three inputs — set cell, target value, cell to change — same result, same iterative approach under the hood, just under a different menu path.

**Goal Seek changes the actual input cell.** Unlike a data table (which shows results without touching your live model) or Scenario Manager (which stores named alternatives without committing to one), Goal Seek **overwrites** the cell you pointed it at. Always know that before you click — if you need to keep the original rate around too, copy it somewhere first, or note it in a comment.

**Goal Seek only ever solves for one input.** If your target depends on two things you could change (say, rate *or* term), Goal Seek needs you to fix one and solve for the other — it cannot solve "either the rate or the term" simultaneously. For genuinely multi-input backward-solving, a data table (Section 3) that you scan visually for the target cell is the practical approach; true multi-variable solving needs a dedicated optimizer (Excel's **Solver** add-in — beyond this week's scope, but worth knowing it exists for later, harder problems).

## 5. Scenario Manager — save and compare named assumption sets

A data table sweeps *one or two* inputs across a *range*. Real business questions are often narrower and more curated: "what does this look like in our best case, our expected case, and our worst case?" — a handful of **complete, named combinations** of several inputs at once, not an exhaustive grid.

**Excel:** **Data → What-If Analysis → Scenario Manager.**

1. **Add** a scenario named `Best Case`. **Changing cells:** select every input cell that varies by scenario (e.g., `AnnualRate`, revenue growth rate, unit price — whichever inputs your model treats as scenario-dependent). Enter the optimistic value for each.
2. **Add** again, named `Base Case`, same changing cells, your expected values.
3. **Add** again, named `Worst Case`, same changing cells, your pessimistic values.
4. **Show** any scenario to instantly swap every changing cell to that scenario's values and watch every downstream formula recalculate.
5. **Summary** generates a new sheet comparing all scenarios side by side against whichever output cells you choose to track — the single fastest way to hand a decision-maker a Best/Base/Worst comparison table.

**Google Sheets has no Scenario Manager.** The reliable workaround is a **scenario switcher**: one dropdown cell, driving every scenario-dependent input via `CHOOSE` or `INDEX`.

```
      A                    B          C          D          E
1   Scenario:            Base      <- data-validation dropdown: Best/Base/Worst
2
3   ASSUMPTIONS           Best      Base       Worst
4   Annual Rate          5.00%     6.00%      7.50%
5   Growth Rate         12.00%     7.00%      2.00%
6
7   Active Annual Rate  =INDEX(B4:D4, MATCH($B$1,B3:D3,0))
8   Active Growth Rate  =INDEX(B5:D5, MATCH($B$1,B3:D3,0))
```

- `B1` is a dropdown built with **Data → Data validation** (Week 5 skill), list of items `Best, Base, Worst`.
- Every scenario-dependent input has **one stored row per scenario** (row 4 for rate, row 5 for growth) plus **one "active" row** (rows 7–8) that pulls whichever column matches the current dropdown selection using `INDEX`/`MATCH` (Week 3 skill).
- The rest of the model references the **active** rows (`B7`, `B8`), never the raw per-scenario rows directly — so changing the dropdown at `B1` instantly re-drives the entire model, the same end result as Excel's **Show** button, built from functions you already know instead of a menu feature Sheets doesn't have.

```mermaid
flowchart LR
  A["Dropdown B1\n(Best / Base / Worst)"] --> B["INDEX/MATCH"]
  C["Per-scenario rows\n(one column per case)"] --> B
  B --> D["Active row\n(B7, B8)"]
  D --> E["Rest of the model\nreferences active row only"]
```
*One dropdown drives INDEX/MATCH, which drives an active row, which drives everything downstream.*

This pattern is worth knowing well beyond this week — a dropdown-driven scenario switcher is one of the most useful things you can build into any Google Sheets model, precisely because Sheets has no native Scenario Manager to lean on.

## 6. Choosing the right tool for the question in front of you

| If the question is… | Reach for… |
|---|---|
| "Show me this output across every rate from 4% to 8%." | One-variable data table |
| "Show me this output across every rate *and* every term combination." | Two-variable data table |
| "What rate gets my payment to exactly $4,500?" | Goal Seek |
| "Compare my three planning cases side by side." | Scenario Manager (or the Sheets switcher) |

A data table shows you *everything*, unfiltered — useful for spotting a pattern or a threshold visually. Goal Seek gives you *one precise answer* to a narrow question. Scenario Manager gives you a handful of *curated, complete, named* comparisons rather than an exhaustive sweep. Most real financial models this week — and in the mini-project — use at least two of the three together: a data table to explore, then named scenarios to communicate the two or three cases that actually matter to a decision-maker.

```mermaid
flowchart TD
  A{"What's the question?"} -->|"Show output across many input values"| B["Data table"]
  A -->|"Find the one input for an exact output"| C["Goal Seek"]
  A -->|"Compare a few curated, named cases"| D["Scenario Manager"]
```
*Pick the what-if tool that matches the shape of the question, not the other way around.*

## 7. Check yourself

- What's the difference between what a data table shows you and what Goal Seek gives you?
- In a two-variable data table, which corner cell holds the output formula reference, and why does it look strange sitting there?
- Why does Google Sheets need a manual fill-down formula instead of a "Data Table" menu command?
- What does Goal Seek actually change when it finishes — and why must you know that before running it?
- In a Sheets scenario switcher, what job does the `INDEX`/`MATCH` "active" row do that the raw per-scenario rows can't do on their own?
- Name one situation where a data table is the better tool, and one where Scenario Manager (or its Sheets equivalent) is the better tool.

If those are automatic, you're ready for this week's exercises, challenges, and the mini-project — all three build directly on the loan and investment model from Lectures 1 and 2, now stress-tested with the tools from this lecture.

## Further reading

- **Microsoft — What-If Analysis overview:** <https://support.microsoft.com/en-us/office/introduction-to-what-if-analysis-22bffa5f-e891-4acc-bbd1-4d251458570f>
- **Microsoft — Data Table (calculate multiple results):** <https://support.microsoft.com/en-us/office/calculate-multiple-results-by-using-a-data-table-e95e2487-6ca6-4413-ad12-77542a5ea50b>
- **Microsoft — Goal Seek:** <https://support.microsoft.com/en-us/office/use-goal-seek-to-find-the-result-you-want-by-adjusting-an-input-value-320131d2-f599-4211-8f8f-b95d0b0a6a37>
- **Microsoft — Scenario Manager:** <https://support.microsoft.com/en-us/office/define-and-analyze-a-what-if-scenario-3d61a8b1-fdfe-4c9b-869d-cad2ab13f866>
- **Google — Goal Seek in Sheets:** <https://support.google.com/docs/answer/9088656>
- **Google — Data validation (for building a scenario switcher dropdown):** <https://support.google.com/docs/answer/186103>
