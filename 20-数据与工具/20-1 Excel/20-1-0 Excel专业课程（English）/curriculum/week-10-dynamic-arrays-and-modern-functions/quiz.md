# Week 10 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 11. A mix of multiple-choice and short "what would happen?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** In a dynamic-array formula that spills into `A1:A5`, which cell holds the actual formula?

- A) All five cells hold identical, independently editable formulas
- B) Only `A1`, the anchor cell — `A2:A5` hold spilled values you can't edit directly
- C) Only `A5`, the last cell
- D) None of them — the formula lives in a hidden system cell

<details>
<summary>Answer</summary>

**B** — only the anchor cell holds the live formula; every other spilled cell shows the same formula grayed out in the formula bar and can't be edited independently.

</details>

---

**Q2.** What does the `#` spill-range operator do, e.g. in `=SUM(A1#)`?

- A) Comments out the rest of the formula
- B) References the entire current spill range anchored at `A1`, however many cells it currently occupies
- C) Forces the formula to recalculate
- D) Converts the array to a single average value

<details>
<summary>Answer</summary>

**B** — `#` means "the whole current spill range from this anchor," and it automatically adjusts if the spill grows or shrinks — unlike a fixed `A1:A5` reference.

</details>

---

**Q3.** `=FILTER(A2:A10, (B2:B10="X")*(C2:C10="Y"))` returns rows where:

- A) Column B is `"X"` OR column C is `"Y"`
- B) Column B is `"X"` AND column C is `"Y"`
- C) Either condition is false
- D) This is invalid syntax — `FILTER` can't combine two conditions

<details>
<summary>Answer</summary>

**B** — multiplying two boolean arrays gives `1` (true) only where both were `TRUE`; that's AND. `+` would be OR.

</details>

---

**Q4.** A `FILTER` formula matches zero rows and has no `if_empty` argument. What happens?

- A) It silently returns a blank cell
- B) It returns `0`
- C) It returns the `#CALC!` error
- D) It returns the `#N/A` error

<details>
<summary>Answer</summary>

**C** — `#CALC!` is the standard "an array function produced an empty result" error; supply an `if_empty` argument to show something friendlier instead.

</details>

---

**Q5.** `=UNIQUE(A2:C10)` (three full columns) returns:

- A) Three separate lists, one per column, each independently de-duplicated
- B) Distinct combinations of the three columns together, treating each row as one unit
- C) Only the values from column A
- D) An error — `UNIQUE` only accepts a single column

<details>
<summary>Answer</summary>

**B** — multi-column `UNIQUE` compares whole rows across all the given columns, returning distinct combinations, not per-column lists.

</details>

---

**Q6.** What's the key difference between `SORT` and `SORTBY`?

- A) They're identical; `SORTBY` is just a newer name
- B) `SORT`'s sort key must be a column inside the array being returned; `SORTBY`'s sort key can be a completely separate array not shown in the output
- C) `SORTBY` only works on text, `SORT` only works on numbers
- D) `SORT` is Excel-only; `SORTBY` is Sheets-only

<details>
<summary>Answer</summary>

**B** — `SORT`'s sort key is an index *into* the returned array; `SORTBY` sorts by a completely independent array, which doesn't have to appear in the output at all.

</details>

---

**Q7.** In `=LET(x, 10, y, x*2, y+1)`, what does this formula return?

- A) `10`
- B) `20`
- C) `21`
- D) An error, because `y` can't reference `x`

<details>
<summary>Answer</summary>

**C** — `x` = 10, `y` = `x*2` = 20 (using the already-defined `x`), final calculation = `y+1` = 21.

</details>

---

**Q8.** Which is a genuine reason to use `LET`, beyond making a formula look nicer?

- A) It's required by Excel for any formula longer than 50 characters
- B) A named sub-expression referenced multiple times is computed once instead of re-derived every time it's used
- C) `LET` formulas run in a completely different calculation engine that's always faster
- D) `LET` is the only way to reference another sheet

<details>
<summary>Answer</summary>

**B** — that's the genuine performance benefit: a named value referenced multiple times is computed once, not re-derived at every reference.

</details>

---

**Q9.** `=SEQUENCE(4, 2)` produces:

- A) A single value, 4×2 = 8
- B) A 4-row, 2-column grid filled 1 through 8, row by row
- C) Four separate unrelated random numbers
- D) An error — `SEQUENCE` only accepts one argument

<details>
<summary>Answer</summary>

**B** — `SEQUENCE(rows, columns)` fills a grid row by row with consecutive integers starting at 1 by default.

</details>

---

**Q10.** Why should a formula never depend on a specific value from `RANDARRAY` staying fixed between two recalculations?

- A) `RANDARRAY` values are locked and never change
- B) `RANDARRAY` regenerates its values on every recalculation, including just reopening the file
- C) `RANDARRAY` can only be used once per workbook
- D) `RANDARRAY` isn't compatible with `LET`

<details>
<summary>Answer</summary>

**B** — `RANDARRAY` is volatile; it recalculates fresh values on every recalculation event, including simply opening the file, so nothing that depends on a specific random value staying put should reference it directly.

</details>

---

**Q11.** To make a `LAMBDA` reusable across a workbook, callable by a plain name like a built-in function, you must:

- A) Save the workbook as a macro-enabled file
- B) Register it with a name (Excel: Define Name / Name Manager; Sheets: Named functions), without the trailing call-parentheses
- C) Nothing extra — every `LAMBDA` is automatically reusable the moment it's typed
- D) Wrap it in a `VBA` module

<details>
<summary>Answer</summary>

**B** — registering a `LAMBDA` under a name (via Name Manager in Excel, Named functions in Sheets) is what turns it from a one-off inline call into a reusable, autocomplete-visible custom function.

</details>

---

**Q12.** Every correct recursive `LAMBDA` must have:

- A) At least three parameters
- B) A base case that stops the recursion, and a recursive case that makes the problem strictly smaller each call
- C) A call to `SEQUENCE` somewhere inside it
- D) No `IF` statement, since `IF` breaks recursion

<details>
<summary>Answer</summary>

**B** — a base case that terminates, and a recursive case that shrinks the problem — miss either and you get infinite (or simply wrong) recursion.

</details>

---

**Q13.** What's the difference between `REDUCE` and `SCAN`?

- A) They're interchangeable
- B) `REDUCE` returns only the final accumulated value; `SCAN` returns every intermediate accumulated value along the way
- C) `REDUCE` works on text only; `SCAN` works on numbers only
- D) `SCAN` is Google Sheets-only; `REDUCE` is Excel-only

<details>
<summary>Answer</summary>

**B** — `REDUCE` collapses to one final value; `SCAN` keeps every intermediate step, which is exactly what you want for a running-total-style column.

</details>

---

**Q14.** `=MAP(A2:A10, LAMBDA(x, x*2))` — what does this do?

- A) Doubles a single cell, `A2`
- B) Applies the doubling calculation to every element of `A2:A10`, spilling one doubled result per input row
- C) Sums `A2:A10` and doubles the total
- D) Errors, because `MAP` requires two arrays minimum

<details>
<summary>Answer</summary>

**B** — `MAP` applies its `LAMBDA` element-by-element across the whole array, spilling a same-shaped result — here, every value in `A2:A10` doubled.

</details>

---

**Q15.** Which statement about Google Sheets vs. Excel dynamic arrays is accurate?

- A) Google Sheets has no equivalent to `FILTER`/`SORT`/`UNIQUE` at all
- B) Excel's `#` spill-range operator has a direct, identically-named equivalent in Google Sheets
- C) Google Sheets' array-returning functions have spilled by default since long before Excel's 2018+ dynamic-array engine; Sheets added `LET` and `LAMBDA` later, in 2022
- D) `LAMBDA` exists in Excel but has never been added to Google Sheets

<details>
<summary>Answer</summary>

**C** — Sheets' array functions have spilled natively for years (predating Excel's 2018 dynamic-array rollout); `LET` and `LAMBDA` arrived in Sheets later, in 2022, with matching syntax to Excel but no `#` spill-range operator.

</details>

**Scoring:** 13+ → start Week 11. 10–12 → re-read the lecture sections behind your misses. <10 → re-read all three lectures from the top; this week's techniques compound directly into Week 11's data-import pipelines and Week 12's automated dashboard.

---
