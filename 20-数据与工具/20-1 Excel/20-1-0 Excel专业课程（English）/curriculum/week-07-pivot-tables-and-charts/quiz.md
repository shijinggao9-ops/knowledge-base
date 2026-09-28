# Week 7 — Quiz

Fifteen questions. Lectures closed. Aim for 13/15 before starting Week 8. A mix of multiple-choice and short "what would happen?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** Every pivot table answers a question of the shape:

- A) "What is the total of every column?"
- B) "By [dimension], what is [measure]?"
- C) "What formula produces this value?"
- D) "Which row has an error?"

<details>
<summary>Answer</summary>

**B** — every pivot boils down to grouping by a dimension and summarizing a measure: "by X, what is Y?"

</details>

---

**Q2.** Which pivot zone would you use to restrict an entire pivot table to just the "Camping" category, without adding a row or column for it?

- A) Rows
- B) Columns
- C) Values
- D) Filters

<details>
<summary>Answer</summary>

**D** — Filters restricts the whole pivot to chosen values of a field without adding it as a visible row or column.

</details>

---

**Q3.** You put `Category` in Rows with `TotalRevenue` set to Sum, and separately with `OrderID` set to Count. Apparel has the most orders, but Camping has the most revenue. What does this demonstrate?

- A) One of the two pivots must be broken
- B) Sum and Count can legitimately rank the same dimension differently, because they answer different questions
- C) Count always agrees with Sum in a correctly built pivot
- D) Apparel and Camping must have the same number of rows

<details>
<summary>Answer</summary>

**B** — Sum and Count are different aggregations answering different questions ("most revenue" vs. "most orders"); it's expected, not a bug, when they disagree.

</details>

---

**Q4.** Why does a pivot table built on an Excel Table (not a bare range) automatically include newly added rows after a refresh?

- A) It doesn't — you always have to manually change the data source
- B) Tables auto-expand their range as rows are added, and the pivot's source range grows with it
- C) Pivot tables ignore the concept of a range entirely
- D) Only Google Sheets pivots support this behavior

<details>
<summary>Answer</summary>

**B** — a Table's range auto-expands as rows are added; a pivot sourced from a Table's structured reference grows along with it on refresh.

</details>

---

**Q5.** In Excel, after you edit a value in the source data, the open pivot table:

- A) Updates instantly, exactly like a formula would
- B) Does not update until you manually Refresh (or Refresh All)
- C) Deletes itself
- D) Shows an error until the workbook is closed and reopened

<details>
<summary>Answer</summary>

**B** — Excel pivot tables cache a snapshot and require a manual (or triggered) Refresh; they do not update live like a formula.

</details>

---

**Q6.** Grouping `OrderDate` by Month alone (without also grouping by Year) becomes a problem when:

- A) The dataset spans more than one calendar year — January of different years gets merged into a single "Jan" bucket
- B) The dataset has fewer than 12 rows
- C) It never causes a problem
- D) Only when using Google Sheets, not Excel

<details>
<summary>Answer</summary>

**A** — grouping by Month only collapses same-named months across different years into one bucket; you need Month+Year (or Month-Year combined) on multi-year data.

</details>

---

**Q7.** A calculated field `RevenuePerUnit = TotalRevenue/Units`, applied to a group of rows, computes:

- A) The average of each individual row's per-unit price
- B) The group's total revenue divided by the group's total units — the aggregate of aggregates
- C) A random sample of one row's per-unit price
- D) The maximum per-unit price in the group

<details>
<summary>Answer</summary>

**B** — a calculated field computes on the group's aggregated totals (sum of revenue ÷ sum of units), not a row-by-row average.

</details>

---

**Q8.** Which "Show Values As" option would answer "what percentage of March's revenue came through the Wholesale channel, specifically within March"?

- A) % of Grand Total
- B) % of Column Total
- C) % of Row Total
- D) Running Total In

<details>
<summary>Answer</summary>

**C** — % of Row Total computes each cell as a percentage of its own row's total — exactly "within March specifically."

</details>

---

**Q9.** In a "Running Total In" pivot sorted chronologically by month, what should the final period's running-total value always equal?

- A) Zero
- B) The average of all periods
- C) The pivot's grand total
- D) The first period's value

<details>
<summary>Answer</summary>

**C** — a correctly configured running total's last period always equals the pivot's grand total; if it doesn't, something (sort order, missing rows) is wrong.

</details>

---

**Q10.** A bar chart comparing 5 categories is generally preferred over a pie chart with the same 5 slices because:

- A) Pie charts cannot display more than 3 categories at all
- B) Human eyes compare bar length more accurately than pie-slice angle/area, especially for near-equal values
- C) Bar charts always use less screen space
- D) Pie charts require a calculated field and bar charts don't

<details>
<summary>Answer</summary>

**B** — length is easier and more accurate for humans to compare than angle or area, especially when slices/bars are close in value.

</details>

---

**Q11.** Truncating a bar chart's y-axis (starting above zero) is considered misleading mainly because:

- A) It makes the chart render more slowly
- B) Bar length is the visual signal viewers read as value, and a non-zero baseline breaks the length-to-value mapping, exaggerating differences
- C) Excel and Sheets don't allow it, so it must be a bug if you see it
- D) It only affects 3D charts, not 2D ones

<details>
<summary>Answer</summary>

**B** — bar length *is* the value signal in a bar/column chart; a non-zero baseline distorts the visual ratio between bars away from the true numeric ratio.

</details>

---

**Q12.** What is the key difference between a true pivot chart and a regular chart built from a copy-pasted range of a pivot's output?

- A) There is no difference — they behave identically
- B) A pivot chart updates automatically when the pivot's configuration changes; a chart on a copied range does not
- C) Pivot charts cannot be resized
- D) Regular charts are always more accurate

<details>
<summary>Answer</summary>

**B** — a true pivot chart's data source is the live pivot output, so it updates automatically as the pivot's fields/grouping/filters change; a chart on a static copied range does not.

</details>

---

**Q13.** Which of these is **not** one of Lecture 3's recommended readability practices?

- A) Title the chart with the finding, not the field name
- B) Sort categorical bars by value rather than alphabetically, unless there's a natural order
- C) Add a 3D effect so viewers can see the data from multiple angles
- D) Use one consistent color per category across every chart in a report

<details>
<summary>Answer</summary>

**C** — 3D effects distort length/angle perception and carry no additional data; Lecture 3 recommends removing them, not adding them.

</details>

---

**Q14.** You have a $0–6 `Units` field and want to bucket it into ranges of 2 (`1-2`, `3-4`, `5-6`) for a distribution chart. What's this technique called, and which lecture covered it?

- A) Filtering — Lecture 1
- B) Numeric grouping/binning — Lecture 2
- C) Calculated fields — Lecture 2
- D) Show Values As — Lecture 2

<details>
<summary>Answer</summary>

**B** — this is numeric grouping/binning, covered in Lecture 2 alongside date grouping.

</details>

---

**Q15.** A 100% stacked column chart is the best fit for which question?

- A) "What's the exact dollar amount West region made in May?"
- B) "How does the channel mix (as a percentage) differ across four regions?"
- C) "Is there a correlation between order size and discount rate?"
- D) "What's the single largest order in the dataset?"

<details>
<summary>Answer</summary>

**B** — a 100% stacked column chart is built exactly for comparing a percentage-based part-to-whole breakdown across multiple categories/groups at once.

</details>

**Scoring:** 13+ → start Week 8. 10–12 → re-read the lecture sections behind your misses. <10 → re-read all three lectures from the top; pivot configuration and chart choice compound directly into Week 8's dashboard work.

---
