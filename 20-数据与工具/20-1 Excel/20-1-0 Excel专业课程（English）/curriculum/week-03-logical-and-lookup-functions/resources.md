# Week 3 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Tools (you already have everything you need)

- **Excel 365, Excel 2021+, or Excel for the web** — required for `XLOOKUP` and `IFS`. Free web version: <https://www.office.com/launch/excel>. On Excel 2019 or earlier, use `INDEX`/`MATCH` everywhere this week uses `XLOOKUP` — the lecture notes tell you where.
- **Google Sheets** — free with any Google account: <https://sheets.google.com>. Has `XLOOKUP` and `IFS` natively since 2022.
- No add-ins, no installs beyond what Week 1 already set up.

## Required reading (this week's core)

- **Microsoft — IF function:** <https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2>
  *Why: the official reference for the function every branching formula this week builds on.*
- **Microsoft — XLOOKUP function:** <https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929>
  *Why: the full argument list including `match_mode` and `search_mode`, with more worked examples than the lecture has room for.*
- **Microsoft — Looking up data with VLOOKUP, INDEX, or MATCH:** <https://support.microsoft.com/en-us/office/looking-up-data-with-vlookup-index-or-match-0bc48973-d3d3-4c15-8324-9e363b2f4e08>
  *Why: Microsoft's own comparison of the three approaches — useful cross-check against this week's "why XLOOKUP replaces VLOOKUP" argument.*
- **Google — XLOOKUP:** <https://support.google.com/docs/answer/12360774>
  *Why: confirms exactly which behaviors match Excel's `XLOOKUP` and which (rarely) differ.*

## Reference (keep in tabs)

- **Microsoft — IFS function:** <https://support.microsoft.com/en-us/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45>
- **Microsoft — AND function:** <https://support.microsoft.com/en-us/office/and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9>
- **Microsoft — OR function:** <https://support.microsoft.com/en-us/office/or-function-7d17ad14-8700-4281-b308-00b131e22af0>
- **Microsoft — NOT function:** <https://support.microsoft.com/en-us/office/not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77>
- **Microsoft — INDEX function:** <https://support.microsoft.com/en-us/office/index-function-a5dcf0dd-996d-40a4-a822-b56b061328bd>
- **Microsoft — MATCH function:** <https://support.microsoft.com/en-us/office/match-function-e8dffd45-c762-47d6-bf89-533f4a37673a>
- **Microsoft — IFERROR function:** <https://support.microsoft.com/en-us/office/iferror-function-c526fd07-caeb-45de-a56f-99b0a1d15edd>
- **Microsoft — IFNA function:** <https://support.microsoft.com/en-us/office/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461>
- **Microsoft — VLOOKUP function** (know the legacy tool you're avoiding): <https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1>
- **Google — Logical and lookup function list:** <https://support.google.com/docs/table/25273>
  *Why: one page covering `IF`/`IFS`/`AND`/`OR`/`NOT`/`XLOOKUP`/`INDEX`/`MATCH`/`IFERROR`/`IFNA` for Sheets specifically.*

## Practice beyond this week's sheets

- **Exceljet — IF function examples:** <https://exceljet.net/excel-functions/excel-if-function>
  *Why: dozens of real-world `IF` formula patterns (grade bands, bonus tiers, pass/fail) with plain-English breakdowns.*
- **Exceljet — XLOOKUP examples:** <https://exceljet.net/excel-functions/excel-xlookup-function>
  *Why: a large gallery of `XLOOKUP` use cases, including two-way and left lookups, to compare against your own solutions.*
- **Exceljet — INDEX and MATCH examples:** <https://exceljet.net/formulas/index-and-match-with-multiple-criteria>
  *Why: extends this week's two-way lookup into multi-criteria lookups, a natural next step once this week feels solid.*
- **GCFGlobal — Excel: Logical Functions (free short course):** <https://edu.gcfglobal.org/en/excel-formulas/>
  *Why: a gentler second pass if any of this week's lecture concepts didn't fully click on the first read.*

## Glossary

| Term | Definition |
|------|------------|
| **Branching** | A formula returning different results based on a condition — the job of `IF`/`IFS`. |
| **Boolean** | A `TRUE`/`FALSE` value; the output of any comparison or logical function. |
| **Nested function** | A function used as an argument inside another function, e.g., `IF` inside `IF`. |
| **Catch-all** | The final `TRUE, value` pair in `IFS`, guaranteeing a result when no earlier condition matched. |
| **Lookup value** | The value you have, and are searching for a match on. |
| **Lookup array / return array** | The range to search, and the range to pull the answer from — independent in `XLOOKUP`. |
| **Exact match** | A lookup mode requiring the lookup value to appear precisely; the safe default. |
| **Approximate match** | A lookup mode returning the nearest bracket boundary rather than an exact hit — used for tiers. |
| **`#N/A`** | The error value meaning "lookup ran, found nothing." |
| **Left-lookup** | A lookup where the value you want is in a column to the *left* of the column you're searching — impossible for plain `VLOOKUP`. |
| **Two-way lookup** | A lookup pinpointed by both a row label and a column label, e.g., `INDEX`/`MATCH` with two `MATCH` calls. |
| **Spilling / dynamic array** | A single formula that fills multiple cells automatically, e.g., `XLOOKUP` returning a whole row. |
| **Fallback / default value** | What a formula returns when the "real" answer is unavailable — the `if_not_found` argument, or the second argument of `IFERROR`/`IFNA`. |

---

*Broken link? Open an issue or PR.*
