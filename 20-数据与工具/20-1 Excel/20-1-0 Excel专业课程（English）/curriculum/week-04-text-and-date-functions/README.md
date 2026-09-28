# Week 4 — Text & Date Functions

> **Goal:** by Sunday you can take a column of raw, imported junk — mashed-together full names, extra spaces, inconsistent casing, phone numbers in five different formats, and dates stored as plain text — and turn every one of those columns into clean, consistent, real Excel/Sheets values using nothing but built-in text and date functions.

Welcome back to **C41 · Crunch Excel**. The first three weeks assumed your data arrived clean. It almost never does. Every export from a CRM, a form, an old system, or a coworker's "quick" spreadsheet drags in the same four problems: names crammed into one cell instead of two, whitespace and invisible characters nobody can see, casing that changes row to row, and dates that *look* like dates but are secretly text strings that no formula will do math on. This week is entirely about fixing exactly those problems — reliably, with formulas, not by retyping thousands of rows by hand.

Text and date functions are also the most-reused skill in this entire course. Whatever you build in later weeks — pivot tables, dashboards, imported datasets — will only be as good as the raw data feeding it, and raw data is dirty by default. Get fluent here and every later week goes faster because your inputs are trustworthy.

You'll build two small workbooks-in-progress as you go: a `Contacts` sheet (messy imported people data) and an `Orders` sheet (dates stored as text, the way a CSV export usually delivers them). No file to download — each lecture tells you exactly what to type.

## Learning objectives

By the end of this week, you will be able to:

- **Slice text** with `LEFT`, `RIGHT`, `MID`, and `LEN` to pull fixed-position substrings out of a larger string.
- **Locate substrings** with `FIND` (case-sensitive, no wildcards) and `SEARCH` (case-insensitive, wildcards allowed), and use the position they return to drive `MID`.
- **Split fields properly** with `TEXTSPLIT` (formula-driven, dynamic) and **Text to Columns** (one-time, manual) — and know when each is the right tool.
- **Clean imported junk** with `TRIM` (extra spaces), `CLEAN` (non-printing characters), and `SUBSTITUTE` (targeted find-and-replace inside a formula).
- **Normalize casing** with `UPPER`, `LOWER`, and `PROPER`.
- **Reassemble** cleaned pieces into single values with `TEXTJOIN` (delimiter + empty-skip) and `CONCAT`/`&`.
- **Explain** that dates are just numbers (serial numbers counting days since an epoch) — and why that fact is the key to *all* date arithmetic.
- **Build and decompose dates** with `DATE`, `YEAR`, `MONTH`, `DAY`, `EOMONTH`, and `WEEKDAY`.
- **Calculate real business date math** — age, tenure, workdays between two dates — with `DATEDIF`, `NETWORKDAYS`, and `TODAY`/`NOW`.
- **Convert reliably** between text and real dates/numbers with `DATEVALUE`, `VALUE`, and `TEXT`, so an imported "date" that's secretly a string becomes one you can actually sort, filter, and do math on.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `BUS-K 201` — Parse, clean and reassemble text with the string functions, and do correct calendar arithmetic on dates, including converting an imported value that only looks like a date. |
| Industry | Normalise an export assembled from three different systems over several years so its columns can finally be sorted, filtered and counted. |
| Beyond the bar | Build a fiscal calendar on a July-start year, where every built-in `YEAR`/`MONTH` answer is the wrong one and the mapping has to be derived — `challenges/challenge-02-build-a-fiscal-calendar.md` |


## Prerequisites

- Weeks 1–3 complete — comfortable with the grid, formulas, `$` reference locking, `IF`/`IFS`, and `XLOOKUP`/`INDEX`+`MATCH`.
- Excel (365 or Excel for the web — `TEXTSPLIT` requires a current version; on Excel 2019 and earlier, use Text to Columns instead, called out where it matters) **and/or** Google Sheets.
- No prior text-processing or date-math experience required.

## Set up your workspace (do this first)

Open a fresh blank workbook (Excel: `crunch-week4.xlsx`; Sheets: blank at <https://sheets.google.com>, rename to `crunch-week4`). Add two sheets, renamed exactly as below:

1. **`Contacts`** — a messy people export you'll parse in Lecture 1 and clean in Lecture 2.
2. **`Orders`** — an order log with text-formatted dates, built in Lecture 3.

Each lecture tells you exactly what to type into its sheet. Sanity check before starting Lecture 1: two renamed, empty sheet tabs, no leftover `Sheet1`/`Sheet2` names.

## Weekly schedule

The schedule below adds up to approximately **27.5 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|--------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | `LEFT`/`RIGHT`/`MID`, `FIND`/`SEARCH`, splitting | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | `TRIM`/`CLEAN`/`SUBSTITUTE`, casing, `TEXTJOIN` | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Date serials, `DATE`/`EOMONTH`/`WEEKDAY`, `TEXT` | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | `DATEDIF`, `NETWORKDAYS`, age/tenure math | 0h | 0h | 1h | 0.5h | 1h | 1h | 3.5h |
| Friday | Address parsing; fiscal calendars; catch-up | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (normalize a messy export) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **26.5h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-text-parsing.md](01-text-parsing.md) | `LEFT`/`RIGHT`/`MID`/`LEN`, `FIND`/`SEARCH`, `TEXTSPLIT`, Text to Columns | 2h |
| 2 | [lecture-notes/02-text-cleaning-and-joining.md](02-text-cleaning-and-joining.md) | `TRIM`/`CLEAN`/`SUBSTITUTE`, `UPPER`/`LOWER`/`PROPER`, `TEXTJOIN`/`CONCAT` | 2h |
| 3 | [lecture-notes/03-dates-and-time-math.md](03-dates-and-time-math.md) | Date serial numbers, `DATE`/`EOMONTH`/`WEEKDAY`, `DATEDIF`/`NETWORKDAYS`, `TEXT` | 2h |
| 4 | [exercises/exercise-01-split-full-names.md](exercise-01-split-full-names.md) | Split full names into parts | 1h |
| 5 | [exercises/exercise-02-clean-imported-text.md](exercise-02-clean-imported-text.md) | Clean imported text fields | 1.5h |
| 6 | [exercises/exercise-03-date-difference-calcs.md](exercise-03-date-difference-calcs.md) | Age & tenure date math | 1.5h |
| 7 | [challenges/challenge-01-parse-inconsistent-addresses.md](challenge-01-parse-inconsistent-addresses.md) | Parse inconsistent addresses | 1h |
| 8 | [challenges/challenge-02-build-a-fiscal-calendar.md](challenge-02-build-a-fiscal-calendar.md) | Build a fiscal-period calendar | 1h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-04-text-and-date-functions/mini-project/README.md) | Normalize a messy contact + orders export | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-04-text-and-date-functions/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-04-text-and-date-functions/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-04-text-and-date-functions/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Take a single "Last, First" cell and reliably split it into two clean columns, with a formula that keeps working as new rows are added.
- Strip stray spaces, invisible characters, and inconsistent casing out of a whole imported column in one pass.
- Rebuild a clean full name, email, or label from several cleaned pieces with `TEXTJOIN`.
- Explain, concretely, why `=A2 - A1` works on two dates but fails (or gives a nonsense number) on two date-*looking text strings* — and fix it with `DATEVALUE`.
- Compute someone's exact age or tenure in years, and the number of business days between two dates, correctly handling leap years and weekends.
- Build a small fiscal calendar that maps any date to its fiscal year, quarter, and period-end.

## Up next

[Week 5 — Data cleaning & validation](../week-05-data-cleaning-and-validation/) — once every column is parsed, clean, and correctly typed, we build guardrails so bad data can't get back in.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
