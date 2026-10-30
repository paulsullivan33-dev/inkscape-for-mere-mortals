#!/usr/bin/env python3
"""Draw a deliberately wobbly circle as 181 straight segments.

Usage: python3 make-wobble.py > wobble.svg

A near-circle built from many short straight lines, the way a
shaky hand or a traced bitmap leaves a path. Chapter 8 feeds it
to Inkscape's simplify action and counts what comes back. The
random wobble uses a fixed seed, so the file is the same every
run.
"""
import math
import random

random.seed(7)
points = []
for i in range(181):
    angle = 2 * math.pi * i / 180
    radius = 80 + random.uniform(-2.5, 2.5)
    points.append((120 + radius * math.cos(angle),
                   120 + radius * math.sin(angle)))
d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in points) + " Z"
print('<svg width="240" height="240" viewBox="0 0 240 240" '
      'xmlns="http://www.w3.org/2000/svg">')
print(f'  <path id="wobble" d="{d}" fill="none" '
      'stroke="#264653" stroke-width="2"/>')
print('</svg>')
