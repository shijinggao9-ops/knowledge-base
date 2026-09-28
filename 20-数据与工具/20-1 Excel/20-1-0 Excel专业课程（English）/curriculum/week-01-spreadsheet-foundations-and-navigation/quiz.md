# Week 1 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 2. A mix of multiple-choice and short "what would happen?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** In the workbook hierarchy, which is the correct order from largest to smallest?

- A) Sheet → Workbook → Row → Cell
- B) Workbook → Sheet → Row/Column → Cell
- C) Cell → Row → Workbook → Sheet
- D) Workbook → Cell → Sheet → Row

<details>
<summary>Answer</summary>

**B** — Workbook contains Sheets, a Sheet is made of Rows and Columns, and a Cell is their intersection — the smallest unit.

</details>

---

**Q2.** What is the A1-notation address of the cell where column `D` meets row `12`?

- A) `12D`
- B) `D-12`
- C) `D12`
- D) `12,D`

<details>
<summary>Answer</summary>

**C** — column letter first, then row number, no separator: `D12`.

</details>

---

**Q3.** A cell displays `$1,235` but you suspect the true stored value isn't a whole dollar amount. What's true?

- A) That's impossible — the display always matches the stored value exactly.
- B) The number format only changes the display; the stored value could still be `1234.5` or similar.
- C) You'd need to delete and retype the cell to find out.
- D) Currency format always rounds and stores the rounded value.

<details>
<summary>Answer</summary>

**B** — formatting is purely a display layer. `$1,235` could be the rounded *display* of a stored `1234.5` (or any value that rounds to 1235); only checking the formula bar/Name Box reveals the true stored value.

</details>

---

**Q4.** You type `1/4` into a completely fresh, unformatted cell. What is the most likely result?

- A) The fraction one-quarter, displayed as `1/4`
- B) An error
- C) The date January 4th of the current year
- D) The text string `1/4`

<details>
<summary>Answer</summary>

**C** — with no formatting applied, `1/4` is parsed as a date (January 4th) rather than a fraction. To get the fraction, format the cell as Fraction first, or type `0 1/4`.

</details>

---

**Q5.** Underneath its display format, a date is actually stored as:

- A) A text string in `YYYY-MM-DD` form
- B) A serial number counting days from a fixed epoch
- C) Two separate numbers — month and day
- D) A special, non-numeric date object that can't be used in math

<details>
<summary>Answer</summary>

**B** — both Excel and Google Sheets store dates as serial numbers (days since a fixed epoch), which is exactly what makes date math possible.

</details>

---

**Q6.** From a cell sitting inside a contiguous block of data, `Ctrl/Cmd+Down` moves you to:

- A) The very last row of the entire sheet
- B) One cell down, same as the Down arrow key
- C) The last row of the current contiguous block of data (or the start of the next block, if you're currently in a gap)
- D) The first row of the sheet

<details>
<summary>Answer</summary>

**C** — the jump goes to the edge of the current contiguous block in that direction, or leaps to the next block's start if you begin inside a gap. It never simply goes to the sheet's absolute last row unless that happens to be the edge of the block.

</details>

---

**Q7.** What's the fastest way to select "the rest of this column of data" from its first cell, without knowing how many rows it has?

- A) Click and drag until you reach the bottom, guessing when to stop
- B) `Ctrl/Cmd+Shift+Down`
- C) `Ctrl/Cmd+A`
- D) Type every row number manually into the Name Box

<details>
<summary>Answer</summary>

**B** — `Ctrl/Cmd+Shift+Down` selects from the current cell to the end of the contiguous data below it, in one keystroke, regardless of how many rows that turns out to be.

</details>

---

**Q8.** How do you select two separate, non-touching ranges at the same time?

- A) It isn't possible in a spreadsheet
- B) Hold `Ctrl` (Windows) / `Cmd` (Mac) while selecting the second range
- C) Select the first range, then press `Tab`
- D) Select the first range, then press `Delete`

<details>
<summary>Answer</summary>

**B** — holding `Ctrl`/`Cmd` while selecting additional ranges creates a non-adjacent (disjoint) multi-selection.

</details>

---

**Q9.** Freezing panes on row 1:

- A) Locks the values in row 1 so they can never be edited
- B) Keeps row 1 visible on screen while the rest of the sheet scrolls — a purely visual effect
- C) Converts row 1 into a header for a Table
- D) Deletes any data below row 1 permanently

<details>
<summary>Answer</summary>

**B** — freezing is purely visual; it doesn't lock cells against editing (that's a separate feature, sheet protection) and doesn't touch the data.

</details>

---

**Q10.** A cell shows `#####` instead of a number. What does this mean?

- A) The formula in the cell has an error
- B) The column is too narrow to display the formatted value; the underlying value is unaffected
- C) The value was accidentally deleted
- D) The cell's data type is unsupported

<details>
<summary>Answer</summary>

**B** — `#####` is Excel's way of saying "this column is too narrow to show the formatted number" — widen or auto-fit the column and the real value reappears unchanged.

</details>

---

**Q11.** Why should raw/source data generally live on a separate sheet from summaries and calculations?

- A) Spreadsheets require it structurally — you can't calculate on the same sheet as data
- B) It's a convention that keeps the workbook maintainable — one place to trust as the source of truth, with calculations built on top and left untouched by hand
- C) It makes the file size smaller
- D) Excel enforces a maximum of one data type per sheet

<details>
<summary>Answer</summary>

**B** — it's a maintainability convention, not a technical requirement: one trusted source of raw data, with everything else built on top of it via reference rather than retyping.

</details>

---

**Q12.** What's the difference between the Currency and Accounting number formats?

- A) They're identical — just different names
- B) Accounting only works with whole numbers
- C) Currency places the symbol immediately before the digits; Accounting aligns the symbol to the far left and the digits flush right, so a column of amounts lines up on the decimal point
- D) Currency is exclusive to Excel; Accounting is exclusive to Google Sheets

<details>
<summary>Answer</summary>

**C** — Accounting format is specifically designed so a column of dollar amounts aligns cleanly regardless of digit count, by pinning the symbol left and the digits right; Currency keeps the symbol snug against the number.

</details>

---

**Q13.** In a custom number format code, what does the digit placeholder `#` do differently from `0`?

- A) They're interchangeable
- B) `#` always shows a digit, even a padding zero; `0` never shows a digit unless there's a real value
- C) `0` always shows a digit, padding with zero if needed; `#` shows a digit only if one exists, with no padding
- D) `#` is for currency only; `0` is for percentages only

<details>
<summary>Answer</summary>

**C** — `0` is a mandatory digit placeholder (pads with zero); `#` is optional (shows nothing if there's no digit there). `#,##0.00` vs `0.00` behave identically for most values but differ on how leading/trailing zeros are padded.

</details>

---

**Q14.** Why should you generally avoid merging cells in any range you might later sort or reference in a formula?

- A) Merged cells cannot hold any data at all
- B) Merging permanently deletes the values in all but the top-left cell going forward
- C) A merged cell breaks row-by-row logic (like sorting), and "Center Across Selection" achieves the same visual effect without merging
- D) Merged cells are automatically converted to text

<details>
<summary>Answer</summary>

**C** — merging breaks the one-cell-per-row-per-column assumption that sorting and many formulas depend on; "Center Across Selection" gets the same spanning-header *look* while leaving each cell independent underneath.

</details>

---

**Q15.** Does applying a conditional formatting rule (e.g., "highlight if greater than 100") change the cell's stored value?

- A) Yes — it rounds the value to fit the rule
- B) No — it only changes the cell's appearance based on the value; the stored value is untouched
- C) Yes, but only in Google Sheets
- D) It converts the value to a boolean

<details>
<summary>Answer</summary>

**B** — conditional formatting is purely presentational, exactly like manual formatting; the underlying stored value never changes because of a formatting rule, in either app.

</details>

**Scoring:** 13+ → start Week 2. 10–12 → re-read the lecture sections behind your misses. <10 → re-read all three lectures from the top; navigation and formatting habits compound every week from here.

---
