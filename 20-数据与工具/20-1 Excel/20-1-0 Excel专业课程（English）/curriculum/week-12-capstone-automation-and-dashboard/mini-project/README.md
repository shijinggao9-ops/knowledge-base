# Mini-Project — Ship a Self-Refreshing Automated Dashboard

> Build one workbook where Power Query pulls and cleans the data, formulas and pivots (or dynamic arrays) summarize it, and a macro or Apps Script routine refreshes, formats, and exports it on a single click. This is the capstone of **C41 · Crunch Excel** — the deliverable that proves every week of this course landed.

**Estimated time:** 4–6 hours, spread across Friday and Saturday.

Twelve weeks ago this course started with typing a value into a single cell. This project is the other end of that arc: a workbook that pulls its own data, cleans itself, summarizes itself, and refreshes itself — the kind of deliverable that gets forwarded around a real company because it *works*, not because someone had to babysit it every morning.

---

## The scenario

You are the analyst at **Crunch Outfitters** (or substitute your own real or realistic dataset — a hobby project, a small business, a public dataset you care about; see "Using your own data" below). Every month, a fresh sales export lands as a CSV. Your job: build the one workbook that turns each new export into an always-current dashboard, with zero manual cleanup.

## Deliverable

A single workbook (Excel `.xlsm`) **or** Google Sheet (with its bound Apps Script project), submitted with:

1. **The workbook/Sheet itself**, fully wired.
2. **`documentation.md`** — the automation README described in lecture 03, §6: what the refresh does step by step, what has to be true for it to work, what happens on failure, and how to change the schedule or data source.
3. **`demo-notes.md`** — a short walkthrough: what you clicked, what happened, and (if you attempted Challenge 1 or 2) how you verified the scheduled/emailed version worked.
4. **Exported source code** — the `.bas` module(s) or `Code.gs`, as plain text, alongside the workbook.

## Requirements — every one of these must be present and working

### 1. Data ingestion (Week 11)

- At least **one Power Query connection** (Excel) or an equivalent repeatable import (Sheets: `IMPORTRANGE`, a scheduled `UrlFetchApp` pull, or manually-pasted-but-query-cleaned data at minimum) that pulls raw data from a source separate from your "clean" table.
- The query performs real cleaning: at minimum, correct data types, trimmed text, and one derived/calculated column (e.g., `Revenue = Units * Unit Price`).

### 2. Summarization (Weeks 6, 7, 10)

- **At least one pivot table** (or, if your platform/data genuinely doesn't suit a pivot, a well-justified `SUMIFS`/`QUERY` summary table) built on the cleaned data.
- **At least one dynamic-array formula** (`FILTER`, `SORT`, `UNIQUE`, or a `LET`/`LAMBDA` — Excel; `FILTER`/`SORT`/`UNIQUE`/`QUERY` — Sheets) that spills a live, formula-driven view (e.g., "Top 5 products by revenue this month") without being manually re-selected each time data changes.

### 3. Dashboard (Week 8)

- A dedicated `Dashboard` sheet with **at least 3 KPI cells** (e.g., Total Revenue, Units Sold, Average Order Value) and **at least one chart** driven by the summarized data — not a static picture, a live chart that updates when the underlying data changes.
- Clean layout: readable at a glance, consistent number formats (currency, percentages where relevant), no leftover gridlines or default styling that wasn't a deliberate choice.

### 4. Automation (this week)

- **One single entry point** — a styled button (Excel) or a custom menu item (Sheets) — that runs the **entire refresh chain**: pull/refresh data → refresh pivots → recalculate dynamic arrays → format the dashboard → stamp a "Last refreshed" timestamp → confirm success to the user.
- **Real error handling**, not a bare catch-and-ignore: a deliberately broken run (rename a source sheet/file, same test as Exercise 3) must produce a specific, useful failure message.
- The refresh macro/function must be **idempotent** — running it five times in a row produces the same correct result as running it once (no duplicate rows, no compounding formatting, no drifting timestamp format).

### 5. Documentation

- `documentation.md` must let a stranger understand and safely operate the workbook without opening the VBA editor or Apps Script project first.

## Stretch goals (optional, not required for a complete submission)

- **Scheduled refresh** (Challenge 1) — wired in and documented, with the failure-visibility safety net.
- **Auto-export + email** (Challenge 2) — wired into the same refresh chain.
- A **second automation entry point** for a different task (e.g., a "Reset to Last Month" macro that archives the current dashboard snapshot before the next refresh overwrites it).
- Support for **multiple source files** in one Power Query folder-based query (genuinely repeatable ETL, not just one hardcoded file path).
- A **light/dark or print-friendly view toggle** driven by a macro/script rather than manual formatting.

## Using your own data

You don't have to use the Crunch Outfitters scenario. If you have a real dataset you care about — personal finances, a hobby league's stats, a small business's orders, a public dataset — use it, provided:

- It has enough rows and enough messiness to make Power Query's cleaning step meaningful (a perfectly clean 10-row table defeats the point).
- It supports at least one meaningful pivot/summary and one meaningful chart.
- You're comfortable it contains no sensitive personal data you wouldn't want in a portfolio piece.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Data ingestion | 15% | Real Power Query (or equivalent) cleaning, not manually pre-cleaned data pasted in |
| Summarization | 15% | A genuine pivot **and** a genuine dynamic-array formula, both live |
| Dashboard | 15% | KPIs + live chart(s), clean and readable, not a screenshot |
| One-click refresh | 20% | Single entry point runs the entire chain correctly, every time |
| Error handling | 15% | Specific, useful failure messages; survives the deliberate-break test |
| Idempotency | 10% | Running the refresh repeatedly never corrupts the result |
| Documentation | 10% | A stranger could operate this workbook from `documentation.md` alone |

**Stretch goals** can push a submission from "great" to "exceptional" but don't substitute for any of the seven required criteria above.

## Milestones

- **Friday, 2h:** Data ingestion + summarization solid — Power Query connection cleaning real data, pivot and dynamic array both working and correct.
- **Friday/Saturday, 1–2h:** Dashboard built — KPIs, chart(s), layout, formatting.
- **Saturday, 1.5–2h:** Automation wired — single entry point, full refresh chain, error handling, idempotency verified with repeated runs and the deliberate-break test.
- **Saturday, 0.5–1h:** `documentation.md` and `demo-notes.md` written; stretch goals if time remains.

## Reflection (`demo-notes.md`, include with your submission)

Answer briefly:

1. Walk through exactly what happens, in order, when you click your refresh button/menu item.
2. What did the deliberate-break test reveal, and how did you fix the error handling in response?
3. Which single skill from this 12-week course felt most load-bearing in this final project — the one thing that, if you didn't know it, this project would have been much harder?
4. If you had one more week on this workbook, what would you build next?

## Submission

Commit the workbook/Sheet export (or a link, if using Google Sheets and sharing access), `documentation.md`, `demo-notes.md`, and your exported macro/script source to your portfolio under `c41-week-12/mini-project/`. This is the final deliverable of **C41 · Crunch Excel** — when it's in, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/quiz.md) to close out the course.
