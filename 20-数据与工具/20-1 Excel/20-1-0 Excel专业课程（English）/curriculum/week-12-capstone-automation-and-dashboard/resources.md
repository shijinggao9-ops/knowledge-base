# Week 12 Resources

Curated, free/official links — enough to go deep on macros, VBA, and Apps Script without drowning in tutorial spam. Nothing here requires a paid course.

## Official documentation — VBA & Excel automation

- **Excel VBA reference (Microsoft Learn)** — https://learn.microsoft.com/en-us/office/vba/api/overview/excel — the authoritative reference for every object (`Range`, `Worksheet`, `PivotTable`, `Workbook`), property, and method used this week.
- **Getting started with VBA in Office** — https://learn.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office — the on-ramp: recording, the editor, the object model basics.
- **`Application.CalculateUntilAsyncQueriesDone`** — https://learn.microsoft.com/en-us/office/vba/api/excel.application.calculateuntilasyncqueriesdone — the exact method lecture 03 relies on to make `RefreshAll` block until Power Query finishes.
- **Range.ExportAsFixedFormat method** — https://learn.microsoft.com/en-us/office/vba/api/excel.worksheet.exportasfixedformat — the PDF-export call used in Challenge 2's Excel track.
- **Macro security in Office** — https://support.microsoft.com/en-us/office/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6 — what the security warning bar means and how trusted locations work (relevant to Homework Part 4).

## Official documentation — Google Apps Script

- **Apps Script overview** — https://developers.google.com/apps-script/overview — what Apps Script is, where code runs, and the services available.
- **`SpreadsheetApp` reference** — https://developers.google.com/apps-script/reference/spreadsheet/spreadsheet-app — every method used in lecture 02 and beyond (`getSheetByName`, `getRange`, `getValues`/`setValues`, `flush`, `toast`).
- **Simple triggers** — https://developers.google.com/apps-script/guides/triggers — `onOpen`, `onEdit`, `onSelectionChange`, and their authorization limits.
- **Installable triggers** — https://developers.google.com/apps-script/guides/triggers/installable — time-driven, on-edit, and on-form-submit triggers, and the `ScriptApp.newTrigger` API used in Challenge 1.
- **Custom menus (`ui.createMenu`)** — https://developers.google.com/apps-script/guides/menus — the full API behind Exercise 2's `onOpen()` menu.
- **`MailApp` reference** — https://developers.google.com/apps-script/reference/mail/mail-app — the email service used in Challenge 2's Sheets track, including the daily quota.
- **Apps Script quotas and limits** — https://developers.google.com/apps-script/guides/services/quotas — execution time limits and daily service quotas (email, `UrlFetchApp`, etc.) referenced throughout this week.

## Power Query (Week 11 carryover, used in the capstone refresh chain)

- **Power Query documentation (Microsoft Learn)** — https://learn.microsoft.com/en-us/power-query/ — the source-of-truth reference for the query connections your `RefreshDashboard` chain depends on.

## Tools to install

- **Nothing new this week.** Excel's VBA editor (`Alt+F11`) and Google's Apps Script editor (`Extensions → Apps Script`) are both built in — no downloads required.
- **Windows Task Scheduler** (Windows only, built-in) — needed only if you attempt Challenge 1's Excel track (Track B). Search "Task Scheduler" in the Start menu; no install needed.
- **Outlook desktop** (Windows only) — needed only if you attempt Challenge 2's Excel track (Track A). If you don't have Outlook configured, do the Google Sheets track instead — it needs nothing beyond a Google account.

## Worth reading once, not required

- **Excel Object Model map** — a mental model of how `Application → Workbooks → Worksheets → Range` nest, available inside the VBA editor's Object Browser (`F2` while the editor is open) — faster than any external article for looking up "does this object have that property," since it's always in sync with your installed Excel version.
- **Apps Script "Executions" log** (left sidebar of the script editor) — not a doc link, but the single most useful debugging tool for a scheduled trigger that silently failed; check it before assuming your trigger never ran.

---

*This closes out the resource list for C41 · Crunch Excel. For what comes after spreadsheets, see [C27 Crunch Data](../../../C27-CRUNCH-DATA/) and [C33 Crunch SQL](../../../C33-CRUNCH-SQL/).*
