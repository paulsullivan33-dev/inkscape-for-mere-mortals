# Exporting — PNG and PDF

Outcome: the badge as a picture for the
web at two sizes, and as a PDF for
print — each one proved to contain the
drawing, in the right colours, at the
size on the label. Exporting is where
vector drawings meet the pixel world,
and where a silent failure does the
most damage, so this chapter proves as
it goes.

## PNG, at the size you ask for

```bash
inkscape badge.svg --export-type=png \
  --export-width=480 --export-filename=badge-480.png
inkscape badge.svg --export-type=png \
  --export-width=96 --export-filename=badge-96.png
```

Success is silent, which chapter 13
will teach you to distrust; so check.
An independent tool reads the files'
own headers:

```bash
file badge-480.png badge-96.png
```

```text
badge-480.png: PNG image data, 480 x 480, 8-bit/color RGBA, non-interlaced
badge-96.png:  PNG image data, 96 x 96, 8-bit/color RGBA, non-interlaced
```

480 by 480 and 96 by 96, as ordered —
and note what did not happen to the
smaller one. It is not a shrunken,
blurred copy of the bigger; Inkscape
drew the badge again at 96 pixels, from
the same numbers. That is the whole
point of chapter 1, arriving as a file
size.

## Proving the picture

A header says a picture exists. It does
not say the picture is the badge. The
lab's checker — `inkscape-lab/check-png.py`,
kept in the lab folder — opens the
pixels with an ordinary image library
and counts them (transcript
`inkscape-lab/transcripts/t02-png-exports.txt`):

```text
badge-480.png: 480x480 px, 995 distinct colours,
167020 of 230400 pixels not transparent
    (253, 246, 227, 255): 87940 px
    (255, 255, 255, 0): 63380 px
    (42, 157, 143, 255): 35189 px
```

Read it against the file from chapter
4. **995 distinct colours** — a real
drawing with antialiased edges, not a
flat placeholder. The commonest colour,
(253, 246, 227), is decimal for the
ring's cream fill `#fdf6e3`, at 87,940
pixels. Third is (42, 157, 143), the
disc's teal `#2a9d8f`, at 35,189.
Counting exactly, the navy `#264653` of
the ring's edge and the letters covers
27,414 pixels, and the star's gold
`#e9c46a` 5,814 — the lettering is in
the picture, not just the shapes under
it. And 63,380 pixels are fully
transparent: the page's corners,
outside the round badge, exactly where
chapter 2 said they would be. A blank
export — the classic silent failure —
would show one colour and no others;
this shows the badge's whole palette,
in proportions that match its design.

## PDF, for print

```bash
inkscape badge.svg --export-type=pdf \
  --export-filename=badge.pdf
```

```bash
pdfinfo badge.pdf
```

```text
Creator:         Inkscape 1.2.2 (https://inkscape.org)
Producer:        cairo 1.18.0 (https://cairographics.org)
Pages:           1
Page size:       180 x 180 pts
```

(Transcript t03.) The PDF is one page,
drawn by the cairo library Inkscape
uses for print formats. Page size 180
points is the 240-unit page in printer's
measure: a PDF point is 1/72 of an
inch, a screen pixel 1/96, so 240 units
leave as 240 × 72/96 = 180 points —
2.5 inches square at print size, with
the shapes inside still vectors,
scaling to whatever the printer can
do. Sending this to a print shop sends
the numbers, not a grid.

## The knobs that matter

Three options cover most real exports,
and all are variations on the runs
above. `--export-width` and
`--export-height` set the PNG's pixel
size directly (the guide's way — say
the size, don't compute it).
`--export-dpi` sets it by resolution
instead: the same badge at 300 dpi
leaves 750 pixels wide, the print-trade
way of asking. And the export area —
page, whole drawing, or a hand-set
rectangle — decides what is in the
frame; the exports above used the
default page area, which is why the
corners are transparent, and the
drawing-area variant
(`--export-area-drawing`) that trims to
the badge's own edges is documented
behaviour this lab did not run.
Chapter 10 uses one more form: a single
object exported on its own.
