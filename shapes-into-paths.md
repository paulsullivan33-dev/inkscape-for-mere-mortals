# Shapes into Paths

Outcome: three conversions, each
measured. A circle stops being a circle
recipe and becomes four arcs. Lettering
stops being text and becomes 32
letter-shaped paths. And a wobbly
181-segment line becomes a smooth curve
of 11 commands. These are the
operations that change what a thing
*is*, not just where it sits — powerful,
and one-way.

## Object to path: the disc

Chapter 2 said every shape sits on a
path underneath. The `object-to-path`
action makes that literal:

```bash
inkscape badge.svg \
  --actions="select-by-id:disc;object-to-path" \
  --export-filename=badge-discpath.svg
grep -c "<circle" badge.svg
grep -c "<circle" badge-discpath.svg
```

```text
2
1
```

(Transcript
`inkscape-lab/transcripts/t05-object-to-path.txt`.)
The badge had two circle elements; now
it has one — the ring survived, the
disc did not. In its place, at the same
id, sits a path whose data the lab's
counter (`inkscape-lab/count-segments.py`)
reports as 89 characters: one move,
four arc segments, one close — a circle
described the way paths describe
things, as four quarter-turns of an
ellipse arc. Re-measuring shows the
drawing did not move: still 127 by 127,
stroke and all. Only its nature
changed. The disc can now be dented,
pointed and reshaped node by node —
and it can never again be resized by
changing a radius, because there is no
radius anymore. Both halves of that
sentence are the reason the operation
exists.

## Text to path: the label

The same action on the lettering is
the chapter's bigger trade:

```bash
inkscape badge.svg \
  --actions="select-by-id:label;object-to-path" \
  --export-filename=badge-textpath.svg
grep -c "<text" badge-textpath.svg
grep -c "<path" badge-textpath.svg
```


```text
0
32
```

No text remains. Where the `<text>`
element stood there is now a group
holding 32 paths — the outlines of
every letter and both bullet dots,
bent around the ring exactly as the
text was. Chapter 9 explains why anyone
would do this: a text object is drawn
by whatever font the *viewing* machine
has, so lettering sent away can change
its face; outlines are just shapes, and
draw identically everywhere. The price
is total: the words are no longer
words. They cannot be searched,
retyped, spell-checked or re-worded —
a typo frozen into outlines is a typo
you redraw. Convert text when the
drawing is finished and leaving home;
keep it text while it is still being
written.

## Simplify: the wobble

The third conversion changes a path's
*economy*. The lab generated a
near-circle the way shaky sources
produce one: 181 straight segments,
each a few units long, jittering around
the true curve (`inkscape-lab/make-wobble.py`;
transcript t06). Its path data is 2,385
characters of mostly noise:

```bash
python3 inkscape-lab/count-segments.py wobble.svg wobble
```

```text
wobble.svg #wobble: 182 commands, 181 coordinate pairs,
2385 characters of path data
```

```bash
inkscape wobble.svg \
  --actions="select-by-id:wobble;path-simplify" \
  --export-filename=wobble-simplified.svg
python3 inkscape-lab/count-segments.py wobble-simplified.svg wobble
```

```text
wobble-simplified.svg #wobble: 11 commands,
214 coordinate pairs, 3730 characters of path data
```

182 commands become 11: the polyline is
gone, replaced by a handful of smooth
curves that pass near the wobble's
points. Read the rest of the line
honestly, though — the character count
*went up*, from 2,385 to 3,730, because
curve commands carry several points
each, written out at full precision.
Simplify buys smoothness and few,
editable nodes; it does not buy a
smaller file, and it is an
*approximation*: the new curve follows
the old one's average, not its exact
jitter. For a traced sketch or a shaky
hand line that trade is the point. For
measured geometry it is vandalism. The
window offers the same operation as
Path → Simplify, with a threshold
setting this command form leaves at its
default — one more case where the
guide ran what it could name.
