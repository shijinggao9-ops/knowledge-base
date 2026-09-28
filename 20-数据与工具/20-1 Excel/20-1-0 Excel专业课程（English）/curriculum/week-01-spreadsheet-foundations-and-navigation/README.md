# Week 1 — Spreadsheet Foundations & Navigation

> **Goal:** by Sunday you can open a blank workbook and, without ever touching the mouse, build a clean, correctly formatted data block — navigating, selecting, and formatting entirely from the keyboard, in both Excel and Google Sheets.

Welcome to **C41 · Crunch Excel**. Before a single formula gets written, you need to be fluent in the thing a formula lives inside: the grid. A spreadsheet is a grid of addressable cells, organized into rows, columns, and sheets, inside a workbook — and every one of the 336 hours ahead of you builds on that grid. Skip this week and you'll spend the rest of the course fighting the interface instead of the problem. Master it now and the interface disappears — you'll think about data, not about where the cursor is.

This week you work in a **blank workbook** you create yourself — no seed file to download. Every lecture, exercise, challenge, and the mini-project has you build directly on the grid.

## Learning objectives

By the end of this week, you will be able to:

- **Explain** the cell/row/column/sheet/workbook model and A1 addressing — and describe how a cell's stored *value* differs from its displayed *format*.
- **Enter, edit, and format** text, numbers, dates, and currency correctly, including the pitfalls that turn a date into text or a number into a string.
- **Navigate and select** ranges fluently with keyboard shortcuts — jumping to the edge of data, selecting to the end of a table, and multi-selecting non-adjacent ranges — without the mouse.
- **Manage sheets** (rename, color, reorder, hide), **freeze panes** so headers stay visible while scrolling, and control **column/row sizing** (width, height, auto-fit).
- **Distinguish** the Excel and Google Sheets interfaces, ribbons/menus, and where each stores and syncs files.
- **Apply** number formats, borders, cell styles, and first conditional formatting rules to make a sheet legible before any math happens.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 3113` — Describe the workbook model — cells, rows, columns, sheets and A1 addressing — and enter and format text, numbers, dates and currency so the value a cell stores and the format it displays agree. |
| Industry | Take a report somebody exported straight out of an old system and make it legible before the meeting it is due at — sections, number formats, frozen headers, a layout a reader takes in at a glance. |
| Beyond the bar | A keyboard-only run at the week — mouse, trackpad and touchscreen banned from the first cell to the last format — `challenges/challenge-02-no-mouse-challenge.md` |


## Prerequisites

- A computer with a mouse/trackpad and keyboard. No prior spreadsheet experience assumed.
- **Excel** (365, 2021, or Excel for the web — all free to trial or already included with many Microsoft 365 plans) **and/or Google Sheets** (free with any Google account). Install/access steps are in [`resources.md`](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/resources.md). You don't need both to do the work, but this course teaches both side by side — pick a primary and peek at the other.
- No formulas, no macros, no prior "spreadsheet knowledge" required. That's the rest of this course.

## Set up your workspace (do this first)

Everything this week happens in one blank workbook you build yourself.

**Excel:**

1. Open Excel → **File → New → Blank workbook**.
2. Save it immediately: **File → Save As** → name it `crunch-week1.xlsx` → pick a folder you'll remember (e.g., a `crunch-excel/` folder in Documents).
3. Note the three tabs at the bottom: `Sheet1`. You'll add more this week.

**Google Sheets:**

1. Go to <https://sheets.google.com> → click the **blank (+)** template.
2. It autosaves to Google Drive the instant you type — rename it via the title field top-left: `crunch-week1`.
3. Google Sheets lives in **Drive**, not on your local disk — Excel lives as a **file** on your disk (or in OneDrive if you save it there). This distinction matters all course long and is covered in Lecture 1.

Sanity check — in cell `A1`, type `Hello, Crunch` and press **Enter**. The text should land in `A1`, left-aligned, and the cursor should move down to `A2`. If that happened, you're set up correctly.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Install/setup; the grid, cells, data types | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Navigation + selection shortcuts | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Freeze panes, multi-sheet management | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Formatting: numbers, dates, currency, borders | 0h | 1.5h | 1h | 0.5h | 1h | 1h | 5h |
| Friday | Conditional formatting; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (rebuild the budget sheet) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **5.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-the-grid-and-the-cell.md](01-the-grid-and-the-cell.md) | Workbook/sheet/row/column/cell model, A1 addressing, data types, value vs. display format | 2h |
| 2 | [lecture-notes/02-navigation-and-selection.md](02-navigation-and-selection.md) | Keyboard navigation, `Ctrl`/`Cmd`-arrow jumps, range selection, freeze panes, multi-sheet management | 2h |
| 3 | [lecture-notes/03-formatting-that-reads.md](03-formatting-that-reads.md) | Number/date/currency formats, alignment, borders, cell styles, first conditional formatting | 2h |
| 4 | [exercises/exercise-01-enter-and-format-data.md](exercise-01-enter-and-format-data.md) | Build and format a real data block from scratch | 1h |
| 5 | [exercises/exercise-02-shortcut-scavenger-hunt.md](exercise-02-shortcut-scavenger-hunt.md) | Timed drills to get shortcuts into your fingers | 1h |
| 6 | [exercises/exercise-03-multi-sheet-setup.md](exercise-03-multi-sheet-setup.md) | Build, rename, color, and link a multi-sheet workbook | 1h |
| 7 | [challenges/challenge-01-reformat-ugly-report.md](challenge-01-reformat-ugly-report.md) | Take a genuinely ugly report and make it readable | 1h |
| 8 | [challenges/challenge-02-no-mouse-challenge.md](challenge-02-no-mouse-challenge.md) | Complete a full task using only the keyboard | 1h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/mini-project/README.md) | Rebuild a formatted monthly budget from a blank sheet | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/homework.md) | Extra practice, spaced across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/resources.md) | Official docs + install links + the few tools worth your time | — |

## By the end of this week you can…

- Describe any workbook's shape — sheets, the active cell, and what A1 addressing means — without hesitating.
- Enter and correctly format text, numbers, dates, and currency so Excel/Sheets stores the *right* underlying value.
- Move and select anywhere in a large sheet without reaching for the mouse.
- Set up a multi-sheet workbook with frozen headers, sized columns, and a clean visual style — before a single formula exists.

## Up next

[Week 2 — Formulas & cell references](../week-02-formulas-and-cell-references/) — once the grid is second nature, we start making it calculate.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
