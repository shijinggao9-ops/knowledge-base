# Challenge 2 — Fix a Misleading Chart

**Time:** 60–75 minutes. **Difficulty:** Medium. **No single "correct" rebuild — but there are clearly worse and better ones.**

## The scenario

A colleague built a chart for the sales director's monthly review and asked you to sanity-check it before it goes out. You open it and something feels off — the story it tells doesn't quite match what you already know about the data from this week's earlier work. Your job: reproduce the flawed chart exactly as specified below, diagnose everything wrong with it, and rebuild a version that tells the truth clearly.

## Part A — Build the flawed chart exactly as specified

Using the monthly revenue totals from `Transactions` (Month, grouped, Sum of `TotalRevenue`), build a **3D column chart, titled "Chart Title,"** with every one of these choices deliberately baked in:

| Setting | Flawed value to use |
|---|---|
| Chart type | **3D Column** |
| Category (x-axis) order | Sorted by revenue **descending** (May, Mar, Jun, Apr, Jan, Feb) — **not** chronological |
| Y-axis minimum | **1,500** (not 0) |
| Title | Left as the default **"Chart Title"** / "Sum of TotalRevenue by Month" — never renamed to state a finding |
| Legend | Visible, showing a "TotalRevenue" key — even though there's only one series |
| Bar colors | A different, unrelated color per bar (not one consistent color) |
| Gridlines | Both horizontal **and** vertical, heavy weight, plus a chart border and a gray background fill |

Take a moment to actually look at it once built. It should look busy, and the bar-height comparison should feel more dramatic than you know it actually is from earlier exercises.

## Part B — Diagnose every flaw

In `challenge-02.md` (or a `Notes` sheet), for **each** of the 6 settings in the table above, write 1–2 sentences answering:

1. **What false impression does this specific choice create?** Be concrete — e.g., "the truncated y-axis makes May's bar look roughly 8× taller than February's, when May's actual revenue (6,666.61) is only about 3.5× February's (1,896.26)."
2. **What would a careful reader wrongly conclude** if they only glanced at the chart for 3 seconds?

## Part C — Rebuild it correctly

Build a second chart, from the same underlying pivot, that fixes every flaw:

- 2D column (or line) chart, chronological month order (Jan → Jun).
- Y-axis starts at 0.
- Title states the actual finding (e.g., "Revenue dipped in February, then grew steadily to a May peak").
- No legend for a single series (or a legend only if you have 2+ series that genuinely need one).
- One consistent color across all bars (unless color is deliberately encoding a second dimension, which isn't the case here).
- Minimal gridlines — light horizontal only, no border, no background fill.

## Part D — Write the before/after comparison

Finish `challenge-02.md` with a short paragraph (~100 words): what's the *one* specific business decision someone might make differently after seeing the flawed chart versus the fixed one? (For example: might they wrongly conclude January-to-February is a catastrophic collapse worth an emergency meeting, when chronologically Jan→Feb is actually the only real dip in an otherwise growing first half?)

## Constraints

- Part A must be built exactly as specified — resist the urge to "fix it a little" while building it. You need to actually see the misleading version to diagnose it properly.
- Part C must be a genuinely separate chart (or at minimum, every one of the 6 settings changed), not a description of what you'd change.
- Every flaw named in Part B must reference the actual numbers involved, not just a general statement like "the axis is misleading" — say *how much* more misleading, using the real data.

## Hints

<details>
<summary>On the truncated y-axis specifically</summary>

Compute the visual ratio a reader would perceive versus the true ratio. With a y-axis starting at 1,500: February's bar height above the baseline is `1,896.26 − 1,500 = 396.26`; May's is `6,666.61 − 1,500 = 5,166.61` — a visual ratio of about **13×**, when the true revenue ratio is only about **3.5×** (6,666.61 / 1,896.26). That gap between the visual impression and the true ratio is the whole problem with a non-zero baseline on a bar chart.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Part A fidelity | Flaws watered down or skipped while building | Every specified flaw is faithfully reproduced, so it can actually be diagnosed |
| Diagnosis depth | Vague ("axis is bad") | Concrete, uses real numbers, names the specific false impression each flaw creates |
| Rebuild quality | Fixes 1–2 flaws | All 6 flaws fixed; title states an actual finding |
| Business framing | Skipped or generic | Names one specific decision the flawed chart could have caused someone to make wrongly |

## Submission

Keep both charts (flawed and fixed) plus `challenge-02.md` in your `crunch-week7` workbook.
