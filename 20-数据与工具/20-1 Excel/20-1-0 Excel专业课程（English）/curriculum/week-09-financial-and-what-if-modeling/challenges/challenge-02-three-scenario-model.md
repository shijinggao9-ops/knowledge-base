# Challenge 2 — Model Best/Base/Worst Scenarios

**Time:** ~75–90 minutes. **Difficulty:** Medium-High.

## The scenario

Crunch's board approved Exercise 2's Project A in principle — but only after seeing more than one number. "What's the NPV if things go well? What if they don't?" is the question every real capital-allocation decision eventually gets asked, and "I only modeled one case" is never an acceptable answer in that meeting. Your job is to turn the single Project A model into three complete, named, defensible scenarios: **Best**, **Base**, and **Worst**.

## Your task

1. **Identify which inputs actually vary by scenario.** Not everything should — a model where every single number changes between scenarios is unfalsifiable (you could justify any outcome). For this challenge, exactly **two** inputs vary: the **annual cash flow** the project generates (demand risk) and the **discount rate** applied (funding-cost risk, since the discount rate should reflect how expensive it would be for Crunch to raise capital under each scenario). The $120,000 initial investment and the 5-year project life stay fixed across all three scenarios — Crunch is committing that capital regardless of which case plays out.

2. **Set the three scenarios' values:**

   | Scenario | Annual Cash Flow | Discount Rate |
   |---|---:|---:|
   | Best | $45,000 | 9.00% |
   | Base | $38,000 | 10.00% |
   | Worst | $30,000 | 12.00% |

   *(Notice the discount rate moves the "wrong" way from what might be your first instinct — Worst uses the **higher** rate. Work out why before you build anything: a worse business environment usually means capital is harder and more expensive to raise, which is exactly what a higher discount rate represents. Write your reasoning in `notes.md`.)*

3. **Build the model** so each scenario produces its own NPV and IRR, using **one of these two approaches:**
   - **Excel:** a real Scenario Manager setup (Lecture 3, Section 5) with three named scenarios, each setting both changing cells, plus a generated **Scenario Summary** report showing NPV and IRR as the result cells for all three side by side.
   - **Google Sheets:** the scenario-switcher pattern (Lecture 3, Section 5) — a dropdown cell, a per-scenario input table, and `INDEX`/`MATCH` "active" rows feeding the NPV/IRR calculation. Manually capture all three scenarios' outputs into a small comparison table (since Sheets can't auto-generate Excel's Summary report) by switching the dropdown to each scenario and recording the result.

4. **Verify your numbers** against the spot-check table below before moving on — a scenario model with a wrong Base case undermines the other two as well.

5. **Write the recommendation.** In `notes.md` (~150 words): given all three outcomes, would you recommend Crunch proceed with the project? Address specifically what the **Worst case** result means for the decision — is a negative-NPV worst case automatically a dealbreaker, or does it depend on how likely that scenario is judged to be? There's no single correct answer here — a defensible argument either way is what's being judged.

## Spot-check values (verify your own scenarios land here)

| Scenario | NPV | IRR |
|---|---:|---:|
| Best | ≈ $55,034 | ≈ 25.4% |
| Base | ≈ $24,050 | ≈ 17.6% |
| Worst | ≈ **-$11,857** | ≈ 7.9% |

Notice the **Worst** case has a **negative** NPV — meaning under those assumptions, Crunch would be better off not doing the project at all. This is exactly the kind of result a single-scenario model would never surface, and exactly why the board asked for three.

## Constraints

- Both changing inputs (cash flow and discount rate) must be swapped **together** as a named unit per scenario — not adjusted independently by hand for each case, which defeats the purpose of naming and saving them.
- Your comparison output must show **all three scenarios' NPV and IRR simultaneously** (or switchable to each in turn, for the Sheets path) — a single number with no comparison isn't a scenario model.
- `notes.md` must state your reasoning for the discount-rate direction (Task 2) and your final recommendation (Task 5) — numbers alone, with no interpretation, are an incomplete submission.

## Hints

<details>
<summary>On why the Worst case uses a higher discount rate</summary>

The discount rate in this kind of model represents the return Crunch could get putting the same money elsewhere, adjusted for risk. A "Worst case" business environment — weak demand, tighter credit, more uncertainty — typically comes with *more expensive* capital, not cheaper. Modeling Worst with the *same* discount rate as Base would understate just how much worse the worst case really is; modeling it with a *lower* rate would be backwards. If this still feels counterintuitive, it's worth re-reading before you build — it's a common point of confusion the first time through.

</details>

<details>
<summary>On the Sheets scenario-switcher comparison table</summary>

Since Sheets has no auto-generated Summary report, build a small three-row table by hand: switch the dropdown to `Best`, read the NPV/IRR output cells, type those two numbers into row 1 of your comparison table; repeat for `Base` and `Worst`. Yes, this means briefly copying a *value*, not a live formula, into the comparison table — that's the correct and expected tradeoff for this workaround, not a mistake.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Mechanics | Inputs changed by hand per scenario, nothing saved/named | Real Scenario Manager (Excel) or dropdown switcher (Sheets), scenarios genuinely swappable |
| Accuracy | NPV/IRR don't match the spot-check table | All three scenarios match within rounding |
| Comparison | Only one scenario's output visible at a time with no record of the others | All three NPV/IRR pairs visible together (summary report or captured table) |
| Reasoning | No explanation for the discount-rate direction or the recommendation | Both explained clearly in `notes.md`, engaging with the Worst case specifically |

## Submission

Commit your model and `notes.md` to your portfolio under `c41-week-09/challenge-02/`.
