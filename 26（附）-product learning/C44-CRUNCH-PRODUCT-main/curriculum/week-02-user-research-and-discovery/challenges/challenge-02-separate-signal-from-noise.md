# Challenge 2 — Separate Real Signal from Feature Requests

**Time:** ~60 minutes. **Difficulty:** Medium-Hard. **No single right answer.**

## The scenario

Shiftly's support inbox and in-app feedback widget produced 20 raw messages this month. Your PM lead drops them on your desk as a flat list and says "see if anything in here is worth acting on." Most teams read a list like this and build whatever the loudest or most-repeated *literal request* is. That is usually a mistake — a stated feature request is a **participant's own proposed solution**, not necessarily the real underlying need, and two very differently-worded requests can point at the exact same root problem (or one clearly-worded request can be noise nobody else has).

This is the same discipline as a good interview (Lecture 2): don't take the surface statement at face value, ladder toward the underlying need. Here you're doing it against written feedback instead of a live conversation, at volume, using SQL instead of a sticky-note wall.

## The raw feedback

```text
1.  "Add a dark mode, my eyes hurt looking at the schedule at night." — in-app widget
2.  "Please let me swap shifts without waiting for my manager to approve it." — support ticket
3.  "The app crashed once when I opened it during a shift change. Annoying but happened once." — in-app widget
4.  "Can you add a button that shows who's free to cover a shift right now?" — support ticket
5.  "I wish I could see my paycheck estimate before the shift ends." — in-app widget
6.  "Every time I think a swap is approved, I find out later it wasn't. Can you add a confirmation?" — support ticket
7.  "The app icon looks outdated compared to other apps I use." — in-app widget
8.  "Add a marketplace where I can post my shift and anyone can grab it." — support ticket
9.  "My manager takes 2 days sometimes to approve a swap and by then it's pointless." — support ticket
10. "Would be cool if the app had a dark mode like Instagram." — in-app widget
11. "I need proof that someone agreed to cover my shift in case there's a dispute later." — support ticket
12. "Can you make the font bigger? Hard to read on my phone." — in-app widget
13. "Add push notifications for schedule changes." — support ticket
14. "I got blamed for a no-show because the person who said they'd cover never actually confirmed anywhere official." — support ticket
15. "It would help to see a live list of who's already agreed to cover open shifts, instead of texting around." — support ticket
16. "Add a way to filter the schedule by department." — in-app widget
17. "One time I couldn't log in for 10 minutes, everything's fine now." — in-app widget
18. "I want a swap marketplace like the one I saw in a different app." — support ticket
19. "It's frustrating that swap approvals happen over text message with no record anywhere in the app." — support ticket
20. "Can the app remember my login so I don't type my password every shift?" — in-app widget
```

## Your task

### Part 1 — Build the tagging table (15 min)

Create a table and load all 20 items:

```sql
CREATE TABLE raw_feedback (
    feedback_id      INTEGER PRIMARY KEY,
    quote_text       TEXT NOT NULL,
    source           TEXT NOT NULL,     -- 'in_app_widget' or 'support_ticket'
    category         TEXT,              -- you fill this in: 'validated_need', 'surface_request', or 'noise'
    underlying_need  TEXT               -- you fill this in, NULL if genuinely noise
);
```

Insert all 20 rows (`category` and `underlying_need` left `NULL` for now — you'll fill them with `UPDATE` statements in Part 2).

### Part 2 — Categorize each item (25 min)

For every row, decide and `UPDATE`:

- **`category`** — one of:
  - `'surface_request'` — a specific proposed solution (a feature name), where you *can* still infer a real underlying need behind it.
  - `'noise'` — a one-off, non-representative, or cosmetic complaint unlikely to represent a broader pattern worth prioritizing.
  - `'validated_need'` — reserve this for an item where the underlying need is *already corroborated elsewhere* — specifically, if it matches a theme already present in this week's seed `interview_quotes` table. (Query that table if you need a refresher on what's already been validated by interview evidence.)
- **`underlying_need`** — a one-sentence statement of the *actual problem*, written the way Lecture 3's finding format does it — not a restatement of their proposed feature. Leave `NULL` only for genuine `noise`.

Some of these are intentionally ambiguous. A defensible answer explains its reasoning in `challenge-02.md`, not just the tag.

### Part 3 — Query and synthesize (20 min)

1. Write a query that groups by `underlying_need` (not the literal quote) and counts how many of the 20 raw items map to each — this is the moment where differently-worded requests should visibly cluster together.
2. Which `underlying_need` clusters have the most items behind them, and does that cluster match a theme already in `interview_quotes`? Cross-reference with a `JOIN` or a second query if useful.
3. Identify the item(s) you tagged `noise`. Write one sentence per item defending why it doesn't rise to a validated need — "only mentioned once" is not by itself sufficient (a rare complaint can still be a real, serious issue) — say what additional evidence *would* change your mind.
4. Name **one item where the literal request and the underlying need are almost the same** (a rare case where taking the request at face value would actually be fine) and explain what makes that one different from the others.

## Constraints

- You must produce at least 3 distinct `underlying_need` values that each cluster 2+ raw items — if every item gets its own unique underlying need, you haven't actually found the pattern.
- At least one `underlying_need` cluster must explicitly connect back to a theme from the seed `interview_quotes` table by name.
- Don't tag more than 4 items as `noise` — if you're reaching for "noise" more than that, you're probably taking the easy way out on items that deserve real laddering.

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Laddering | Tags items by their literal feature request | States the underlying need one level up from the request |
| Clustering | Every item is its own island | Differently-worded items correctly cluster under one shared need |
| Cross-referencing | Ignores the existing interview themes | Explicitly ties at least one cluster to a named `interview_quotes` theme |
| Noise judgment | Dismisses anything mentioned once | Distinguishes "rare and low-stakes" from "rare but serious," with reasoning |
| Restraint | Recommends specific features from this list | Stops at validated needs — no feature recommendations (that's next week) |

## Submission

Commit your SQL (`feedback.sql`) and your written reasoning (`challenge-02.md`) to your portfolio under `c44-week-02/challenge-02/`.
