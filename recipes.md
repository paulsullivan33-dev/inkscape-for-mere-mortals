# Recipes

Each recipe here is assembled from
operations the earlier chapters ran and
proved; where a recipe adds a step the
lab did not run, the step is flagged
rather than smuggled in.

## One object, on its own

The star, as its own picture, at its
own size (chapter 5's box, chapter 6's
method):

```bash
inkscape badge.svg --export-id=star \
  --export-id-only --export-type=png \
  --export-filename=star-only.png
```

Inkscape even narrates this one:
"Exporting only object with id="star";
all other objects hidden." The result
(transcript
`inkscape-lab/transcripts/t07-export-one-object.txt`)
is a 74 by 68 PNG — the star's bounding
box at the default 96 dpi, gold star,
navy edge, nothing else. The uses are
everyday: an icon pulled from a logo
sheet, one diagram element reused in a
document, a single part sent to a
cutter. The discipline is chapter 5's:
the id must exist, so list first.

## Plain SVG, for the web

A file Inkscape saves carries its
workshop notes — extra namespaces
(`sodipodi`, `inkscape:`) recording
things like the window's last view.
Browsers ignore them; tidiness and the
occasional strict tool do not. The
plain export strips them:

```bash
inkscape badge-scaled.svg \
  --export-plain-svg \
  --export-filename=badge-scaled-plain.svg
```

Transcript t08 has the measurements:
2,205 bytes become 1,779, the sodipodi
mentions go from 3 to 0, and the
drawing is unchanged — plain SVG is
the same picture with the notes torn
off. Hand the plain one to web pages
and other programs; keep Inkscape's
own save as your working copy, because
the notes are how it remembers your
setup.

## A run of sizes, in one pass

Chapter 6 exported two sizes as two
commands. A shell loop turns that into
every size a project needs — favicon,
page, poster — from the one file:

```bash
for w in 32 96 256 480 1024; do
  inkscape badge.svg --export-type=png \
    --export-width=$w \
    --export-filename=badge-$w.png
done
```

The two middle sizes are chapter 6's
verified runs; the loop around them is
ordinary shell, and the same
`check-png.py` pass afterwards proves
the set — every file present, at its
labelled size, with the badge's
palette inside. Because each export is
drawn fresh from the vectors, the 32
and the 1024 are equals: small is not a
degraded big.

## Smooth a shaky line

A scanned sketch traced to paths, or a
line drawn with a unsteady hand,
arrives as chapter 8's wobble did —
hundreds of segments of jitter. The
recipe is that chapter's run:

```bash
inkscape drawing.svg \
  --actions="select-by-id:wobble;path-simplify" \
  --export-filename=drawing-smooth.svg
```

with the id replaced by your path's,
and `count-segments.py` before and
after as the evidence. Simplify on a
copy, never the original: the
approximation cannot be unaveraged,
and the wobble sometimes *was* the
drawing — a coastline, a signature.

## Measure before you print

Before a drawing goes to a printer or
a cutter, ask it the print questions
with chapter 5's instrument:
`--query-all` for what is in it, and the
page size against the paper. The
badge's page is 240 units — 2.5 inches,
180 points, as chapter 6's PDF showed.
A drawing that measures 240 units and
was designed as a 24-inch banner is
not wrong, because vectors scale; but
its stroke widths and letter sizes, in
real inches, are worth one multiplication
before the print shop does it for you.
