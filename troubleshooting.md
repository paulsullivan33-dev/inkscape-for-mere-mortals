# Troubleshooting

The failures this guide actually met,
in the order a reader is likely to
meet them. Transcript
`inkscape-lab/transcripts/t09-three-traps.txt`
holds the first three, verbatim.

## "It ran fine" — and the file is wrong

The master trap, from which the others
hang. Inkscape's command line exits 0
on almost everything, including total
failure. A run that prints nothing and
exits 0 has told you nothing. The
defence is the guide's standing habit:
after any run that matters, interrogate
the output — `file` for its type and
size, `check-png.py` for its contents,
a query for its geometry. Three
specific forms follow.

## The missing file that opens anyway

```bash
inkscape nofile.svg --query-all
```

```text
** (inkscape:...): WARNING **: Can't open file:
.../nofile.svg (doesn't exist)
ink_file_open: '.../nofile.svg' cannot be opened!
InkscapeApplication::document_open: Failed to open: ...
ConcreteInkscapeApplication::on_open: failed to create document!
```

Four complaints, no results — and exit
code 0. In a script this looks exactly
like a drawing with no objects. The
tell is on stderr, which is why scripts
should treat *any* stderr naming the
input file as failure, whatever the
exit code says.

## The name that answered for the whole drawing

```bash
inkscape badge.svg --query-id=nosuchthing --query-width
```

```text
select_by_id: Did not find object with id: nosuchthing
230
```

One quiet line on stderr, then a
perfectly good number — the width of
the entire drawing — presented as the
missing object's measurement. A typo'd
id does not stop a query; it demotes
it to the whole page. The fix is
chapter 5's discipline: `--query-all`
first, and treat `select_by_id: Did
not find` as the error it is.

## The drawing that was cut off, and drew anyway

A badge file truncated mid-tag produced
(libxml's words, verbatim):

```text
broken.svg:2: parser error : Couldn't find end of Start Tag circle line 1
broken.svg:2: parser error : Premature end of data in tag svg line 1
```

— and then a finished PNG export, exit
0. Inside it: a black circle, alone, on
a 300 by 150 page the original never
had. The parser salvaged the unclosed
element, defaulted its paint to black,
defaulted the page, and Inkscape drew
the salvage. Parser errors on stderr
mean the picture is not the file, even
when a picture arrives. Unexpected
dimensions — 300 by 150 for a 240
drawing — are the smoke; check sizes
against expectations, always.

## The export that came out blank

A PNG export with nothing in it has a
short list of usual causes, and
`check-png.py` separates them in one
run. If it reports **one colour, all
transparent**: the frame held nothing —
wrong export area, or the objects live
off the page. If it reports the
*background only*: the object you
wanted was not in the frame — and if
the export named an object with
`--export-id`, check the spelling
against `--query-all` before anything
else, because chapter 5 showed how
quietly a wrong name can pass in this
program. If it reports the
right colours at the *wrong size*: the
width, height and dpi options argue —
set one, let the others follow. A blank
export is never a mystery once the
pixels are counted; it is only a
mystery while the exit code is being
believed.

## The warning that means nothing

From chapter 3:

```text
** (inkscape:...): WARNING **: Failed to wrap object of type
'GtkRecentManager'...
```

Desktop bookkeeping noise on machines
without a session for it; the command's
real output is unaffected. Learn to
tell it apart from warnings that name
your file, your object or your parser
— those three above all matter. The
rule: a warning is about whatever it
names.

## The letters changed on another machine

The drawing opens elsewhere and the
words are wider, narrower, a different
face entirely. Nothing broke: the file
names a font the second machine lacks,
and a substitute drew the words —
chapter 9's whole story. Confirm by
asking that machine's Inkscape for the
label's bounding box and comparing with
chapter 5's; different numbers give it
away. Cure for shipping: embed by
converting to paths (chapter 8), or
export the PDF, which carries the
letters as drawn.

## The file grew when I simplified it

It did; chapter 8 measured it doing so
(2,385 to 3,730 characters). Fewer
commands, heavier commands. Not a bug
and not a failed run — simplify is
about nodes you can edit, not bytes.
