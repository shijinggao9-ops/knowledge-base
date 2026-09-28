# Challenge 2 — Complete a Task With No Mouse

**Time:** ~30–45 minutes. **Difficulty:** Medium (mentally, not technically). **No single right answer on *how*, but the end state is exactly specified.**

## The rule

For this entire challenge: **no mouse, no trackpad, no touchscreen.** Keyboard only, from the moment you create the sheet to the moment the last format is applied. If you catch yourself reaching for the mouse, put your hand back on the keyboard and find the keyboard path instead — that friction is the entire point of the exercise. (One narrow exception: if your OS genuinely requires a click to focus the browser/app window in the first place, that one click is fine — everything *inside* the sheet is keyboard-only.)

## The task

Build the following, from a blank sheet, entirely by keyboard:

1. **Create a new sheet** using a keyboard shortcut (not the `+` button) — research the shortcut for your app/OS if you don't already know it (hint: it's in [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-01-spreadsheet-foundations-and-navigation/resources.md)). Rename it `Challenge 2` using the keyboard (`F2` in Excel to rename via keyboard once the tab context is right, or tab into rename mode — find the path that works without a click).

2. **Enter this 4×4 block starting at `A1`**, using only `Tab`/`Enter` to move between cells:

   | Q1 | Q2 | Q3 | Q4 |
   |---|---|---|---|
   | 120 | 135 | 142 | 158 |
   | 98 | 110 | 105 | 121 |
   | 76 | 82 | 91 | 88 |

   (Row 1 is the header `Q1, Q2, Q3, Q4`; the three data rows follow — 3 rows × 4 columns of numbers.)

3. **Select the entire block** (`A1:D4`) using a single navigation + selection shortcut combo (Lecture 2, section 3) — not click-and-drag.

4. **Apply bold to the header row only** (`A1:D1`) — select it with a keyboard shortcut (`Shift+Space`-style row selection won't work here since you only want 4 cells, not the whole row; think about the range-select shortcuts from Lecture 2 instead), then apply bold with `Ctrl/Cmd+B`.

5. **Apply Number format with 0 decimals** to the data rows (`A2:D4`) using `Ctrl+1` (Excel) or the Format menu reached via `Alt`/keyboard menu navigation (Sheets), never a toolbar click.

6. **Freeze row 1** using the keyboard-accessible menu path (`Alt` then the ribbon key-tips in Excel; `Alt` then arrow/enter through the View menu in Sheets, or the documented shortcut if one exists in your version).

7. **Add a border under the header row** the same way — menu/dialog navigated by keyboard, not a toolbar icon click.

8. **Save the workbook** with the keyboard shortcut (`Ctrl/Cmd+S` — trivial in Sheets since it autosaves, but do it deliberately in Excel).

## Log your path

For at least steps 1, 4, 6, and 7 — the ones without an obvious single keystroke — write down **exactly** the key sequence you used in a short `challenge-02-log.md`. Example format:

```
Step 1 (new sheet, Excel, Windows): Shift+F11
Step 4 (select A1:D1 from A1): Ctrl+Shift+Right
Step 6 (freeze row 1, Excel): Alt, W, F, R
Step 7 (border under header, Excel): Ctrl+1, then Alt+B, then Down arrow to bottom border, Enter, Enter
```

If a step in your app genuinely has **no** keyboard path (rare, but it happens — some deep dialog options are mouse-only in older versions), note that explicitly rather than silently clicking — that's useful information, not a failure.

## Why this is worth 30–45 minutes of your life

Real spreadsheet work under time pressure — closing a report five minutes before a meeting, cleaning data live on a call — rewards exactly this fluency. The people who look fast in a spreadsheet aren't smarter; they've simply never let their hands default to the mouse for something the keyboard does in one motion. This challenge is designed to be mildly annoying the first time and completely unremarkable the fifth time.

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Compliance | Mouse used for anything beyond initial window focus | Genuinely zero mouse use, or explicitly logged exceptions |
| Completeness | Skipped a step that seemed "too hard" without the mouse | All 8 steps completed or explicitly logged as keyboard-inaccessible |
| Documentation | No log, or vague description ("used menus") | Exact key sequences logged for steps 1, 4, 6, 7 |
| End state | Formatting doesn't match the spec | Bold header, 0-decimal data, frozen row 1, bottom border — all present |

## Submission

Keep the `Challenge 2` sheet plus `challenge-02-log.md` in your workbook/portfolio.
