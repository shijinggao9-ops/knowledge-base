# Week 5 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 6. A mix of multiple-choice and short "what would happen?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** Which of the three rules of "tidy data" is violated by a single cell containing `"Maria Alvarez, CA, Gold"`?

- A) Each variable is a column
- B) Each observation is a row
- C) Each value is atomic
- D) None — this is a valid tidy-data cell

<details>
<summary>Answer</summary>

**C** — three pieces of information (name, state, tier) crammed into one cell violates the "each value is atomic" rule specifically, even though the row/column shape looks fine at a glance.

</details>

---

**Q2.** `"WA"` and `"Washington"` in the same `State` column are an example of:

- A) An exact duplicate
- B) A tidy-data violation of the "atomic value" rule
- C) The same real-world value represented by two different strings — a standardization problem
- D) A type mismatch

<details>
<summary>Answer</summary>

**C** — this is a standardization problem: two different strings representing the exact same real-world value. It's not a duplicate (the *rows* may be otherwise different) and not strictly an "atomic value" violation (each cell holds one value) — it's about the *value itself* being spelled inconsistently.

</details>

---

**Q3.** Why does `COUNTA(A2:G2) = 0` fail to correctly identify a row where every cell contains only a single space character?

- A) `COUNTA` ignores spaces automatically
- B) `COUNTA` counts non-blank cells, and a cell holding a space is technically non-blank
- C) `COUNTA` only works on numeric ranges
- D) It doesn't fail — it works correctly for this case

<details>
<summary>Answer</summary>

**B** — `COUNTA` counts any non-blank cell, and a space character makes a cell non-blank as far as `COUNTA` is concerned, even though it displays as visually empty. The `TRIM`-based check (`SUMPRODUCT(--(TRIM(range)<>""))=0`) is needed to catch this case.

</details>

---

**Q4.** In the Remove Duplicates dialog, checking only the `CustID` column as the match criterion, when every ID in the sheet happens to be unique, will:

- A) Remove all rows
- B) Remove nothing, even if other columns (name, email) have real duplicates
- C) Throw an error
- D) Only remove rows with blank IDs

<details>
<summary>Answer</summary>

**B** — matching only on a column where every value is already unique removes nothing, regardless of real duplication in other columns. The columns you check in the dialog are the *only* ones that count toward the duplicate definition.

</details>

---

**Q5.** Why should you generally run Remove Duplicates **after** standardizing category text and casing, not before?

- A) Remove Duplicates only works on already-sorted data
- B) Standardizing first turns near-duplicates (differing only by casing/whitespace) into exact duplicates, which the tool can then actually catch
- C) It's purely a matter of preference — order doesn't affect the result
- D) Remove Duplicates deletes formatting, so it must run last regardless

<details>
<summary>Answer</summary>

**B** — standardizing casing/whitespace first turns rows that were technically different strings (but the same real value) into byte-for-byte identical rows, which Remove Duplicates' exact-match logic can then correctly catch.

</details>

---

**Q6.** What's the specific difference between what `TRIM` fixes and what `CLEAN` fixes?

- A) They do the exact same thing
- B) `TRIM` removes leading/trailing/extra internal spaces; `CLEAN` strips non-printing control characters that aren't ordinary spaces
- C) `TRIM` only works on numbers; `CLEAN` only works on text
- D) `CLEAN` deletes the entire cell contents

<details>
<summary>Answer</summary>

**B** — `TRIM` handles ordinary spaces (leading, trailing, and collapsing internal runs); `CLEAN` handles non-printing control characters like embedded line breaks, which `TRIM` does not touch.

</details>

---

**Q7.** When using Find & Replace to collapse `"CA"`, `"California"`, and `"ca"` down to one canonical value, which setting is critical to avoid accidentally corrupting unrelated cells?

- A) Match case
- B) Match entire cell contents
- C) Search within formulas
- D) Regular expressions

<details>
<summary>Answer</summary>

**B** — "Match entire cell contents" ensures you're replacing the whole value, not a substring buried inside a longer, unrelated string — critical when replacing a short code like `"CA"` that could otherwise match inside other text.

</details>

---

**Q8.** What is the key limitation of Flash Fill (or Split-to-columns) compared to a formula-based text extraction?

- A) Flash Fill can only handle numbers, not text
- B) Flash Fill produces static, one-time values — the result does not update if the source cell later changes
- C) Flash Fill is Google Sheets-only
- D) Flash Fill cannot handle more than 10 rows at once

<details>
<summary>Answer</summary>

**B** — Flash Fill (and Split-to-columns) produces plain static values as a one-time operation; if the source data changes later, the Flash Fill result does not recompute, unlike a genuine formula.

</details>

---

**Q9.** A "wide" table has one row per customer with three separate columns (`Order1`, `Order2`, `Order3`) holding order amounts. Reshaping this into one row per order, with the customer name repeated, is called:

- A) Filtering
- B) Unpivoting
- C) Deduplicating
- D) Normalizing to Accounting format

<details>
<summary>Answer</summary>

**B** — unpivoting is the specific term for turning data spread across multiple similar columns into one column with more rows, stacking what used to be side-by-side into top-to-bottom.

</details>

---

**Q10.** In Data Validation, choosing **Stop** as the Error Alert style versus **Warning** means:

- A) Stop and Warning behave identically; the label is cosmetic
- B) Stop rejects the entry outright with no way to proceed; Warning lets the user confirm and override
- C) Warning is only available in Google Sheets
- D) Stop only applies to numeric validation, never to List validation

<details>
<summary>Answer</summary>

**B** — Stop is a hard block with no override; Warning shows a confirmation dialog the user can dismiss and proceed anyway, useful for rare legitimate exceptions.

</details>

---

**Q11.** What does the Excel spill reference operator `#` (as in `=Lookups!$H$2#`) mean when used as a Data Validation List source?

- A) It refers to a single fixed cell, `H2` only
- B) It refers to however many cells the formula in `H2` currently spills into — the drop-down list auto-adjusts as that spill grows or shrinks
- C) It's a comment marker and has no functional effect
- D) It forces the validation to ignore blank cells

<details>
<summary>Answer</summary>

**B** — the `#` spill reference means "the full current output of this spilling formula," so the drop-down list automatically tracks however many items the formula currently returns, without needing to be manually re-sized.

</details>

---

**Q12.** After changing a parent drop-down's value (e.g., `Category` from `Apparel` to `Footwear`) in a dependent-drop-down setup, what happens to a dependent cell (`Subcategory`) that already held a value valid only for the *old* parent value?

- A) It automatically clears itself
- B) It automatically updates to a valid value for the new parent
- C) It keeps its old (now stale/invalid) value — validation controls what can be typed next, not what's already there
- D) The whole row is automatically deleted

<details>
<summary>Answer</summary>

**C** — Data Validation only restricts *new* input; it does not retroactively touch a value already sitting in the cell, so a stale dependent value silently persists until either re-typed or caught by a separate conditional-formatting flag.

</details>

---

**Q13.** Which of these is something conditional formatting can catch that Data Validation on the same cell generally cannot?

- A) A value typed manually into the cell one character at a time
- B) A bad value that arrived via a bulk paste, which can bypass live validation rules in many spreadsheet apps
- C) A value that's an exact match to the validation list
- D) Nothing — they catch identical cases

<details>
<summary>Answer</summary>

**B** — a bulk paste operation in most spreadsheet apps can insert values without triggering live Data Validation checks the way manual typing does; conditional formatting evaluates every cell's current value regardless of how it got there, so it catches what validation missed.

</details>

---

**Q14.** In the conditional-formatting rule `=OR($B2="", $C2="")` applied to the range `$A2:$F2`, why does the `$` sit before the column letters (`B`, `C`) but not before the row number (`2`)?

- A) It's a stylistic choice with no functional effect
- B) It locks the column reference so the rule always checks columns B and C specifically no matter which column of the highlighted range is being evaluated, while letting the row number adjust per row
- C) Row numbers can never be locked in conditional formatting
- D) It disables the rule for row 2 specifically

<details>
<summary>Answer</summary>

**B** — locking the column (`$B`, `$C`) but not the row means the rule always checks the specific `B` and `C` columns for every row in the applied range, while the row number adjusts to whichever row is currently being evaluated — exactly the mixed-reference pattern from Week 2.

</details>

---

**Q15.** A `Weight` column mixes `"2.3kg"` and `"900g"` as text. Why can't casing tools like `PROPER` or `UPPER` fix this the way they fix `"gold"` → `"Gold"`?

- A) They can — this is exactly the same kind of problem
- B) Casing functions only change letter case; unit mismatch requires extracting the number, detecting the unit, and mathematically converting — a different category of problem entirely
- C) `PROPER` cannot process any cell containing a number
- D) `UPPER` would delete the numeric portion of the cell

<details>
<summary>Answer</summary>

**B** — casing functions operate purely on letters and never touch the numeric value or perform unit conversion; fixing `"2.3kg"` vs `"900g"` requires extracting the number, identifying the unit, and mathematically converting one to the other — a fundamentally different kind of transformation than a spelling/casing fix.

</details>

**Scoring:** 13+ → start Week 6. 10–12 → re-read the lecture sections behind your misses. <10 → re-read all three lectures from the top; a shaky grip on audit-then-clean will make the mini-project (and every later week's real-data work) noticeably harder.

---
