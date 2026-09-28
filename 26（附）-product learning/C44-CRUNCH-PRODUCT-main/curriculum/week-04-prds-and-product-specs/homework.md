# Week 4 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of writing, critique, and SQL practice. Commit each.

All problems reference **Loopline** and the seed `events` table from the [README](./README.md) unless a problem says otherwise.

---

## Problem 1 — Find five real PRDs and grade their non-goals (60 min)

Search publicly available product specs, RFCs, or "how we built X" engineering blog posts (many companies publish these — Basecamp's Shape Up writeups, Stripe's changelog rationale posts, Linear's public methodology posts, and many startups' engineering blogs are good hunting grounds). Find **five** that describe a specific feature (not a whole product) in enough detail to evaluate.

**Deliver** `prd-survey.md` with, for each of the five:
1. The link and a one-sentence description of the feature.
2. Does it have anything resembling a non-goals or "out of scope" section? Quote it if so.
3. Your grade (Strong / Weak / Absent) for how clearly it separates "what we're building" from "what we're deliberately not building."
4. If it's Weak or Absent, write the non-goals section you think it was missing, in one sentence.

End with 3–4 sentences: across your five, was a clear non-goals section common or rare? What's your theory on why?

---

## Problem 2 — Rewrite five bad user stories (45 min)

Each of these is a real style of story PMs write when rushed. Rewrite each into a proper `As a / I want / so that` story, run the INVEST test, and flag which letter(s) the *original* violated.

1. "Add pagination to the task list."
2. "Make the mobile app faster."
3. "Build a new onboarding flow."
4. "As a user, I want the app to be intuitive, so that it's easy to use."
5. "Refactor the notifications backend to use a message queue."

**Deliver** `story-rewrites.md` — original, rewrite, INVEST violation named, for each of the five.

---

## Problem 3 — Acceptance criteria for a story outside this week's feature (75 min)

Write full Given/When/Then acceptance criteria (minimum 5) for this story, unrelated to Stuck Task Alerts:

> As a Loopline user, I want to bulk-archive all my completed tasks older than 30 days, so that my active task list stays clean without me archiving one at a time.

Cover: the happy path, an exact boundary (a task completed *exactly* 30 days ago — archived or not?), a "does NOT happen" case (what must NOT get archived), a permission case (can a teammate bulk-archive *another* person's completed tasks?), and one case involving what happens if new tasks complete *during* the bulk-archive operation.

**Deliver** `bulk-archive-ac.md`.

---

## Problem 4 — Edge-case audit of a product you use (60 min)

Pick one feature in a real product you use regularly (not Loopline) — a "like" button, a comment-edit feature, a recurring calendar event, a shopping-cart quantity stepper, anything with real state and real users. Deliberately try to break it: test boundaries, go offline mid-action, try it with zero items, try it twice fast, try it as a second collaborator would.

**Deliver** `edge-case-audit.md`: at least 6 things you tried, what actually happened (observed behavior, not guessed), and for each, whether you think the behavior you saw was a **deliberate product decision** or an **unhandled gap** — and why you believe that.

---

## Problem 5 — Extend the seed events schema and write two new metric queries (60 min)

Using the seed `events` table from the [README](./README.md), imagine Loopline is shipping a second, unrelated feature: **"Task Comments"** (users can comment on a task; a comment does *not* count as a status change for stuck-detection purposes — state that explicitly, since it interacts with this week's feature).

1. Write `INSERT` statements adding a `task_commented` event type, with realistic properties (`comment_id`, `author_id`, `task_id`, a `body_length` integer instead of storing full comment text — explain in one sentence why you might choose not to store full free-text comment bodies in the events table).
2. Insert at least 4 `task_commented` events across the existing seed tasks.
3. Write a query: which tasks have comments but have **never** had a `task_status_changed` event — i.e., discussion is happening but the task itself hasn't moved. Is this itself worth turning into an alert? Answer in one sentence — is it, or is it scope creep for a different feature?

**Deliver** `task-comments-events.sql` (inserts + query) and a short written answer to part 3.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 60 min |
| 2 | 45 min |
| 3 | 75 min |
| 4 | 60 min |
| 5 | 60 min |
| **Total** | **~5 h** |

After homework, take the [quiz](./quiz.md) and ship the [mini-project](./mini-project/README.md).
