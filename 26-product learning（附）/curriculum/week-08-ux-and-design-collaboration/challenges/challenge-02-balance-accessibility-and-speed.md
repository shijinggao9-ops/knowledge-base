# Challenge 2 — Balance Accessibility Against Ship Speed

**Time:** ~60 minutes. **Difficulty:** Medium. **No single right answer — but every answer must show real reasoning.**

## The scenario

Loopline's redesigned checkout flow (the one you might have just proposed in Challenge 1) is two days from a committed launch date that marketing has already promoted in an email to 40,000 users. During final QA, engineering and design surface **six accessibility findings**. You, the PM, have to make a ship-now-or-hold call on each — today — using the four-input trade-off framework from [Lecture 3](03-critique-and-tradeoffs.md#5-negotiating-trade-offs-with-designers-and-engineers): **user impact, cost, risk, reversibility.**

## The six findings

For each, decide: **fix before ship**, **ship now with a dated fast-follow**, or **ship as-is**. Justify every decision using all four inputs — a decision that only mentions one or two inputs is incomplete.

**F1 — Confirm-and-pay button fails color contrast (3.1:1, needs 4.5:1)**
The button text is legible to most people but technically fails WCAG AA. Engineering estimates the fix (swap two color tokens used in 40+ other places) at 15 minutes, but it touches a shared design-system token, so it needs a full visual QA pass across the app — estimated half a day.

**F2 — The `[x]` close button on the Order Summary screen has no accessible label**
A screen reader announces it only as "button," with no indication of what it does. Fix is a one-line `aria-label` addition, testable in 10 minutes, isolated to this one screen.

**F3 — The seat-count stepper is unreachable by keyboard**
It only responds to mouse clicks on the `+`/`-` icons; Tab skips over it entirely. A keyboard-only user cannot complete checkout at all — full stop, not a degraded experience. Fix requires rebuilding the component's event handling; engineering estimates 1.5 days and wants to do it properly rather than patch it.

**F4 — The processing spinner has no `aria-live` announcement**
A screen-reader user gets no audible indication that anything is happening after tapping "Confirm and pay," and no announcement when it resolves — they may believe the tap did nothing and tap again (which is itself now a duplicate-charge risk, a separate bug). Fix is small (add an `aria-live` region), estimated at 2 hours, isolated to this screen.

**F5 — Error messages on the manual card-entry screen are color-only** (red text, no icon, no text label like "Error:")
A user with red-green color blindness may not notice the field is in an error state at all, though the message text itself (once seen) is otherwise clear. Fix is small — add an icon and a text prefix — estimated at 3 hours.

**F6 — The legal disclaimer text doesn't scale with the browser/OS text-size setting** (fixed pixel size, ignores user zoom preferences)
Low-vision users who've set their OS or browser to a larger default text size see every other on-screen text scale except this one paragraph. Fix requires a CSS unit change across a shared component, estimated at 4 hours, low risk of breaking anything else.

## Your task

For each of F1–F6, write:

```
Finding: <F-number>
User impact: <how many people, how severely — total blocker vs. degraded experience>
Cost: <effort estimate as given, plus any hidden cost like the shared-token ripple>
Risk: <legal/compliance/brand exposure if shipped as-is>
Reversibility: <how bad is it if we ship now and fix in a week vs. fix now>
Decision: <fix before ship / ship + dated fast-follow / ship as-is>
```

Then answer, in a short paragraph each:

1. **Which finding was the easiest call, and why?** (Hint: one of the six is a total blocker for an entire class of users — that changes the calculus completely from a "degraded but usable" issue.)
2. **Which finding was the hardest call, and why?** Name the specific trade-off that made it hard — don't just say "it was close."
3. **You can only get engineering to commit to fixing 2 of the 6 before the ship date, with certainty (not "we'll try").** Which 2, and what happens to the other 4? Give the fast-follow dates you'd commit to (relative, e.g. "sprint +1") for the ones you're not blocking on.
4. **What would you say in the launch email follow-up thread if a user with a screen reader reports they couldn't complete checkout at all — assuming F3 shipped unfixed?** Two to three sentences, written as you'd actually send it internally, not defensively.

## Constraints

- You must use all four inputs (impact, cost, risk, reversibility) for every finding — a decision using only cost ("it's small, just fix it") or only impact ("everyone deserves accessible checkout, fix everything") is an incomplete answer, even if the final call happens to be reasonable.
- "Ship as-is, forever, no follow-up" is a valid answer for at most one of the six findings — if you use it more than once, you need to explicitly defend why more than one of these should never get fixed.
- No finding may be silently ignored — six decisions, six justifications.

## How success is judged

| Signal | Weak answer | Strong answer |
|---|---|---|
| Framework use | Justifies with 1 input or vague reasoning | All four inputs addressed per finding |
| Impact accuracy | Treats every finding as equally severe | Distinguishes a total blocker (F3) from a degraded-but-usable issue (F1, F5, F6) |
| Cost honesty | Ignores hidden/rippling costs | Accounts for F1's shared-token ripple effect explicitly |
| Commitment quality | "We'll try to fix it soon" | Named 2 fixes with real dated fast-follows for the rest |
| Communication | Defensive or hand-wavy on Question 4 | Direct, owns the gap, names the fix timeline |

## Submission

Commit `accessibility-triage.md` (the six findings) and `reflection.md` (the four questions) to your portfolio under `c44-week-08/challenge-02/`.
