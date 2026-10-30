# Measuring the Drawing

Outcome: for every object in the badge,
you can say where it is and how big —
from Inkscape's own mouth, without
opening the window — and you can
reconcile each number with the file
that produced it. This is the guide's
basic instrument; chapters 7 and 8 read
their results off it.

## Ask for everything

```bash
inkscape badge.svg --query-all
```

```text
svg12,5,5,230,230
ring,5,5,230,230
label-path,26,26,188,188
label,13.9351,13.7075,212.404,212.387
disc,56.5,64.5,127,127
star,82.7502,84.7502,74.4996,68.3997
waves,86,162,68,12
```

(Transcript
`inkscape-lab/transcripts/t01-badge-and-queries.txt`,
which also prints the badge in full.)
Each line is one object: its id, then
the **bounding box** from chapter 2 —
the x and y of the box's top-left
corner, its width, and its height, in
the file's own units. The first line,
`svg12`, is the root of the drawing
itself.

## Reading the numbers against the file

The instrument is only worth having if
its answers can be checked. Take them
one at a time:

- **ring: 5, 5, 230, 230.** The circle
  is centred at (120, 120) with radius
  112, so the shape itself spans 224.
  Its stroke is 6 wide and counts in
  the box (chapter 2), adding 3 a side:
  230 across, starting at 120 − 115,
  which is 5. Exact.
- **disc: 56.5, 64.5, 127, 127.** Radius
  62 makes 124; stroke 3 adds 1.5 a
  side: 127. The y of 64.5 confirms the
  disc sits lower than centre — its
  centre is at y=128 by design.
- **star: 82.7502, 84.7502, 74.4996,
  68.3997.** The ten points span 72 wide
  (84 to 156) and about 65.9 high; the
  2.5-wide stroke and its rounded joins
  bring the box to the measured values.
  Four decimal places is normal here —
  the box hugs the painted edge, not the
  tidy numbers typed into the file.
- **label: 13.9351, 13.7075, 212.404,
  212.387.** The lettering is not a tidy
  shape; its box is wherever the curved
  words reach. Text boxes depend on the
  font doing the drawing — chapter 9's
  warning lives in numbers like these.
- **waves: 86, 162, 68, 12.** One path,
  five humps, 68 wide; the height of 12
  is the humps' 8 plus the 4-wide stroke.
- **label-path: 26, 26, 188, 188.** The
  invisible rail is a circle of radius
  94: 188 across, centred, with no
  stroke to add. It measures exactly
  like a visible object, because
  measuring does not care about paint.

## One object at a time

The same questions can be asked of a
single object, which is the form later
chapters use after an edit:

```bash
inkscape badge.svg --query-id=star \
  --query-x --query-y --query-width --query-height
```

```text
82.7502
84.7502
74.4996
68.3997
```

The four answers arrive in the order
the options were asked. Nothing is
labelled, so ask in a fixed order and
keep it — the guide always asks
x, y, width, height.

## The discipline this buys

Two habits follow from having an
instrument. First: **list before you
ask.** Chapter 13 shows why — a query
for an id that does not exist does not
fail; it quietly answers for the whole
drawing instead, and 230 looks like a
measurement until `--query-all` says
there is no such object. Second:
**measure before and after.** Every
edit in chapters 7 and 8 is presented
as a pair of measurements with the
arithmetic between them. An edit you
cannot measure is an edit you are
taking on trust, and this tool's
command line makes trust unnecessary
surprisingly often.
