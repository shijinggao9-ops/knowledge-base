# Week 2 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 3. A mix of multiple-choice and short "what does this formula return?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** What does `=6+2*3` evaluate to?

- A) `24`
- B) `12`
- C) `16`
- D) `21`

<details>
<summary>Answer</summary>

**B** — `12`. Multiplication runs before addition: `2*3=6`, then `6+6=12`.

</details>

---

**Q2.** Which pair of operators share the **same** precedence level and are evaluated **left to right** when tied?

- A) `^` and `*`
- B) `*` and `/`
- C) `+` and `*`
- D) `(` and `)`

<details>
<summary>Answer</summary>

**B** — `*` and `/` are tied and evaluate left to right (as do `+` and `-`, separately).

</details>

---

**Q3.** A range `B2:B6` has 3 numeric cells, 1 blank cell, and 1 cell containing the text `"pending"`. What does `=AVERAGE(B2:B6)` divide the sum by?

- A) `5`
- B) `4`
- C) `3`
- D) It errors, because of the text cell

<details>
<summary>Answer</summary>

**C** — `AVERAGE` divides by the count of **numeric** cells only (3), ignoring the blank and the text cell entirely — it doesn't treat either as zero.

</details>

---

**Q4.** Which function counts a cell containing the text `"N/A"` but a plain `COUNT` would not?

- A) `SUM`
- B) `COUNTA`
- C) `MIN`
- D) `AVERAGE`

<details>
<summary>Answer</summary>

**B** — `COUNTA` counts any non-blank cell, including text like `"N/A"`. Plain `COUNT` only counts numeric cells.

</details>

---

**Q5.** You copy the formula `=B2*C2` from `D2` down to `D5`. What formula does `D5` contain?

- A) `=B2*C2` (unchanged)
- B) `=B5*C5`
- C) `=$B$2*$C$2`
- D) `=B2*C5`

<details>
<summary>Answer</summary>

**B** — `=B5*C5`. Both references are relative, so both shift down by 3 rows when the formula moves from `D2` to `D5`.

</details>

---

**Q6.** A tax rate lives in `F1`. You want every row's tax formula, when filled down, to keep pointing at `F1`. Which reference do you use for the rate in the formula?

- A) `F1`
- B) `$F1`
- C) `F$1`
- D) `$F$1`

<details>
<summary>Answer</summary>

**D** — `$F$1`, fully absolute, so neither the column nor the row shifts no matter where the formula is filled.

</details>

---

**Q7.** What's the difference between `$A1` and `A$1`?

- A) They behave identically
- B) `$A1` locks the row and lets the column float; `A$1` locks the column and lets the row float
- C) `$A1` locks the column and lets the row float; `A$1` locks the row and lets the column float
- D) `$A1` is invalid syntax

<details>
<summary>Answer</summary>

**C** — `$A1` locks the **column** (`A` never changes) and lets the row float; `A$1` locks the **row** (`1` never changes) and lets the column float. The `$` sits immediately before the part it locks.

</details>

---

**Q8.** Starting from a plain reference `B2`, how many times do you press `F4` to reach the fully absolute form `$B$2`?

- A) `0`
- B) `1`
- C) `2`
- D) `4`

<details>
<summary>Answer</summary>

**B** — just **1** press. The `F4` cycle goes `B2` → `$B$2` (press 1) → `B$2` (press 2) → `$B2` (press 3) → `B2` (press 4, back to start). Fully absolute is the very first stop.

</details>

---

**Q9.** A formula `=$A2*B$1` sits in `B2` and is filled to cover the block `B2:D4`. What does the cell `C3` contain after filling?

- A) `=$A2*B$1` (unchanged)
- B) `=$A3*C$1`
- C) `=$A2*C$1`
- D) `=$A3*B$1`

<details>
<summary>Answer</summary>

**B** — `=$A3*C$1`. Filling from `B2` to `C3` moves 1 column right and 1 row down: the column-locked `$A2` advances its row only, becoming `$A3`; the row-locked `B$1` advances its column only, becoming `C$1`.

</details>

---

**Q10.** Which of the following is **not** a valid named-range name?

- A) `TaxRate`
- B) `Tax_Rate`
- C) `B12`
- D) `_rate`

<details>
<summary>Answer</summary>

**C** — `B12` is rejected because it's indistinguishable from an actual cell address. `TaxRate`, `Tax_Rate`, and `_rate` are all valid (start with a letter or underscore, no spaces).

</details>

---

**Q11.** By default, when a formula containing a named range is copied to a new cell, the named-range reference behaves like:

- A) A relative reference — it shifts with the copy
- B) An absolute reference — it stays pointed at the same cell
- C) It becomes invalid and shows `#NAME?`
- D) It only works on the sheet where the name was defined, regardless of scope settings

<details>
<summary>Answer</summary>

**B** — a named range behaves like an absolute reference by default: it keeps pointing at the same cell(s) regardless of where the formula containing it is copied.

</details>

---

**Q12.** You want a formula on a sheet called `Summary` to add cell `B2` from a sheet called `Q1 Data` (note the space in the name). Which is correct?

- A) `=Q1 Data!B2`
- B) `='Q1 Data'!B2`
- C) `=Q1_Data!B2`
- D) `=[Q1 Data]B2`

<details>
<summary>Answer</summary>

**B** — sheet names containing a space must be wrapped in single quotes: `'Q1 Data'!B2`. Option A is invalid syntax; C invents an underscore that isn't the actual sheet name; D uses the wrong bracket syntax (square brackets are for external *workbook* names, not sheet names).

</details>

---

**Q13.** A column that used to be referenced by a formula was deleted entirely. The formula now shows:

- A) `#VALUE!`
- B) `#DIV/0!`
- C) `#REF!`
- D) `#NAME?`

<details>
<summary>Answer</summary>

**C** — `#REF!` means a formula's reference points at a cell, row, or column that no longer exists — exactly what happens when the referenced column is deleted.

</details>

---

**Q14.** A formula shows `#NAME?`. What is the **most likely** cause?

- A) Division by zero somewhere in the formula
- B) A misspelled function name or an undefined/misspelled named range
- C) A cell reference that no longer exists
- D) Text was added to a number

<details>
<summary>Answer</summary>

**B** — `#NAME?` means the formula contains something the engine doesn't recognize as a valid function, name, or syntax element — almost always a typo in a function name or a named range that was never defined (or was deleted/misspelled).

</details>

**Scoring:** 12+ → start Week 3. 9–11 → re-read the lecture sections behind your misses, especially the `F4` cycle and mixed-reference fill behavior. <9 → re-read all three lectures from the top; references are the mechanic every remaining week of this course builds on directly.

---
