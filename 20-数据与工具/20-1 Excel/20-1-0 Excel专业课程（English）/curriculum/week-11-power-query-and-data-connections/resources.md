# Week 11 — Resources

Curated links only — official documentation and the handful of tools actually worth your time this week. Everything here is free.

## Official documentation — Power Query fundamentals

- **Microsoft — Power Query overview:** <https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query>
- **Microsoft — Quickstart: Using Power Query in Excel:** <https://support.microsoft.com/en-us/office/quickstart-using-power-query-in-excel-27ff4d76-d19a-4802-a3ea-2eb852be4d5f>
- **Microsoft — Power Query M formula language overview:** <https://learn.microsoft.com/en-us/powerquery-m/power-query-m-language-specification>
- **Microsoft — Data types in Power Query:** <https://learn.microsoft.com/en-us/power-query/data-types>
- **Microsoft — About Power Query (add-in for Excel 2010/2013):** <https://support.microsoft.com/en-us/office/microsoft-power-query-for-excel-download-and-installation-664cad72-2e64-4785-8353-cb7745342d6b>

## Official documentation — import sources

- **Microsoft — Import data from a folder with multiple files (From Folder):** <https://learn.microsoft.com/en-us/power-query/combine-files-overview>
- **Microsoft — Import data from a database using native database query:** <https://learn.microsoft.com/en-us/power-query/native-database-query>
- **Microsoft — Import data from Web:** <https://support.microsoft.com/en-us/office/import-data-from-the-web-b13eec4b-b9d0-4a03-9994-9d5304a3f5ef>
- **Microsoft — Text/CSV connector:** <https://learn.microsoft.com/en-us/power-query/connectors/textcsv>

## Official documentation — transform steps

- **Microsoft — Split a column of text (Power Query):** <https://support.microsoft.com/en-us/office/split-a-column-of-text-power-query-1d938214-2b47-4d78-8fb1-7c1b17862fee>
- **Microsoft — Unpivot columns (Power Query):** <https://learn.microsoft.com/en-us/power-query/unpivot-column>
- **Microsoft — Pivot columns (Power Query):** <https://learn.microsoft.com/en-us/power-query/pivot-column>
- **Microsoft — Group or summarize rows (Power Query):** <https://learn.microsoft.com/en-us/power-query/group-by>
- **Microsoft — Filter by values (Power Query):** <https://learn.microsoft.com/en-us/power-query/filter-values>
- **Microsoft — Remove errors:** <https://learn.microsoft.com/en-us/power-query/remove-errors>

## Official documentation — combining queries and refresh

- **Microsoft — Merge queries overview:** <https://learn.microsoft.com/en-us/power-query/merge-queries-overview>
- **Microsoft — Append queries:** <https://learn.microsoft.com/en-us/power-query/append-queries>
- **Microsoft — Query dependencies view:** <https://learn.microsoft.com/en-us/power-query/query-dependencies-view>
- **Microsoft — Refresh data connections in Excel:** <https://support.microsoft.com/en-us/office/refresh-an-external-data-connection-in-excel-1524175f-777a-4b3b-967e-05359daf6e00>
- **Microsoft — Data Model overview (loading to the Data Model for multi-source pivots):** <https://support.microsoft.com/en-us/office/create-a-data-model-in-excel-87e7a54c-87dc-488e-9410-5c75dbcb0f7b>

## Google Sheets equivalents

- **Google — IMPORTRANGE function:** <https://support.google.com/docs/answer/3093340>
- **Google — IMPORTDATA function:** <https://support.google.com/docs/answer/3093335>
- **Google — IMPORTHTML function:** <https://support.google.com/docs/answer/3093339>
- **Google — IMPORTXML function:** <https://support.google.com/docs/answer/3093342>
- **Google — About Connected Sheets:** <https://support.google.com/docs/answer/9702507>
- **Google — Apps Script overview** (the code-level answer to folder/file automation Sheets has no built-in connector for): <https://developers.google.com/apps-script/overview>

## Tools to install (optional, but useful all course long)

- **Nothing new required this week.** Power Query ships built into the Data tab on Excel 365 and Excel 2016 or later. If you're on Excel 2010 or 2013, install the free **Power Query add-in** (linked above) before starting Lecture 1.
- A plain-text editor (Notepad, TextEdit, VS Code, or any editor that saves literal `.txt`/`.csv` files without adding formatting) — you'll use it repeatedly this week to build and edit CSVs by hand, deliberately outside of Excel, so the files behave like real external data rather than something Excel itself produced and already understands.

## A note on versions and licensing

Power Query's engine is identical across Excel 365, Excel 2016–2021, and the standalone add-in for 2010/2013 — the ribbon layout differs slightly release to release, but every technique in this week's lectures (import, transform, merge, append, folder-combine, refresh) is available on any of them. The **Data Model** destination (Close & Load To → Data Model) requires Excel 2013 or later; if you're on an older add-in version, load to a Table instead and build pivots against that Table directly — you lose the ability to relate multiple loaded tables inside one pivot without a helper `VLOOKUP`/`XLOOKUP`, but every other outcome this week teaches is unaffected.
