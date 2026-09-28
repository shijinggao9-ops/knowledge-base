# Week 12 Exercises — Overview

Three exercises, done in order, each building on the last. They take you from "record a macro and don't understand it" to "have a working one-click refresh button wired into your capstone workbook." Do them **after** all three lectures — each one assumes vocabulary and code patterns from the lecture with the matching number.

| # | Exercise | Builds on | ~Time |
|--:|----------|-----------|------:|
| 1 | [Record & Edit Your First Macro](exercise-01-record-first-macro.md) | [01-macros-and-vba.md](01-macros-and-vba.md) | 1h |
| 2 | [Add a Custom Menu in Apps Script](exercise-02-apps-script-menu.md) | [02-apps-script-automation.md](02-apps-script-automation.md) | 1h |
| 3 | [Wire a One-Click Refresh Button](exercise-03-one-click-refresh.md) | [03-capstone-integration.md](03-capstone-integration.md) | 1.5h |

## How to work these

- You need **either** an Excel workbook with the Developer tab enabled (Exercise 1, 3) **or** a Google Sheet (Exercise 2, and 3's Sheets track) — do both platforms if you can; the capstone lets you choose one, but employers and the quiz expect you to recognize both.
- Use your own Week 11 Power Query / dashboard workbook if you have one going, or the lightweight Crunch Outfitters stand-in described in each exercise's setup — either is fine for these three.
- Keep every macro/script you write. Exercise 3's refresh button reuses code from Exercises 1 and 2 almost verbatim.
- **Save as you go.** Excel: `.xlsm`, every time — a plain `.xlsx` silently discards your VBA. Apps Script: autosaves, but click the save icon in the editor before switching tabs to be sure.

## Submission

Each exercise ends with a short "Done when…" checklist and tells you exactly what to commit to your portfolio. Commit macro/script source as plain text (`.bas`/`.vb` export from the VBA editor, or a copy-pasted `.gs` file) even though the "real" copy lives inside the workbook/Sheet — reviewers and graders need to read code without opening a spreadsheet app.
