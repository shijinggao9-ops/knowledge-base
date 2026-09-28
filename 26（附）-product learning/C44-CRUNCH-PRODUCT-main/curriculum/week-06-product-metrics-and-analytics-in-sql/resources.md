# Week 6 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first

This week's SQL leans harder on window functions and date arithmetic than any prior week, and PostgreSQL becomes the course's primary engine from here on.

- **PostgreSQL 16+** — install now if you haven't already: <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer. Verify with `psql --version`.
- **SQLite 3.35+** (window-function support requires 3.25+; 3.35+ recommended) — the zero-setup fallback engine, ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- **Python 3.10+ with pandas** — used for the DAU/WAU/MAU cross-check in Lecture 3 and Exercise 3: `pip install pandas` — <https://pandas.pydata.org/docs/getting_started/install.html>. `sqlite3` ships with Python's standard library; for PostgreSQL from Python, `pip install psycopg2-binary`.
- **A plain Markdown editor** — anything works (VS Code, Obsidian, even a plain text editor). Written deliverables this week are all Markdown files in your portfolio.

## Required reading (this week's core)

- **Amplitude, "North Star Playbook":** <https://amplitude.com/north-star>
  *Why: the canonical modern treatment of choosing and defending a North Star Metric — read before Lecture 1.*
- **Reforge, "Growth Accounting" (New/Retained/Resurrected/Churned):** <https://www.reforge.com/blog/retention-metrics>
  *Why: the exact decomposition this week's metric tree and retention cohort work are built on — read before Lecture 1 §5 and Lecture 3.*
- **PostgreSQL, "Window Functions" (tutorial):** <https://www.postgresql.org/docs/current/tutorial-window.html>
  *Why: the funnel and cohort queries in Lecture 2 and 3 depend on `MIN() OVER`, `ROW_NUMBER()`, and `PARTITION BY` — this is the primary-source explanation.*
- **Mixpanel, "Stickiness" (DAU/MAU):** <https://mixpanel.com/blog/stickiness/>
  *Why: the standard practitioner definition and benchmark ranges for the metric Lecture 3 §5 computes — read before that section.*

## Reference (keep in tabs)

- **PostgreSQL — Date/Time Functions and Operators:** <https://www.postgresql.org/docs/current/functions-datetime.html>
  *Why: `date_trunc`, `EXTRACT(EPOCH FROM ...)`, and `INTERVAL` arithmetic show up in nearly every query this week.*
- **SQLite — Date and Time Functions:** <https://www.sqlite.org/lang_datefunc.html>
  *Why: `julianday()`, `strftime()`, and the `'weekday N'` / `'-N days'` modifiers are SQLite's equivalents for the same date math.*
- **PostgreSQL — Aggregate Expressions (`FILTER`):** <https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-AGGREGATES>
  *Why: `FILTER (WHERE ...)` is the clean Postgres syntax for conditional aggregates used throughout Lecture 2's funnel queries.*
- **SQLite — Window Functions:** <https://www.sqlite.org/windowfunctions.html>
  *Why: confirms exactly which window-function syntax SQLite supports (and where it differs from Postgres, e.g. no `FILTER`).*
- **Amplitude, "How to Build a Funnel Analysis":** <https://amplitude.com/blog/product-funnel-analysis>
  *Why: a practitioner's framing of funnel analysis, complementary to Lecture 2's SQL-first approach.*
- **Reforge, "Activation Rate":** <https://www.reforge.com/blog/activation-metrics-that-matter> (also see Amplitude's overview: <https://amplitude.com/blog/activation-rate>)
  *Why: how real growth teams find and validate an activation moment — the process Lecture 3 §4 walks through on Loopline's seed data.*

## Practice beyond this week's exercises

- **PostgreSQL Exercises — window functions section:** <https://pgexercises.com/questions/window/>
  *Why: free, browser-based drills on exactly the window-function patterns this week uses, against a different dataset — good for building speed.*
- **Mode Analytics SQL Tutorial — window functions:** <https://mode.com/sql-tutorial/sql-window-functions/>
  *Why: a second explanation of `PARTITION BY`/`OVER`, useful if Lecture 2's treatment didn't fully click on the first pass.*
- **A real product's public events/analytics blog post** (search "[company] events schema" or "[company] North Star metric") — most growth-stage companies (Airbnb, Spotify, Duolingo, Notion) have published at least one engineering or growth blog post describing their real events pipeline or NSM choice.
  *Why: seeing a real, messier version of this week's schema and metric tree is the fastest way to confirm the toy version actually generalizes.*

## Deeper background (optional this week)

- **Sean Ellis & Morgan Brown, "Hacking Growth"** (book) — the growth-accounting and North Star framing's most cited popular-press treatment.
  *Why: broader context for the metric-tree thinking in Lecture 1, beyond the SQL mechanics.*
- **Cindy Alvarez, "Lean Customer Development"** (book) — connects activation-moment thinking back to the discovery work from Weeks 2–3.
  *Why: ties this week's quantitative activation analysis to the qualitative research skills earlier in the course.*

## Glossary

| Term | Definition |
|------|------------|
| **North Star Metric (NSM)** | The single metric a team treats as the clearest proxy for delivered customer value and long-term business health. |
| **Metric tree (driver tree)** | A decomposition of the NSM into the input metrics that add or multiply together to explain it. |
| **Vanity metric** | A metric that goes up almost regardless of what you do, and is not actionable when it moves. |
| **Gameable metric** | A metric that can be increased through a change a reasonable person would call a regression — needs a paired guardrail metric. |
| **Events table** | A single wide table logging every user action as a row: user, event name, timestamp, and context — the standard shape for product analytics data. |
| **Funnel** | An ordered sequence of steps a user progresses through, measured as the distinct-user count (and conversion rate) reaching each step. |
| **Window function** | A SQL function computed across a set of rows related to the current row (`OVER (PARTITION BY ... ORDER BY ...)`), without collapsing the row count the way `GROUP BY` does. |
| **Cohort** | A group of users who share a defining starting event (typically the same signup week), tracked together over time. |
| **Right-censoring** | When a data point (e.g. a cohort's week-4 retention) can't yet be fully observed because not enough time has passed as of the report date. |
| **Activation** | The specific, evidence-backed early action (or threshold of actions) that meaningfully predicts a new user will stick around. |
| **DAU / WAU / MAU** | Daily / Weekly / Monthly Active Users — distinct users with a qualifying event in a trailing 1-, 7-, or 30-day window. |
| **Stickiness (DAU/MAU)** | The ratio of daily to monthly active users — a proxy for how habitual, versus occasional, product usage is. |
| **Growth accounting** | The identity `Active (this period) = New + Retained + Resurrected − Churned`, used to explain *why* an active-user metric moved. |

---

*Broken link? Open an issue or PR.*
