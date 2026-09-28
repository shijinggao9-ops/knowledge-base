# Week 12 — Resources

Free, public, no signup unless noted. This week's reading list is deliberately short — you've already read the deep-dive material for every framework this week uses, back in Weeks 1–10. What's here is synthesis-focused: how experienced PMs and companies tell the "zero to one" story end to end, plus a couple of narrow references for the SQL and experiment-design pieces.

## Install first (should already be done from prior weeks)

- **PostgreSQL 16+** or **SQLite 3.35+** — <https://www.postgresql.org/download/> (macOS: [Postgres.app](https://postgresapp.com/)); SQLite ships on macOS/most Linux — check with `sqlite3 --version`.
- **Python 3.10+** with `pandas`:
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  pip install pandas sqlalchemy psycopg2-binary
  ```

## Required reading (this week's core)

- **Marty Cagan (SVPG), "The Right Way to Test a Product Idea":**
  <https://www.svpg.com/the-right-way-to-test-a-new-product-idea/>
  *Why: a widely cited voice in the field on how to validate a zero-to-one idea before over-investing — directly relevant to Exercise 1's evidence discipline.*
- **Y Combinator, "How to Talk to Users":**
  <https://www.ycombinator.com/library/6f-how-to-talk-to-users>
  *Why: practical, primary-source guidance on gathering the kind of specific, real evidence Exercise 1 asks for, from a source that's coached thousands of zero-to-one launches.*
- **Amplitude, "The North Star Playbook" (free, no signup for the core guide):**
  <https://amplitude.com/north-star>
  *Why: the canonical modern treatment of North Star selection and metric trees — the exact judgment call Lecture 2 walks through for AI Task Summaries.*
- **Julie Zhuo, "How to Write a Great PM Resume / Portfolio" (search her public Medium archive for portfolio-specific posts):**
  <https://medium.com/@joulee>
  *Why: a former VP of Product at Meta writing publicly about what makes a product portfolio piece (like this week's mini-project) actually convincing to a hiring panel.*

## Reference (keep in tabs)

- **Reforge / Lenny's Newsletter public archive — search "launch retro" or "product narrative":**
  <https://www.lennysnewsletter.com/>
  *Why: real, named examples of companies presenting a launch's honest, mixed results — the exact genre Lecture 3's worked example belongs to.*
- **First Round Review, "The Right Way to Prioritize" and related PM archive:**
  <https://review.firstround.com/>
  *Why: free, deeply reported essays from operators who've run this exact discover→spec→prioritize→measure→launch loop at real companies — useful for Homework Problem 5's real-product audit.*
- **PostgreSQL — Aggregate Functions and `GROUP BY`:**
  <https://www.postgresql.org/docs/current/tutorial-agg.html>
  *Why: the reference for the `GROUP BY` + `CASE WHEN` patterns used throughout Lecture 2 and Exercise 3.*
- **Evan Miller, "How Not to Run an A/B Test" (classic, still-relevant primer on experiment pitfalls):**
  <https://www.evanmiller.org/how-not-to-run-an-ab-test.html>
  *Why: a sharp, free treatment of the sample-size and peeking pitfalls directly relevant to Challenge 1's experiment plan.*
- **pandas documentation, "Group by: split-apply-combine":**
  <https://pandas.pydata.org/docs/user_guide/groupby.html>
  *Why: for Exercise 3's stretch-goal pandas cross-check.*

## For the mini-project specifically

- **A public example of a real "zero to one" retro or launch postmortem** — search any of the following for "launch retro," "post-launch review," or "what we learned": Basecamp's public blog, Linear's public changelog/blog, or Intercom's blog. Reading even one real company's honest account of a launch's mixed results is the single best model for Section 6 of your mini-project.
  <https://linear.app/blog> · <https://www.intercom.com/blog> · <https://basecamp.com/shapeup>
  *Why: seeing a real company narrate a real, imperfect launch is more useful preparation for Challenge 2 than any hypothetical example.*

## Glossary — full course recap

| Term | Definition |
|------|------------|
| **Five-act product narrative** | This week's framing: Discover → Spec → Prioritize → Measure → Launch & grow, where each act's output is the next act's input. |
| **Orphaned artifact** | Any output (PRD, roadmap item, metric, next bet) that can't be traced back to the artifact that should have produced it. |
| **JTBD (Job to Be Done)** | The functional + emotional + social outcome a user is really hiring a product to accomplish (Weeks 1–2). |
| **RICE** | Reach × Impact × Confidence ÷ Effort — a value-per-effort prioritization score (Week 5). |
| **WSJF** | Weighted Shortest Job First — Cost of Delay ÷ Job Size (Week 5). |
| **Now/Next/Later roadmap** | A roadmap format expressing decreasing certainty instead of specific dates (Week 5). |
| **North Star Metric (NSM)** | The single metric that best proxies durable, sustained product value (Week 6). |
| **Metric tree** | A North Star decomposed into the input metrics that drive it (Week 6). |
| **Trial rate** | Percentage of exposed users who ever engage with a feature at least once — a first-contact metric, not a habit metric. |
| **WASU (Weekly Active Summary Users)** | This week's worked North Star example: distinct users engaging with a specific feature in a given week — a sustained-usage proxy. |
| **Day-0 activation** | Whether a user engages with a feature the same day they're exposed to it — a proxy for how legible the value proposition is on first sight. |
| **Guardrail metric** | A metric that must not meaningfully worsen even if an experiment's primary metric improves (Week 7, referenced in Challenge 1). |
| **Pre-registered decision rule** | A ship/kill/ambiguous rule for an experiment, written down before the result is known (Week 7). |
| **Minimum detectable effect (MDE)** | The smallest change in a metric an experiment is powered to reliably detect — a required input to any honest sample-size estimate. |
| **Coherence audit** | This week's five-point checklist for verifying every artifact in a product story traces to the one before it (Lecture 1, Section 3). |
| **Next-quarter bet** | A forward ask with three required parts: a specific action, a specific metric and threshold, and a specific decision date (Lecture 3, Section 4). |

---

*Broken link? Open an issue or PR. This is the final resources file of C44 · Crunch Product — thank you for building all twelve weeks' worth of product judgment the hard way, one query and one PRD at a time.*
