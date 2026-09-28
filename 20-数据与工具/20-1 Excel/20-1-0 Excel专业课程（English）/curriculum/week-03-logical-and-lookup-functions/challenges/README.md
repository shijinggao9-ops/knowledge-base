# Week 3 — Challenges

Two open-ended problems. Unlike the exercises, these have **no single "correct" cell reference to match** — the skill is judgment: spotting fragility in someone else's formulas, and designing branching logic from a plain-English business rule. Do them after the three exercises.

1. **[Challenge 1 — Replace every VLOOKUP in a model](challenge-01-replace-every-vlookup.md)** — a small workbook full of fragile `VLOOKUP`s; find each one, explain what breaks it, and replace it with `XLOOKUP` or `INDEX`/`MATCH`. *(~1 hour.)*
2. **[Challenge 2 — Build tiered commission logic](challenge-02-tiered-commission-logic.md)** — turn a manager's plain-English commission policy into a correct, maintainable formula, and defend a design choice between `IFS` and a lookup table. *(~1 hour.)*

## How these are judged

There's no answer key with exact formulas to match. Instead, each challenge tells you what a *strong* submission looks like. You're being judged on:

- **Correctness** — does the formula actually produce the right number for every test case, including the edge cases?
- **Fragility awareness** — can you name, specifically, what would break the old approach (a column insert, a re-sort, a boundary value) and explain why your replacement survives it?
- **Readability** — would another person be able to read your formula and understand the business rule it encodes, without you standing over their shoulder?
- **Explicit assumptions** — where the plain-English rule is ambiguous (inclusive vs. exclusive boundary, what happens exactly at a tier edge), did you state the interpretation you chose?

Keep your work in `challenge-01.md` / `challenge-02.md` with your formulas **and** your written reasoning. The reasoning is the point — a correct formula with no explanation of *why* it's correct is an incomplete answer.
