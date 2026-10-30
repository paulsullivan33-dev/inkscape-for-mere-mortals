# Inkscape for Mere Mortals

A photograph is a grid of coloured dots.
Make it bigger and the dots just get
bigger with it: edges go soft, then
blocky. A **vector** drawing is built
the other way round. It is not dots at
all but a list of shapes — a circle is
stored as a centre and a radius, a star
as ten corner points — and the picture
is worked out from those numbers every
time it is shown. **Inkscape** is the
free program that draws this way. It
stores its drawings as **SVG**, a text
format you can open in any editor and
read with your own eyes, and the same
small file prints as a sharp badge, a
poster, or a web icon, because the size
is decided at the last moment, from the
numbers.

This guide explains what a vector
drawing is made of, how to install
Inkscape, and how to make, measure and
export a drawing. It takes an unusual
route for a drawing program: everything
is done from the **command line**, which
Inkscape supports in full, and every
result is **proved** — the exported
pictures are taken apart pixel by pixel,
the geometry is checked against the
arithmetic, and the edits are measured
before and after. The lab that wrote
this guide had no screen it could draw
on, so it never once claims a picture
*looks* right. It shows you the numbers
that say the drawing is there, at the
size claimed, in the colours asked for.

The lab ran the real thing: **Inkscape
1.2.2**, Ubuntu 24.04's own build of it,
against one small drawing — a badge for
an invented coffee shop, written out as
a text file in chapter 4. Against that
badge the lab measured every object,
exported it as PNG at two sizes and as
PDF, counted the colours and the exact
pixels of each part, scaled and rotated
the star by command and checked the new
measurements to the fourth decimal,
turned circles and lettering into raw
paths, simplified a 181-segment wobbly
line down to 11 smooth commands, and
deliberately broke things: a missing
file, a wrong object name, and a drawing
cut off in mid-sentence — all three of
which Inkscape forgives so quietly that
only checking the output catches them.

What the lab could not do, it did not
fake. Drawing with the mouse — the way
most people will actually use Inkscape —
is taught from the program's own
documentation and labelled as such
wherever it appears. `criteria.md`
keeps the full ledger of what was run
and what was only read.

## What this guide covers

- [**What Inkscape is**](what-inkscape-is.md) —
  the mental model: shapes and numbers
  in, a picture out at any size, and
  why a drawing stored as text is a
  feature, not a quirk
- [**The moving parts**](the-moving-parts.md) —
  the page, the objects and their names,
  shapes and paths, fills and outlines,
  and the box every object lives in
- [**Installing Inkscape**](installing-inkscape.md) —
  the ordinary install routes, and the
  version check that proves it runs
- [**Your first drawing**](your-first-drawing.md) —
  a complete badge written as a text
  file, read line by line, and seen for
  free in any web browser
- [**Measuring the drawing**](measuring-the-drawing.md) —
  asking Inkscape where every object is
  and how big, and why the answers
  include the width of the outlines
- [**Exporting — PNG and PDF**](exporting-png-and-pdf.md) —
  the same badge as a web picture at two
  sizes and as a print-ready PDF, with
  the pictures proved pixel by pixel
- [**Editing by command**](editing-by-command.md) —
  selecting an object by name and
  scaling or rotating it, with the
  results checked against the arithmetic
- [**Shapes into paths**](shapes-into-paths.md) —
  turning circles and letters into raw
  paths, and smoothing a wobbly line
  from 182 commands down to 11
- [**Text and fonts**](text-and-fonts.md) —
  words on a curve, and the catch: your
  letters are drawn by whatever font the
  viewing machine happens to have
- [**Recipes**](recipes.md) — one object
  exported on its own, plain SVG for the
  web, a run of picture sizes in one
  pass, and a measuring habit for print
- [**The neighbours**](the-neighbours.md) —
  GIMP the pixel editor, diagrams drawn
  by code, and the commercial rivals:
  what each does that Inkscape doesn't,
  and vice versa
- [**Limits**](limits.md) — exit codes
  that say success when nothing worked,
  a parser that repairs damage silently,
  fonts that travel badly, and smoothing
  that moves numbers while it removes
  them
- [**Troubleshooting**](troubleshooting.md) —
  the three forgiving traps, the export
  that came out blank, the warning that
  means nothing, and the name that
  answered for the whole drawing
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Drawing on paper's behalf at print-shop
depth — colour separations, spot
colours and press proofing are a
professional world of their own, pointed
at in chapter 12, not taught. Photo
editing is likewise another tool's job:
the GIMP guide in this series covers
the pixel side. Engineering drawing
with tolerances belongs to the CAD
guides. And while chapter 4 writes a
drawing as text because the lab could
check every character of it, nobody is
expected to work that way for real art:
the mouse chapters are labelled
documented-only because the lab had no
screen, not because the mouse is the
wrong way to draw.

## How to use this guide

Read chapter 1 for the model, and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapter 4 hands you the badge the whole
guide uses; chapters 5 and 6 measure it
and export it in the same sitting.
Chapter 6 is the one to read slowly
even if you have a screen: its checks
are how you catch the silent successes —
the exports that report nothing wrong
and contain nothing you wanted — before
they reach a printer or a web page. The
lab's transcripts live in
`inkscape-lab/transcripts/`; its badge
is `inkscape-lab/badge.svg`, and its
measuring scripts are
`inkscape-lab/check-png.py` and
`inkscape-lab/count-segments.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [GIMP for Mere Mortals](https://paulsullivan33-dev.github.io/gimp-for-mere-mortals/)
- [Graphviz for Mere Mortals](https://paulsullivan33-dev.github.io/graphviz-for-mere-mortals/)
- [OpenSCAD for Mere Mortals](https://paulsullivan33-dev.github.io/openscad-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/inkscape-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/inkscape-for-mere-mortals/blob/main/LICENSE-CODE).
