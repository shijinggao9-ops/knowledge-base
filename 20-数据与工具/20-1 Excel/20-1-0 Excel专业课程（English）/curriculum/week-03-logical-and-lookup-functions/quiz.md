# Week 3 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 4. A mix of multiple-choice and short "what does this return?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** In `=IF(B2>=70, "Pass", "Fail")`, what happens if `B2` contains the text `"85"` (a number stored as text, from a Week 1-style entry mistake) instead of the number `85`?

- A) It still evaluates normally, returning `"Pass"`.
- B) The comparison may behave unexpectedly, since text and numbers don't always compare the way you'd expect.
- C) The formula throws a `#VALUE!` error immediately, always.
- D) `IF` automatically converts text to numbers, so this is never an issue.

<details>
<summary>Answer</summary>

**B** — comparing text and numbers with `>=` doesn't behave the way you'd expect from pure math; a number stored as text can sort/compare inconsistently depending on the engine and context, which is exactly why Week 1's "value vs. display, and don't let numbers become text" matters here too.

</details>

---

**Q2.** You're nesting `IF` for grade bands (90/80/70/60) and write the tests in this order: `B2>=60`, then `B2>=70`, then `B2>=80`, then `B2>=90`. A student with `95` will get graded as:

- A) `A` — the formula finds the best match regardless of order.
- B) `D` — the first (least restrictive) condition it hits is `TRUE`, so evaluation stops there.
- C) `#N/A` — thresholds must be in ascending order or the formula errors.
- D) It depends on whether you used `IF` or `IFS`.

<details>
<summary>Answer</summary>

**B** — with least-restrictive-first ordering, `B2>=60` is the first condition tested and it's `TRUE` for `95`, so the formula stops there and returns `"D"`, even though `95` also satisfies every stricter test. This is why threshold order matters, covered in Lecture 1 Section 3.

</details>

---

**Q3.** What does `IFS` return if **none** of its listed conditions evaluate to `TRUE`, and there is no `TRUE, ...` catch-all pair?

- A) `0`
- B) An empty string `""`
- C) `#N/A`
- D) It falls through to the last pair regardless of its condition.

<details>
<summary>Answer</summary>

**C** — `#N/A`. Without a catch-all `TRUE, ...` pair, an input matching none of the listed conditions has nothing to return.

</details>

---

**Q4.** For `AND(A, B)` to return `TRUE`:

- A) At least one of `A` or `B` must be `TRUE`.
- B) Both `A` and `B` must be `TRUE`.
- C) Exactly one of `A` or `B` must be `TRUE`.
- D) `A` and `B` must be equal.

<details>
<summary>Answer</summary>

**B** — `AND` requires every argument to be `TRUE`; one `FALSE` argument makes the whole thing `FALSE`.

</details>

---

**Q5.** `=XLOOKUP(A2, B:B, C:C, "Not found")` — what does the fourth argument, `"Not found"`, control?

- A) What's returned if `A2` is blank.
- B) What's returned if the lookup finds no match in column B.
- C) What's returned if column C contains an error.
- D) A default sort order for the result.

<details>
<summary>Answer</summary>

**B** — the fourth argument, `if_not_found`, is what `XLOOKUP` returns specifically when no match is found in the lookup array — it does not affect blank inputs or errors elsewhere.

</details>

---

**Q6.** Which is the single most specific reason `VLOOKUP` breaks when a new column is inserted into the middle of its source table, while `XLOOKUP` typically doesn't?

- A) `VLOOKUP` always searches left to right; `XLOOKUP` searches right to left.
- B) `VLOOKUP`'s return column is a hard-coded position number that doesn't shift with the insert; `XLOOKUP`'s `return_array` is a direct range reference that does.
- C) `VLOOKUP` can't handle more than 5 columns; `XLOOKUP` has no column limit.
- D) They behave identically — inserting a column breaks both equally.

<details>
<summary>Answer</summary>

**B** — `VLOOKUP`'s `col_index_num` is a plain counted number that doesn't know a column was inserted; `XLOOKUP`'s `return_array` is a real range reference that Excel automatically updates when columns shift.

</details>

---

**Q7.** `=XLOOKUP(18, A2:A6, B2:B6, "N/A", -1)` where `A2:A6` holds `0, 5, 10, 25, 50`. What does `match_mode = -1` cause this to return?

- A) `#N/A`, because `18` isn't an exact match anywhere in `A2:A6`.
- B) The value next to `25`, because it's the closest number to `18`.
- C) The value next to `10`, the largest listed number that is still `≤ 18`.
- D) The value next to `0`, the smallest number in the range.

<details>
<summary>Answer</summary>

**C** — `match_mode = -1` means "exact match, or if none, the next **smaller** item." `18` isn't listed; the largest listed value still `≤ 18` is `10`, so the row next to `10` is returned. (Not `25` — that's *larger* than 18, which is what `match_mode = 1` would use instead.)

</details>

---

**Q8.** `MATCH("Priya", A2:A6, 0)` returns `3`. What does that `3` represent?

- A) The value `Priya` is stored as, internally.
- B) The number of characters in `"Priya"`.
- C) The position of `"Priya"` within the range `A2:A6` — she's the 3rd item.
- D) An error code meaning "found, but ambiguous."

<details>
<summary>Answer</summary>

**C** — `MATCH` returns a **position**, not a value. `3` means "3rd item in the range," which is exactly what `INDEX` needs as a coordinate.

</details>

---

**Q9.** You need to look up an `EmployeeID` in column C and return the corresponding `FullName` from column A — column A sits to the **left** of column C. Which built correctly?

- A) `VLOOKUP(id, A:C, 1, FALSE)` — works fine, `VLOOKUP` searches any column you tell it to.
- B) `INDEX(A:A, MATCH(id, C:C, 0))` — works, because `MATCH` searches column C independently and `INDEX` reads from column A using that position.
- C) `HLOOKUP(id, A:C, 1, FALSE)` — the horizontal version fixes the direction problem.
- D) This can't be done with any built-in function; it requires VBA/Apps Script.

<details>
<summary>Answer</summary>

**B** — `INDEX`/`MATCH` doesn't care about column order: `MATCH` searches column C for the position, and `INDEX` independently reads that position from column A. `VLOOKUP` (option A) only ever searches its *first* column, so it cannot search column C while returning from column A within the same `A:C` range. `HLOOKUP` (option C) has the identical first-row-only limitation, just rotated — it doesn't fix the left/right direction problem at all.

</details>

---

**Q10.** What is the practical difference between wrapping a lookup formula in `IFERROR(...)` versus `IFNA(...)`?

- A) There is no difference; they're aliases for the same function.
- B) `IFERROR` catches every error type (including ones caused by real bugs elsewhere in the formula); `IFNA` catches only the "not found" (`#N/A`) case and lets other errors surface.
- C) `IFNA` is Google Sheets-only; `IFERROR` is Excel-only.
- D) `IFERROR` only works on lookup functions; `IFNA` works on any formula.

<details>
<summary>Answer</summary>

**B** — `IFERROR` is a blunt catch-all for any error type; `IFNA` catches only `#N/A` specifically, letting other error types (which usually indicate a real bug, like `#REF!` or `#VALUE!`) surface instead of being silently hidden.

</details>

---

**Q11.** A two-way lookup needs both a row position and a column position. Which combination correctly builds one?

- A) `INDEX(range, MATCH(row_val, row_labels, 0), MATCH(col_val, col_labels, 0))`
- B) `MATCH(range, INDEX(row_val, col_val))`
- C) `XLOOKUP(row_val, col_val, range)`
- D) `INDEX(row_val, col_val, range)`

<details>
<summary>Answer</summary>

**A** — `INDEX` takes the range plus two positions, each supplied by its own `MATCH` call against the row labels and column labels respectively.

</details>

---

**Q12.** In Excel, which versions have `XLOOKUP` available out of the box?

- A) Every version ever released, back to Excel 97.
- B) Only Excel for the web, never desktop Excel.
- C) Excel 365 and Excel 2021+; Excel 2019 and earlier do not have it.
- D) Only if a paid add-in is installed.

<details>
<summary>Answer</summary>

**C** — `XLOOKUP` requires Excel 365 or Excel 2021+. Perpetual-license Excel 2019 and earlier don't have it; `INDEX`/`MATCH` is the fallback there.

</details>

---

**Q13.** `=IF(NOT(AND(B2>=60, C2>=0.75)), "At Risk", "On Track")` — a student has `B2 = 55` and `C2 = 0.9`. What does this return?

- A) `"On Track"`, because attendance alone is high enough.
- B) `"At Risk"`, because the inner `AND` is `FALSE` (score fails), so `NOT` flips it to `TRUE`.
- C) `#VALUE!`, because `NOT` can't wrap `AND`.
- D) It depends on which comes first in the `AND`, `B2` or `C2`.

<details>
<summary>Answer</summary>

**B** — `AND(55>=60, 0.9>=0.75)` = `AND(FALSE, TRUE)` = `FALSE`. `NOT(FALSE)` = `TRUE`, so the `IF` returns its `value_if_true`, `"At Risk"` — correctly flagging the low score even though attendance alone looks fine.

</details>

---

**Q14.** Why does this course recommend supplying `if_not_found` (or wrapping in `IFERROR`/`IFNA`) on essentially every lookup formula that touches human-entered data, rather than only where you expect it to fail?

- A) It's required syntax — `XLOOKUP` won't run without it.
- B) It makes the formula calculate faster.
- C) Typos and missing entries in real data are a certainty, not an edge case, once a human is typing the lookup value — an unhandled `#N/A` reaching a downstream `SUM` or chart silently corrupts the result.
- D) It's only a stylistic preference with no functional benefit.

<details>
<summary>Answer</summary>

**C** — a typo'd SKU or misspelled name in a lookup is a normal, expected occurrence with real human-entered data, not a rare edge case — an unhandled `#N/A` will silently break any `SUM`, chart, or further formula that touches it downstream, so defaulting to defensive lookups is the professional habit, not paranoia.

</details>

**Scoring:** 12+ → start Week 4. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; branching and lookups compound directly into everything from Week 4 onward.

---
