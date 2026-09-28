# Week 8 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 9. A mix of multiple-choice and short "what would you do here" scenarios — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** What is the core functional difference between a "report" and a "dashboard," as this week defines it?

- A) A dashboard always has more charts than a report
- B) A dashboard is designed for a five-second glance answering one governing question; a report is a fuller collection of correct numbers a viewer sits with
- C) A report is built in Excel; a dashboard is built in Google Sheets
- D) There is no real difference — the terms are interchangeable

<details>
<summary>Answer</summary>

**B** — a dashboard is built for a five-second glance that answers one specific governing question; a report is a fuller, correct collection of numbers a viewer is expected to sit with and explore.

</details>

---

**Q2.** Per this week's visual-hierarchy discussion, where should the single most important number on a dashboard generally be placed?

- A) Bottom-right, since that's where the eye naturally rests last
- B) Centered, so it draws attention from all directions equally
- C) Top-left, largest — first in the Z-pattern scan path and biggest in size
- D) It doesn't matter as long as it's on the screen somewhere

<details>
<summary>Answer</summary>

**C** — top-left, largest. The Z-pattern eye-scan path lands there first, and larger size independently signals "most important" regardless of position.

</details>

---

**Q3.** What does the "single-screen rule" actually require?

- A) The dashboard must be exactly 1920×1080 pixels
- B) The dashboard must be fully visible with no scrolling, at a realistic window size and 100% zoom
- C) The dashboard must contain no more than five total elements
- D) The dashboard must be printed on a single page, regardless of screen behavior

<details>
<summary>Answer</summary>

**B** — full visibility with zero scrolling, at a realistic window size and 100% zoom — not a specific pixel count, element count, or print requirement.

</details>

---

**Q4.** You insert a slicer directly from `PivotByRegion`. You click a button in it, and only `PivotByRegion` updates — the other three pivots don't move. What's the most direct fix?

- A) Delete the slicer and rebuild all four pivots from scratch
- B) Use Report Connections (or PivotTable Connections) on the slicer to check the other three pivots
- C) Insert a second, separate slicer for each of the other three pivots
- D) Convert all four pivots into regular Tables first

<details>
<summary>Answer</summary>

**B** — Report Connections (or PivotTable Connections) is the specific dialog that links one slicer to multiple pivot tables at once; without it, a slicer only affects the pivot it was inserted from.

</details>

---

**Q5.** What can a Timeline filter that a standard slicer cannot?

- A) Text fields with more than 10 unique values
- B) Numeric fields like `UnitPrice`
- C) Date fields, with a draggable range and a Years/Quarters/Months/Days zoom level
- D) Nothing — a Timeline is just a slicer with a different name

<details>
<summary>Answer</summary>

**C** — a Timeline is specifically for date fields, offering a draggable range and a Years/Quarters/Months/Days zoom level that a standard slicer's checkbox-per-value interface doesn't provide.

</details>

---

**Q6.** A slicer built from a pivot on one data source cannot connect, via Report Connections, to a pivot built from a *different* source. Why?

- A) Excel limits every workbook to one slicer total
- B) Report Connections can only link pivots that share the same underlying source data
- C) This is false — any slicer can connect to any pivot in the workbook regardless of source
- D) Only pivot charts, not pivot tables, can be connected this way

<details>
<summary>Answer</summary>

**B** — Report Connections only lists pivots sharing the same underlying source; a pivot built from an unrelated data source simply won't appear as a connectable option.

</details>

---

**Q7.** What does `GETPIVOTDATA` return?

- A) The raw, unfiltered total from the pivot's original source data
- B) The currently displayed (i.e., currently filtered) value from a specified pivot table
- C) A list of every unique value in a pivot field
- D) The pivot table's field settings as text

<details>
<summary>Answer</summary>

**B** — `GETPIVOTDATA` returns the currently displayed (i.e., currently filtered) value from the pivot table it references, which is exactly why it's ideal for filter-aware KPI tiles.

</details>

---

**Q8.** Why does this week's Average Order Value KPI tile formula reference the Total Sales and Total Orders tile cells directly, instead of computing an independent pivot-based average?

- A) It's faster to calculate that way
- B) `GETPIVOTDATA` cannot return averages under any circumstances
- C) It keeps one single source of truth — a filter's effect only has to propagate correctly through one path, not be re-derived independently in multiple places
- D) Google Sheets requires this pattern; Excel does not

<details>
<summary>Answer</summary>

**C** — referencing the other tiles keeps one single source of truth for the filtered data; a filter's effect then only needs to propagate correctly through one calculation path, not be independently re-derived (and potentially get out of sync) in multiple places.

</details>

---

**Q9.** A KPI tile formula is `=[Total Sales]/[Total Orders]` with no error handling. Under what specific condition will this throw `#DIV/0!` on the live dashboard?

- A) Whenever the Region slicer has more than one region selected
- B) Whenever a filter combination results in zero matching orders
- C) Whenever the workbook is reopened after being closed
- D) This formula can never throw an error

<details>
<summary>Answer</summary>

**B** — whenever the active filter combination (region, category, and/or timeline selection together) results in zero matching orders, Total Orders becomes `0` and the division fails.

</details>

---

**Q10.** What is the primary Google Sheets limitation that forces KPI tiles there to be built with `SUMIFS`/`COUNTIFS` instead of the Excel-preferred technique?

- A) Sheets doesn't support pivot tables at all
- B) Sheets has no `GETPIVOTDATA`-equivalent function for reading a pivot's currently displayed value
- C) Sheets formulas can't reference other sheet tabs
- D) Sheets pivot tables can't be filtered interactively

<details>
<summary>Answer</summary>

**B** — Google Sheets has no function equivalent to `GETPIVOTDATA` for reading a pivot table's currently displayed value directly, so KPI tiles there fall back to `SUMIFS`/`COUNTIFS` against the source data instead.

</details>

---

**Q11.** Which sparkline type is described this week as best for a continuous trend over time, such as twelve months of sales?

- A) Win/Loss
- B) Column
- C) Line
- D) Pie

<details>
<summary>Answer</summary>

**C** — Line sparklines best represent a continuous trend over time; Column emphasizes discrete period values, and Win/Loss reduces everything to a binary up/down signal.

</details>

---

**Q12.** In Google Sheets, how is a sparkline created?

- A) `Insert → Sparklines`, identical menu path to Excel
- B) It cannot be done in Google Sheets at all
- C) By typing the `=SPARKLINE()` function directly into a cell
- D) By inserting a full chart and manually resizing it to fit one cell

<details>
<summary>Answer</summary>

**C** — Google Sheets sparklines are created entirely by typing the `=SPARKLINE()` function into a cell — there is no menu-driven insert path like Excel's.

</details>

---

**Q13.** Which conditional-formatting visual type does this week's material identify as **lacking a native equivalent** in Google Sheets (requiring a `SPARKLINE(..., {"charttype","bar"})` formula workaround instead)?

- A) Color scales
- B) Data bars
- C) Bold text formatting
- D) Cell borders

<details>
<summary>Answer</summary>

**B** — Data bars have no native Google Sheets conditional-formatting equivalent; the closest workaround is a `SPARKLINE` formula with `charttype` set to `"bar"`.

</details>

---

**Q14.** Why does the lecture material warn against setting a color scale's thresholds to the automatic min/max of whatever data currently happens to be in the range?

- A) Automatic min/max thresholds are slower to calculate
- B) If the range is always comfortably above target, something will still always show as "red," and the viewer learns to ignore the color signal entirely
- C) Excel doesn't allow automatic thresholds on shared workbooks
- D) Automatic thresholds only work with three colors, never two

<details>
<summary>Answer</summary>

**B** — if thresholds always scale to whatever's currently in the range, something will always land at the "red" end even when every value is actually healthy against a real target, and the viewer stops trusting the color as a meaningful signal.

</details>

---

**Q15.** A dashboard's slicers and timeline are all cleared back to their defaults — the fully unfiltered view. Per this week's polish guidance, how should that default state compare, in quality, to any filtered view a user might select?

- A) It can be rougher, since most viewers will apply a filter immediately anyway
- B) It should be just as polished and complete as any filtered view, since it's the state most viewers see first
- C) It should show placeholder text instead of real numbers until a filter is applied
- D) It doesn't matter, since KPI tiles are hidden until a slicer selection is made

<details>
<summary>Answer</summary>

**B** — the fully-cleared, unfiltered state is what most viewers will see first, so it needs to be exactly as complete and polished as any filtered view a user might click into afterward.

</details>

**Scoring:** 13+ → start Week 9. 10–12 → re-read the lecture sections behind your misses, especially Report Connections and the `GETPIVOTDATA`/`SUMIFS` distinction. <10 → re-read all three lectures from the top; this week's interactivity mechanics are the foundation Week 9's model-building dashboards build on directly.

---
