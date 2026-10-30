# Limits

What Inkscape will not do, will do
quietly wrong, or does in a way that
surprises — collected in one place, as
this series requires. Everything here
was met in the lab unless it is marked
as documented.

## Success that means nothing

The deepest limit is not a missing
feature. Inkscape's command line
reports success — exit code 0, no
complaint — for a missing input file,
for a query about an object that does
not exist, and for a drawing file cut
off in the middle, which it partially
repairs and exports as a different
picture on a different page size.
Chapter 13 gives the three cases in
full. The consequence is a rule, not a
worry: **a script that trusts
Inkscape's exit code will eventually
ship a wrong file.** Check the output —
its size, its contents, its colour
counts — the way chapters 5 and 6 do.

## The parser repairs, silently

That third case deserves its own line.
Inkscape reads SVG with a forgiving
XML parser. Damage that should stop a
stricter tool — an unclosed tag, a file
truncated mid-element — is repaired as
best the parser can, the salvage is
drawn, and the only evidence is error
text on stderr and an output that is
not what the file described. For
hand-written and machine-generated SVG
this kindness is a hazard masquerading
as robustness.

## Text is only half yours

A text object names a font it does not
contain (chapter 9). On any machine
without that font, the words redraw in
a substitute, at different widths, with
no report. The bounding box of
lettering is therefore a property of
the machine that measured it, not of
the file alone. Converting to paths
ends the dependence and the editability
in the same stroke.

## Conversions are one-way

Object-to-path destroys the recipe: no
radius to change, no words to retype
(chapter 8). Simplify approximates: the
new curve follows the old one's
average, and the original is not kept
anywhere. Neither operation warns, asks
or apologises. Work on copies; the
guide's every conversion wrote a new
file, and that habit is the limit's
practical answer.

## Simplify is not shrink

Measured, not assumed: the wobble's
path data *grew* from 2,385 to 3,730
characters while its commands fell from
182 to 11, because curve segments carry
more numbers each, at full precision.
Simplify trades node count for node
weight. Anyone promising it as a file
diet is selling the wrong half of the
result.

## Measurements include the paint

Every bounding box in this guide
includes half the stroke width on each
side (the ring: 230 measured, 224 of
shape). That is Inkscape's convention,
consistently applied — but a reader
comparing against another tool, or
against the raw geometry in the file,
will find small, real differences and
should know which side of them is the
stroke.

## The window is beyond this guide's evidence

The lab ran the command line only, so
this guide's authority ends where the
mouse begins: drawing feel, snapping,
the alignment tools, extensions that
open dialogues — all taught from
documentation, none of it verified
here. That is a limit of the guide,
stated in chapter 1, not of the
program.

## Print depth, and the version on the shelf

Two documented limits close the list.
Inkscape works in RGB; professional
print wants CMYK separations, spot
colours and press proofing, and while
workarounds and companions exist, that
world is not this program's home —
chapter 11's commercial bench earns
its money there. And the build verified
here, 1.2.2, is Ubuntu 24.04's from
December 2022; the project has released
newer series since, with interface and
command refinements this guide does
not describe. The operations it teaches
are old, stable parts of the program —
but a reader on the newest Inkscape
may find extra doors in rooms this
guide maps plainly.
