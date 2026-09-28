# Week 12 Homework

A practice set tying macros, Apps Script, and the wider course together. Work through these after the exercises; before or alongside the mini-project is fine — several of these feed directly into it.

**Estimated time:** 3 hours total.

## Part 1 — Read and fix broken VBA (45 min)

Below is a macro someone else wrote for a different Crunch Outfitters report. It "mostly works" but has three real bugs. Find and fix all three; write one sentence per bug explaining what would go wrong and when.

```vb
Sub UpdateReport()
    Range("A1").Select
    Selection.End(xlDown).Select
    lastRow = Selection.Row

    For i = 2 To lastRow
        If Cells(i, 3).Value = "Sales" Then
            Cells(i, 5).Value = Cells(i, 4).Value * 1.1
        End If
    Next i

    Range("F1").Value = "Updated " & Now
    ActiveWorkbook.Save
End Sub
```

*(Hints, don't peek until you've tried: what happens if row 1 or the whole column has a gap partway down? What happens the very first time this runs, before `lastRow` or `i` have ever been declared — does VBA even complain? What does `Selection.End(xlDown)` do if `A1` itself is already the last non-empty cell before a gap?)*

<details>
<summary>Reveal after attempting</summary>

1. **No `Option Explicit` / undeclared variables** — `lastRow` and `i` are never `Dim`'d. VBA silently creates them as `Variant`, which works but hides typos (a mistyped variable name elsewhere becomes a *new* variable instead of a compile error). Fix: add `Option Explicit` at the top of the module and `Dim lastRow As Long, i As Long`.
2. **`Range("A1").Select` → `Selection.End(xlDown)` breaks on the first gap** — `End(xlDown)` simulates `Ctrl+Down`, which stops at the *first* blank cell it hits, not the true last row of data. If column A has even one blank cell partway down, `lastRow` will be wrong (too small), silently skipping real data below the gap. Fix: use the "last row" idiom from lecture 01 — `Cells(Rows.Count, "A").End(xlUp).Row` — which starts from the very bottom and works upward, immune to internal gaps.
3. **No error handling at all** — any failure (a locked sheet, a formula error in column D) crashes with a raw runtime dialog and no context. Fix: wrap with `On Error GoTo ErrHandler` and a `MsgBox` naming `Err.Description`.

</details>

## Part 2 — Translate a VBA macro to Apps Script (45 min)

Take your fixed version of `UpdateReport` from Part 1 and rewrite it as an Apps Script function operating on an equivalent Google Sheet (columns A–F, same meaning). Use the batch `getValues()`/`setValues()` pattern from lecture 02 rather than a cell-by-cell loop — this is a good test of whether you actually internalized *why* that pattern matters, not just VBA syntax translated word-for-word into JavaScript syntax.

## Part 3 — Design (don't necessarily build) a refresh chain for a different scenario (45 min)

Pick one:

- A weekly **fitness tracker** dashboard pulling from a Google Form/Sheet of daily workout logs.
- A **rental property** dashboard pulling monthly expense/income CSVs.
- A **fantasy sports** dashboard pulling weekly stats exports.

Write out, as a numbered list (like lecture 03 §1's five-step chain), exactly what your refresh routine would need to do in order, and note which steps have a real dependency on the previous step finishing first versus which could theoretically run in any order. Note one specific way this refresh could fail in production, and what your error message should say when it does.

## Part 4 — Security reasoning (30 min)

In 150–250 words, answer: a colleague asks why Excel "randomly" shows a security warning bar on some workbooks and not others, and whether it's safe to just always click "Enable Content" without reading it. Write the explanation you'd actually give them — cover what the warning means, when clicking through is reasonable versus risky, and what a **trusted location** is and why it exists as an alternative to disabling the warning globally.

## Part 5 — Course retrospective (15 min)

You're 12 weeks into this course. In a short paragraph: which single week's skill do you use *without thinking about it* now — the one that became reflexive? Which week's skill do you still have to consciously look up? This isn't graded on the "right" answer — it's useful data for you about what to keep practicing after the course ends.

## Submission

Commit `part1-fixed.bas`, `part2-translated.gs`, `part3-refresh-design.md`, `part4-security.md`, and `part5-retrospective.md` to your portfolio under `c41-week-12/homework/`.
