# Week 8 — Challenges

Two problems that push past the exercises. The first is a **constraint** challenge — your dashboard already works; the test is whether it survives a hard, real-world layout limit without losing its usefulness. The second is a **porting** challenge — rebuild the same dashboard on a different platform and document, precisely, everywhere the two tools stop being equivalent.

1. **[Challenge 1 — Fit it all on one screen](challenge-01-single-screen-rule.md)** — take your working dashboard and make it survive a hard, measured single-screen constraint, cutting or resizing whatever doesn't fit. *(~60 min.)*
2. **[Challenge 2 — Rebuild the dashboard in Google Sheets](challenge-02-dashboard-in-sheets.md)** — port the entire dashboard to Sheets and write up every place its slicer, timeline, and formula tooling diverges from Excel's. *(~90-120 min.)*

## How these are judged

Neither challenge has partial credit for "the numbers are right but it's cluttered" or "it's a nice layout but wired wrong" — a dashboard has to be both correct *and* legible to actually do its job. You're being judged on:

- **Correctness under the constraint** — Challenge 1's dashboard still shows correct, live-filtered numbers after you've resized/cut things to fit; a smaller layout that broke a formula reference doesn't pass.
- **Ruthlessness, not just shrinking** — Challenge 1 specifically rewards *choosing what to cut*, following Lecture 1's "few numbers that matter" discipline, over simply shrinking every font until it technically fits but nothing is readable.
- **Accurate, specific documentation** — Challenge 2's write-up needs to name the *exact* feature gap (e.g., "no Report Connections dialog," "no GETPIVOTDATA function") and the specific workaround you used, not a vague "Sheets is a bit different."

Keep your work in the challenge files described inside each challenge, plus the dashboard sheet/workbook itself.
