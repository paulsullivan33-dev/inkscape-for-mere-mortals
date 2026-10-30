# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's drawing is a badge for an invented coffee shop.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   does badly or surprisingly: exit code 0 on missing files,
   failed queries and damaged input alike; a parser that
   repairs truncated files and exports the salvage; query
   fallback to the whole drawing on a misspelled id; text that
   depends on fonts the file does not contain; one-way
   conversions; simplify growing the file it smooths; bounding
   boxes that include the stroke; and a guide whose evidence
   stops at the command line.
8. **The reuse rule is in the text, early.** Inkscape raises no
   interception question of the kind other guides in this
   series carry, but it has a line of its own, drawn in
   chapter 1 and again in chapter 9 before the procedures that
   lean on it: tracing a picture turns it into paths, not into
   your property, and fonts are other people's work with
   licences of their own — converting text to paths does not
   change that.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox,
shared with other work while the lab ran. Inkscape **1.2.2**
(Ubuntu package `inkscape 1.2.2-2ubuntu12`, build b0a8486541)
was obtained as the distribution's own `.deb` files — the
Inkscape package plus fourteen library packages it needed,
24 MB in all — and unpacked with `dpkg -x` into a private
tree, because the sandbox could not install packages
system-wide. The binary run throughout is the distribution's
own, unmodified, reached through a small wrapper that sets
`LD_LIBRARY_PATH` to the unpacked libraries; transcript t00
shows the package list, the unpack step and the wrapper. All
transcripts live in `inkscape-lab/transcripts/`; the fixture
is `inkscape-lab/badge.svg`, and the measuring scripts are
`inkscape-lab/check-png.py` (pixel and colour counts, via
Pillow), `inkscape-lab/count-segments.py` (path-data counts)
and `inkscape-lab/make-wobble.py` (the chapter 8 wobble,
fixed seed, identical on every run).

The lab had **no display and never opened Inkscape's
window**. Every claim about the drawing is therefore a
measurement — bounding boxes, element counts, pixel counts —
and the guide never grades how the badge *looks*. One
stderr line, a `GtkRecentManager` warning caused by the
missing desktop session, appeared on many runs; it is shown
and explained in transcript t00's note and once in t09, and
elided where it would only repeat, which the transcripts
state. In transcripts t02 and t09 a `python3 -c` command's
quoting was consumed by the shell that recorded it, so the
script lines appear bare under the command line; the outputs
are the runs' own.

Run for real, with transcripts as evidence:

- Version and install facts: package list, unpacked size
  (109 MB), the wrapper, and `inkscape --version` answering
  `Inkscape 1.2.2 (b0a8486541, 2022-12-01)` (t00).
- Measuring: `--query-all` over the badge's seven ids, and
  per-id `--query-x/-y/-width/-height` for ring, disc, star,
  label and waves — each reconciled in chapter 5 against the
  file's geometry plus half the stroke width (ring 224 + 6 =
  230; disc 124 + 3 = 127; the invisible label-path exactly
  188, its radius-94 path) (t01).
- PNG exports at width 480 and 96: `file` confirms 480x480
  and 96x96 RGBA; the pixel count finds 995 distinct colours
  at 480 (731 at 96), 167,020 of 230,400 pixels drawn, and
  exact-colour counts for the ring's cream `#fdf6e3`
  (87,940 px), the disc's teal `#2a9d8f` (35,189 px), the
  navy `#264653` of edge and letters (27,414 px) and the
  star's gold `#e9c46a` (5,814 px) — the textPath lettering
  is present in the render, not only the shapes (t02).
- PDF export: `file` reports PDF 1.5; `pdfinfo` reports
  Creator Inkscape 1.2.2, Producer cairo 1.18.0, one page at
  180 x 180 points — the 240-unit page at print measure
  (t03).
- Actions: `select-by-id:star` with `transform-scale:1.5`
  produced width 111.749 and height 102.6 — exactly 1.5 x
  the chapter 5 measurements, centre unmoved at x=120; with
  `transform-rotate:30` the star's box moved to 74.2451 x
  71.0707, the direction a tipped star leans (t04).
- Object to path, twice: the disc's `<circle>` count across
  the file fell 2 → 1, its replacement a path of one move,
  four arc parameter sets and a close (89 characters of path
  data), bounding box unchanged at 127; the label's `<text>`
  matches fell to 0 and the converted file holds 32 `<path>`
  elements — the letter outlines (t05).
- Simplify: the lab's 181-point wobbly circle (182 commands,
  2,385 characters of path data) became 11 commands under
  `path-simplify` — while its path data grew to 3,730
  characters, the honest number chapter 8 quotes (t06).
- Single-object export: `--export-id=star --export-id-only`
  printed Inkscape's own "Exporting only object" line and
  produced a 74x68 PNG, the star's box at 96 dpi (t07).
- Plain SVG: the Inkscape-saved file (2,205 bytes, 3
  `sodipodi` mentions) exported plain at 1,779 bytes with 0
  (t08).
- The three traps, verbatim: a missing file's four stderr
  complaints; an unknown id's `select_by_id: Did not find`
  line followed by the whole drawing's width, 230; a
  truncated SVG's two libxml parser errors followed by a
  finished 300x150 PNG holding 4,860 black pixels — the
  salvaged circle, default paint, default page. All three
  runs exited 0, verified directly, not through a pipe (t09).
- Spot checks the chapters quote as arithmetic: `--export-dpi=300`
  produced a 750x750 PNG (2.5 in x 300), and `--action-list`
  listed 61 actions (t10).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Everything done with the mouse: drawing and editing in the
  window, the Transform and Object Properties dialogues,
  Text → Put on Path, Path → Simplify's threshold setting,
  layers work, snapping and alignment. The command-line runs
  perform the same named operations; the clicks themselves
  were never performed here.
- Install routes other than the lab's unpacked packages:
  `apt install`, the Windows and macOS installers, AppImage
  and Flatpak. The version check they all end at was run.
- Exports beyond the ones above: `--export-area-drawing`
  and hand-set areas, other formats (EPS, the print and
  cutter variants), and Inkscape's own save dialogues.
- Tracing a bitmap into paths (mentioned as a use, never
  run), extensions that open dialogues, and the neighbour
  tools of chapter 11 — GIMP, Graphviz, OpenSCAD, the
  commercial editors — characterised, not benchmarked.
- Actually *seeing* any of it: the badge's appearance, the
  quality of the antialiasing, whether the star looks right
  turned 30 degrees. The browser check in chapter 4 is
  prescribed for the reader; the lab had no browser it could
  look through, and its exports were verified by counting,
  not viewing.

Fixtures are this guide's own and deliberately generic: a
badge for North Pier Coffee, a shop that does not exist, in
five flat colours and a widely available open font, plus a
wobbled circle from a seeded script. No real business,
person, place or artwork appears anywhere in the guide or
its lab.
