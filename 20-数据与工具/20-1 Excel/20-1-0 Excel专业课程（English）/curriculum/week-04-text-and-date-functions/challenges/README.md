# Week 4 — Challenges

Two problems that push past the exercises. The first is a genuinely messy real-world parsing problem — addresses that don't share one consistent shape, forcing you to combine multiple text functions and make judgment calls. The second is a construction challenge — build a small fiscal-period calendar system from date functions alone, the kind of thing finance and ops teams rely on constantly.

1. **[Challenge 1 — Parse inconsistent addresses](challenge-01-parse-inconsistent-addresses.md)** — split street, city, state, and ZIP out of addresses that don't all follow the same format. *(~60 min.)*
2. **[Challenge 2 — Build a fiscal-period calendar](challenge-02-build-a-fiscal-calendar.md)** — map any calendar date to its fiscal year, quarter, and period using a fiscal year that doesn't start in January. *(~60 min.)*

## How these are judged

Neither challenge has one single "correct" formula — there are usually two or three reasonable ways to solve each. You're being judged on:

- **Correctness** — every row parses/computes correctly, verified against the spot checks given in each challenge.
- **Robustness** — Challenge 1 specifically rewards formulas that don't silently break the moment a row doesn't match your first assumption about the address shape.
- **Judgment, documented** — both challenges have genuine ambiguous cases; state the decision you made and why, not just the formula.

Keep your work in the challenge files described inside each challenge.
