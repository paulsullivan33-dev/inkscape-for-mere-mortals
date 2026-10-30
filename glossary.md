# Glossary

**Action** — a named operation
Inkscape can perform on a selection,
driven from the command line
(`--actions="..."`) or by the window's
menus. Chapter 7.

**Bézier curve** — the standard curve
of vector drawing: a segment whose
bend is set by control handles on its
end nodes. What simplify produces from
straight segments. Chapter 8.

**Bounding box** — the smallest upright
rectangle containing an object,
reported as corner x, corner y, width,
height. In Inkscape it includes half
the stroke width on every side.
Chapter 5.

**DPI** — dots per inch; the resolution
an export is drawn at when size is
given by resolution rather than pixels.
Chapter 6.

**Export** — writing the drawing (or
part of it) in another format — PNG,
PDF, plain SVG — usually at a chosen
size. Chapters 6 and 10.

**Fill** — the paint inside a closed
object; may be a colour, a gradient, a
pattern, or none. Chapter 2.

**Font** — a file of letter shapes,
owned by the machine, that a text
object refers to by name. The drawing
does not contain it. Chapter 9.

**Group** — a collection of objects
that moves, scales and converts as
one. Chapter 2.

**Id** — an object's unique name inside
the file (`star`, `disc`), used to
select and query it. Chapters 2 and 5.

**Layer** — a named group in a list of
such groups, the standard way to keep
a complicated drawing in coats.
Chapter 2.

**Node** — a point on a path; segments
run between nodes, and editing a path
is largely moving its nodes.

**Object** — anything in a drawing: a
shape, a path, text, a group, a placed
picture. Chapter 2.

**Object to path** — the conversion
that replaces a shape's recipe, or a
text object, with the raw paths that
draw it. One-way. Chapter 8.

**Path** — a chain of points joined by
straight lines and curves; the
universal geometry underneath every
shape. Its file form is the `d`
attribute of letters and numbers.

**Plain SVG** — SVG with a program's
private editor notes stripped out; the
same drawing, for handing to other
software and the web. Chapter 10.

**Query** — asking Inkscape, from the
command line, for an object's bounding
box (`--query-id`, `--query-all`, and
friends). Chapter 5.

**Raster** — a picture stored as a
grid of pixels: a photo, a PNG, a JPEG.
Fixed at its saved size. Chapter 1.

**Segment** — one straight or curved
piece of a path, between two nodes.
Chapter 8 counts them.

**Simplify** — the operation that
replaces many small segments with fewer
smooth curves approximating them.
Chapter 8.

**Stroke** — the paint on an object's
outline, with its own colour and width;
may be none. Counted in bounding boxes.
Chapter 2.

**SVG** — Scalable Vector Graphics:
the text format Inkscape saves, an XML
description of shapes that browsers
and printers draw at any size.

**Text path** — a path used as a rail
for lettering, so words follow its
curve. Chapters 4 and 9.

**Vector** — a picture stored as shapes
described by numbers, drawn fresh at
whatever size is asked. Chapter 1.

**ViewBox** — the coordinate rule in
an SVG header that maps the file's
numbers onto any display size.
Chapter 4.
