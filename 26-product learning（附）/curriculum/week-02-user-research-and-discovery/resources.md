# Week 2 — Resources

Free and public unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first (if you haven't already)

- **PostgreSQL 16+** — the course's primary engine: <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **SQLite 3.35+** — the zero-setup fallback; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- **A plain text/Markdown editor** — for interview scripts, screeners, and the findings brief. Nothing fancy needed; VS Code, or even a plain `.md` file, is fine.
- **A note-taking method you can use live** — a laptop with a Markdown file open, or pen and paper you'll transcribe same-day. Don't try to build a fancy notes app for this week; the format in Lecture 2 is deliberately low-tech.

## Required reading (this week's core)

- **Rob Fitzpatrick — *The Mom Test* (free sample + full framing):** <http://momtestbook.com/>
  *Why: the single most influential short framework for non-leading interviews in the product world. Read at least the free sample before Lecture 2's exercises.*
- **Nielsen Norman Group — "Generative vs. Evaluative Research":** <https://www.nngroup.com/articles/generative-research-evaluative-research/>
  *Why: the clearest short explanation of the split Lecture 1 is built around.*
- **Nielsen Norman Group — "User Interviews: How, When, and Why to Conduct Them":** <https://www.nngroup.com/articles/user-interviews/>
  *Why: practical mechanics — recruiting, structure, note-taking — that pair directly with Lecture 2.*
- **Nielsen Norman Group — "10 Tips for Creating Good Survey Questions":** <https://www.nngroup.com/articles/survey-tips/>
  *Why: the exact bias patterns Lecture 3's checklist is drawn from, with more examples.*
- **Nielsen Norman Group — "Affinity Diagramming: Collaboratively Sort UX Findings and Design Ideas":** <https://www.nngroup.com/articles/affinity-diagram/>
  *Why: the traditional sticky-note version of the SQL-based synthesis you did in Lecture 3 and Exercise 3 — useful to see the physical-world original.*

## Reference (keep in tabs)

- **Nielsen Norman Group — "Which UX Research Methods":** <https://www.nngroup.com/articles/which-ux-research-methods/>
  *Why: the fuller method matrix behind Lecture 1's table — bookmark for later weeks (usability testing returns in Week 8, A/B testing gets its own week in Week 7).*
- **Nielsen Norman Group — "Avoid Leading Questions in Usability Testing and User Research":** <https://www.nngroup.com/articles/leading-questions/>
  *Why: more worked examples of leading questions across both interviews and usability tests.*
- **PostgreSQL — Aggregate Functions:** <https://www.postgresql.org/docs/current/functions-aggregate.html>
  *Why: `COUNT`, `COUNT(DISTINCT ...)`, and `AVG` are the whole synthesis toolkit this week — this is the exact reference.*
- **PostgreSQL — `CASE` Expressions:** <https://www.postgresql.org/docs/current/functions-conditional.html>
  *Why: for bucketing Likert scales into readable bands, as in Lecture 3 and Exercise 2.*
- **PostgreSQL — Boolean and `NULL` handling in `WHERE`:** <https://www.postgresql.org/docs/current/functions-comparison.html>
  *Why: revisit if Q10/Q11 on the quiz felt shaky — the `NULL`-as-"not applicable" pattern from `would_pay` recurs constantly in real research data.*

## Screener and survey tooling (optional, free tiers exist)

- **Google Forms** — free, sufficient for a small class survey: <https://forms.google.com/>. Export responses as CSV, then load the CSV into your SQL table with your engine's import tool rather than analyzing the spreadsheet directly — the data still belongs in SQL once collected, per this course's data tooling rule.
- **Calendly (or any free scheduler)** — for booking interview slots without an email back-and-forth: <https://calendly.com/>. Not required; a shared doc works too.

## Ethics note (read once, applies every week you do research)

- Always get explicit consent before recording an interview, and offer notes-only as a fallback.
- Anonymize participant data as you transcribe — labels like `P1`, not names — as required in this week's mini-project.
- If an incentive is involved, disclose it upfront; don't spring it as a surprise after the interview.

## Glossary

| Term | Definition |
|------|------------|
| **Generative research** | Exploratory research that surfaces problems and needs before a solution exists. |
| **Evaluative research** | Research that tests a specific existing solution (prototype or shipped feature). |
| **The Mom Test** | A discipline for interview questions: ask about specific past behavior, not opinions or hypotheticals, so even a biased participant gives useful data. |
| **Leading question** | A question phrased to nudge the participant toward a particular answer. |
| **Double-barreled question** | A single question that actually asks two things at once, making the answer uninterpretable. |
| **Workaround** | An ad hoc fix a user has built themselves — strong behavioral evidence of an unmet need. |
| **Affinity mapping** | Clustering individual observations (quotes, feedback) into named themes based on what they're really about. |
| **Theme** | A short label describing what a group of related observations is about. |
| **Finding** | A specific, evidence-backed statement of a validated need — not a solution recommendation. |
| **Validated need** | A need supported by multiple independent participants and, ideally, more than one research method. |
| **Screener** | A short set of questions used to decide who qualifies for a study, run before recruiting proceeds. |
| **Convergence** | When two independent research methods (e.g., interviews and a survey) point at the same underlying finding. |

---

*Broken link? Open an issue or PR.*
