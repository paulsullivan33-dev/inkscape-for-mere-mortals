# Text and Fonts

Outcome: you can explain where the
badge's curved lettering comes from,
and name the one thing about text that
no other object in the drawing suffers
from — it is not fully *in* the file.
The check is chapter 6's export: the
navy pixels counted there include the
letters, drawn by a font this machine
chose.

## Words on a rail

The badge's label is one text object
doing something text rarely gets to do
on paper: bending. Its mechanism, from
chapter 4's file:

```xml
<path id="label-path" fill="none" stroke="none"
      d="M 120,120 m -94,0 a 94,94 0 1,1 188,0 a 94,94 0 1,1 -188,0"/>
<text id="label" font-family="DejaVu Sans" font-size="16.5"
      font-weight="bold" fill="#264653" letter-spacing="2">
  <textPath xlink:href="#label-path" startOffset="2">
    NORTH PIER COFFEE &#8226; FRESH EVERY DAY &#8226;
  </textPath>
</text>
```

The text names a **textPath**, and the
textPath names a path — the invisible
circle of radius 94. Inkscape walks the
words along that rail, letter by
letter, turning each one to follow the
curve; `startOffset` says where along
the rail the first letter sits, and
`letter-spacing` spreads the words so
they fill the ring. Delete the rail and
the words have nowhere to bend around;
chapter 5 measured both — the rail a
tidy 188 by 188, the words an untidy
212 by 212, because letters lean out
from the rail on their stems and
curves. In the window, the same effect
is Text → Put on Path; the file form
here is the verified half, the menu the
documented.

## The font is not in the file

Read the text object again: it carries
a font *name* — DejaVu Sans — and no
font. The letter shapes live in a font
file on the machine doing the drawing.
Inkscape asks the machine for DejaVu
Sans, the machine's font system hands
over the shapes, and those are what
chapter 6 counted: 27,414 navy pixels,
letters among them, drawn by *this*
machine's DejaVu Sans.

Now send the badge somewhere else. If
that machine has the font, the words
look the same. If it has a different
font under a similar name, or falls
back to a substitute, the words still
appear — in another face, at slightly
different widths, with a different
bounding box than chapter 5 measured.
Nothing reports the change. This is
the single most common way a vector
drawing "goes wrong" in transit, and it
is wrongness no exit code will ever
mention, because nothing failed: the
file asked for a font by name and got
what the machine had.

DejaVu Sans was a deliberate choice for
the fixture: it ships with most Linux
systems, so the badge's words draw
almost anywhere a reader of this guide
is likely to stand. Choosing widely
available fonts — or bundling the
drawing as PDF, where chapter 6's
cairo export renders the letters into
the page — is the everyday defence.

## Freezing the words

The complete defence is chapter 8's:
when the words are final and the
drawing is leaving home, convert the
text to paths. The letters become
shapes — 32 of them for this label —
identical on every machine forever,
because there is no longer a font
involved. What is lost is everything
that makes text text: searchability,
editing, the words themselves. The
guide's rule, stated there and repeated
here because it is the chapter in one
line: *text while you are writing,
paths when you are shipping.*

## A word about other people's letters

Fonts are software, and software has
licences. The handsome display face on
a font website may be free for a
poster and forbidden for a logo, or
free everywhere except embedded in a
file you sell. Converting text to paths
does not launder a font's licence — the
letter shapes are still the designer's
work. The badge's DejaVu Sans is an
open font, free for this use; before
real lettering leaves home, its font
deserves the same ten seconds of
checking as any other borrowed thing.
