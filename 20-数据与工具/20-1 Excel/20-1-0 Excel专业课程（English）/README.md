# C41 · Crunch Excel

> A free, open-source 12-week course that takes you from your first cell to expert-level spreadsheets — formulas, modeling, pivot tables, dashboards, Power Query, and automation in Excel and Google Sheets.

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)
[![Excel · Google Sheets](https://img.shields.io/badge/stack-Excel_·_Google_Sheets-2463EB.svg)](#stack)
[![Built in the open](https://img.shields.io/badge/built-in%20the%20open-2463EB.svg)](https://github.com/CODECRUNCHWORLDWIDE)

C41 is the dedicated spreadsheet course — Excel and Google Sheets *are* the subject and the tool, start to finish. It goes all the way: from typing your first value into a cell to building an automated, self-refreshing dashboard driven by Power Query and macros. This is the one place spreadsheets are taught as the main tool, and the practical data foundation the [C27 Crunch Data](../C27-CRUNCH-DATA/) and [C33 Crunch SQL](../C33-CRUNCH-SQL/) courses build on.

---

## Pathway summary

- **Full-time:** 12 weeks · ~28 hrs/week · ~336 hours
- **Working-professional pace:** 6 months · ~14 hrs/week
- **Evening pace:** 12 months · ~7 hrs/week

See [`SYLLABUS.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/SYLLABUS.md).

---

## Standards & equivalency

> C41 stands in for a university's spreadsheet-modelling course, and for the spreadsheet half of its business-analytics course.

**University equivalent.** Two of them, not one. **Spreadsheet Modeling and Analysis** — `ISM 3113`, `QMB 3600`, `MGMT 47200`, `BUS-K 201`. **Business Analytics** — `ISM 4402`, `QMB 3200`, `BUS 4750`.

Coverage: **full** against Spreadsheet Modeling and Analysis, **partial** against Business Analytics. Partial has a precise meaning here, and it is not "most of it". A business-analytics section is three things at once — prepare and model the data, test it statistically, and communicate what you found — and C41 is the first of the three. Every Business Analytics outcome claimed in the table below is taught here at the same depth or deeper and is assessed; the statistical half (estimation, hypothesis testing, regression, A/B design) is claimed under the same ledger entry by [C61 · Crunch Stats](../C61-CRUNCH-STATS/), and the communication half by [C62 · Crunch Viz](../C62-CRUNCH-VIZ/). So partial here is a matter of which third of the course C41 answers for, not of anything taught thinly — there is no outstanding work recorded against C41 on that claim, and nothing left for a learner to discover.

C41 carries no credit, no transcript entry, no accreditation and no proctored exam. The equivalence is one of **content and skill**: the outcomes below are taught here at the same depth or deeper, and every one of them is assessed. What a registrar records is not something an open repository can give you.

| University outcome | Where this course teaches it | Depth |
| --- | --- | --- |
| The workbook model — cells, rows, columns, sheets, A1 addressing — and entering and formatting values so the stored value and the displayed one agree | [Week 01](curriculum/week-01-spreadsheet-foundations-and-navigation/) | same |
| Build arithmetic and aggregate formulas, and choose relative, absolute or mixed references so a formula survives being copied | [Week 02](curriculum/week-02-formulas-and-cell-references/) | same |
| Read and repair the standard formula errors — `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` — rather than working around them | [Week 02](curriculum/week-02-formulas-and-cell-references/) | deeper |
| Conditional logic and lookup functions: branch on business rules, look a value up across tables, and trap the miss | [Week 03](curriculum/week-03-logical-and-lookup-functions/) | deeper |
| Text and date functions — parse, clean and reassemble imported strings, and do correct calendar arithmetic | [Week 04](curriculum/week-04-text-and-date-functions/) | deeper |
| Prepare a dataset for analysis: duplicates, inconsistent categories, type mismatches, and input rules that stop the mess recurring | [Week 05](curriculum/week-05-data-cleaning-and-validation/) | deeper |
| Structure data as a table with named, structured references, and aggregate it conditionally with `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` | [Week 06](curriculum/week-06-tables-and-structured-references/) | same |
| Summarise a large dataset with a pivot table — group, aggregate, reframe as a share of total — and chart the result honestly | [Week 07](curriculum/week-07-pivot-tables-and-charts/) | same |
| Present a result as an interactive report a decision-maker can read and filter without touching a formula | [Week 08](curriculum/week-08-dashboards-and-visualization/) | deeper |
| Financial functions and the time value of money: loan amortisation with `PMT`/`IPMT`/`PPMT`, and `NPV`/`IRR` on a cash-flow series | [Week 09](curriculum/week-09-financial-and-what-if-modeling/) | same |
| Scenario and sensitivity analysis — one- and two-variable data tables, Goal Seek, and named Best/Base/Worst scenarios | [Week 09](curriculum/week-09-financial-and-what-if-modeling/) | same |
| Build a model somebody else can audit: inputs, calculations and outputs separated, assumptions documented, outputs stress-tested | [Week 09](curriculum/week-09-financial-and-what-if-modeling/) | deeper |
| Write formulas that return a whole range of results rather than one value, and name intermediate steps so a long formula stays readable | [Week 10](curriculum/week-10-dynamic-arrays-and-modern-functions/) | deeper |
| Automate repetitive spreadsheet work — record a macro, read the code it produced, edit it by hand, and put it behind a button | [Week 12](curriculum/week-12-capstone-automation-and-dashboard/) | same |
| Complete a substantial workbook of the learner's own, documented well enough that a stranger can operate it | [Week 12](curriculum/week-12-capstone-automation-and-dashboard/) | deeper |
| **Business Analytics** — data preparation as the first step of any analysis, and what "tidy" means before a single figure is computed | [Week 05](curriculum/week-05-data-cleaning-and-validation/) | deeper |
| **Business Analytics** — descriptive summarisation of a business dataset: aggregate by dimension, group by period, express as a share of the whole | [Week 07](curriculum/week-07-pivot-tables-and-charts/) | same |
| **Business Analytics** — communicate a finding to a manager in a form they can act on rather than a table they must interpret | [Week 08](curriculum/week-08-dashboards-and-visualization/) | same |
| **Business Analytics** — build a decision model and test the decision against a range of assumptions rather than a single case | [Week 09](curriculum/week-09-financial-and-what-if-modeling/) | deeper |
| **Business Analytics** — a repeatable path from raw source to analysis-ready data, so the answer can be reproduced next month | [Week 11](curriculum/week-11-power-query-and-data-connections/) | deeper |

Every row above points at a week that **assigns work** on that outcome — an exercise, a challenge, homework, a quiz item or the mini-project — not merely a week that mentions it.

**The industry bar.** What an employer expects of somebody paid to work in a spreadsheet, and where this course makes the learner do it. C41's deliverable is a workbook, not a program, so several of these clauses are met in that medium — an audit trail instead of a diff, a named-range and formula-audit discipline instead of a linter, a spot-checked expected result instead of a test suite. Where that is what is happening, the row says so plainly rather than claiming tooling this course does not ship.

| What the job expects | Where this course does it |
| --- | --- |
| Work lands somewhere durable and reviewable, not on your desktop | Most weeks end by committing the sheet or an export, plus a short write-up, to a portfolio folder the learner owns — the convention is stated at [`curriculum/week-12-capstone-automation-and-dashboard/exercises/README.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/exercises/README.md), including exporting macro and script source as plain text so a reviewer can read it without opening a spreadsheet app. C41 does not teach git itself, and Weeks 4, 7 and 8 keep their deliverables inside the workbook rather than committing them |
| You read work you did not write and form a judgement on it | Three separate times: repair an inherited workbook producing six wrong answers at [`curriculum/week-02-formulas-and-cell-references/challenges/challenge-02-fix-the-broken-references.md`](challenge-02-fix-the-broken-references.md), audit a departed colleague's fragile `VLOOKUP` model at [`curriculum/week-03-logical-and-lookup-functions/challenges/challenge-01-replace-every-vlookup.md`](challenge-01-replace-every-vlookup.md), and sanity-check a chart before it goes to a director at [`curriculum/week-07-pivot-tables-and-charts/challenges/challenge-02-misleading-chart-fix.md`](challenge-02-misleading-chart-fix.md) |
| The work is checked against a stated expected result, not eyeballed | C41 ships no test suite and no test runner — there is nothing to run `pytest` against. What it ships instead is the spreadsheet equivalent: published spot-check values every exercise must reproduce, a `Done when…` checklist on each one, and the capstone's deliberate-break and repeated-run checks at [`curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md) |
| You read the error the tool actually returned instead of guessing | C41 has no `Common bugs to catch` section. The error strings are quoted verbatim where they arise and each is paired with its cause and fix — `#REF!`, `#DIV/0!`, `#VALUE!` and `#NAME?` at [`curriculum/week-02-formulas-and-cell-references/lecture-notes/03-named-ranges-and-cross-sheet.md`](03-named-ranges-and-cross-sheet.md), `#N/A` at [`curriculum/week-03-logical-and-lookup-functions/lecture-notes/03-index-match-and-errors.md`](03-index-match-and-errors.md), `#SPILL!` at [`curriculum/week-10-dynamic-arrays-and-modern-functions/lecture-notes/01-the-spill-model.md`](01-the-spill-model.md) |
| Tooling used the way a team uses it | There is no formatter, no linter and no pipeline here, because a workbook has none. The discipline that stands in its place is taught explicitly: named ranges instead of bare addresses and Trace Precedents / Trace Dependents to walk a dependency chain at [`curriculum/week-02-formulas-and-cell-references/lecture-notes/03-named-ranges-and-cross-sheet.md`](03-named-ranges-and-cross-sheet.md), and stepping a long formula with `LET` and Evaluate Formula at [`curriculum/week-10-dynamic-arrays-and-modern-functions/resources.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/resources.md) |
| A model is laid out so a reviewer can follow it | Inputs, calculations and outputs kept separate, with assumptions written down beside them, at [`curriculum/week-09-financial-and-what-if-modeling/lecture-notes/02-model-structure.md`](02-model-structure.md) |
| Something that runs unattended, and fails visibly when it fails | A scheduled refresh with a deliberate failure path at [`curriculum/week-12-capstone-automation-and-dashboard/challenges/challenge-01-scheduled-auto-refresh.md`](challenge-01-scheduled-auto-refresh.md) |
| The output is portfolio-grade: a stranger can operate it from the documentation alone | The capstone's rubric weights exactly that, and requires `documentation.md` beside the workbook — [`curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md) |
| The practice is named, not implied | Every week carries its own `Standards this week meets` block naming the professional task it builds |

**Beyond both bars.** Clearing the two floors is entry, not success. Open any of these and check it in under a minute.

| What we add | Which bar it beats | Where it lives |
| --- | --- | --- |
| Every quiz publishes its own answer key in the same file, folded under the questions it answers, and explains the reasoning rather than giving the letter — no key withheld until a deadline | both | [`curriculum/week-03-logical-and-lookup-functions/quiz.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/quiz.md) |
| `Under the hood` blocks carry the mechanics a spreadsheet syllabus stops short of — why `INDEX`/`MATCH` costs what it costs, what a date serial number really is — folded so a learner may skip every one and still finish | university | [`curriculum/week-03-logical-and-lookup-functions/lecture-notes/03-index-match-and-errors.md`](03-index-match-and-errors.md) |
| The learner finishes holding a workbook somebody can open and run — data pull, cleaning, summary, dashboard and one-click refresh, with its documentation and its macro source exported as readable text — not a grade only a registrar can see | both | [`curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md) |
| Every technique is taught in two applications at once, Excel and Google Sheets, with the divergences named rather than glossed — and one challenge a week that is the port itself | both | [`curriculum/week-06-tables-and-structured-references/challenges/challenge-02-sheets-vs-excel-tables.md`](challenge-02-sheets-vs-excel-tables.md) |
| A written repair of a workbook somebody else built: six seeded defects, none of which raise an error, diagnosed and documented before a single cell is changed | industry | [`curriculum/week-02-formulas-and-cell-references/challenges/challenge-02-fix-the-broken-references.md`](challenge-02-fix-the-broken-references.md) |
| Three weeks sit past what a spreadsheet-modelling section contains at all — a repeatable ETL pipeline, recursive custom functions, and automation that runs with nobody at the keyboard | university | [`curriculum/week-11-power-query-and-data-connections/`](curriculum/week-11-power-query-and-data-connections/) |
| A published, weighted rubric on every mini-project, so the learner grades their own work against the same criteria a reviewer would | both | [`curriculum/week-09-financial-and-what-if-modeling/mini-project/README.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/mini-project/README.md) |

**Gaps we declare.** None against either outcome set as claimed. Two scope limits are worth stating anyway, because neither is a gap a learner should discover late: C41 answers for the data-preparation and modelling third of a business-analytics course only — the statistical third and the communication third are C61's and C62's, under the same ledger entry — and C41 teaches spreadsheets, not version control, so the portfolio convention it uses is a folder per week rather than a repository workflow of its own.

---

## What you will be able to do at the end of 12 weeks

- **Navigate fluently:** move, select, and format any workbook without the mouse, and understand rows, columns, sheets, and references cold.
- **Write formulas that hold up:** relative, absolute, and mixed references; nested logic; and error handling that never silently breaks.
- **Look anything up:** `IF`, `IFS`, `XLOOKUP`, and `INDEX`/`MATCH` — pick the right tool and know why `VLOOKUP` isn't it.
- **Wrangle messy data:** parse and reshape text, do real date math, split and clean imported junk, and enforce input rules with data validation.
- **Summarize at scale:** turn raw rows into answers with Tables, structured references, and pivot tables — then chart them clearly.
- **Build dashboards:** design interactive, single-screen dashboards with slicers, KPIs, and controls that a manager can actually read.
- **Model money and decisions:** amortization, NPV/IRR, what-if analysis, Goal Seek, Scenario Manager, and data tables.
- **Work like a modern spreadsheet:** dynamic arrays (`FILTER`, `SORT`, `UNIQUE`, `LET`, `LAMBDA`), Power Query ETL, and macros/VBA plus Apps Script automation.
- **Automate the whole thing:** build a dashboard that pulls, cleans, and refreshes itself on a click — the capstone.

---

## Curriculum (12 weeks)

| Week | Topic | You leave able to… |
|------|-------|--------------------|
| 1 | [Spreadsheet foundations & navigation](curriculum/week-01-spreadsheet-foundations-and-navigation/) | Move around any workbook and format cells with confidence. |
| 2 | [Formulas & cell references](curriculum/week-02-formulas-and-cell-references/) | Write formulas with relative, absolute, and mixed refs. |
| 3 | [Logical & lookup functions](curriculum/week-03-logical-and-lookup-functions/) | Branch with IF/IFS and look up data with XLOOKUP + INDEX/MATCH. |
| 4 | [Text & date functions](curriculum/week-04-text-and-date-functions/) | Parse text and do correct date/time math. |
| 5 | [Data cleaning & validation](curriculum/week-05-data-cleaning-and-validation/) | Clean imported data and enforce input rules. |
| 6 | [Tables & structured references](curriculum/week-06-tables-and-structured-references/) | Turn ranges into Tables that grow and read clearly. |
| 7 | [Pivot tables & charts](curriculum/week-07-pivot-tables-and-charts/) | Summarize thousands of rows and chart the result. |
| 8 | [Dashboards & visualization](curriculum/week-08-dashboards-and-visualization/) | Build an interactive single-screen dashboard with slicers. |
| 9 | [Financial & what-if modeling](curriculum/week-09-financial-and-what-if-modeling/) | Model cash flows and run Goal Seek + scenarios. |
| 10 | [Dynamic arrays & modern functions](curriculum/week-10-dynamic-arrays-and-modern-functions/) | Spill results with FILTER/SORT/UNIQUE and write LAMBDA. |
| 11 | [Power Query & data connections](curriculum/week-11-power-query-and-data-connections/) | Build a repeatable ETL pipeline from external sources. |
| 12 | [Capstone — automation & the automated dashboard](curriculum/week-12-capstone-automation-and-dashboard/) | Automate a self-refreshing dashboard with macros + Apps Script. |

---

## How to navigate a week

Every week folder holds the same structure:

- **`README.md`** — the week overview + how the pieces fit + the week's goal.
- **`lecture-notes/`** — 3 lectures (~2 hrs each), the conceptual core.
- **`exercises/`** — 3 short, guided reps in a real workbook.
- **`challenges/`** — 2 open-ended problems with no single right answer.
- **`mini-project/`** — one build that ties the week together.
- **`homework.md`**, **`quiz.md`**, **`resources.md`** — practice, self-check, and further reading.

---

## Stack

Microsoft Excel (365 / 2021+) as the primary engine, with Google Sheets taught alongside it — you'll learn both, and where they differ (functions, Power Query vs. Apps Script, macros vs. Apps Script) is called out explicitly. Excel for the web and the free Google Sheets both work for every week. You'll also use sample workbooks and datasets shipped with the course.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · [Browse all courses](https://codecrunchglobal.vercel.app/courses)*
