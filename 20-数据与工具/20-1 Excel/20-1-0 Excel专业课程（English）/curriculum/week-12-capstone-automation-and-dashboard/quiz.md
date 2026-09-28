# Week 12 — Quiz

Fifteen questions. Lectures closed. Aim for 12/15 before calling the course complete. Mix of multiple-choice and short "what does this do?" — the answer key explains the *why*, not just the letter.

---

**Q1.** When you record a macro and choose to store it in the **Personal Macro Workbook**, where does it end up?

- A) Inside the current workbook only
- B) A hidden file (`PERSONAL.XLSB`) available in every workbook you open on that computer
- C) A cloud file synced to your Microsoft account across all devices
- D) Nowhere — recording always requires choosing "This Workbook"

<details>
<summary>Answer</summary>

**B** — the Personal Macro Workbook is a hidden file, local to that computer, available across every workbook opened there — it does not travel with a file you share or email.

</details>

---

**Q2.** What is the main problem with recorded VBA that repeatedly does `Range("A1").Select` followed by `Selection.Font.Bold = True`?

- A) It's syntactically invalid
- B) It's unnecessarily indirect, and it clobbers whatever the user previously had selected
- C) `Selection` doesn't exist in VBA
- D) It only works on the first sheet in the workbook

<details>
<summary>Answer</summary>

**B** — selecting first and acting on `Selection` second is indirect and, worse, overwrites the user's previous selection; acting on the `Range` object directly avoids both problems.

</details>

---

**Q3.** What does `Cells(ws.Rows.Count, "A").End(xlUp).Row` compute?

- A) The row number of the very first cell in column A
- B) The total number of rows in the worksheet
- C) The last row in column A that actually contains data
- D) A random row for testing

<details>
<summary>Answer</summary>

**C** — it starts at the very bottom of the sheet and simulates `Ctrl+Up`, landing on the last row in column A that actually has data — immune to a hardcoded row number going stale.

</details>

---

**Q4.** In VBA, what does `On Error GoTo ErrHandler` do?

- A) Stops the macro immediately on any error, with no message
- B) Jumps execution to the `ErrHandler:` label if a runtime error occurs on a later line
- C) Prevents all errors from ever occurring
- D) Only works inside loops

<details>
<summary>Answer</summary>

**B** — it redirects execution to the labeled line the moment a runtime error occurs on any subsequent line, rather than crashing.

</details>

---

**Q5.** Why must `Exit Sub` appear immediately before an `ErrHandler:` label in a `Sub` using `On Error GoTo`?

- A) It's not required — purely stylistic
- B) Without it, the success path falls through into the error-handling code even when nothing went wrong
- C) `Exit Sub` is required syntax after every `On Error` statement
- D) It stops the macro from being recorded again

<details>
<summary>Answer</summary>

**B** — without `Exit Sub`, code that completes successfully would fall straight through into the error-handling block anyway, showing a "failure" message even when nothing failed.

</details>

---

**Q6.** A workbook containing VBA macros is saved with the default `.xlsx` extension. What happens?

- A) The macros are preserved but disabled by default
- B) Excel refuses to save at all
- C) The macros are silently discarded
- D) Nothing — `.xlsx` supports macros identically to `.xlsm`

<details>
<summary>Answer</summary>

**C** — `.xlsx` cannot store VBA; Excel discards the macros silently on save (you may get a warning dialog, but the macros are gone if you proceed). Always save macro-containing workbooks as `.xlsm`.

</details>

---

**Q7.** In Apps Script, what kind of trigger is `onOpen()`?

- A) An installable trigger that must be registered manually via `ScriptApp.newTrigger`
- B) A simple trigger — Google calls it automatically by its reserved name, with limited authorization
- C) A time-driven trigger
- D) Not a real trigger — just a naming convention with no special behavior

<details>
<summary>Answer</summary>

**B** — `onOpen()` is a simple trigger: Google recognizes the reserved function name and calls it automatically, with the tradeoff of limited authorization compared to an installable trigger.

</details>

---

**Q8.** Why can't a time-driven Apps Script trigger's error handler call `SpreadsheetApp.getUi().alert(...)`?

- A) `getUi()` doesn't exist in Apps Script
- B) Alerts are disabled globally for all triggers
- C) There is no user interface present when a trigger fires unattended, so `getUi()` throws its own error
- D) `alert()` requires a paid Google Workspace account

<details>
<summary>Answer</summary>

**C** — a time-driven trigger fires with nobody watching; there's no UI context for `getUi()` to attach to, so calling it throws its own error inside the error handler.

</details>

---

**Q9.** What is the main performance problem with calling `sheet.getRange(r, 1).getValue()` inside a 500-iteration loop, instead of one `getValues()` call covering the whole range?

- A) `getValue()` doesn't exist — it would throw an error every time
- B) Each call is a separate round-trip to Google's servers, making the loop far slower than one batched read
- C) It works identically in performance; the loop version is just harder to read
- D) `getValue()` only works on the first row

<details>
<summary>Answer</summary>

**B** — every `getValue()`/`getRange()` call is a network round-trip to Google's servers; batching into one `getValues()`/`setValues()` call collapses hundreds of round-trips into one or two.

</details>

---

**Q10.** What is the practical difference between a *simple* trigger and an *installable* trigger in Apps Script?

- A) There is no difference — the terms are interchangeable
- B) Simple triggers can only be edit-based; installable triggers can only be time-based
- C) Simple triggers (like `onOpen`, `onEdit`) run automatically with no setup but limited authorization; installable triggers must be registered explicitly and can do more (e.g., run fully unattended, send email)
- D) Installable triggers only work on paid Google accounts

<details>
<summary>Answer</summary>

**C** — simple triggers need zero setup but run with limited authorization; installable triggers require explicit registration (`ScriptApp.newTrigger` or the Triggers UI) but can do more, including running fully unattended.

</details>

---

**Q11.** Which statement about VBA versus Apps Script execution is correct?

- A) Both run entirely on the user's local machine
- B) VBA runs locally inside Excel and requires the workbook to be open; Apps Script runs on Google's servers and can run whether or not the Sheet is open
- C) Apps Script requires a desktop application to be running at all times, just like VBA
- D) VBA can run unattended on a schedule with no external scheduler needed

<details>
<summary>Answer</summary>

**B** — this is the core execution-model difference: VBA lives inside a running Excel process on one machine; Apps Script runs server-side and doesn't need any device to have the file open.

</details>

---

**Q12.** In the capstone's refresh chain, why must `Application.CalculateUntilAsyncQueriesDone` (or an equivalent wait) come immediately after `wb.RefreshAll` when Power Query is involved?

- A) It isn't necessary — `RefreshAll` always blocks until every query fully completes
- B) Power Query refreshes asynchronously by default, so the next line of VBA can run before the query has actually returned data unless you explicitly wait
- C) It only matters for workbooks with more than 10 sheets
- D) `RefreshAll` doesn't affect Power Query connections at all

<details>
<summary>Answer</summary>

**B** — Power Query's refresh is asynchronous; without an explicit wait, VBA proceeds to the next line before the data has actually arrived, so later steps (pivot refresh, formatting) can run against stale data.

</details>

---

**Q13.** Why is a "single entry point" (one button/menu item that calls a chain of private helper routines) considered better design than five separate buttons for five separate steps?

- A) VBA and Apps Script technically don't allow more than one button per sheet
- B) It guarantees the steps always run in the correct order and prevents the user from forgetting a step or running them out of sequence
- C) It's not actually better — more buttons give the user more control
- D) Five buttons would exceed Excel's macro limit

<details>
<summary>Answer</summary>

**B** — a single entry point enforces correct ordering and removes the chance of a user running steps out of sequence or skipping one — exactly the bug pattern described in lecture 03 §1.

</details>

---

**Q14.** A scheduled Apps Script trigger's function throws an error, and the `catch` block does nothing but swallow it silently (`catch (err) {}`). What's the practical consequence?

- A) None — silently catching an error is always the safest option
- B) The dashboard will appear to have refreshed (no visible error) while actually still showing stale data, with no record of what went wrong
- C) Apps Script automatically emails the developer regardless of what the catch block does
- D) The trigger will automatically retry until it succeeds

<details>
<summary>Answer</summary>

**B** — the dashboard looks "successfully refreshed" from the outside (no crash, no visible error) while actually showing outdated data, and there's no log or notification pointing anyone toward the real problem.

</details>

---

**Q15.** What does it mean for a refresh macro/function to be **idempotent**, and why does the mini-project require it?

- A) It means the macro runs faster each time it's called
- B) It means running it multiple times in a row produces the same correct result as running it once — no duplicate rows, no compounding formatting, no drifting state
- C) It means the macro can only be run once per session
- D) It means the macro requires no error handling

<details>
<summary>Answer</summary>

**B** — idempotency means repeated runs stay correct; without it, clicking Refresh twice by habit (very common in practice) could double-flag rows, re-append duplicate data, or otherwise corrupt state, which is unacceptable in something meant to run unattended or be clicked casually.

</details>

**Scoring:** 12+ → you've completed C41 Crunch Excel. 9–11 → revisit the lecture sections behind your misses before calling the mini-project final. <9 → re-read all three lectures and redo Exercise 3 before submitting the mini-project; the capstone leans hard on these ideas.

---
