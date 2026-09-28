# Week 9 Resources

Curated, mostly-official reading and the tools you need installed. You do not need to read everything here to pass the week — the lectures are self-contained. Use this as a reference when you want the primary source behind a concept, or when the mini-project pushes you past what the lectures covered.

## Install first

- **PostgreSQL 16+** — <https://www.postgresql.org/download/> — the course's primary database engine.
- **SQLite 3.35+** — <https://www.sqlite.org/download.html> — zero-setup fallback; everything this week runs unchanged on either engine except where a lecture notes an engine-specific function (e.g., `julianday()` vs. `EXTRACT(EPOCH FROM ...)`).
- **Python 3.10+ with pandas** — for the mini-project's dashboard work:
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  pip install pandas sqlalchemy psycopg2-binary
  ```
- A terminal SQL client — `psql` (ships with PostgreSQL) or `sqlite3` (ships with SQLite on macOS/Linux).

## Positioning and messaging

- **April Dunford — product positioning framework overview:** <https://www.aprildunford.com/what-is-product-positioning> — the "Obviously Awesome" method this week's template is compatible with; the clearest modern treatment of positioning as a decision, not a tagline exercise.
- **Atlassian — how to write a positioning statement:** <https://www.atlassian.com/agile/product-management/positioning-statement>
- **Segment — writing consistent marketing copy across channels:** <https://segment.com/blog/great-marketing-copy/>
- **Product Marketing Alliance — positioning vs. messaging, explained:** <https://www.productmarketingalliance.com/what-is-positioning-vs-messaging/>

## Launch tiers, channels, and coordination

- **LaunchDarkly — what feature flags are and why progressive delivery matters:** <https://launchdarkly.com/blog/what-are-feature-flags/>
- **LaunchDarkly — kill switches specifically:** <https://launchdarkly.com/blog/what-is-a-feature-flag-kill-switch/>
- **Atlassian — building a RACI matrix:** <https://www.atlassian.com/work-management/project-management/raci-chart>
- **Google Cloud Architecture Center — canary releases and phased rollout patterns:** <https://cloud.google.com/architecture/application-deployment-and-testing-strategies>
- **Product Hunt — a practical guide to launching well:** <https://www.producthunt.com/launch-guide>

## Instrumented rollouts, incidents, and postmortems

- **Google SRE Book — Postmortem Culture: Learning from Failure:** <https://sre.google/sre-book/postmortem-culture/> — the canonical reference for blameless postmortems; short, free, and directly applicable outside of infrastructure incidents.
- **Atlassian — incident postmortem template:** <https://www.atlassian.com/incident-management/postmortem>
- **PagerDuty — incident response fundamentals:** <https://response.pagerduty.com/>

## SQL references used this week

- **PostgreSQL — aggregate `FILTER` clause (used for conditional counts):** <https://www.postgresql.org/docs/current/sql-expressions.html#SYNTAX-AGGREGATES>
- **PostgreSQL — date/time functions (`EXTRACT`, interval arithmetic):** <https://www.postgresql.org/docs/current/functions-datetime.html>
- **SQLite — date and time functions (`julianday`, `strftime`):** <https://www.sqlite.org/lang_datefunc.html>
- **PostgreSQL — `LEFT JOIN` and outer joins, "Joins Between Tables":** <https://www.postgresql.org/docs/current/queries-table-expressions.html#QUERIES-JOIN>
- **SQLite — `JOIN` syntax:** <https://www.sqlite.org/syntax/join-clause.html>

## Where this week fits

- Reuses the RICE/Kano-scored backlog from [Week 5 — Prioritization & Roadmapping](../week-05-prioritization-and-roadmapping/) — Guest & External Collaborator Access is Week 5's backlog item 10.
- Builds directly toward [Week 10 — Pricing & Growth](../week-10-pricing-and-growth/), where the question shifts from "did the launch work" to "what is this worth, and how does it compound."
- If SQL joins, `FILTER`/`CASE WHEN`, or date arithmetic feel shaky, [C33 Crunch SQL](../../../C33-CRUNCH-SQL/) covers all of it from first principles — not required for this course, but a strong companion.
