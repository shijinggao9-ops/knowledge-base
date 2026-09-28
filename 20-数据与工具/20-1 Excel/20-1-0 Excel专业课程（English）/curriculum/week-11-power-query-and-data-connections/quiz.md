# Week 11 — Quiz

Fourteen questions. Lectures closed. Aim for 12/14 before starting Week 12. A mix of multiple-choice and short "what would happen?" — the answer key at the bottom explains the *why*, not just the letter.

---

**Q1.** In the initial Power Query import dialog, what's the practical difference between clicking **Load** and clicking **Transform Data**?

- A) They do the same thing; the labels are cosmetic
- B) **Load** dumps the data onto a sheet as-is with no editor opened; **Transform Data** opens the Power Query Editor first, before anything is written to a sheet
- C) **Load** only works for CSV files; **Transform Data** only works for Excel files
- D) **Transform Data** deletes the source file after import

<details>
<summary>Answer</summary>

**B** — Load skips the editor and writes the data straight to a sheet as-is; Transform Data opens the full Power Query Editor first, letting you build steps before anything lands on a sheet.

</details>

---

**Q2.** What does clicking a step three rows up in the Applied Steps pane do to the data preview?

- A) Nothing — Applied Steps are for display only, not interactive
- B) It shows the data exactly as it looked immediately after that earlier step ran, letting you inspect the pipeline's state at that point
- C) It permanently deletes every step after the one clicked
- D) It re-runs the entire query from scratch against a fresh copy of the source

<details>
<summary>Answer</summary>

**B** — clicking an earlier step shows the preview exactly as it looked right after that step executed, which is the core debugging technique for finding which step introduced a problem.

</details>

---

**Q3.** `Orders_Raw_Export.csv` has three metadata lines above its real header row. Why must `Remove Top Rows` run *before* `Use First Row as Headers`?

- A) It doesn't matter — Power Query auto-detects the real header regardless of order
- B) `Use First Row as Headers` promotes whatever the *current* top row is; if the metadata rows aren't removed first, one of them gets promoted as the header instead of the real header
- C) `Remove Top Rows` requires headers to already be promoted before it can run
- D) Metadata rows automatically convert to comments and are ignored by both steps

<details>
<summary>Answer</summary>

**B** — `Use First Row as Headers` always promotes whatever row is *currently* on top; if metadata rows are still there, one of them (not the real header) gets promoted, and the real header row ends up as a normal data row instead.

</details>

---

**Q4.** A `Qty` column auto-detects as `Text` after import, even though every value looks numeric at a glance. What's the most likely cause?

- A) Power Query cannot detect numeric columns automatically, ever
- B) At least one cell in that column contains a value that isn't parseable as a plain number (a unit suffix like `"8 units"`, for example), so Power Query conservatively leaves the whole column as text
- C) The column header itself must be renamed before numbers can be detected
- D) Text-typed columns are the default for every column regardless of content

<details>
<summary>Answer</summary>

**B** — Power Query conservatively types a whole column as `Text` if even one value in it fails to parse as the more specific type, which is exactly what a stray unit suffix like `"8 units"` causes.

</details>

---

**Q5.** What's the specific difference between `Remove Blank Rows` and `Remove Errors`?

- A) They're two names for the exact same operation
- B) `Remove Blank Rows` deletes rows that are entirely empty across every column; `Remove Errors` deletes rows where a step (often a type conversion) produced an actual `Error` value in some cell
- C) `Remove Errors` only applies to numeric columns
- D) `Remove Blank Rows` requires manual row-by-row selection; `Remove Errors` is fully automatic

<details>
<summary>Answer</summary>

**B** — `Remove Blank Rows` targets rows with nothing in any column; `Remove Errors` targets rows where a specific cell holds an actual computed `Error` value, typically from a failed type conversion — different problems, different fixes.

</details>

---

**Q6.** `Unpivot Other Columns` is generally preferred over manually selecting the wide columns (e.g., `Jan`, `Feb`, `Mar`) to unpivot directly. Why?

- A) `Unpivot Other Columns` runs faster on large datasets
- B) It unpivots whatever isn't in the selected "keep" column(s), so if a new wide column (e.g., `Apr`) is added to the source later, it gets unpivoted automatically on refresh with zero step edits — the manual-selection variant would silently leave it out
- C) There is no functional difference; it's purely a naming preference
- D) `Unpivot Other Columns` is the only variant available in Google Sheets

<details>
<summary>Answer</summary>

**B** — because it unpivots "everything not explicitly kept," a new wide column added to the source later gets swept into the unpivot automatically on the next refresh, with no step edit required; manually selecting the wide columns by name would silently exclude any new one.

</details>

---

**Q7.** What does `Group By` compute, and which earlier-course Excel feature does it most closely resemble?

- A) It removes duplicate rows; resembles Remove Duplicates
- B) It collapses many rows into one row per distinct value of a chosen column, computing an aggregate per group; resembles pivot tables / `SUMIFS`-`COUNTIFS`-`AVERAGEIFS`
- C) It sorts rows alphabetically; resembles the Sort & Filter ribbon group
- D) It splits one column into several; resembles Split Column

<details>
<summary>Answer</summary>

**B** — Group By collapses rows into one-per-group aggregates, the same conceptual job Week 6's `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` and Week 7's pivot tables perform, just expressed as a query step instead of a formula or drag-and-drop field.

</details>

---

**Q8.** Give the one-sentence rule for choosing **Merge** vs. **Append** for a new two-source combination task.

- A) Always use Merge; Append is deprecated
- B) If the task needs more **columns** describing the same rows, use Merge (a join); if it needs more **rows** of the same columns, use Append (a stack)
- C) Merge is for Excel sources; Append is for CSV sources only
- D) They're interchangeable — either always produces the same result

<details>
<summary>Answer</summary>

**B** — more columns describing the same rows means Merge (a join); more rows of the same columns means Append (a stack). This is the single question to ask when unsure which operation a task needs.

</details>

---

**Q9.** In a Power Query Merge with **Left Outer** join kind, what happens to a row from the top table whose key has no match in the bottom table?

- A) The entire row is dropped from the result
- B) The row is kept, with the new columns from the bottom table left blank for that row
- C) The query throws a hard error and refuses to load
- D) The row is duplicated once for every row in the bottom table

<details>
<summary>Answer</summary>

**B** — Left Outer keeps every row from the top table regardless of match; unmatched rows simply get blank values in the new columns, mirroring how `XLOOKUP` returns nothing rather than deleting the row when nothing matches.

</details>

---

**Q10.** What does a **Left Anti** join specifically isolate, and why is that useful?

- A) Every row that matched in both tables — useful for confirming complete overlap
- B) Only rows from the top table that had **no** match in the bottom table — useful for finding orphaned records, like an order referencing a `SKU` the lookup table doesn't have
- C) Only rows from the bottom table — useful for auditing the lookup table alone
- D) Nothing — Left Anti and Left Outer always return identical results

<details>
<summary>Answer</summary>

**B** — Left Anti keeps only unmatched top-table rows, which directly surfaces orphaned references (e.g., an order pointing at a `SKU` missing from the Products lookup) — a genuinely useful data-quality check, not just an academic join variant.

</details>

---

**Q11.** `South_Week1.csv` has its columns in a different physical order than `North_Week1.csv` and `West_Week1.csv`. Why did Append Queries combine all three correctly anyway?

- A) Append Queries ignores column order entirely and matches columns by **name**, not position
- B) Power Query automatically reorders every source file to match before appending
- C) It didn't — the South data landed in the wrong columns and had to be fixed manually
- D) Append Queries only works when all sources have identical column order; this scenario would fail

<details>
<summary>Answer</summary>

**A** — both Merge and Append match by column **name**, not physical position, which is exactly why South's differently-ordered columns combined correctly without any manual realignment.

</details>

---

**Q12.** What specifically happens, internally, when a `From Folder` combine query encounters a new file added to the folder after the query was originally built?

- A) Nothing — new files are ignored until the query is manually rebuilt
- B) Power Query re-applies the same transform-step function (originally built from a sample file) to the new file automatically, appending its result into the combined output on the next refresh
- C) The query throws an error and must be deleted and recreated
- D) Only files present at the moment the query was first created can ever be included

<details>
<summary>Answer</summary>

**B** — `From Folder` builds its transform steps once, from a sample file, then wraps them as a reusable function applied to every file currently in the folder — including files added after the query was first built, the next time it's refreshed.

</details>

---

**Q13.** Why should an intermediate query (like a standalone `Products` lookup query feeding a later merge) generally be loaded as **Only Create Connection** rather than **Table**?

- A) Connection-only queries run transforms faster than Table-loaded queries
- B) Loading every intermediate query to its own sheet clutters the workbook and slows `Refresh All` with no benefit; only the final, consumer-ready output needs a visible Table
- C) Excel enforces a hard limit of one loaded Table per workbook
- D) Connection-only queries cannot be used as a Merge or Append source, so they must stay unloaded

<details>
<summary>Answer</summary>

**B** — every extra loaded Table adds visible clutter and refresh overhead with no benefit if nothing downstream needs to see it directly on a sheet; reserving Table-loading for the final output keeps the workbook clean and Refresh All fast.

</details>

---

**Q14.** Which of the following is something Power Query's Applied Steps pane provides that a single Google Sheets `IMPORTHTML` formula cannot?

- A) The ability to pull data from a web page at all
- B) A reorderable, individually-inspectable, renameable sequence of named transform steps that can be debugged one step at a time
- C) The ability to refresh on demand
- D) The ability to handle more than one table on a page

<details>
<summary>Answer</summary>

**B** — Power Query's Applied Steps pane is a genuinely different kind of tool: a saved, ordered, individually-clickable and renameable sequence of operations you can step through and debug one at a time, which a single atomic `IMPORTHTML` formula simply doesn't provide, even though both can pull web-page data and both can be set to refresh.

</details>

**Scoring:** 12+ → start Week 12. 9–11 → re-read the lecture sections behind your misses. <9 → re-read all three lectures from the top; the merge/append distinction and the dependency-chain refresh behavior are the two ideas the mini-project (and every later automated workbook you build) depend on most heavily.

---
