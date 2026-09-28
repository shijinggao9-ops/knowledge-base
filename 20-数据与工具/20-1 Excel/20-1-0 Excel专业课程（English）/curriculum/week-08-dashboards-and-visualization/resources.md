# Week 8 — Resources

Free, official, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Tools (you already have these)

- **Excel** (365, 2021, or Excel for the web) — <https://www.microsoft.com/microsoft-365/excel>
- **Google Sheets** — <https://sheets.google.com> (free with any Google account)

Nothing new to install this week — slicers, timelines, sparklines, and conditional formatting are all built into the same apps you've been using since Week 1.

## Required reading (this week's core)

- **Microsoft — Overview of PivotTables and PivotCharts:** <https://support.microsoft.com/en-us/office/overview-of-pivottables-and-pivotcharts-527c8fa3-02c0-445a-a2db-7794676bce96>
  *Why: this week's dashboard is built entirely on top of the pivots this page covers — a quick refresh before wiring slicers to them.*
- **Microsoft — Use slicers to filter data:** <https://support.microsoft.com/en-us/office/use-slicers-to-filter-data-249f966b-a9d5-4b0f-b31a-12651785d29d>
  *Why: the canonical, official walkthrough of inserting, formatting, and connecting slicers — the source of truth behind Lecture 2, Sections 2-3.*
- **Microsoft — Create a PivotTable timeline to filter dates:** <https://support.microsoft.com/en-us/office/create-a-pivottable-timeline-to-filter-dates-d3956083-01be-408c-906d-6fc99d9fadfa>
  *Why: the full Timeline reference — inserting, zoom levels, multi-pivot connections — behind Lecture 2, Section 4.*
- **Microsoft — GETPIVOTDATA function:** <https://support.microsoft.com/en-us/office/getpivotdata-function-8c083b99-a922-4ca0-af5e-3af55960761f>
  *Why: full syntax and argument reference for the function every Excel KPI tile in this week's mini-project depends on.*
- **Microsoft — Use sparklines to show data trends:** <https://support.microsoft.com/en-us/excel/get-started/use-sparklines-to-show-data-trends>
  *Why: the official reference for Line/Column/Win-Loss sparklines, high/low-point marking, and axis scaling from Lecture 3, Section 2.*
- **Google — Filter charts and tables with Slicers:** <https://support.google.com/docs/answer/9245556>
  *Why: the Sheets-side slicer reference — read this alongside Lecture 2, Section 8 to see exactly where it diverges from Excel's model.*
- **Google — SPARKLINE function:** <https://support.google.com/docs/answer/3093289>
  *Why: full syntax for the options object (`charttype`, `color`, `highcolor`, `lowcolor`, and more) used throughout Lecture 3 and this week's mini-project.*

## Reference (keep in tabs)

- **Microsoft — Use data bars, color scales, and icon sets to highlight data:** <https://support.microsoft.com/en-us/excel/use-data-bars-color-scales-and-icon-sets-to-highlight-data>
- **Google — Use conditional formatting rules in Google Sheets:** <https://support.google.com/docs/answer/78413>
- **Google — Create & use pivot tables (Sheets Help):** <https://support.google.com/docs/answer/1272900>
- **Microsoft — INDEX function** (used in this week's Top Region KPI tile): <https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd>
- **Microsoft — MATCH function** (used alongside `INDEX` in the same KPI tile): <https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a>
- **Microsoft — IFERROR function** (used to guard the Average Order Value tile against `#DIV/0!`): <https://support.microsoft.com/en-us/office/iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611>

## Practice beyond this week's exercises

- **Microsoft — Excel help & learning hub** (search "dashboard," "slicer," or "sparkline" for current walkthroughs and video tutorials): <https://support.microsoft.com/en-us/excel>
- **GCFGlobal — Excel: Charts tutorial** (a slower, screenshot-heavy second pass on chart fundamentals, useful before this week's chart-hierarchy work if any of it felt shaky): <https://edu.gcfglobal.org/en/excel/charts/1/>

## Glossary

| Term | Definition |
|------|------------|
| **Dashboard** | A single-screen, designed visual summary built to answer one governing question at a glance, as opposed to a fuller report meant to be explored. |
| **Visual hierarchy** | The deliberate use of size, position, and color to signal which element on a screen matters most, second-most, and so on. |
| **Single-screen rule** | The constraint that a dashboard must be fully visible with no scrolling at a realistic window size and zoom level. |
| **KPI (Key Performance Indicator)** | One of a small number (typically 3-5) of actionable, decision-relevant numbers chosen to headline a dashboard. |
| **Slicer** | A clickable button panel that filters one or more connected pivot tables (or Tables) by a chosen field's values. |
| **Timeline** | A date-specific filtering control offering a draggable range and a Years/Quarters/Months/Days zoom level, applicable only to date fields. |
| **Report Connections** (Excel) / **PivotTable Connections** | The dialog that links a single slicer or timeline to multiple pivot tables at once, so one click filters all of them simultaneously. |
| **`GETPIVOTDATA`** | An Excel function that reads the currently displayed (filtered) value from a specified pivot table — the backbone of filter-aware KPI tiles in Excel. |
| **Dynamic title** | A title built from a formula (typically string concatenation with `&`) that changes its displayed text based on the current filter state. |
| **Sparkline** | A miniature chart contained entirely within a single cell, showing a trend without any axis, legend, or chart frame. |
| **Data bars** | A conditional-formatting type that draws a horizontal bar inside a cell, proportional to its value relative to the range. |
| **Color scale** | A conditional-formatting type that shades a cell's background along a gradient based on its value. |
| **Icon set** | A conditional-formatting type that places a small icon (arrow, traffic light, flag) in a cell based on which value tier it falls into. |
| **Chart junk** | Unnecessary chart elements — 3D effects, redundant legends, excess gridlines, repetitive axis titles — that add visual noise without adding readable information. |

---

*Broken link? Open an issue or PR.*
