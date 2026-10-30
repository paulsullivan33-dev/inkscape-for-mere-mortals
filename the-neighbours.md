# The Neighbours

Inkscape sits in a crowded workshop.
These are the tools a reader is most
likely to confuse it with, reach for
instead, or meet alongside — what each
does that Inkscape doesn't, and the
reverse. They are characterised from
their documentation and this series'
own guides, not benchmarked here; the
one this lab ran is Inkscape.

## GIMP — the pixel side

GIMP edits raster pictures: photographs,
scans, screenshots. Its world is the
fixed grid — retouching, compositing,
colour correction — everything chapter
1 said a vector drawing is not. The two
tools meet constantly in real work: a
logo drawn in Inkscape is exported to
PNG (chapter 6) and finished in GIMP; a
photo prepared in GIMP is placed inside
an Inkscape layout. The test for which
tool: if the thing you are editing is
*made of shapes*, Inkscape; if it is
*made of pixels*, GIMP. This series'
GIMP guide covers that side in full.

## Diagrams from code — Graphviz and friends

Some drawings are better described
than drawn: family trees, organisation
charts, network maps with two hundred
boxes. Graphviz and its kin take a text
list of nodes and arrows and lay the
diagram out themselves. Inkscape is
where such a diagram goes afterwards
to be tidied, coloured and lettered —
and where a diagram with twelve boxes
should probably have started, drawn by
hand in minutes. The series' Graphviz
guide covers the code-drawn side;
chapter 4 of this guide, writing a
drawing as text at all, is the bridge
between the two habits of mind.

## Code-drawn solid things — OpenSCAD, CAD

OpenSCAD and the CAD tools also produce
exact drawings from numbers, but their
numbers mean *parts*: dimensions,
tolerances, things that must fit other
things. Inkscape's numbers mean
*appearance*: this curve looks right.
Feeding a laser cutter from Inkscape is
normal craft practice; designing a
gearbox in it would be a category
error. The series' OpenSCAD and CAD
guides live on that side of the line.

## Illustrator, Affinity, CorelDRAW — the commercial bench

Adobe Illustrator is the professional
incumbent: the same vector model, a
deeper bench of tools, print-trade
depth Inkscape does not attempt
(chapter 12), and a subscription.
Affinity Designer and CorelDRAW sell
the same territory for a single
payment. Drawings move between all of
them and Inkscape through SVG and PDF,
imperfectly — fonts (chapter 9) and
each program's private features are
where the seams show. Inkscape's
counters are price, openness, and an
SVG file that is native rather than
exported: what you save is what the
web reads.

## The browser, quietly

Every modern web browser is an SVG
viewer, and most can print one to PDF.
For a drawing that only needs *showing*
— chapter 4's free check — the browser
is the fastest neighbour of all. It
edits nothing, which is exactly its
virtue as a second opinion: what the
browser draws is what the file says,
with no editor's kindness in between.
