# Mini-Project — Run 5 User Interviews and Ship a Validated-Findings Brief

> Pick a real problem, talk to 5 real people about it, store every quote and code in SQL, and ship a one-page brief a stakeholder could act on. This is the week's capstone — everything from generative-vs-evaluative through the Mom Test through SQL-backed synthesis, done once, for real, on a problem you chose.

**Estimated time:** 2.5–3 hours of your own work, spread across at least two days — plus the calendar time to actually schedule and run 5 interviews, which will likely take longer than the working time itself. Start recruiting on **Monday**, not Saturday.

This is the shape of real discovery work: a fuzzy hunch, five conversations, and a defensible one-pager that tells your team what's actually true. Do it once, deliberately, and every future round of research you run will be faster and better because the muscle is built.

---

## Step 0 — Pick your research question

Choose **one** of these two paths:

**Path A — Continue the Shiftly scenario.** Interview 5 people (real or, if you genuinely cannot access shift workers, close proxies — see the note below) about a scheduling, coordination, or shift-work problem, generative-style: don't mention any specific feature, just explore how they currently handle covering a shift, requesting time off, or communicating with a manager about availability.

**Path B — Pick your own real problem.** Choose a real product, tool, or process you have access to real users of (a tool at your job, a community you're part of, an app you and 5 friends all use differently) and pick one generative research question about it — something you genuinely don't know the answer to yet, not something you're trying to confirm.

Either way, write your research question as **one sentence**, in `research-question.md`, before you recruit anyone. A vague question ("what do people think of the app?") produces vague interviews. A sharp one ("what do people actually do in the 30 minutes before their team's weekly meeting?") produces a sharp interview.

> **If you truly cannot access 5 real target users:** interview 5 people who plausibly resemble the segment (classmates, coworkers, online community members) and say so explicitly in your brief's limitations section. Interviewing 5 people who aren't your real users and *not* disclosing it is a research integrity problem — interviewing 5 proxies and disclosing it clearly is an honest, useful mini-project.

---

## Step 1 — Recruit and screen

- Write 3–4 screener questions (see Challenge 1 for the pattern) that confirm each candidate is a genuine fit for your research question.
- Recruit at least 5 people who pass your screener. Note how you recruited each one — you'll want the variety (don't take all 5 from one friend group or one channel; that's a sampling bias you can avoid at zero cost).

## Step 2 — Build your interview script

- Write a 5–7 question script using Lecture 2's warm-up / body / wrap-up structure.
- Every body question must ask about a specific past event or observable behavior — run every question through the Mom Test before your first interview. (This is a good moment to reuse Exercise 1's rewriting discipline on your own draft.)
- Do **not** mention any specific solution or feature in your questions. You're still in the problem space.

## Step 3 — Run the 5 interviews

- 20–30 minutes each. Take notes live using the `Q:` / `O:` / `I:` format from Lecture 2.
- Get consent to take notes (and to record, if you do). If a participant is uncomfortable with either, respect that and take notes only.
- Immediately after each interview (same day, not batched at the end of the week), write up your raw notes into clean, verbatim-quote form while the conversation is still fresh — memory degrades fast, and this is the single biggest quality lever in the whole project.

## Step 4 — Store it all in SQL

Set up a project database (reuse the pattern from the week seed, adapted to your own scenario):

```sql
CREATE TABLE mp_participants (
    participant_id  INTEGER PRIMARY KEY,
    label           TEXT NOT NULL,     -- a short non-identifying label, e.g. 'P1', not a real name
    segment         TEXT,              -- if relevant to your question
    recruited_via   TEXT NOT NULL,
    interviewed_on  DATE NOT NULL
);

CREATE TABLE mp_quotes (
    quote_id        INTEGER PRIMARY KEY,
    participant_id  INTEGER NOT NULL REFERENCES mp_participants(participant_id),
    quote_text      TEXT NOT NULL,
    theme           TEXT               -- filled in during Step 5
);
```

- Insert one row per participant (5 rows).
- Insert every distinct, atomic quote worth keeping from your 5 interviews (aim for 5–10 quotes per interview — 25–50 rows total). Use real verbatim language, not paraphrases, exactly as in Exercise 3.
- **Never put participant names or other identifying details in `label` or `quote_text`** — anonymize as you transcribe. This is a real research-ethics practice, not busywork.

## Step 5 — Code and synthesize

- Assign a `theme` to every quote (`UPDATE mp_quotes SET theme = '...' WHERE quote_id = ...`). Let themes emerge from your actual data — don't force-fit a theme you expected before you started.
- Write and run the Lecture 3 ranking query, adapted to your table names:

```sql
SELECT theme,
       COUNT(*)                       AS n_quotes,
       COUNT(DISTINCT participant_id) AS n_participants
FROM mp_quotes
WHERE theme IS NOT NULL
GROUP BY theme
ORDER BY n_participants DESC, n_quotes DESC;
```

- For your top 2–3 themes by `n_participants`, pull every quote behind each and re-read them together — does the theme label still hold for all of them? Adjust if not.

## Step 6 — Write the brief

Produce `findings-brief.md`, **one page maximum** (roughly 400–500 words), containing:

1. **Research question** (your Step 0 sentence) and method (5 interviews, generative, dates run).
2. **Who you talked to** — a one-line summary of your 5 participants (segment/context, not names), and an honest note on any sampling limitation (small N, proxy users, single recruiting channel, etc.).
3. **2–4 validated findings**, each written in the Lecture 3 finding format: the claim, how many participants independently support it, the strongest verbatim quote as evidence, and — critically — what's **not yet validated** (the boundary of what this research can and can't tell you).
4. **One open question** your research raised that you'd want to answer next, and what method (from Lecture 1's menu) you'd use to answer it.

**What this brief must NOT contain:** a recommended feature or solution. This mini-project ends at validated problems, on purpose — Week 3 is where problem framing and opportunity sizing happen. A brief that jumps to "so we should build X" hasn't actually stayed in the discovery lane.

---

## Deliverable

A directory in your portfolio `c44-week-02/mini-project/` containing:

1. `research-question.md` — your one-sentence question and path (A or B).
2. `screener.md` — your 3–4 screening questions and recruiting notes.
3. `interview-script.md` — your 5–7 question script.
4. `seed.sql` — your `CREATE TABLE` and all `INSERT`/`UPDATE` statements for participants and quotes.
5. `synthesis-queries.sql` — the queries you ran to rank and cross-check themes.
6. `findings-brief.md` — the one-page deliverable described in Step 6.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Question quality & Mom Test discipline | 20% | Sharp, non-hypothetical research question; no script question presupposes a solution or a future hypothetical |
| Interview execution | 20% | Verbatim quotes captured, behavior followed over opinion, evident from the raw `mp_quotes` data |
| SQL discipline | 15% | Real schema, real `INSERT`/`UPDATE`, no participant identifying info, queries run cleanly |
| Synthesis rigor | 20% | Themes emerged from data, ranked by `n_participants` not raw count, cross-checked against the actual quotes |
| Brief quality | 15% | Fits one page, states findings *and* their limits, zero solution-jumping |
| Honesty about limitations | 10% | Sampling bias, small N, and proxy-user caveats (if applicable) stated plainly, not buried or omitted |

---

## Why this matters

Every later week of this course assumes you can do this: turn a vague hunch into real conversations, real conversations into structured evidence, and structured evidence into a brief someone can act on without having sat in the room. Problem framing (Week 3), PRDs (Week 4), and prioritization (Week 5) all consume the *output* of a process exactly like this one. Keep your brief — Week 3's mini-project extends it into a sized, written problem statement.

When done: push your work, take the [quiz](../quiz.md), and start [Week 3 — Problem & opportunity framing](../../week-03-problem-and-opportunity-framing/).
