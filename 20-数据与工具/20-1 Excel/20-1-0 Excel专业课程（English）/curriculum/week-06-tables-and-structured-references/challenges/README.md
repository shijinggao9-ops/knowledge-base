# Week 6 — Challenges

Two open-ended problems. Unlike the exercises, these ask you to design something and then prove it works, rather than follow a fixed recipe. Do them after the three exercises.

1. **[Challenge 1 — Build a self-growing tracker](challenge-01-self-growing-tracker.md)** — design a small expense/budget tracker from scratch where every total, format, and summary formula keeps itself correct no matter how many rows get added later. *(~60 min.)*
2. **[Challenge 2 — Port a Table model to Google Sheets](challenge-02-sheets-vs-excel-tables.md)** — take your `Orders` workbook (or an equivalent) into the *other* app from the one you've been using, rebuild the Table-driven model there, and document exactly where the two apps diverge. *(~60 min.)*

## How these are judged

There's no answer key with fixed numbers for Challenge 1 (you're designing your own dataset) and Challenge 2 is explicitly comparative. Instead, each challenge tells you what a *strong* submission looks like. You're being graded on:

- **Correctness of the growth test** — did you actually add new rows after building the model and prove nothing broke, rather than just asserting it would work?
- **Structured references used deliberately** — no `A2:A25`-style ranges hiding inside a formula that's supposed to demonstrate Table behavior.
- **Honest comparison** — Challenge 2 specifically wants you to name what's *worse* or *missing* in whichever app you moved to, not just what's the same.

Keep your work in the workbook itself plus a short `challenge-01.md` / `challenge-02.md` with your design notes and comparison table. The reasoning is the point.
