# Challenge 2 — Repair a Workbook of Broken References

**Time:** ~60–75 minutes. **Difficulty:** Medium-hard. **Diagnosis first, fix second.**

## The scenario

You've inherited a small workbook from a coworker who left the company. It computes a simple monthly expense summary for a household — rent, utilities, groceries, a savings rate — and it's producing **six different wrong or error results**. Nothing crashed; the sheet opens fine and every cell shows *something*. Your job is to find each of the six bugs, name what kind of bug it is, and fix it — without breaking anything that already works.

## Build the broken workbook yourself

There's no file to download — you're going to **deliberately recreate this exact broken workbook**, bug for bug, so you experience each failure mode with your own hands before fixing it. In a fresh sheet tab `Challenge2`, build this:

```
      A                B
1   Monthly Income   4800
2   Savings Rate     0.15
3
4   Category          Amount
5   Rent              1500
6   Utilities         210
7   Groceries         480
8   Subscriptions     45
9
10  Total Expenses    [formula — see Bug 1]
11  Savings Target    [formula — see Bug 2]
12  Remaining         [formula — see Bug 3]
13  Avg Expense       [formula — see Bug 4]
14  Expense Ratio     [formula — see Bug 5]
15  Category Count    [formula — see Bug 6]
```

Now enter these **exact, intentionally buggy** formulas:

- **`B10` (Bug 1):** `=B5+B6+B7`  *(should total all four expense categories, but stops at Groceries)*
- **`B11` (Bug 2):** `=B1*B2` — then **delete row 2** (select row 2's row header, right-click, Delete Row) right after entering this formula. Watch what `B11` becomes.
- **`B12` (Bug 3):** before deleting row 2, this was meant to be `=B1-B10` (income minus total expenses). Enter it *after* the row-2 deletion, adjusting cell references as the deletion shifted them, but make it read `=B1-B9` on purpose (an off-by-one row reference).
- **`B13` (Bug 4):** `=AVERAGE(B5:B8)` where `B8`'s "Subscriptions" `45` has, in this broken copy, been accidentally typed as the text `"$45"` (with a leading dollar sign typed manually, forcing text). Retype `B8` as literal text `$45` to recreate the bug, then check what `B13` does.
- **`B14` (Bug 5):** meant to compute total expenses as a fraction of income: type `=SUM(B5:B8)/Icome` — a deliberate typo of a named range (`Icome` instead of the intended name). Don't define any named range at all yet — just type the formula with the typo as shown.
- **`B15` (Bug 6):** meant to count how many expense categories there are: `=COUNT(A5:A8)` (note: `A5:A8`, the **label column**, not `B5:B8`, the numbers).

## Your task

For **each** of the six bugs:

1. **Observe the symptom** — what does the cell actually show (a wrong number, or which error value)?
2. **Diagnose** — in one sentence, name the *category* of bug (e.g., "range doesn't cover the full data," "reference shifted after a row was deleted," "off-by-one reference," "value stored as text instead of number," "typo'd/undefined named range," "wrong column referenced").
3. **Fix it** — write the corrected formula and confirm the sheet now produces a sensible result.

Write your six diagnoses and fixes in `challenge-02.md`, one section per bug, in the format:

```
### Bug N — [cell]
**Symptom:** ...
**Diagnosis:** ...
**Fix:** `=...`
```

## Expected results once fully fixed

- `B10` (Total Expenses) → `2235` (`1500+210+480+45`).
- `B11` (Savings Target) — after row 2's deletion, the original `0.15` rate no longer exists as a separate cell; decide how to correctly restore this calculation (re-enter a rate cell, or hardcode `0.15` with a comment explaining the tradeoff — both are defensible, but you must justify your choice in writing).
- `B12` (Remaining) → `Income − Total Expenses` = `4800 − 2235 = 2565` (once pointed at the correct, current total-expenses cell).
- `B13` (Avg Expense) → `558.75` (once `B8` is corrected back to the number `45`, average of the four categories: `2235/4`).
- `B14` (Expense Ratio) → `0.465625` (`2235/4800`) once the named-range typo is resolved.
- `B15` (Category Count) → `4` once pointed at the numeric column instead of the label column *(note: `COUNTA(A5:A8)` on the label column would also correctly return `4` — the deeper lesson of this bug is picking the range that matches the function's intent, not just "any range that happens to return the right number by luck")*.

## Constraints

- Fix each bug with the **smallest correct change** — don't rewrite formulas that already work.
- Every fix must be justified by your diagnosis, not just "I changed it until the number looked right."
- Bug 2 in particular has no single "correct" answer once the rate cell is gone — state your reasoning.

## Hints

<details>
<summary>On Bug 2 (the deleted row)</summary>

Deleting row 2 shifted everything below it up by one row — `B3` became the old `B2`... but the `Savings Rate` value was *in* the deleted row, so it's simply gone, not shifted. A formula that referenced it (`B11`, if it had said `=B1*B2` and you check it *after* the deletion) now likely shows `#REF!` or silently points at whatever now occupies that address. This is exactly the `#REF!` failure mode from Lecture 3, section 7 — the fix isn't mechanical, it's a judgment call about what the formula should reference now that its target is gone.

</details>

<details>
<summary>On Bug 5 (the named-range typo)</summary>

`Icome` was never defined as a name at all in this exercise — so this isn't really a "typo of an existing name," it's a reference to a name that **doesn't exist**, which is exactly what produces `#NAME?`. The fix has two valid forms: define the name correctly (`Income` pointing at `B1`) and fix the spelling in the formula, or abandon the named-range approach here and reference `B1` directly. Either is acceptable if you explain the choice.

</details>

## Stretch

- Once every bug is fixed, add a **seventh** check formula: `=IF(B12<0, "OVER BUDGET", "ON TRACK")` — you haven't formally learned `IF` yet (Week 3), but see if you can get this one working from the pattern shown in Exercise 3's commission formula.
- Rebuild the whole `B1:B2` income/rate block using named ranges from the start, and confirm Bug 2 and Bug 5's failure modes become structurally impossible when named ranges are used consistently rather than raw addresses.

## Submission

Keep the `Challenge2` sheet (fully fixed) and `challenge-02.md` (your six diagnoses) together in your workbook/portfolio for this week.
