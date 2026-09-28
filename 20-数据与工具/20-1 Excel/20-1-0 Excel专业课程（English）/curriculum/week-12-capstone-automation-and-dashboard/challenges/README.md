# Week 12 Challenges — Overview

Two challenges. Where the exercises taught you the mechanics, these push you into the two things a truly *unattended* dashboard needs: running without a human present, and delivering its own output somewhere a human will actually see it.

| # | Challenge | Difficulty | ~Time |
|--:|-----------|-----------|------:|
| 1 | [Schedule an Automatic Refresh](challenge-01-scheduled-auto-refresh.md) | Medium–Hard | 60–75 min |
| 2 | [Auto-Export & Email the Dashboard](challenge-02-email-the-dashboard.md) | Medium–Hard | 60–75 min |

## How to work these

- Both challenges build directly on **Exercise 3**'s single-entry-point refresh routine. Have that working before you start.
- Google Sheets is the natural platform for Challenge 1 (true unattended scheduling is Apps Script's strength — see lecture 02, §7). Excel's equivalent requires an external scheduler (Windows Task Scheduler) since VBA alone can't wake up a closed workbook; the Excel path is documented as an alternative in Challenge 1.
- These are open-ended by design — there's more than one correct wiring. Each challenge gives a rubric, not a single expected answer.
- Test failure paths, not just the happy path. An automation that only ever gets tested when everything goes right isn't tested.
