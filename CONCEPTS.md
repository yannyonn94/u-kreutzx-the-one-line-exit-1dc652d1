# Concept Test — The One-Line Exit

Bounty: **The One-Line Exit** (`u-kreutzx-the-one-line-exit-1dc652d1`).
Judge: AI pairwise (z-ai/glm-5.3-flash), criteria in order — (1) funny one-line
resignation letter, (2) surprise / unexpected punchline, (3) fits the form
(one line, no grievance list, reads like a real letter), (4) specific voice
(recognizable job / workplace / person), (5) quotable / memorable.
Tie-break: fewer bytes wins, then earlier submission. Gate: 1–140 characters,
UTF-8, not only whitespace.

Scoring: /25 — specificity (5) + surprise (5) + voice (5) + quotable (5)
+ form fit (5).

## V1 — 23/25 — WINNER

> I resign effective immediately — the office plant has been promoted above me twice now, and honestly, it earned it.

- 115 characters, 117 bytes.
- Specificity 5/5: the office plant, promoted *twice* — a concrete, absurd workplace detail.
- Surprise 5/5: the punchline turns twice — first the plant outranks the writer, then the writer *concedes* it deserved it.
- Voice 4/5: unmistakably an office worker's resignation, but the job itself is generic office.
- Quotable 5/5: "the office plant has been promoted above me twice now" is the kind of line a colleague forwards.
- Form fit 4/5: reads like a real resignation letter; the em-dash aside is the only slightly stylized beat.

## V2 — 22/25

> Dear boss, I resign: the night shift taught me the ghosts clock in on time every night, but I never will again.

- 111 characters, 111 bytes.
- Specificity 5/5: night shift, ghosts clocking in — a vivid, specific workplace.
- Surprise 4/5: ghosts on the night shift is a good turn, but "haunted workplace" is a more familiar joke setup than a promoted plant.
- Voice 5/5: the night-shift worker's voice is unmistakable.
- Quotable 4/5: "the ghosts clock in on time" is memorable, but the second clause is slightly wordy.
- Form fit 4/5: "Dear boss" opening reads like a real letter.

## V3 — 20/25

> I quit — after six years, the coffee machine got a farewell party, a plaque, and a pension plan, and I got this form.

- 117 characters, 119 bytes.
- Specificity 4/5: the coffee machine with a plaque and pension is concrete, but "six years" is a generic tenure line.
- Surprise 3/5: the list-of-rewards turn is funny, but it leans toward a list of grievances, which the judge's form criterion penalizes.
- Voice 4/5: the long-serving employee is recognizable.
- Quotable 4/5: "a farewell party, a plaque, and a pension plan" is quotable, but the triple list costs punch.
- Form fit 5/5: reads like a real letter.

## Why V1 wins

V1 beats V2 by one point on surprise and quotability: the double turn
(promoted plant → it earned it) lands a punchline nobody expects, and the
whole line is forwardable as-is. On the byte tie-break V2 is actually
smaller (111 vs 117 bytes), but the tie-break only decides exact ties on
win rate, and V1's one-point concept lead is the stronger signal. V1 beats
V3 by three points because V3's triple list flirts with the "list of
grievances" shape the judge is told to penalize, while V1 stays a single
clean sentence.

## V4 — not submitted

I considered a fourth variant (a printer-therapist line and a
spreadsheet-replacement line) but neither scored above 23/25 on the same
rubric: both reused a familiar "inanimate object replaces me" setup without
V1's second turn, and both scored lower on surprise (4/5 at best) with no
gain on voice or quotability. V1 stands as the entry.

## Entry

**V1 is implemented in `main.py`.**
