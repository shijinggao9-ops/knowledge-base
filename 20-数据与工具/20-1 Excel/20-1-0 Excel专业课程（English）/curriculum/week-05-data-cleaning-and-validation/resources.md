# Week 5 — Resources

Curated links only — official documentation and the handful of tools actually worth your time this week. Everything here is free.

## Official documentation — cleaning

- **Microsoft — Find and remove duplicates:** <https://support.microsoft.com/en-us/office/find-and-remove-duplicates-00e35bea-b46a-4d5d-b28e-66a552dc138d>
- **Google — Remove duplicate rows in Google Sheets:** <https://support.google.com/docs/answer/9532984>
- **Microsoft — Using Flash Fill:** <https://support.microsoft.com/en-us/office/using-flash-fill-in-excel-3f9bcf1e-db93-4890-94a0-1578341f73f7>
- **Google — Split text into columns:** <https://support.google.com/docs/answer/6325535>
- **Microsoft — TRIM function:** <https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9>
- **Microsoft — CLEAN function:** <https://support.microsoft.com/en-us/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba2a>
- **Microsoft — SUBSTITUTE function:** <https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4c7d-a3b3-e498d81c7ecf>
- **Microsoft — Find or replace text and numbers:** <https://support.microsoft.com/en-us/office/find-or-replace-text-and-numbers-on-a-worksheet-0e304ca5-4249-4a13-b74f-9a03a4ec3e6f>
- **Microsoft — UNIQUE function:** <https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e>
- **Google — UNIQUE function:** <https://support.google.com/docs/answer/9367201>

## Official documentation — validation and drop-downs

- **Microsoft — Apply data validation to cells:** <https://support.microsoft.com/en-us/office/apply-data-validation-to-cells-29fecbcc-d1b9-42c1-9d76-eff3ce5f7249>
- **Microsoft — Create a drop-down list:** <https://support.microsoft.com/en-us/office/create-a-drop-down-list-7693307a-59ef-400a-b769-c5402dce407d>
- **Microsoft — Create a dependent drop-down list:** <https://support.microsoft.com/en-us/office/create-a-dependent-drop-down-list-c5c9edfb-38d0-4d51-88d2-a3f4c8b1b1f7>
- **Google — Add data validation to cells:** <https://support.google.com/docs/answer/186103>
- **Microsoft — FILTER function:** <https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759>
- **Google — FILTER function:** <https://support.google.com/docs/answer/3093197>
- **Microsoft — INDIRECT function** (for the pre-`FILTER` dependent-drop-down fallback): <https://support.microsoft.com/en-us/office/indirect-function-474b3a3a-8a26-4f44-b491-92b6306fa261>
- **Microsoft — Use conditional formatting rules with a custom formula:** <https://support.microsoft.com/en-us/office/use-a-formula-to-apply-conditional-formatting-fed60dfa-1d3f-4e13-9ecb-f1951ff89d7f>
- **Google — Use conditional formatting rules in Google Sheets:** <https://support.google.com/docs/answer/78413>

## Reading worth your time

- **Hadley Wickham — "Tidy Data" (the paper that defined the term used throughout this week):** <https://vita.had.co.nz/papers/tidy-data.pdf>. Written for R/statistics audiences, but the three rules in Section 2 apply directly to spreadsheet work and are worth reading once, straight through — this course's Lecture 1 leans on this paper's exact framing.

## Tools to install (optional, but useful all course long)

- **Nothing new required this week.** Everything — Remove Duplicates, Flash Fill/Split-to-columns, Data Validation, `FILTER`, conditional formatting — ships in the base Excel or Google Sheets app you already set up in Week 1.
- If your Excel version predates `FILTER`/dynamic arrays (Excel 2019 or earlier, no Microsoft 365 subscription), the `INDIRECT` + named-ranges fallback for dependent drop-downs (Lecture 3, Section 4) works on every version back to the 2000s — no upgrade needed to complete this week.

## A note on versions

Dynamic-array functions (`UNIQUE`, `FILTER`) and the Excel spill reference operator (`#`) require **Excel 365 or Excel 2021+**, or the current web version of **Google Sheets** (Sheets has supported these for years). If your Excel is older, every exercise and challenge has a stated fallback (`INDIRECT` for dependent drop-downs, a per-value `COUNTIF` in place of `UNIQUE` for frequency audits) — you are not blocked from completing this week on an older license, but plan slightly more manual setup time for the drop-down exercises.
