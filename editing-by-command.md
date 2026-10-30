# Editing by Command

Outcome: the badge's star, made exactly
one and a half times bigger and, in a
second copy, turned by 30 degrees —
each saved as a new file, each verified
by re-measuring, with the original
untouched. This is Inkscape's **actions**:
the same operations the window's menus
perform, driven by name from the
command line.

## How actions work

An action run names the file, the
actions to perform in order, and where
the result goes:

```bash
inkscape badge.svg \
  --actions="select-by-id:star;transform-scale:1.5" \
  --export-filename=badge-scaled.svg
```

Actions chain with semicolons, and each
does one thing: `select-by-id:star`
selects the object named star (and only
it — the selection is the whole game,
as chapter 5's discipline warned), and
`transform-scale:1.5` scales what is
selected. With no `--export-filename`,
the changes are thrown away when the
run ends; with one, the edited drawing
is written there. The input file is
never modified by an action run, which
is why this chapter's experiments each
start from the same badge.

Inkscape carries dozens of these verbs
— `--action-list` prints the catalogue
(sixty-odd entries in this build):
clones, exports, transforms, path
operations, selection tools. The window
user meets the same operations as menu
items and toolbar buttons; which clicks
drive which action is the documented
half of this chapter, but the
operations themselves are identical,
and every one this chapter and the next
uses was run, not read about.

## Scaling, checked by arithmetic

The star before (chapter 5): width
74.4996, height 68.3997, top-left at
(82.7502, 84.7502). After the run above,
the new file measures (transcript
`inkscape-lab/transcripts/t04-actions-transform.txt`):

```bash
inkscape badge-scaled.svg --query-id=star \
  --query-x --query-y --query-width --query-height
```

```text
64.1253
67.6503
111.749
102.6
```

74.4996 × 1.5 = 111.749, and 68.3997 ×
1.5 = 102.6 — to the digit. The scaling
is about the object's centre: the
centre was at x = 120 before
(82.7502 + 74.4996/2) and is at x =
119.9998 after (64.1253 + 111.749/2) —
the middle of the badge, unmoved, while
the star grew around it. Nothing else
in the file changed: this is the same
operation the window's Transform
dialogue performs, with the advantage
that its result here is a number you
can demand to see.

## Rotating, checked by shape

```bash
inkscape badge.svg \
  --actions="select-by-id:star;transform-rotate:30" \
  --export-filename=badge-rotated.svg
inkscape badge-rotated.svg --query-id=star \
  --query-width --query-height
```

```text
74.2451
71.0707
```

A five-pointed star is not symmetric
under 30 degrees, so a turned star
presents a different silhouette: the
box narrows slightly (74.4996 to
74.2451) and grows taller (68.3997 to
71.0707), exactly the direction a
one-point-up star leans when tipped.
Rotation, like scaling, happens about
the object's centre. The check is
weaker than the scale's — no single
multiplication predicts it — which is
itself the lesson: for some edits the
proof is exact arithmetic, and for
others it is a measurement moving the
right way by a believable amount, and
knowing which kind of proof you hold
is part of using the instrument well.

## Why drive it this way

Not because the mouse is lesser — for
drawing, the mouse is the tool. The
command form earns its place when the
edit is repetitive (forty icons resized
identically), when it must be exact
(1.5, not "about half as big again"),
when it must be repeated later by a
script, or when the person directing
it cannot see the screen and works —
as this whole guide does — by names and
numbers. Chapter 10 turns two of those
reasons into recipes.
