# Week 12 — Capstone — Automation & the Automated Dashboard

> **Goal:** by Sunday you can hand someone a workbook that pulls its own data, cleans it, summarizes it, charts it, and refreshes itself — in Excel with a recorded/edited VBA macro, and in Google Sheets with Apps Script — so opening it or clicking one button is the only "work" left.

Welcome to the last week of **C41 · Crunch Excel**. Every week before this taught you a skill in isolation: formulas, lookups, cleaning, tables, pivots, charts, financial modeling, dynamic arrays, Power Query. This week you stop learning new spreadsheet *features* and start learning the thing that turns a spreadsheet into a **product**: automation. A workbook that still needs you to click Refresh, fix formatting, and re-export a PDF every Monday morning isn't finished — it's a chore with extra steps. This week you finish it.

We use one running scenario all week: **Crunch Outfitters**, a small outdoor-gear retailer that drops a fresh sales export into a folder every month (the same shape of data your Week 11 Power Query pipeline was built to eat). By Friday you will have a workbook where a single click — a macro button in Excel, a custom menu item in Google Sheets — refreshes the Power Query connection, recalculates the pivots and dynamic arrays, reformats anything that needs it, stamps a "last refreshed" time, and (in the challenges) exports and emails the result. That workbook, tuned to your own data, is the capstone deliverable and the centerpiece of your portfolio for this course.

## Learning objectives

By the end of this week, you will be able to:

- **Record** a macro in Excel, **read** the VBA it generates, and **edit** that VBA by hand instead of re-recording from scratch.
- **Write** VBA that references ranges, loops over rows, tests conditions, and handles errors with `On Error`, without relying on the recorder for everything.
- **Attach** a macro to a button, shape, or keyboard shortcut so a non-technical user can run it with one click.
- **Write** Google Apps Script functions against the `SpreadsheetApp` object model, and add a custom menu with `onOpen()`.
- **Distinguish** simple triggers (`onOpen`, `onEdit`) from installable triggers (time-driven, edit, form-submit) in Apps Script, and know when VBA has no real equivalent.
- **Trigger** a full refresh — Power Query connections, pivot tables, dynamic-array formulas, and dashboard formatting — from a single entry point in both Excel and Sheets.
- **Wire together** everything from Weeks 1–11 (Power Query, Tables, pivots, dynamic arrays, dashboards) into one workbook with one refresh path and basic error handling.
- **Ship** a documented, self-refreshing automated dashboard end-to-end — the capstone.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 3113` — Automate repetitive spreadsheet work — record a macro, read and hand-edit the code it produced, and put it behind a button — and complete a substantial workbook of the learner's own, documented well enough for a stranger to operate. |
| Industry | Ship the workbook that pulls, cleans, summarises and refreshes itself on a single click, and hand it to somebody who did not build it. |
| Beyond the bar | A refresh nobody triggers: a time-driven schedule whose failure announces itself instead of quietly serving yesterday's numbers — `challenges/challenge-01-scheduled-auto-refresh.md` |


## Prerequisites

- Everything through **Week 11 (Power Query & data connections)** — this week assumes you already have a workbook with at least one Power Query connection, a pivot table or dynamic-array summary, and a dashboard sheet with a chart or two. If your Week 11 workbook is thin, spend 20–30 minutes fleshing it out before Monday; automation only pays off once there's something real to automate.
- **Excel:** Windows Excel (Excel for Mac's VBA editor is more limited but the concepts transfer; VBA itself does not exist in Excel for the web).
- **Google Sheets:** any Google account with Sheets + the built-in Apps Script editor (Extensions → Apps Script). No installs required.
- Comfort with basic programming ideas — variables, loops, if/else — helps but isn't required; both lectures build from zero.

## Setup — enable what you'll need

**Excel — show the Developer tab and set macro security:**

1. `File → Options → Customize Ribbon` → check **Developer** in the right-hand list → OK.
2. `Developer → Macro Security` → choose **Disable all macros with notification**. This is the safe default: Excel warns you and lets you enable macros per-file, rather than silently blocking everything or silently running everything.
3. Any workbook that contains macros must be saved as **`.xlsm`** (macro-enabled) — a plain `.xlsx` silently discards VBA on save. Save your capstone workbook as `Crunch-Outfitters-Dashboard.xlsm` now, before you write a single line.

**Google Sheets — open the Apps Script editor:**

1. In your Sheet, `Extensions → Apps Script`. This opens a separate script project bound to the spreadsheet.
2. The default file is `Code.gs` — Apps Script is JavaScript with Google's `SpreadsheetApp`, `DriveApp`, `MailApp`, etc. bolted on. No install needed; it runs on Google's servers.
3. The first time any function touches the spreadsheet, Drive, or Gmail, Google will prompt you to **authorize** the script — review the scopes and accept. This is normal and expected, not a red flag.

## This week's map

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-macros-and-vba.md](01-macros-and-vba.md) | Recording macros, reading generated VBA, editing it, `Range`/`Sub`/loops/`On Error`, buttons | 2h |
| 2 | [lecture-notes/02-apps-script-automation.md](02-apps-script-automation.md) | Apps Script fundamentals, custom menus, simple vs. installable triggers, VBA vs. Apps Script | 2h |
| 3 | [lecture-notes/03-capstone-integration.md](03-capstone-integration.md) | Wiring Power Query + pivots + dynamic arrays + dashboard into one refresh path, error handling | 2h |
| 4 | [exercises/exercise-01-record-first-macro.md](exercise-01-record-first-macro.md) | Record, read, and edit your first macro | 1h |
| 5 | [exercises/exercise-02-apps-script-menu.md](exercise-02-apps-script-menu.md) | Add a custom menu with two working commands | 1h |
| 6 | [exercises/exercise-03-one-click-refresh.md](exercise-03-one-click-refresh.md) | Wire a button/menu item that refreshes and reformats | 1.5h |
| 7 | [challenges/challenge-01-scheduled-auto-refresh.md](challenge-01-scheduled-auto-refresh.md) | Make the refresh run on a schedule, unattended | 1.5h |
| 8 | [challenges/challenge-02-email-the-dashboard.md](challenge-02-email-the-dashboard.md) | Auto-export the dashboard to PDF and email it | 1.5h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/mini-project/README.md) | Ship the full self-refreshing automated dashboard (capstone) | 4h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/homework.md) | Extra practice tying macros, Apps Script, and the pipeline together | 3h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-12-capstone-automation-and-dashboard/resources.md) | Official VBA/Apps Script docs + the tools worth installing | — |

## Weekly schedule

Adds up to roughly the course's full-time pace, ~19 hours this final week (lighter than earlier weeks since it's mostly integration of skills you already have, plus the capstone).

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|---------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | VBA: record, read, edit, attach to a button | 2h | 1h | 0h | 0h | 0.5h | 0h | 3.5h |
| Tuesday | Apps Script: menus and triggers | 2h | 1h | 0h | 0h | 0.5h | 0h | 3.5h |
| Wednesday | Wiring the capstone refresh path | 2h | 1.5h | 0h | 0h | 0.5h | 0h | 4h |
| Thursday | Scheduling + emailing the dashboard | 0h | 0h | 3h | 0h | 0.5h | 0h | 3.5h |
| Friday | Start the mini-project | 0h | 0h | 0h | 0h | 1h | 2h | 3h |
| Saturday | Finish + document the mini-project | 0h | 0h | 0h | 0h | 0h | 2h | 2h |
| Sunday | Quiz + course review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **3.5h** | **3h** | **1h** | **2.5h** | **4h** | **~20.5h** |

## By the end of this week you can…

- Turn a repetitive manual task into a one-click macro or Apps Script function, in either Excel or Google Sheets.
- Read VBA or Apps Script you didn't write, understand what object it's touching and why, and edit it safely.
- Design a refresh path with a single entry point, sensible error handling, and a visible "it worked" signal (a timestamp, a message box, a toast).
- Explain the real differences between VBA and Apps Script — not just "one's for Excel" — including triggers, execution environment, and quotas.
- Ship a complete, documented, automated, self-refreshing dashboard — the deliverable this entire 12-week course has been building toward.

## Course complete

This is the final week of **C41 · Crunch Excel**. Once your mini-project is submitted and your quiz score logged, you've gone from a blank cell to an automated, self-refreshing dashboard — the full arc of the course. If you want to keep going with data, the practical next stops are [C27 Crunch Data](../../../C27-CRUNCH-DATA/) and [C33 Crunch SQL](../../../C33-CRUNCH-SQL/), which pick up where a single spreadsheet starts to strain.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
