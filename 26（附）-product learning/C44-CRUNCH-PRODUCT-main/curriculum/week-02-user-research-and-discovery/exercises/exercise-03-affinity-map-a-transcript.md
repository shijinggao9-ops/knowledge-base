# Exercise 3 — Affinity-Map an Interview Transcript

**Goal:** Take a raw, never-touched interview transcript, extract the quotes worth keeping, load them into SQL as individual rows, code each into a theme, and query the result — the full synthesis pipeline from Lecture 3, on data you haven't seen coded already.

**Estimated time:** 75–90 minutes.

## Setup

You already ran the seed (see the [week README](../README.md)). This exercise adds one more participant and a fresh batch of quotes on top of it — you'll write the `INSERT` statements yourself.

First, add the 16th participant this transcript belongs to:

```sql
INSERT INTO participants VALUES
(16,'shift_worker','warehouse',11,'panel','2026-06-06');
```

## The transcript

Below is a lightly-edited transcript of a 20-minute interview with participant 16, **Marcus**, a warehouse shift worker with 11 months of tenure, interviewed about how he handles a shift he can't make. Read the whole thing once before you code anything — themes should emerge from the full conversation, not from your reaction to the first striking line.

> **Interviewer:** Thanks for making time, Marcus. Tell me about the last time you couldn't make a scheduled shift.
>
> **Marcus:** Yeah, so, like two weeks ago my kid was sick and I had a 6am shift the next day. I knew by like 9pm I wasn't gonna make it.
>
> **Interviewer:** Walk me through exactly what you did after that.
>
> **Marcus:** First thing, I texted my shift lead. She doesn't always check her phone at night though, so I also posted in our crew's group chat — we've got like 30 people in it, mostly just for this exact reason.
>
> **Interviewer:** And what happened after you posted?
>
> **Marcus:** Two guys said they could maybe do it, but neither one confirmed for real. I ended up calling one of them around 11 to lock it down. He said yes on the phone.
>
> **Interviewer:** Then what?
>
> **Marcus:** Then I had to text my shift lead again in the morning to tell her it was covered, because she never responded to the first text. I didn't actually know for sure it was "approved" until I saw the schedule updated the next afternoon.
>
> **Interviewer:** How long between when you first realized you needed coverage and when you actually knew it was handled?
>
> **Marcus:** Honestly like 18 hours. And I was checking my phone the whole next morning because I wasn't sure if it actually went through.
>
> **Interviewer:** Has a swap ever fallen through on you?
>
> **Marcus:** Oh yeah. One time the guy who said he'd cover just didn't show. I wasn't even there — I only found out because my shift lead texted me asking where I was, and I had to explain the whole thing after the fact. That one got messy. She didn't believe at first that I'd actually arranged coverage, because there was nothing to show her.
>
> **Interviewer:** What did you do differently after that?
>
> **Marcus:** Now I take a screenshot. Every time. Whoever says they'll cover, I screenshot the text and I don't delete that thread until after the shift happens.
>
> **Interviewer:** How often does this whole situation come up for you — needing someone to cover?
>
> **Marcus:** Maybe twice a month? Sometimes more if it's flu season or whatever.
>
> **Interviewer:** Is there anything about this we haven't talked about that you think I should know?
>
> **Marcus:** I guess — the group chat thing works, kind of, but it's honestly chaos. Thirty people, half of them muted it. I don't think management even knows how much actually gets arranged in there versus through them officially.

## Tasks

### Part 1 — Extract and load (20 min)

Pull out **8 to 10 distinct, atomic quotes** from Marcus — each one a single self-contained observation, not the whole paragraph. Write them as `INSERT` statements into `interview_quotes`, leaving `theme` as `NULL` for now:

```sql
INSERT INTO interview_quotes (quote_id, participant_id, quote_text, theme) VALUES
(21, 16, '<your extracted quote>', NULL),
(22, 16, '<your extracted quote>', NULL);
-- ... continue through at least quote_id 28
```

Use `quote_id` values starting at 21 (the seed data ends at 20). Trim filler words but keep his actual phrasing — don't paraphrase into your own words; that's the mistake Lecture 2 warned about.

### Part 2 — Code each quote (25 min)

For each quote, assign a `theme` using an `UPDATE`. You may reuse a theme from the seed data (`manual_texting`, `no_shows_trust`, `no_visibility`, `manager_bottleneck`, `last_minute_stress`, `fairness_concerns`, `record_keeping`) where it genuinely fits, **or** introduce a new theme if none of the existing seven capture what Marcus is describing — his transcript has at least one thing the original seven don't quite cover.

```sql
UPDATE interview_quotes SET theme = 'record_keeping' WHERE quote_id = 21;
-- ... one UPDATE per quote_id
```

### Part 3 — Query it (20 min)

Write and run these four queries against the now-combined dataset (participants 1–16):

1. Every quote now tagged with each theme Marcus's interview touched, grouped by theme.
2. Whether any theme from Marcus's interview also appears among the *managers'* quotes from the original seed (join `interview_quotes` to `participants`, filter `segment = 'manager'`) — does his experience corroborate what a manager independently said?
3. `COUNT(DISTINCT participant_id)` per theme across **all 16 participants now**, re-running the Lecture 3 ranking query — did adding Marcus change which theme has the most independent participants behind it?
4. If you introduced a new theme not in the original seven, a query pulling every quote under that new theme.

## Done when…

- [ ] `interview_quotes` has 8–10 new rows for participant 16, `quote_id` 21+.
- [ ] Every new row has a non-`NULL` theme after Part 2.
- [ ] All four Part 3 queries run and you've written one sentence per query stating what it told you.
- [ ] You can name which of Marcus's quotes is a workaround (per Lecture 2's definition) and explain why it counts as strong evidence, not just an opinion.

## Stretch

- Marcus mentions checking his phone anxiously for 18 hours not knowing if the swap "went through." Write one sentence arguing whether this belongs under `no_visibility`, `record_keeping`, or deserves its own theme — and defend your call.
- Re-run the Lecture 3 `n_participants` ranking query filtered to `workplace_type = 'warehouse'` only. Does the warehouse-specific ranking differ from the all-workplace ranking?

## Submission

Commit your `INSERT`/`UPDATE`/`SELECT` statements as `affinity-map.sql`, plus a short `findings.md` with your one-sentence answers, to your portfolio under `c44-week-02/exercise-03/`.
