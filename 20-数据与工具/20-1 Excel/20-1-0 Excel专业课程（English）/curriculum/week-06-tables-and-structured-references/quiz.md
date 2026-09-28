# Week 6 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 7. A mix of multiple-choice and short "what does this formula return?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** You select a cell inside a plain range and press `Ctrl+T` in Excel. What happens?

- A) Nothing, unless the whole range was pre-selected first
- B) Excel detects the contiguous range automatically and offers to convert it to a Table
- C) It transposes the range
- D) It deletes all formatting in the range

<details>
<summary>Answer</summary>

**B** — Excel detects the contiguous data block around the active cell automatically; you don't need to pre-select the whole range (though doing so also works and lets you confirm the exact boundaries).

</details>

---

**Q2.** A Table's default name in Excel is:

- A) The sheet's name
- B) `Range1`
- C) `Table1` (incrementing for each new Table in the workbook)
- D) Whatever the first cell's value is

<details>
<summary>Answer</summary>

**C** — `Table1`, `Table2`, etc. Always rename it to something meaningful (`Orders`) immediately — every structured reference downstream depends on that name.

</details>

---

**Q3.** You type a new row directly below a Table's last row. Which of these happens **automatically**, with no further action from you?

- A) The Table's border/banding extends to include the new row
- B) A formula in the row above's computed column fills into the new row
- C) The Total Row (if enabled) recalculates to include the new row
- D) All of the above

<details>
<summary>Answer</summary>

**D** — all three happen automatically the instant you type into the row adjacent to the Table's current boundary; that's the entire value proposition of a Table over a plain range.

</details>

---

**Q4.** In the structured reference `[@Qty]`, what does the `@` specifically mean?

- A) "Every row of the `Qty` column"
- B) "The `Qty` value in this same row as the formula"
- C) "An email-style reference to another user"
- D) It's optional decoration with no functional meaning

<details>
<summary>Answer</summary>

**B** — `@` scopes the reference to "this row" — the row the formula itself lives in. Without it, `Table[Column]` means the *whole* column, not one row's value.

</details>

---

**Q5.** `Orders[Total]` written **outside** the Table (e.g., in a `Summary` sheet formula) refers to:

- A) Just the current row's `Total` value
- B) The entire `Total` column's data rows (not the header, not the Total Row)
- C) A syntax error — structured references only work inside the Table
- D) The Table's name only, ignoring the column

<details>
<summary>Answer</summary>

**B** — a bare `Table[Column]` (no `@`) means every data row of that column — equivalent to `Table[#Data]` implicitly, excluding the header and the Total Row.

</details>

---

**Q6.** You insert a new column between two existing columns of a Table. What happens to a `[@Qty]*[@UnitPrice]` formula elsewhere in the Table?

- A) It breaks with `#REF!`
- B) It silently starts referencing the wrong columns
- C) It's unaffected — structured references track columns by name, not position
- D) Excel deletes the formula automatically

<details>
<summary>Answer</summary>

**C** — this is the entire point of Lecture 2: structured references name columns, so their meaning doesn't shift when a column is physically inserted elsewhere in the Table.

</details>

---

**Q7.** What is `Orders[[#Totals],[Total]]`?

- A) A syntax error
- B) The `Total` column's Total Row cell specifically
- C) Every value in the `Total` column, summed inline
- D) The header text `"Total"` as a string

<details>
<summary>Answer</summary>

**B** — the double-bracket form `Table[[#Specifier],[Column]]` combines a special-item specifier with a specific column; here it's "the Total Row's value in the `Total` column" specifically.

</details>

---

**Q8.** `=SUMIFS(Orders[Total], Orders[Region], "East", Orders[Category], "Software")` — the two criteria pairs are combined with:

- A) `OR` — either condition alone is enough
- B) `AND` — both conditions must be true for a row to count
- C) `XOR` — exactly one must be true
- D) It depends on a setting

<details>
<summary>Answer</summary>

**B** — every additional (criteria_range, criteria) pair in `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` is combined with an implicit `AND`. There's no built-in `OR` across pairs.

</details>

---

**Q9.** Why does this course teach `SUMIFS` exclusively, even for a single criterion, instead of the older `SUMIF`?

- A) `SUMIF` no longer exists in modern Excel
- B) `SUMIFS` is faster to calculate
- C) `SUMIFS` puts the sum range first consistently, avoiding the argument-order confusion `SUMIF`'s different order can cause
- D) `SUMIF` doesn't work with Tables at all

<details>
<summary>Answer</summary>

**C** — `SUMIFS(sum_range, range1, crit1, ...)` always puts the range to aggregate first; `SUMIF(range, criteria, [sum_range])` puts it last (and makes it optional, defaulting to `range` itself) — a genuinely common source of transposed-argument mistakes when people mix the two mentally.

</details>

---

**Q10.** `=AVERAGEIFS(Orders[Total], Orders[Rep], "New Rep")` where "New Rep" has zero matching orders returns:

- A) `0`
- B) Blank
- C) `#DIV/0!`
- D) The average of every rep combined

<details>
<summary>Answer</summary>

**C** — `AVERAGEIFS` divides by the count of matching rows; zero matches means division by zero, a real `#DIV/0!` error, not a friendly `0`. Wrap in `IFERROR` if you want `0` instead.

</details>

---

**Q11.** To express "Region is East **or** West" as a single dollar total using `SUMIFS`, the correct approach is:

- A) `SUMIFS(Orders[Total], Orders[Region], "East OR West")`
- B) `SUMIFS(Orders[Total], Orders[Region], "East") + SUMIFS(Orders[Total], Orders[Region], "West")`
- C) `SUMIFS(Orders[Total], Orders[Region], {"East","West"})`
- D) It cannot be done with `SUMIFS` under any circumstances

<details>
<summary>Answer</summary>

**B** — sum two independent, fully-specified `SUMIFS` calls. There's no native `OR` syntax inside one call's criteria list for this family of functions.

</details>

---

**Q12.** In the summary matrix formula `=SUMIFS(Orders[Total], Orders[Region], $A2, Orders[Category], B$1)`, filled across and down a grid, the reference `$A2`:

- A) Locks the row so it never changes while filling down
- B) Locks the column so it stays on column A while filling right, but the row still updates while filling down
- C) Is a full absolute reference, locked in both directions
- D) Is invalid inside a `SUMIFS` criteria argument

<details>
<summary>Answer</summary>

**B** — `$A2` locks the column letter (`A`) so every cell in the filled row keeps pointing at column A, while the row number (`2`) is free to change as you fill down to rows 3, 4, 5. This is a mixed reference, not a full absolute lock.

</details>

---

**Q13.** What is the single biggest practical reason a formula built with structured references survives a mid-Table row insertion, while the equivalent `SUM(D2:D25)`-style formula might not?

- A) Structured references recalculate faster
- B) Structured references are anchored to the Table's logical structure (its named columns and current data extent), not to a snapshot of specific cell addresses
- C) `SUM(D2:D25)` is not a valid formula in a Table
- D) There is no actual difference — both behave identically in every case

<details>
<summary>Answer</summary>

**B** — the mechanism is that structured references resolve against the Table's live logical structure (column names, current data extent) at calculation time, not against a fixed set of cell coordinates captured when the formula was typed.

</details>

---

**Q14.** Google Sheets Tables, compared to Excel Tables, are best described as:

- A) Functionally identical in every respect, including formula syntax
- B) Sharing most visual/behavioral Table features (auto-expansion, styles, filters, a totals row) plus a column-type feature Excel Tables lack, but without Excel's bracket structured-reference formula syntax
- C) A completely unrelated feature with no overlap at all
- D) Only available on paid Google Workspace accounts

<details>
<summary>Answer</summary>

**B** — Sheets Tables match most of Excel Tables' visible/behavioral features and add column-type validation Excel lacks natively, but formulas inside a Sheets Table don't use Excel's `Table[Column]`/`[@Column]` bracket syntax — that's the concrete gap Challenge 2 has you document firsthand.

</details>

**Scoring:** 12+ → start Week 7. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; pivot tables next week assume this is second nature.

---
