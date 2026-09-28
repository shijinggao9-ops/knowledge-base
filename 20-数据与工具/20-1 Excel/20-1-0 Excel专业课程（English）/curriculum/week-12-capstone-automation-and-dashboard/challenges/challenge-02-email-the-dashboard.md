# Challenge 2 — Auto-Export & Email the Dashboard

**Time:** ~60–75 minutes. **Difficulty:** Medium–Hard.

## The scenario

The Crunch Outfitters sales manager doesn't want to open a workbook every morning — she wants a PDF snapshot of the dashboard sitting in her inbox before she gets to her desk. Your job: after the refresh completes, export the dashboard as a PDF and email it, automatically, as the last step of the same refresh chain.

## Your task

Extend `RefreshDashboard` (Excel) or `refreshDashboard` (Sheets) from Exercise 3 / Challenge 1 with one more step: **export → attach → send**. The refresh, the export, and the send must all happen from one call — not three separate buttons the user has to click in sequence.

### Track A — Excel (VBA + Outlook, Windows only)

1. Export the `Dashboard` sheet to PDF with `ExportAsFixedFormat`:

   ```vb
   Sub ExportDashboardPDF()
       Dim pdfPath As String
       pdfPath = ThisWorkbook.Path & "\Dashboard_" & Format(Date, "yyyy-mm-dd") & ".pdf"
       Worksheets("Dashboard").ExportAsFixedFormat Type:=xlTypePDF, Filename:=pdfPath, _
           Quality:=xlQualityStandard, IncludeDocProperties:=True, IgnorePrintAreas:=False
   End Sub
   ```

2. Send it via Outlook automation (requires Outlook installed and configured — this is the Windows-only piece; there is no built-in cross-platform VBA mail sender):

   ```vb
   Sub EmailDashboardPDF(pdfPath As String)
       Dim OutApp As Object, OutMail As Object
       Set OutApp = CreateObject("Outlook.Application")
       Set OutMail = OutApp.CreateItem(0)

       With OutMail
           .To = "sales-manager@crunchoutfitters.example"
           .Subject = "Crunch Outfitters Dashboard — " & Format(Date, "mmm d, yyyy")
           .Body = "Attached is this morning's automatically refreshed sales dashboard."
           .Attachments.Add pdfPath
           .Send        ' use .Display instead of .Send while testing, to preview without sending
       End With

       Set OutMail = Nothing
       Set OutApp = Nothing
   End Sub
   ```

3. Wire both into the tail end of `RefreshDashboard`, wrapped in the same `On Error` handler — if the export or the send fails, the error message must say *which* step failed (export vs. send), not just "something went wrong."
4. **While developing, use `.Display` instead of `.Send`** so you can see the drafted email without actually sending anything — swap to `.Send` only once you've confirmed it looks right, and only if you have a real Outlook profile to test with responsibly.

### Track B — Google Sheets (Apps Script; cross-platform, no extra software)

1. Export the `Dashboard` sheet region as a PDF blob using the Sheets export URL pattern:

   ```javascript
   function exportDashboardPdf_() {
     const ss = SpreadsheetApp.getActive();
     const sheet = ss.getSheetByName('Dashboard');
     const url = ss.getUrl().replace(/edit$/, '') +
       'export?format=pdf&gid=' + sheet.getSheetId() +
       '&size=A4&portrait=true&fitw=true&gridlines=false';
     const response = UrlFetchApp.fetch(url, {
       headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() }
     });
     return response.getBlob().setName(
       'Dashboard_' + Utilities.formatDate(new Date(), ss.getSpreadsheetTimeZone(), 'yyyy-MM-dd') + '.pdf'
     );
   }
   ```

2. Email it with `MailApp.sendEmail`:

   ```javascript
   function emailDashboardPdf_(pdfBlob) {
     MailApp.sendEmail({
       to: 'sales-manager@crunchoutfitters.example',
       subject: 'Crunch Outfitters Dashboard — ' + Utilities.formatDate(
         new Date(), SpreadsheetApp.getActive().getSpreadsheetTimeZone(), 'MMM d, yyyy'
       ),
       body: 'Attached is this morning\'s automatically refreshed sales dashboard.',
       attachments: [pdfBlob]
     });
   }
   ```

3. Call both from the tail of `refreshDashboard()`, inside the existing `try` block, so a failure at either step is caught by the same error handling from Exercise 3 — and update `notifyFailure_` (from lecture 03) to name which stage failed.
4. `MailApp.sendEmail` counts against Google's **daily email quota** (100/day on a free consumer account, higher on Workspace) — mention this in your write-up as a real constraint on how often this could run.

## Constraints

- Export and send must be **part of the same refresh chain**, not a manually-triggered afterthought — running the one refresh button/menu item does everything: refresh, format, export, send.
- Don't actually spam a real inbox while testing. Excel: use `.Display`. Sheets: point `to:` at your own test address, or comment out the actual `sendEmail` call and log what *would* have been sent while you're iterating.
- The email must be recognizable at a glance — a clear subject line with the date, a one-line body, and the PDF attached (not linked, attached).

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Integration | Export/send exist as separate manual macros | Both fire automatically as the last steps of the one refresh chain |
| Error specificity | One generic failure message for the whole chain | Error message names which stage failed (refresh vs. export vs. send) |
| Safety while testing | Sends real emails during development | Uses `.Display` (VBA) or a test address / logging (Apps Script) until verified |
| Real-world awareness | Ignores platform limits | Notes the Outlook-desktop dependency (Track A) or the daily email quota (Track B) |

## Submission

Commit the extended macro/script and a `write-up.md` describing what you tested, what you deliberately did *not* send to a real inbox, and the one platform limitation (Outlook dependency or email quota) most relevant to running this in production, to `c41-week-12/challenge-02/`.
