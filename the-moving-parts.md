# The Moving Parts

By the end of this chapter you can name
every part of an Inkscape drawing, and
say which part holds what — the
knowledge that turns "it looks wrong"
into a sentence with an object in it.
The check: run `inkscape badge.svg
--query-all` on the chapter 4 badge and
match each line to a part named here.

## The document and the page

A drawing lives in a **document**: one
SVG file. Inside it sits the **page**,
the rectangle the drawing is composed
on — the badge's page is 240 by 240
units. The page matters at export time,
because a PNG export normally pictures
the page, corners and all; the badge's
corners are empty, which is why chapter
6 finds transparent pixels there.
Things can also live off the page —
Inkscape allows a working area around
it — but what exports by default is the
page.

Units inside the file are just numbers.
SVG calls them user units; Inkscape
shows them as pixels, millimetres or
inches depending on settings, and
chapter 6 shows the same 240-unit page
leaving as 480 pixels and as a
180-point PDF page. The numbers in the
file never change; only the ruler at
the edge does.

## Objects, and their names

Everything in a drawing is an
**object**: a shape, a line of text, a
picture placed inside. Every object
can carry an **id**, a unique name —
`ring`, `disc`, `star`, `label`,
`waves` in the badge. The id is how the
command line talks about one object
among many, how chapter 7 selects the
star and nothing else, and how chapter
10 exports it alone. In the window, ids
are set in the Object Properties
dialogue; in the file, they are just an
attribute among others. An object
without an id still draws; it is simply
harder to address.

Objects stack. Later objects in the
file draw over earlier ones: in the
badge, the disc is listed after the
ring, so the teal disc covers the
ring's middle, and the star sits on
top of the disc. In the window this is
the Raise and Lower business; in the
file it is reading order, top of file
to bottom, back to front.

## Shapes and paths

Some objects are **shapes** with a
recipe: a circle knows its centre and
radius, a rectangle its corner and
sides, a star its points. Shapes are
convenient — change the radius number,
get a bigger circle — and limited: a
circle recipe cannot grow a dent.

Underneath every shape sits a **path**:
a chain of points joined by straight
lines and curves. Paths are the
universal currency. Any shape can be
converted into one (chapter 8 does it,
and watches a circle become four arcs),
lettering can be converted into them,
traced pictures arrive as them. A path
is drawn by **segments**; each segment
runs between **nodes** (points), and
curved segments bend according to
handles attached to their nodes — the
idea chapter 8 uses when it counts a
path's commands before and after
simplifying.

In the file, a path's whole geometry
is one attribute, `d`, a compact string
of letters and numbers: `M` moves the
pen, `L` draws a straight line, `C`
draws a curve, `Z` closes the shape.
The badge's waves are a single path of
quadratic curves, five humps in one
string.

## Fill and stroke

Every closed object has two paint
jobs. The **fill** colours the inside;
the **stroke** colours the outline, and
has a width. Either can be switched off
(`fill="none"`), which is how the
badge's invisible label-path exists:
it is a circle with no paint at all,
there only to carry words around the
ring (chapter 9).

Colour is written as three pairs of
hexadecimal digits, red, green, blue:
`#2a9d8f` is the disc's teal. Chapter 6
meets those exact numbers again from
the other side, counted as pixels —
(42, 157, 143) is `#2a9d8f` read in
decimal, and the export contains
35,189 pixels of it.

## The bounding box

Ask where an object is and Inkscape
answers with its **bounding box**: the
smallest upright rectangle that
contains it, given as the x and y of
its top-left corner plus its width and
height. One subtlety runs through the
whole guide: **the box includes the
stroke**. The ring's circle is 224
units across (twice its radius of 112),
but its box measures 230 — the 6-unit
outline adds 3 on every side. Every
measurement in chapters 5 and 7 carries
that extra half-stroke, and forgetting
it makes good arithmetic look wrong.

## Groups, layers, and text

Objects can be gathered into a
**group**, which moves, scales and
hides as one thing; chapter 8's
converted lettering comes back as a
group of 32 letter-shaped paths.
**Layers** are groups with a name and a
place in a list, the standard way to
keep a complicated drawing in coats —
sketch on one, ink on another. The
badge is small enough to need neither,
and the guide keeps them as concepts
rather than procedures: the lab could
not click through the Layers panel, so
it teaches what layers are and leaves
their buttons to the documentation.

**Text** is an object like any other,
with two special properties the guide
returns to. It is set in a **font** —
a separate file of letter shapes, owned
by the machine, not the drawing — and
it can be made to follow a path, as the
badge's label follows its invisible
circle. Chapter 9 is devoted to both,
and to the trouble the first one
causes when a drawing moves to a
machine with different fonts.
