# Week 11 — Challenges

Two open-ended problems. Unlike the exercises, these ask you to build a pipeline and then **prove it survives change** — a new file, a live web page — rather than follow a fixed recipe against static data. Do them after the three exercises.

1. **[Challenge 1 — Combine a folder of files](challenge-01-folder-of-files-pipeline.md)** — build a single `From Folder` query that combines all three warehouse exports automatically, then prove it by adding a fourth warehouse file and refreshing, no query edits. *(~1.5 hours.)*
2. **[Challenge 2 — Build a refreshable web import](challenge-02-refreshable-web-import.md)** — pull a real table from a live web page into Power Query, clean it, and demonstrate that clicking Refresh re-pulls current data from the page. *(~1.5 hours.)*

## How these are judged

Neither challenge has a single fixed numeric answer key — Challenge 1's growth test depends on data you invent for the fourth warehouse, and Challenge 2 pulls from a live page whose exact numbers change over time. Instead, each challenge tells you what a *strong* submission looks like. You're being graded on:

- **Correctness of the refresh test** — did you actually add a new file (Challenge 1) or actually click Refresh against the live page (Challenge 2) and confirm the result updated, rather than just asserting it would?
- **Step hygiene** — a query whose Applied Steps are named sensibly and would make sense to someone who didn't build it, not a pile of `Changed Type3`/`Custom1` steps.
- **Honest documentation of what broke** — if a step failed on the new file or the page's structure didn't match what you expected, name specifically what happened and how you fixed it. A found-and-fixed problem is worth more than a pipeline that happened to work by luck.

Keep your work in the workbook itself plus a short `challenge-01.md` / `challenge-02.md` with your notes and refresh-test log.
