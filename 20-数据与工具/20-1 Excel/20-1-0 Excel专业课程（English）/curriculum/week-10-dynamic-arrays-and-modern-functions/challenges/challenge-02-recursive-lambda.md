# Challenge 2 — Solve It With a Recursive LAMBDA

**Time:** ~90 minutes. **Difficulty:** Hard. **Ties back to Week 9.**

## The scenario

Back in Week 9, you built a full amortization schedule for a $250,000 equipment loan — 60 monthly rows, each computed with `PMT`/`IPMT`/`PPMT`, one row per period. That's the right tool when you need to *see* every period. But sometimes a stakeholder asks a narrower question: **"What will the balance be after exactly 24 payments?"** — and doesn't want a 60-row schedule to get one number.

This is a genuinely recursive problem. The balance after period `n` depends on the balance after period `n-1` — there's no way to compute it directly from the loan's original terms alone without either (a) building the whole schedule, or (b) using the closed-form future-value-of-an-annuity formula (which exists, but isn't the point of this challenge — you're here to practice recursion). Your job: solve it with a **recursive `LAMBDA`** that computes the balance after `n` payments, with no helper schedule anywhere.

## The math

Each period, the loan balance grows by one month's interest, then shrinks by the fixed payment:

```
balance(0) = original principal
balance(k) = balance(k-1) × (1 + monthly_rate) − payment
```

That's the recursive definition: a base case (`balance(0)` is just the principal — no computation needed) and a recursive case (every other period depends on the period before it).

## Requirements

1. Write and register a recursive `LAMBDA` named `LOANBALANCE` with four parameters: `principal`, `rate` (the *periodic*, i.e. monthly, rate — not annual), `pmt` (the fixed payment amount, as a positive number), and `n` (how many payments have been made). It should implement exactly the recursive definition above.
2. Using `PMT` (Week 9), compute the correct monthly payment for a **$250,000 loan, 6% annual rate, 60-month term**. Feed that payment into `LOANBALANCE` as the `pmt` argument.
3. Compute and report the balance after **12 payments**, after **24 payments**, and after **60 payments** (all 60 — the loan should be fully paid off).
4. **Cross-check** your `n = 60` answer: it should be at or extremely close to `0` (a few cents off due to rounding is fine; more than a dollar off means a bug). Cross-check `n = 12` and `n = 24` against a real amortization schedule if you still have one from Week 9, or build a quick one now purely to verify — then delete the verification schedule; it isn't part of the deliverable.

## Expected results (to the nearest cent)

Using `PMT` on a $250,000 loan at 6% annual (0.5% monthly) for 60 months, the payment is **$4,833.20**. With that payment:

| `n` (payments made) | Balance |
|---:|---:|
| 12 | ≈ $205,799.21 |
| 24 | ≈ $158,872.21 |
| 60 | ≈ $0.00 |

If your numbers are off by more than a few cents, check two things first: is your `rate` argument the **monthly** rate (annual ÷ 12), not the annual rate? And is your base case triggering at exactly `n = 0`, not `n = 1`?

## Constraints

- `LOANBALANCE` must genuinely call **itself** — a non-recursive version that just computes the closed-form annuity balance formula directly does not satisfy this challenge, even if it produces the right number.
- No helper schedule, no dragged-down rows, no `SCAN`. The whole computation lives inside the one recursive `LAMBDA`.
- Handle `n = 0` correctly as a pure base case — no arithmetic, just return `principal` directly.

## Hints

<details>
<summary>On the base case</summary>

Every recursive `LAMBDA` needs an `IF` whose condition is checkable in one step and whose "true" branch does **no** recursive call: `IF(n = 0, principal, <recursive case>)`. Get this backwards (recursing when `n = 0` too) and you get infinite recursion.

</details>

<details>
<summary>On feeding in a computed PMT</summary>

`PMT` in Excel/Sheets returns a **negative** number (money going out — Week 9, Lecture 1). `LOANBALANCE`'s recursive definition above expects `pmt` as a **positive** amount being subtracted. Either wrap your `PMT` call in `-PMT(...)` when you pass it in, or flip the sign inside `LOANBALANCE` itself — just be consistent and say in your write-up which you chose.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|---------------|
| Genuine recursion | Closed-form formula, no self-call | `LOANBALANCE` calls itself, base case at `n=0` |
| Correctness | `n=60` balance is far from zero | `n=60` balance is within a few cents of $0.00 |
| Rate handling | Annual rate used directly | Monthly rate correctly derived and passed in |
| Verification | No cross-check shown | `n=12`/`n=24` verified against an independent method |

## Stretch

- Generalize `LOANBALANCE` to also accept an **extra principal payment** made every period (a common real-world scenario — paying $200 extra each month) as a fifth parameter, and recompute how many fewer payments it takes to reach a $0 balance.
- Write a second recursive `LAMBDA`, `PAYOFFPERIOD`, that — instead of taking `n` and returning a balance — takes a **target balance** (e.g., `0`) and recurses until it finds the smallest `n` where `LOANBALANCE(...) <= target`, returning that `n`.

## Submission

Commit `challenge-02.md` (your `LOANBALANCE` definition as text, your three reported balances, and your verification note) to your portfolio under `c41-week-10/challenge-02/`.
