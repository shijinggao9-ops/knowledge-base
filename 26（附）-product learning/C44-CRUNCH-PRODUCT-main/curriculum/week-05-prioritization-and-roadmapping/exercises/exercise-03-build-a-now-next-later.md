# Exercise 3 — Build a Now/Next/Later Roadmap

**Goal:** Take the full scored, dependency-aware backlog and turn it into a real, capacity-constrained now/next/later roadmap in pandas — the exact pipeline Lecture 3 walked through, run yourself, end to end.

**Estimated time:** 90 minutes.

## Setup

```bash
source .venv/bin/activate   # from the week README's Python setup
python3
```

Confirm your connection:

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///loopline_backlog.db")   # or your Postgres URL
backlog = pd.read_sql("SELECT * FROM backlog_items", engine)
print(len(backlog))   # must print 14
```

Create a script `roadmap.py` and build it up task by task.

## Tasks

### Task 1 — Compute WSJF in pandas

Load `backlog_items` into a DataFrame and add a `cost_of_delay` column and a `wsjf` column (don't recompute these in SQL this time — practice doing the arithmetic directly in pandas with vectorized column operations, not a Python loop). Sort descending by `wsjf` and print the full ranked table.

*(Expected: same ranking as Lecture 2's table — `guest_external_access` first, `ai_task_summaries` last.)*

### Task 2 — Load dependencies and check for cycles

Load `backlog_dependencies` into a second DataFrame. Write a short function `prerequisites_met(item_key, scheduled_set)` that returns `True` if every prerequisite of `item_key` is already in `scheduled_set`. Test it manually: confirm `prerequisites_met('guest_external_access', set())` is `False`, and `prerequisites_met('guest_external_access', {'audit_log_compliance'})` is `True`.

### Task 3 — Implement the capacity-constrained sequencer

Implement the full scheduling loop from Lecture 3 (or write your own version that produces an equivalent result): walk the WSJF-ranked backlog, respecting dependencies, filling **Now** up to 20 job-size points, then **Next** up to 20 more, with everything else falling to **Later**.

Print three lists: `now_items`, `next_items`, `later_items` (item keys).

*(Expected: Now = `guest_external_access`, `audit_log_compliance`, `configurable_stuck_threshold`, `bulk_task_reassignment`, `stuck_alert_digest_mode` — 20 points exactly. Next = `task_templates`, `recurring_tasks`, `mobile_push_notifications` — 19 points.)*

### Task 4 — Verify the dependency was actually respected

Write one assertion (a real `assert` statement, not a comment) that proves `audit_log_compliance` appears in your `now_items` list at or before `guest_external_access`'s position in the overall schedule order — i.e., prove your sequencer didn't just get lucky on ranking, it actually enforced the constraint.

### Task 5 — Render a roadmap table

Using `now_items`, `next_items`, `later_items` and the original `backlog` DataFrame, build and print a single tidy DataFrame with columns `roadmap_column` (Now/Next/Later), `title`, `requested_by`, `job_size_points`, `wsjf`, sorted by column then by WSJF descending within each column. This is the shape of table you'll paste into the mini-project's roadmap doc.

## Expected results (spot checks)

- Task 1 → top of WSJF ranking is `guest_external_access` at 4.0.
- Task 3 → Now bucket sums to exactly 20 job-size points; Next bucket sums to 19.
- Task 3 → Later bucket has 6 items.
- Task 4's assertion passes without modification if your sequencer is correct.

## Done when…

- [ ] `roadmap.py` runs top to bottom with no errors and prints all 5 tasks' output.
- [ ] Task 1's WSJF ranking matches Lecture 2's table.
- [ ] Task 3's Now/Next/Later buckets match the spot checks (or you've written a short note explaining a deliberate, justified deviation).
- [ ] Task 4's assertion is a real `assert`, and it passes.
- [ ] Task 5 produces one clean, sorted DataFrame — not three disconnected lists.

## Stretch

- Parameterize `NOW_CAPACITY` and `NEXT_CAPACITY` as function arguments, then re-run with `NOW_CAPACITY = 13` (a leaner quarter). Which item falls out of Now first, and does it change which dependency has to be pulled forward?
- Add a `.to_csv("roadmap.csv", index=False)` call and open the file — this is the artifact you'd actually attach to a roadmap review doc.

## Submission

Commit `roadmap.py` and `roadmap.csv` to your portfolio under `c44-week-05/exercise-03/`.
