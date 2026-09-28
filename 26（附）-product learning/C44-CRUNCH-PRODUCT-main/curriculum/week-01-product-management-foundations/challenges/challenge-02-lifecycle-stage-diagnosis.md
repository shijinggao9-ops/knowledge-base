# Challenge 2 — Diagnose a Real Product's Lifecycle Stage

**Time:** ~75–90 minutes. **Difficulty:** Medium–Hard. **No single right answer.**

## The scenario

Lecture 3 gave you a clean, seeded metrics table for Loopline. Real life doesn't hand you that table — you have to build your evidence base out of public, imperfect signals: app store reviews, changelogs, press coverage, job postings, pricing page history. This challenge asks you to do the diagnosis for real, with real uncertainty, and to be honest about which conclusions your evidence actually supports versus which ones you're guessing at.

## Your task

1. **Pick a real product** you can research without needing an insider's dashboard. Good choices: a well-known consumer or B2B app that's been around 3+ years (so it has a visible history) — a note-taking app, a fitness app, a project-management tool, a social platform, a once-hyped app that's now quiet. Avoid a brand-new product (under 18 months old) — there won't be enough public history to diagnose a stage shift.

2. **Gather at least five pieces of public evidence**, from at least **three different source types**. Candidates:
   - App store review trends over time (ratings, and *what* recent reviews complain about vs. praised 2+ years ago)
   - The product's own changelog or release notes (is it shipping new capability, or mostly bug fixes and maintenance?)
   - Pricing page history (via the Wayback Machine) — has pricing gotten more aggressive, added tiers, added enterprise features, or gone quiet?
   - Job postings (are they hiring growth/acquisition roles, or platform/reliability/enterprise-sales roles? What a company is hiring for is a strong tell for what stage it thinks it's in)
   - News coverage or public statements (funding rounds, layoffs, a pivot announcement, an acquisition, a "sunset" notice)
   - Public usage signals (App Annie/Similarweb-style estimates if accessible, or simpler: is the app still getting meaningful update frequency and store ranking movement?)

3. **Write `diagnosis.md`** with:
   - The product name and one sentence on what it does.
   - Your five+ pieces of evidence, each with its source and what it actually shows (quote or paraphrase specifics — "reviews mention slow support" is weaker than "12 of the last 20 reviews, dated within the last 6 months, mention support response time, versus 1 of 20 from two years ago").
   - Your diagnosed lifecycle stage (from Lecture 3's five stages), with the evidence mapped explicitly to your conclusion.
   - One competing interpretation of the same evidence that a skeptic could reasonably raise — and why you still land where you do (or why it changed your mind).
   - The metric you'd want to see, that you *don't* have access to, that would most resolve your remaining uncertainty.

## Constraints

- **Cite your sources with URLs or specific, checkable references** (a Wayback Machine snapshot date, a specific job posting title and date, a specific review excerpt). "I feel like it's declining" is not evidence.
- Every one of your five pieces of evidence must be independently checkable by someone else — a grader (or a future you) should be able to click through and see what you saw.
- Do not pick a product currently in open, well-publicized crisis (a company that just announced shutdown, a massive public scandal) — that makes the diagnosis trivial and skips the actual skill of reading subtler signals.

## Hints

<details>
<summary>On finding pricing history</summary>

The [Wayback Machine](https://web.archive.org/) has snapshots of most public pricing pages going back years. Compare a snapshot from 2–3 years ago to today: did the number of tiers grow (usually a maturity/monetization-expansion signal)? Did an "Enterprise — contact us" tier appear where there wasn't one before (a classic growth → maturity signal, chasing bigger accounts as new-user growth slows)?

</details>

<details>
<summary>On reading job postings as a signal</summary>

A company hiring "Growth PM," "Performance Marketing Manager," or "User Acquisition Lead" roles is signaling it still believes in expanding the top of the funnel — a growth-stage posture. A company hiring "Enterprise Account Executive," "Platform Reliability Engineer," or "Customer Success Manager (Renewals)" roles is signaling a maturity posture — defending and expanding existing revenue rather than chasing new logos. Neither is inherently good or bad; it's a signal of what the company itself believes its stage is.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Evidence quality | Vague impressions, no sources | Five+ specific, checkable, sourced pieces of evidence |
| Source diversity | All evidence from one type (e.g., only reviews) | At least three different source types |
| Diagnosis reasoning | Jumps to a stage with no evidence trail | Each piece of evidence explicitly connects to the diagnosed stage |
| Intellectual honesty | Presents the conclusion as certain | States a real competing interpretation and engages with it seriously |
| Self-awareness | No acknowledgment of limits | Names the specific metric that would most resolve remaining uncertainty |

## Submission

Commit `diagnosis.md` to your portfolio under `c44-week-01/challenge-02/`.
