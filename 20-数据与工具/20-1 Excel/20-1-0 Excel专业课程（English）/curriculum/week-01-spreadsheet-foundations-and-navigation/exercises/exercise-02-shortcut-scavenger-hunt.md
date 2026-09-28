# Exercise 2 — Keyboard Shortcut Scavenger Hunt

**Goal:** Force the Lecture 2 shortcuts out of your short-term memory and into your fingers, under light time pressure. This is a drill, not a design task — speed and no-mouse discipline are the point.

**Estimated time:** 30 minutes.

## Setup

Add a new sheet, rename it `Exercise 2`. You need a bigger block of data than Exercise 1 to make the "jump to edge" shortcuts meaningful, so build it fast:

1. In `A1`, type `ID`, `Tab`, `Value`, `Enter`.
2. In `A2`, type `1`, `Tab`, `100`, `Enter`.
3. Select `A2:B2`, then look for the small square at the bottom-right corner of the selection (the **fill handle**). Drag it down to row 51 — both apps auto-continue the `ID` sequence (`1, 2, 3…`) and repeat/pattern the `Value` column. You now have 50 rows of data, `A1:B51`.
4. Manually delete the contents of `B27` only (select it, press `Delete`) — this creates one gap you'll use for a jump-to-edge task below.

**Rule for this whole exercise: mouse for clicking the fill handle in step 3 only. Everything below, keyboard only.** If you catch your hand reaching for the mouse, that's the exact habit this exercise exists to break.

## Round 1 — Basic movement (5 min)

Time yourself. From `A1`:

1. Jump to the last used cell in the sheet. Which cell did you land on? _______
2. From there, jump straight back to `A1` in one keystroke.
3. Move to `B1` using `Tab`, not an arrow key.
4. Move back to `A1` using `Shift+Tab`.
5. Type `Header Check` into `C1`, press `Enter` — which cell is now active? _______

## Round 2 — Jump-to-edge (10 min)

From `A1`:

1. Press `Ctrl/Cmd+Down`. Which row did you land on, and why did it stop there (recall the gap you made at `B27`)? _______
2. From `A1`, this time navigate to `B1` first, then press `Ctrl/Cmd+Down`. Where do you land, and why is it *different* from step 1? _______ *(Hint: think about which column has the gap.)*
3. From `B1`, press `Ctrl/Cmd+Down` twice in a row. Where are you after the second press, and what does that tell you about how the jump treats the empty cell at `B27`? _______
4. From wherever you are, press `Ctrl/Cmd+Home`. Confirm you're back at `A1`.

## Round 3 — Selection (10 min)

1. From `A1`, select the entire `ID` column's data in one motion (no dragging) — write the shortcut you used: _______
2. From `A1`, select the full rectangle `A1:B51` in one continuous keyboard motion — write the two shortcuts, in order, that you chained: _______
3. Select column `A` in its entirety (not just the data — the whole column, all 1,048,576/unlimited rows) using one shortcut: _______
4. Now select **both** column `A` and column `C` at once, without column `B` — this needs the mouse/trackpad for the `Ctrl/Cmd`-click, but confirm you can still describe why it works from Lecture 2, section 3: _______
5. Type `A1:B51` directly into the Name Box and press Enter. Confirm the same rectangle from step 2 gets selected instantly.

## Round 4 — Sheets and freezing (5 min)

1. Create two more sheets (any method). Rename them `Scratch A` and `Scratch B`.
2. Using only the keyboard, switch from `Exercise 2` to the next sheet tab, then to the one after that, then back. Write the shortcut you used: _______
3. Delete `Scratch A` and `Scratch B` — you don't need them beyond this drill.
4. Back on `Exercise 2`, freeze row 1. Scroll down to row 40 and confirm the header is still visible.

## Answer check

- Round 2, Q1 → `A51`, the true bottom of the used range. Column `A` (the `ID` column) has **no** gap — only `B27` is empty — so the jump from `A1` sails straight through to the last row with no interruption. If you landed somewhere else, re-read Lecture 2 section 2: the jump is entirely column-specific, it only cares about breaks in the column you're standing in.
- Round 2, Q2 → from `B1`, `Ctrl/Cmd+Down` lands on `B26` — the last row *before* the gap at `B27`, because column `B` genuinely has a break there. Same shortcut, different landing spot, purely because you started in a different column.
- Round 2, Q3 → the second press from `B26` jumps to `B51` — over the single gap at `B27` and on to the end of the next block.
- Round 3, Q1 → `Ctrl/Cmd+Shift+Down` from `A1` (or `Ctrl/Cmd+Space` then it's already selected as a column — but the edge-selection shortcut is the intended answer here).
- Round 3, Q3 → `Ctrl/Cmd+Space` selects the entire column.

## Done when…

- [ ] You completed all 4 rounds without touching the mouse except where explicitly allowed (fill handle, non-adjacent click-select).
- [ ] Your Round 2 answers match the reasoning in the Answer check — if not, redo Round 2 until the "why" actually clicks, not just the keystroke.
- [ ] You can now do the entire "jump to end of a column, select the whole thing, freeze the header" sequence without looking at Lecture 2.

## Stretch

- Reduce your total time for Rounds 1–3 by at least 30% on a second attempt, on a fresh sheet with the same data shape.
- In Google Sheets specifically, try `Ctrl+Alt+Shift+H` (Windows) or the equivalent shortcut-help overlay to see the *full* shortcut list live in the app — do the same in Excel via `Alt` (Windows) to reveal ribbon key-tips, or `Cmd+/` (Mac) for the shortcut search.

## Submission

No file to submit — this is a drill. Move to Exercise 3.
