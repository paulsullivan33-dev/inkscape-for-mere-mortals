# Your First Drawing

Outcome: a complete drawing on disk —
the badge every later chapter measures,
edits and exports — and two proofs that
it is real before Inkscape is even
opened: the file describes itself, and
a web browser draws it.

Most first drawings are made with the
mouse, and yours can be too. This one
is written as a text file, for a reason
worth stating: the lab that wrote this
guide works without a screen, and a
drawing in text can be checked
character by character, quoted in full,
and regenerated identically by anyone.
Nothing about the result is second
class — Inkscape opens this file
exactly as it opens a drawn one. The
window's way of making the same shapes
is the documented half of this guide;
the file below is the verified half.

## The badge

Save this as `badge.svg`. It also lives
in the lab as `inkscape-lab/badge.svg`,
character for character.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg width="240" height="240" viewBox="0 0 240 240"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">
  <title>North Pier Coffee badge</title>
  <!-- outer ring -->
  <circle id="ring" cx="120" cy="120" r="112"
          fill="#fdf6e3" stroke="#264653" stroke-width="6"/>
  <!-- the path the label text runs along (not drawn itself) -->
  <path id="label-path" fill="none" stroke="none"
        d="M 120,120 m -94,0 a 94,94 0 1,1 188,0 a 94,94 0 1,1 -188,0"/>
  <!-- words around the ring -->
  <text id="label" font-family="DejaVu Sans" font-size="16.5"
        font-weight="bold" fill="#264653" letter-spacing="2">
    <textPath xlink:href="#label-path" startOffset="2">
      NORTH PIER COFFEE &#8226; FRESH EVERY DAY &#8226;
    </textPath>
  </text>
  <!-- inner disc -->
  <circle id="disc" cx="120" cy="128" r="62"
          fill="#2a9d8f" stroke="#264653" stroke-width="3"/>
  <!-- five-pointed star, centre 120,120, outer r 34, inner r 13.6 -->
  <polygon id="star" fill="#e9c46a" stroke="#264653" stroke-width="2.5"
           stroke-linejoin="round"
           points="120,86 130.5,109.5 156,110.6 136.6,127.3 143,151.9
                   120,138 97,151.9 103.4,127.3 84,110.6 109.5,109.5"/>
  <!-- waves under the star -->
  <path id="waves" fill="none" stroke="#fdf6e3" stroke-width="4"
        stroke-linecap="round"
        d="M 88,168 q 8,-8 16,0 t 16,0 t 16,0 t 16,0"/>
</svg>
```

It is a badge for an invented coffee
shop: a cream ring with a navy edge,
the shop's name lettered around the
inside, a teal disc, a gold star, and
a line of pale waves for the water.
North Pier Coffee does not exist, which
is the point of a fixture — the shapes
are what matters, and they are all
ordinary ones.

## Reading it

Top to bottom, the file says:

- The `<svg>` header sets the stage:
  a page 240 units square, and a
  **viewBox** — the rule that those
  coordinates mean the same drawing at
  any display size.
- `ring` is a **circle** by recipe:
  centre (120, 120), radius 112, cream
  fill, navy stroke 6 wide.
- `label-path` is a circle drawn as a
  **path** of two arcs — and painted
  with nothing at all. It exists only
  so the next object has a rail to run
  on.
- `label` is **text**: the shop's name,
  set on the label-path with a
  `textPath`, so the words bend around
  the ring. Chapter 9 takes this apart.
- `disc` is another circle, lower and
  smaller — its centre is at y=128, not
  120, leaving room for the words at
  the top.
- `star` is a **polygon**: ten points,
  alternating outer and inner, which is
  all a five-pointed star is.
- `waves` is one path of little humps:
  `q` curves up and over, and each `t`
  repeats the hump, mirror-wise, five
  times across.

Five object kinds — circle, path,
text, polygon, and a text-on-a-path —
cover a surprising share of all real
logos, and each one gets a chapter's
worth of handling later.

## The two free checks

First, ask the file system what the
file is:

```bash
file badge.svg
```

```text
badge.svg: SVG Scalable Vector Graphics image
```

The answer comes from the file's own
contents, not its name — a mislabelled
file would be caught here.

Second, open `badge.svg` in any web
browser. Browsers draw SVG natively,
and the badge appears: ring, words,
disc, star, waves. No Inkscape, no
plugins, nothing to install. This is
the reader-with-a-screen version of the
proof habit the whole guide uses — the
drawing is checked by something other
than the program that will edit it. The
lab, having no browser it could look
through, used Inkscape's own measuring
commands and the pixel counts of
chapter 6 as its second opinion
instead, which is where the guide goes
next.
