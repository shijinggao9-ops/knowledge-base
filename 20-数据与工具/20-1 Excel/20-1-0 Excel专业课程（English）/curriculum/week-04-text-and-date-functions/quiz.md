# Week 4 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 5. A mix of multiple-choice and short "what does this return?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** Given `A1` contains `"Hopper, Grace"`, what does `=LEFT(A1, FIND(",", A1) - 1)` return?

- A) `"Hopper,"`
- B) `"Hopper"`
- C) `"Grace"`
- D) An error, because `FIND` can't be used inside `LEFT`

<details>
<summary>Answer</summary>

**B** — `FIND(",", A1)` locates the comma at position 8; `- 1` drops it, leaving everything before it: `"Hopper"`.

</details>

---

**Q2.** What is the key difference between `FIND` and `SEARCH`?

- A) `FIND` is case-insensitive; `SEARCH` is case-sensitive
- B) `SEARCH` is case-insensitive and supports wildcards; `FIND` is case-sensitive and does not
- C) They are identical in every Excel/Sheets version
- D) `FIND` only works on numbers

<details>
<summary>Answer</summary>

**B** — `SEARCH` is case-insensitive and accepts `*`/`?` wildcards; `FIND` is case-sensitive and takes the search text literally.

</details>

---

**Q3.** `=MID("ENG-2019-045", 5, 4)` returns:

- A) `"2019"`
- B) `"ENG-"`
- C) `"019-"`
- D) `"045"`

<details>
<summary>Answer</summary>

**A** — counting from position 5 (`"2"`), grab 4 characters: `"2019"`.

</details>

---

**Q4.** You run `=TEXTSPLIT(A2, ", ")` in cell `B2` only. What happens if `C2` already contains a value?

- A) `TEXTSPLIT` overwrites `C2` silently
- B) The formula returns `#SPILL!` because the spill range is blocked
- C) `TEXTSPLIT` ignores `C2` and only fills `B2`
- D) Excel automatically moves the value in `C2` out of the way

<details>
<summary>Answer</summary>

**B** — `TEXTSPLIT`'s spill range is blocked by existing data in `C2`, producing `#SPILL!` rather than silently overwriting or being ignored.

</details>

---

**Q5.** What does `=TRIM("  Grace  Hopper ")` return?

- A) `"GraceHopper"` (all spaces removed)
- B) `"Grace  Hopper"` (only outer spaces removed)
- C) `"Grace Hopper"` (outer spaces removed, internal double space collapsed to one)
- D) The original string, unchanged

<details>
<summary>Answer</summary>

**C** — `TRIM` removes leading/trailing spaces and collapses internal multi-space runs to a single space, but does not touch genuinely single internal spaces.

</details>

---

**Q6.** Why does the recommended pattern for cleaning a freshly imported text column wrap it as `TRIM(CLEAN(text))` rather than just `TRIM(text)`?

- A) `CLEAN` is required before `TRIM` will run at all
- B) `CLEAN` strips non-printing control characters that `TRIM` (which only handles spaces) does not touch
- C) `TRIM` alone causes a circular reference error
- D) There's no real difference; it's just a stylistic habit

<details>
<summary>Answer</summary>

**B** — `CLEAN` strips non-printing ASCII control characters (like a stray line feed) that `TRIM` was never designed to handle, since `TRIM` only recognizes literal space characters.

</details>

---

**Q7.** `=SUBSTITUTE("2024-01-15-Q1", "-", "/", 1)` returns:

- A) `"2024/01/15/Q1"` (every dash replaced)
- B) `"2024/01-15-Q1"` (only the first dash replaced)
- C) `"2024-01-15-Q1"` (unchanged, because `1` is invalid)
- D) An error

<details>
<summary>Answer</summary>

**B** — the 4th argument, `instance_num = 1`, restricts the replacement to only the first occurrence of the dash.

</details>

---

**Q8.** What specific bug does `TEXTJOIN`'s `ignore_empty = TRUE` argument prevent, that plain `&` concatenation does not?

- A) It prevents numbers from being converted to text
- B) It prevents doubled delimiters/stray delimiters when one of the joined pieces is blank
- C) It prevents the result from exceeding Excel's character limit
- D) It automatically capitalizes the joined result

<details>
<summary>Answer</summary>

**B** — without `ignore_empty`, joining values where one piece is blank still inserts that piece's delimiter, producing a doubled or stray delimiter (e.g., `"Grace, , Hopper"`); `TEXTJOIN` with `TRUE` skips both the blank value and its delimiter.

</details>

---

**Q9.** What is a date, fundamentally, under the hood in Excel or Google Sheets?

- A) A special text data type that formulas parse on the fly
- B) An integer serial number counting days since a fixed epoch, displayed with a date format
- C) A pair of numbers (month, day) stored together
- D) An external reference to the system clock, recalculated every time the file opens

<details>
<summary>Answer</summary>

**B** — every date is an integer serial number (days since a fixed epoch) that's simply *displayed* with date formatting; the underlying value is always numeric.

</details>

---

**Q10.** `B1` contains the real date `2026-08-01`. `A1` contains the real date `2026-07-18`. What does `=B1 - A1` return (assuming the result cell isn't formatted as a date)?

- A) `14`
- B) A `#VALUE!` error, because you can't subtract dates
- C) `"2026-08-01 minus 2026-07-18"` as text
- D) `0`, because both are "dates" and dates can't be compared numerically

<details>
<summary>Answer</summary>

**A** — `14`. Subtracting two real dates subtracts their underlying serial numbers, giving a day count.

</details>

---

**Q11.** Why is `EOMONTH(date, 0)` a better choice than manually checking whether a month has 30 or 31 days?

- A) It isn't better — manual checks are always more reliable
- B) `EOMONTH` correctly handles every month length, including February in leap vs. non-leap years, without any manual logic
- C) `EOMONTH` only works on the current month
- D) `EOMONTH` returns a text string, which is easier to compare

<details>
<summary>Answer</summary>

**B** — `EOMONTH` correctly computes the last day of any month, including handling February's 28-vs-29-day leap year variation automatically, with no manual day-count logic required.

</details>

---

**Q12.** A column of "dates" imported from a CSV is left-aligned instead of right-aligned. What does this most likely indicate, and what function fixes it?

- A) The dates are formatted in a foreign locale; no fix needed
- B) The values are actually text strings that look like dates; `DATEVALUE` converts them to real dates
- C) The column width is too narrow; widening the column fixes it
- D) Nothing is wrong — alignment is arbitrary and carries no meaning

<details>
<summary>Answer</summary>

**B** — left-alignment on a column expected to be dates or numbers is the classic tell that the values are actually text; `DATEVALUE` converts a text date string into a real, usable date serial number.

</details>

---

**Q13.** `=DATEDIF(A1, A2, "YM")` (where `A1` is an earlier date and `A2` is a later date) returns:

- A) The total number of months between the two dates, ignoring years
- B) The total number of days between the two dates
- C) The number of complete years between the two dates
- D) The number of months, 0–11, remaining after subtracting all complete years — i.e., months ignoring years

<details>
<summary>Answer</summary>

**D** — `"YM"` returns the leftover months (0–11) after removing all complete years — months-ignoring-years, not the total month count.

</details>

---

**Q14.** `=WEEKDAY(A1, 2)` returns `6`. What does that tell you about the day `A1` falls on?

- A) It's a Sunday
- B) It's a Saturday
- C) It's a Friday, because `return_type = 2` counts Monday as 1
- D) It's meaningless without knowing the year

<details>
<summary>Answer</summary>

**C** — with `return_type = 2`, Monday = 1 through Sunday = 7, so `6` corresponds to Friday.

</details>

**Scoring:** 12+ → start Week 5. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; text and date cleaning are used constantly in every remaining week.

---
