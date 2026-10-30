# Installing Inkscape

Outcome: Inkscape on the machine, and
one command whose answer proves it
runs — the same command whatever route
installed it. If the version line below
does not appear, stop here; nothing
later in the guide can work until it
does.

## The ordinary routes

On Ubuntu and Debian, Inkscape is one
package:

```bash
sudo apt install inkscape
```

On Windows and macOS, the installers
from inkscape.org do the same job, and
the project also publishes an AppImage
and Flatpak for other Linux setups.
Those windowed routes are described
from the project's documentation — the
lab that wrote this guide installed
nothing in the ordinary way, for
reasons explained below — but every
route ends at the same program, and
the check is the same:

```bash
inkscape --version
```

```text
Inkscape 1.2.2 (b0a8486541, 2022-12-01)
```

That is transcript
`inkscape-lab/transcripts/t00-install.txt`:
one line, the version and the exact
build. Two things are worth knowing
about it. The version a distribution
hands you lags the project's own
releases — Ubuntu 24.04 carries 1.2.2
from December 2022, while the project
has published newer series since — and
for everything in this guide the older
build is enough; where a newer release
differs, chapter 12 says so. And the
answer comes from the program itself,
not from a package list: a half-finished
install can leave the package "present"
and the program unusable, which is
exactly the failure this check exists
to catch.

## How the lab installed it

Honesty about provenance: this guide's
lab is a shared, headless sandbox where
installing packages system-wide was not
an option. So the lab downloaded the
genuine Ubuntu packages — `inkscape`
1.2.2-2ubuntu12 and the fourteen
libraries it needed that were not
already present, 24 MB in all — and
unpacked them, without installing, into
a private folder, then ran the real
binary from there with its libraries
beside it. Transcript t00 shows the
package list and the small wrapper
script that points at it.

The binary is the distribution's own,
byte for byte; nothing was patched or
rebuilt. But the arrangement is the
lab's, not a recommendation: on your
machine, use your normal install route
and the same version check.

## One warning you may meet

Run from a terminal on a machine with
no desktop session — or, depending on
the build, even with one — Inkscape
sometimes adds a line like this to its
output:

```text
** (inkscape:63791): WARNING **: Failed to wrap object of type
'GtkRecentManager'. Hint: this error is commonly caused by
failing to call a library init() function.
```

It looks alarming and means little: a
desktop bookkeeping service was not
there to talk to. The command still
runs and the output is unaffected. The
lab's transcripts note where this line
was left out for readability, and
chapter 13 returns to it — because the
habit it teaches matters: read warnings
for which part of the machine they are
about, and a warning about the desktop
says nothing about your drawing.
Contrast it with the warnings that do
matter in chapter 13, which name your
file.

## What you have now

A program that opens, measures, edits
and exports SVG files, from its window
and from the command line alike. The
next chapter puts the guide's running
example on the table: a complete,
finished drawing, small enough to read
in one sitting.
