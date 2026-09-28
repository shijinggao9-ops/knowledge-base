# Week 2 — Homework

Five problems, ~4 hours total, spread across the week. These reinforce the lectures with a mix of hands-on formula-writing, a written explanation, and a build-your-own-sheet task. Keep each in its own tab within a `crunch-week2-homework` workbook.

---

## Problem 1 — Twenty formula warm-ups (60 min)

Write and check each formula. Put each in its own cell in a `Warmups` tab, with the formula text also visible (toggle formula view with `Ctrl+`` ``, or add a text label beside each showing what you typed).

1. `=15+3*2` — predict, then check.
2. `=(15+3)*2` — predict, then check.
3. `=48/6/2` — predict, then check (watch left-to-right).
4. `=2^4-5` — predict, then check.
5. A cell `A1=250`; write `=A1*1.07` (a 7% markup) and confirm it equals `267.5`.
6. Build a 5-row list of any numbers in `B1:B5`; write `=SUM(B1:B5)`.
7. Same range: `=AVERAGE(B1:B5)`.
8. Same range: `=MAX(B1:B5)-MIN(B1:B5)` (the spread).
9. Same range: `=COUNT(B1:B5)` after making one cell blank — confirm it drops to 4.
10. `=ROUND(19.995, 2)` — predict the result before checking (careful with the rounding-up edge case).
11. Build `C1=100` and `C2` with a **relative** reference `=C1*2`. Fill `C2` right to `D2`, `E2`. What happened to each, and why?
12. Build `D1=100` (a fixed base) and in `D2` write `=$D$1*2`. Fill right to `E2`, `F2`. Confirm all three show the same result and explain why, unlike #11.
13. Build a small 2-row, 2-column block and write one mixed-reference formula that could fill correctly in both directions (this is a smaller rehearsal of Challenge 1).
14. Name any single cell `MyRate` and write a formula elsewhere that references it by name.
15. Force a `#DIV/0!` error on purpose (`=5/0` or reference a blank cell as a divisor), then wrap it so it displays `0` instead using a guard formula — a plain `IF` is fine even before Week 3's formal lecture on it: `=IF(B1=0, 0, 5/B1)`.
16. Force a `#VALUE!` error on purpose (add a number to a text cell), then explain in a comment cell what caused it.
17. Force a `#NAME?` error on purpose (misspell a function name), then fix it.
18. Reference a cell on a second sheet tab you create, using the `Sheet!Cell` syntax, without clicking to build it — type it by hand.
19. Write a formula combining two functions (nesting): round the average of a range to one decimal place in a single formula.
20. Write one formula using `&` to combine a number and a text label into a single readable sentence, e.g. `="Total: $"&SUM(B1:B5)`.

---

## Problem 2 — Reference type identification (30 min)

In a `RefTypes` tab, for each formula pattern below, write **one word** — `Relative`, `Absolute`, or `Mixed` — and **one sentence** explaining what happens to it when filled diagonally (both down and right):

1. `=A1+B1`
2. `=$A$1+B1`
3. `=$A1+B1`
4. `=A$1+B1`
5. `=SUM($B$2:$B$10)`
6. `=B2*TaxRate` *(a named range — treat it as behaving like which of the three types, and why?)*

---

## Problem 3 — Explain the errors (45 min)

In `errors-writeup.md`, answer in prose (no more than 400 words total):

1. You open a workbook and see `#REF!` in a formula that used to work fine last week. What are the two most likely causes, and how would you distinguish between them?
2. A formula computing "average score" shows `#DIV/0!` for one student but works for the other twenty-nine. What's the most likely explanation, given what you know about how `AVERAGE`-style calculations work?
3. Explain, in your own words, why `#VALUE!` and `#NAME?` are fundamentally different kinds of mistakes — one about *data*, the other about *syntax*. Give one real example of each.
4. Why does `#N/A` (mentioned briefly in Lecture 3) usually mean a formula is working *correctly*, unlike the other four errors?

---

## Problem 4 — Build a tip calculator (60 min)

In a `TipCalc` tab, build a small restaurant bill splitter:

1. Cells for `Bill Amount`, `Tip Percentage` (as a formatted percentage, e.g., `18%`), and `Number of People`.
2. A formula for `Tip Amount` = Bill × Tip Percentage.
3. A formula for `Total With Tip` = Bill + Tip Amount.
4. A formula for `Amount Per Person` = Total With Tip ÷ Number of People, **rounded to 2 decimal places**.
5. Name at least the `Tip Percentage` cell and use the name in your Tip Amount formula.
6. Test: change `Number of People` from 4 to 3 and confirm only `Amount Per Person` changes — everything else stays the same. Change `Tip Percentage` from 18% to 20% and confirm `Tip Amount`, `Total With Tip`, and `Amount Per Person` all ripple correctly.

**Deliver** the working `TipCalc` tab plus one sentence on which cell(s) needed absolute/named references and why.

---

## Problem 5 — Cross-sheet rollup (45 min)

Build three small sheet tabs: `Jan`, `Feb`, `Mar`, each with a single `Total Sales` figure in cell `B1` (any numbers you invent, e.g. `4200`, `3900`, `5100`).

1. On a fourth tab `Q1 Summary`, write three formulas that pull each month's total using `Sheet!Cell` syntax: `=Jan!B1`, `=Feb!B1`, `=Mar!B1`.
2. Write a fourth formula summing those three cells for the quarter total.
3. Write a fifth formula computing the average monthly sales for the quarter.
4. Change `Feb!B1` to a different number and confirm `Q1 Summary` updates automatically without you touching it.

**Deliver** all four tabs plus one sentence on why typing `Jan!B1` by hand is riskier than clicking the `Jan` tab and clicking `B1` while building the formula (think about what's easy to mistype).

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 60 min |
| 2 | 30 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 45 min |
| **Total** | **~4 h** |

After homework, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/quiz.md) and ship the [mini-project](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/mini-project/README.md).
