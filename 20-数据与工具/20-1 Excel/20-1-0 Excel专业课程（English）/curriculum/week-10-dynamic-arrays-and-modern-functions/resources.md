# Week 10 — Resources

Curated links only — official documentation for every function this week touches, plus the version notes that matter. Everything here is free.

## Version requirements (read this first)

This week's functions are **not available in every Excel version**. If a formula from the lectures throws `#NAME?`, this is almost always why:

- **Excel 365** (subscription) — full support for everything this week, including `LAMBDA`, `MAP`, `REDUCE`, `SCAN`, `BYROW`, `BYCOL`.
- **Excel 2021** — has `FILTER`, `SORT`, `SORTBY`, `UNIQUE`, `SEQUENCE`, `RANDARRAY`, `LET`, and `LAMBDA`. `MAP`/`REDUCE`/`SCAN`/`BYROW`/`BYCOL` may not be included depending on your exact build — check via **File → Account → About Excel** for your version number if one of these throws `#NAME?`.
- **Excel 2019 and earlier (perpetual license)** — **none** of this week's functions exist. There is no workaround; this week requires an upgrade or a switch to Excel for the web (free with any Microsoft account) or Google Sheets.
- **Google Sheets** — `FILTER`, `SORT`, `SORTBY`, `UNIQUE`, `SEQUENCE`, `RANDARRAY` have been available for years. `LET`, `LAMBDA`, `MAP`, `BYROW`, `BYCOL` were added in 2022 and are available to any current free account. `SCAN` does not currently have a direct Sheets equivalent (Lecture 3, Section 6).

Quick self-test: type `=SEQUENCE(3)` in a blank cell. If three stacked numbers (1, 2, 3) spill downward, your app supports this week's material.

## Official documentation

**Microsoft — dynamic arrays and the spill model**

- **Dynamic arrays and spilled array behavior (overview):** <https://support.microsoft.com/en-us/office/dynamic-arrays-and-spilled-array-behavior-205c6b06-03ba-4151-89a1-87a7eb36e531>
- **`FILTER` function:** <https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759>
- **`SORT` function:** <https://support.microsoft.com/en-us/office/sort-function-22f63bd0-ccc8-492f-953d-c20e8e44b86c>
- **`SORTBY` function:** <https://support.microsoft.com/en-us/office/sortby-function-cd3437d6-b7c0-4be0-a5a2-a90d3d1e6d7f>
- **`UNIQUE` function:** <https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e>
- **`SEQUENCE` function:** <https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90>
- **`RANDARRAY` function:** <https://support.microsoft.com/en-us/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33>
- **`TAKE`/`DROP` functions:** <https://support.microsoft.com/en-us/office/take-function-25382ff1-8a5c-486c-a5ea-6e2d75dab2e9>
- **`HSTACK`/`VSTACK` functions:** <https://support.microsoft.com/en-us/office/hstack-function-9d1a2ac6-458b-414a-960d-8577f0d4b90a>
- **`CHOOSEROWS`/`CHOOSECOLS` functions:** <https://support.microsoft.com/en-us/office/chooserows-function-51ace859-f869-4d0c-8188-1bd4a45ee938>
- **The `#SPILL!` error:** <https://support.microsoft.com/en-us/office/how-to-fix-a-spill-error-2b1a1811-9622-4ff1-a5c3-1568a9d2237b>
- **The `#CALC!` error:** <https://support.microsoft.com/en-us/office/calc-error-in-excel-d4fe30ac-9860-4325-9942-59a1de88c5ab>

**Microsoft — LET and LAMBDA**

- **`LET` function:** <https://support.microsoft.com/en-us/office/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999>
- **`LAMBDA` function:** <https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67>
- **Create custom, reusable functions with LAMBDA:** <https://support.microsoft.com/en-us/office/create-custom-collaborative-functions-with-lambda-5d944738-77dc-4f26-a6bf-93a2ba0a7a7c>
- **`MAP` function:** <https://support.microsoft.com/en-us/office/map-function-48006093-f97c-47c1-bfcc-749263bb1f01>
- **`REDUCE` function:** <https://support.microsoft.com/en-us/office/reduce-function-42e39910-b345-45f3-84b8-0642b568b7cb>
- **`SCAN` function:** <https://support.microsoft.com/en-us/office/scan-function-d58dfd11-9969-4439-b2dc-e7062724de29>
- **`BYROW`/`BYCOL` functions:** <https://support.microsoft.com/en-us/office/byrow-function-2e04c677-78c8-4e6b-8c10-a4602f2602bb>

**Google — Sheets equivalents**

- **`FILTER` function:** <https://support.google.com/docs/answer/3093197>
- **`SORT` function:** <https://support.google.com/docs/answer/3093150>
- **`SORTN`/array-sorting notes:** <https://support.google.com/docs/answer/3093176>
- **`UNIQUE` function:** <https://support.google.com/docs/answer/3093198>
- **`SEQUENCE` function:** <https://support.google.com/docs/answer/10218653>
- **`RANDARRAY` function:** <https://support.google.com/docs/answer/10251762>
- **`LET` function:** <https://support.google.com/docs/answer/12475830>
- **`LAMBDA` function:** <https://support.google.com/docs/answer/12508178>
- **Named functions in Google Sheets:** <https://support.google.com/docs/answer/12504534>
- **`MAP` function:** <https://support.google.com/docs/answer/12571317>
- **`ARRAYFORMULA` (legacy, still widely seen):** <https://support.google.com/docs/answer/71291>

## Tools worth installing (optional)

- **Nothing new is required this week** — everything runs inside Excel or Google Sheets, provided your version supports dynamic arrays (see above). If you're on a version that doesn't, the free options are: Excel for the web (any Microsoft account) or Google Sheets (any Google account) — both fully support this week's material at no cost.

## A note on formula debugging this week

Dynamic-array formulas are harder to debug by eyeballing than single-cell formulas, because one formula now controls many cells at once. Two habits worth building now:

- **Build nested formulas one layer at a time.** Get `FILTER` working correctly and confirm its row count before wrapping it in `SORT`; get `SORT` working before wrapping the whole thing in `LET`. Debugging a broken 4-layer nested formula all at once is far harder than confirming each layer independently as you add it.
- **Use the formula bar's "Evaluate Formula" tool (Excel: Formulas → Evaluate Formula) or step through a `LET` by temporarily returning an intermediate name instead of the final calculation** (e.g., temporarily change a `LET`'s last line to just `shipped_rows` instead of the full downstream logic, confirm it looks right, then put the real final line back).
