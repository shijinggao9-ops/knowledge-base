# Week 10 — Challenges

Two open-ended problems. Unlike the exercises, these ask you to design a solution and prove it works, rather than follow a fixed recipe. Do them after the three exercises.

1. **[Challenge 1 — Whole Report in One Formula](challenge-01-one-formula-report.md)** — collapse a multi-step, multi-cell report (filter, then sort, then re-label, then rank) into a single spilling `LET` formula, with no helper cells anywhere. *(~90 min.)*
2. **[Challenge 2 — Solve It With a Recursive LAMBDA](challenge-02-recursive-lambda.md)** — build a recursive `LAMBDA` that computes a loan's remaining balance after any number of payments, a problem that genuinely can't be expressed as a single non-recursive formula. *(~90 min.)*

## How these are judged

Neither challenge has one fixed "correct" formula — there's more than one valid way to structure a `LET` chain or a recursive base case. Instead, each challenge tells you what a *strong* submission looks like. You're being graded on:

- **Zero helper cells** — Challenge 1 specifically bans intermediate cells outside the one formula; everything must happen inside `LET`.
- **A correct, minimal base case** — Challenge 2's recursion must terminate correctly and match the non-recursive `PMT`-based answer from Week 9 within a cent.
- **Readable naming** — every `LET`-named value and every `LAMBDA` parameter should read like a sentence, not `x`, `y`, `z`.

Keep your work in the workbook itself plus a short `challenge-01.md` / `challenge-02.md` with your formula (as text, copy-pasted from the formula bar) and a two-sentence explanation of your design choices. The reasoning is the point.
