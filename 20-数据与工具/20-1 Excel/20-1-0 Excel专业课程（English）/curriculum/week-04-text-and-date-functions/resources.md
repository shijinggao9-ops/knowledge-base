# Week 4 — Resources

Curated links only — official documentation for every function used this week, plus the handful of tools worth knowing about. Everything here is free.

## Official documentation — text functions

- **Microsoft — LEFT, LEFTB functions:** <https://support.microsoft.com/en-us/office/left-leftb-functions-9203d2d2-7960-479b-84c6-1ea52b99640c>
- **Microsoft — RIGHT, RIGHTB functions:** <https://support.microsoft.com/en-us/office/right-rightb-functions-240267ee-9afa-4639-a02b-f19e1786d8ba>
- **Microsoft — MID, MIDB functions:** <https://support.microsoft.com/en-us/office/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028>
- **Microsoft — LEN, LENB functions:** <https://support.microsoft.com/en-us/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb>
- **Microsoft — FIND, FINDB functions:** <https://support.microsoft.com/en-us/office/find-findb-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628>
- **Microsoft — SEARCH, SEARCHB functions:** <https://support.microsoft.com/en-us/office/search-searchb-functions-9ab04538-0e55-4719-a72e-b6f54513b495>
- **Microsoft — TEXTSPLIT function:** <https://support.microsoft.com/en-us/office/textsplit-function-b1ca414e-4c21-4ca0-b1b7-bdecace8a6e7>
- **Microsoft — TRIM function:** <https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9>
- **Microsoft — CLEAN function:** <https://support.microsoft.com/en-us/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba41>
- **Microsoft — SUBSTITUTE function:** <https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4c7a-a3a4-a2966fabcf1a>
- **Microsoft — UPPER, LOWER, PROPER functions:** <https://support.microsoft.com/en-us/office/upper-function-c11f29b3-d1a3-4537-8df6-04d0049963d6>
- **Microsoft — TEXTJOIN function:** <https://support.microsoft.com/en-us/office/textjoin-function-357b449a-ec91-49d0-80c3-0e8fc845691c>
- **Microsoft — CONCAT function:** <https://support.microsoft.com/en-us/office/concat-function-9b1a9a3f-94ff-41af-9736-694cbd6b4ca2>
- **Microsoft — Text to Columns:** <https://support.microsoft.com/en-us/office/split-text-into-different-columns-with-the-convert-text-to-columns-wizard-30d5c5e6-ce02-40ea-be5f-2d0c7b0a1c4b>
- **Google — Text function list (SPLIT, TRIM, SUBSTITUTE, TEXTJOIN, etc.):** <https://support.google.com/docs/table/25273>
- **Google — Split text into columns:** <https://support.google.com/docs/answer/6033206>

## Official documentation — date functions

- **Microsoft — DATE function:** <https://support.microsoft.com/en-us/office/date-function-e36c0c8c-4104-49da-ab83-82328b832349>
- **Microsoft — YEAR, MONTH, DAY functions:** <https://support.microsoft.com/en-us/office/year-function-c64f017a-1354-490d-981f-578e8ef8a0b0>
- **Microsoft — EOMONTH function:** <https://support.microsoft.com/en-us/office/eomonth-function-7314ffa1-2bc9-4005-9d66-f49db127d628>
- **Microsoft — WEEKDAY function:** <https://support.microsoft.com/en-us/office/weekday-function-60e44483-2ed1-4f82-ab55-b6eb1a49bd6e>
- **Microsoft — DATEDIF function:** <https://support.microsoft.com/en-us/office/datedif-function-25dba1a4-2812-480b-84dd-8b32a451b35c>
- **Microsoft — NETWORKDAYS function:** <https://support.microsoft.com/en-us/office/networkdays-function-48e717bf-a7a3-495f-969e-5005e3eb18e7>
- **Microsoft — WORKDAY function:** <https://support.microsoft.com/en-us/office/workday-function-f764a5b7-05fc-4864-a1f9-4c5d2f0e2a13>
- **Microsoft — DATEVALUE function:** <https://support.microsoft.com/en-us/office/datevalue-function-df8b07d4-7761-4a93-bc33-b7471bbff252>
- **Microsoft — VALUE function:** <https://support.microsoft.com/en-us/office/value-function-257d0108-07dc-437d-ae1c-bc2d3953d8c2>
- **Microsoft — TEXT function (and full format code reference):** <https://support.microsoft.com/en-us/office/text-function-20d5ac4d-7b94-49fd-bb38-93d29371225c>
- **Microsoft — TODAY and NOW functions:** <https://support.microsoft.com/en-us/office/today-function-5eb3078d-a82c-4736-8930-2f51a028fdd9>
- **Google — Date and time function list:** <https://support.google.com/docs/table/25273>

## Tools to install (optional)

- **Nothing new this week.** Everything above is a built-in function in both Excel and Google Sheets — no add-ins, extensions, or installs required.
- If you want a quick scratchpad to test regex-like text patterns before building them into a formula, any plain-text editor works — you don't need anything specialized for this week's formula patterns.

## A note on function-name differences and locale

- `TEXTSPLIT` requires **Excel 365 or Excel 2021+** (dynamic arrays). Excel 2019 and earlier: use Text to Columns (manual) or `FIND`/`MID` (formula) instead — both are covered in Lecture 1.
- `DATEDIF` works in both Excel and Google Sheets, but doesn't appear in Excel's function autocomplete/Insert Function dialog — Microsoft has historically documented it as present for backward compatibility rather than actively promoted. It still works reliably; just know you may need to type it from memory rather than finding it in a menu.
- **Date parsing locale matters.** `DATEVALUE("01/15/2026")` assumes `MM/DD/YYYY` (US-style) by default in a US-locale spreadsheet; a spreadsheet set to a `DD/MM/YYYY` locale (much of Europe, for example) would parse the identical text string as a different date, or error if the day value exceeds 12. If your dates are coming out wrong after `DATEVALUE`, check your app's locale setting (Excel: File → Options → Language; Sheets: File → Settings → Locale) before assuming the formula itself is broken.
