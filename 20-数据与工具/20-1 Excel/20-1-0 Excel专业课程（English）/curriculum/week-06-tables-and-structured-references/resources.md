# Week 6 — Resources

Free, official, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install / access

- **Excel** — 365, 2021, or Excel for the web all support Tables and everything this week teaches: <https://www.microsoft.com/microsoft-365/excel>
- **Google Sheets** — free with any Google account: <https://sheets.google.com>. Tables (**Insert → Tables**) roll out progressively across accounts/domains — if your account doesn't have it yet, Challenge 2's named-range fallback pattern still gets you most of the same behavior.
- **A local copy of this week's data** — recreate the `Orders` seed from the [week README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/README.md); there's no file to download, it's typed/pasted by hand on purpose (Week 5's data-entry discipline, still in effect).

## Required reading (this week's core)

- **Microsoft — Overview of Excel tables:** <https://support.microsoft.com/en-us/office/overview-of-excel-tables-7ab0bb7d-3a9e-4b56-a3c9-6c94334e492c>
  *Why: the official explanation of what a Table actually is and every behavior it changes — the foundation for Lecture 1.*
- **Microsoft — Using structured references with Excel tables:** <https://support.microsoft.com/en-us/office/using-structured-references-with-excel-tables-f5ed2452-2337-4f71-bed3-c8ae6d2b276e>
  *Why: the canonical syntax reference for `[@Column]`, `Table[Column]`, and every special-item specifier — bookmark it, you'll use this syntax for the rest of the course.*
- **Microsoft — SUMIFS function:** <https://support.microsoft.com/en-us/office/sumifs-function-c9e748f5-7ea7-455d-9406-611cebce642b>
  *Why: the full argument reference, including every criteria pattern (`">="`, wildcards, cell references) beyond what Lecture 3 covers.*
- **Google — Use and format tables in Google Sheets:** <https://support.google.com/docs/answer/14471021>
  *Why: the other app's Table feature, straight from the source — read this before Challenge 2.*

## Reference (keep in tabs)

- **Microsoft — COUNTIFS function:** <https://support.microsoft.com/en-us/office/countifs-function-dda3dc6e-f74e-4aee-88bc-aa8c2a866842>
- **Microsoft — AVERAGEIFS function:** <https://support.microsoft.com/en-us/office/averageifs-function-48910c45-1fc0-4389-a028-f7c5c3001690>
- **Microsoft — Total the data in an Excel table:** <https://support.microsoft.com/en-us/office/total-the-data-in-an-excel-table-fa749a3c-ab7d-4e10-a1b0-ac1e4bb9e5b3>
  *Why: every per-column aggregate function the Total Row dropdown offers, explained individually.*
- **Microsoft — Create and format an Excel table:** <https://support.microsoft.com/en-us/office/create-and-format-an-excel-table-e81aa349-b006-4f8a-9806-5af9df0ac664>
  *Why: the full style-gallery and Table Style Options reference (banded rows, first/last column, etc.).*
- **Microsoft — Use slicers to filter data:** <https://support.microsoft.com/en-us/office/use-slicers-to-filter-data-249f966b-a9d5-4b0f-b31a-12651785d29d>
  *Why: for the mini-project's stretch goal — visual, click-to-filter Table controls.*
- **Google — SUMIFS:** <https://support.google.com/docs/answer/9088700>
  *Why: Sheets' own function reference, confirming syntax parity with Excel's version.*

## Practice beyond the seed data

- **ExcelJet — Excel Tables guide:** <https://exceljet.net/excel-tables>
  *Why: a well-regarded independent reference with dozens of extra structured-reference formula examples beyond what this week covers.*
- **ExcelJet — SUMIFS function:** <https://exceljet.net/functions/sumifs-function>
  *Why: more worked examples of multi-criteria aggregation than any single lecture can cover — good for the homework's trickier warm-ups.*

## Deeper background (optional this week)

- **Microsoft — Excel table compatibility issues:** <https://support.microsoft.com/en-us/office/excel-table-compatibility-issues-62d2f11c-52ac-4b64-b7b6-fb1c66d19abb>
  *Why: what happens when a Table-based workbook is opened in an older Excel version — relevant the moment you share a workbook outside your own machine.*
- **Google Workspace Updates blog — Tables in Google Sheets:** <https://workspaceupdates.googleblog.com/> (search "Tables")
  *Why: Sheets' Tables feature is newer and still evolving — this is where Google announces what changed, useful if Challenge 2's observations ever feel out of date.*

## Glossary

| Term | Definition |
|------|------------|
| **Table** | A range converted into a self-describing, auto-expanding structure with a name, styling, and (optionally) a Total Row. |
| **Structured reference** | A formula reference that names a Table and/or column instead of a cell address — `Table[Column]`, `[@Column]`. |
| **`@` (current row)** | The scoping symbol that limits a structured reference to the same row the formula lives in. |
| **Special item specifier** | A bracketed keyword (`#Headers`, `#Data`, `#Totals`, `#All`) addressing a structural part of a Table beyond its plain data. |
| **Total Row** | An optional row pinned to a Table's bottom edge with per-column aggregate functions, always excluded from the Table's own data range. |
| **Auto-expansion** | A Table's automatic growth of its range, formatting, and formulas when a new row or column is typed adjacent to it. |
| **`SUMIFS`** | Sums a range where one or more parallel ranges each match a given criterion — the sum range comes first. |
| **`COUNTIFS`** | Counts rows where one or more ranges each match a given criterion — no sum range at all. |
| **`AVERAGEIFS`** | Averages a range where one or more parallel ranges each match a given criterion — divides by the matching count, not the total row count. |
| **Criteria string** | A `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` argument like `">=3"` or `"*Desk*"` — a comparison or wildcard expressed as text. |
| **Column type (Sheets)** | A Google Sheets Table feature enforcing a data type or dropdown list per column — no direct Excel Table equivalent. |

---

*Broken link? Open an issue or PR.*
