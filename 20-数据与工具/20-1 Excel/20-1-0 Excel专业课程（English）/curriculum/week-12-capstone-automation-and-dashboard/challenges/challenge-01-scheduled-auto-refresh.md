# Challenge 1 — Schedule an Automatic Refresh

**Time:** ~60–75 minutes. **Difficulty:** Medium–Hard.

## The scenario

Crunch Outfitters' sales exports land in a shared folder every night around midnight. Right now, someone has to remember to open the dashboard and click "Refresh" every morning — and on the mornings they forget, the dashboard silently shows stale data with no warning. Your job: make the refresh happen **on its own**, with no human required to click anything, and make sure a failure is *visible* rather than silent.

## Your task

Pick a platform and implement true scheduled automation.

### Track A — Google Sheets (recommended; this is Apps Script's actual strength)

1. Take `refreshDashboard()` from Exercise 3 (or your capstone-in-progress version).
2. Register an **installable time-driven trigger** that calls it once a day, in a sensible early-morning window (e.g. 6–7am), using `ScriptApp.newTrigger(...)` in code — not just clicking through the Triggers UI — so the setup is reviewable and reproducible.
3. Since a trigger fires with **no UI present**, your error path cannot call `getUi().alert(...)`. Route failures to something that *will* be seen: at minimum, `console.error(...)` (visible in `Executions` in the Apps Script editor); for a real "someone gets notified" signal, also write the failure into a dedicated `Automation_Log` sheet with a timestamp and the error message, appending a new row each time (don't overwrite — you want history).
4. Write a second function, `checkLastRefresh()`, that a human can run manually (or that runs on `onOpen()`) to compare `Dashboard!B2`'s timestamp against `new Date()` and show a warning if it's more than 26 hours old — a safety net in case the trigger itself silently stopped firing (which does happen — Google disables triggers that error repeatedly).

### Track B — Excel (the honest alternative)

VBA cannot wake a *closed* workbook on a schedule by itself — there's no VBA-only equivalent of an installable time-driven trigger. Two legitimate approaches, pick one:

1. **`Workbook_Open` + Windows Task Scheduler.** Write a `Private Sub Workbook_Open()` event handler (in the `ThisWorkbook` object in the VBA editor, not a regular module) that calls `RefreshDashboard` automatically whenever the file is opened. Then create a Windows Task Scheduler task that opens the `.xlsm` file itself every morning at a fixed time (`Actions → Start a program → excel.exe → Add arguments: "C:\path\Crunch-Outfitters-Dashboard.xlsm"`). Document the exact Task Scheduler settings you'd use (trigger time, "run whether user is logged on or not," etc.) even if you can't fully test unattended execution in this environment.
2. **`Application.OnTime`.** If the workbook is expected to stay open on a machine all day, `Application.OnTime` can schedule a macro to run at a specific time *while Excel is running* — write a `Sub ScheduleNextRefresh()` that calls `Application.OnTime TimeValue("06:00:00"), "RefreshDashboard"`, and have `RefreshDashboard` re-schedule itself for the next day at its end. Explain in your write-up why this only works while Excel stays open, and what happens if someone closes it.

## Constraints

- The refresh function itself must be the **exact same function** used by the manual button/menu item from Exercise 3 — don't fork a separate "scheduled version." One code path, two triggers (manual + scheduled).
- A failure during the scheduled run must leave **evidence** someone will actually find — a log row, a console entry, a changed cell — not just a silently caught exception.
- Document, in a short `write-up.md`, exactly what triggers your automation (the trigger type/time, or the Task Scheduler config) and how you verified it actually ran unattended (or, if full unattended verification isn't possible in your environment, what you'd check to confirm it in production).

## Hints

<details>
<summary>On Apps Script's "disabled after repeated failures" behavior</summary>

Google automatically disables an installable trigger after it errors on several consecutive runs, and emails the script owner about it. This is a real, important fact about the platform — it means Track A's `checkLastRefresh()` safety net isn't paranoia, it's covering a documented failure mode.

</details>

<details>
<summary>On why Track B can't fully replicate Track A</summary>

VBA macros only run inside an open instance of Excel. A time-driven Apps Script trigger runs on Google's servers regardless of whether any device has the Sheet open. This is the concrete version of the VBA-vs-Apps-Script table from lecture 02 — Track B's workaround is real and used in production environments, but it depends on an external scheduler (the OS, not Excel) doing the "wake up" part.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Single code path | Separate "scheduled" and "manual" versions of the refresh logic | One function, called from both a manual trigger and a scheduled one |
| Failure visibility | Errors caught and silently discarded | Errors logged somewhere a human will actually look, with enough detail to diagnose |
| Realism | Assumes the trigger always fires | Accounts for triggers/tasks silently failing (Apps Script's auto-disable, Task Scheduler misconfiguration) with a safety net |
| Documentation | "I set up a trigger" | Exact trigger type, time, and how you'd verify it ran in production |

## Submission

Commit your trigger-setup code (or Task Scheduler screenshot/config), the updated `Code.gs`/module, and `write-up.md` to your portfolio under `c41-week-12/challenge-01/`.
