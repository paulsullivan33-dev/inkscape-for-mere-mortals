#!/usr/bin/env python3
"""Count the segments in one object's path data inside an SVG.

Usage: python3 count-segments.py FILE.svg OBJECT-ID

Finds the element with the given id, reads its path data (the
"d" attribute), and reports how many drawing commands and how
many coordinate pairs it holds. Simplifying a path, or turning
a shape into a path, shows up here as a changed count.
"""
import re
import sys


def main(argv):
    fname, elem_id = argv[1], argv[2]
    text = open(fname).read()
    m = re.search(r'<[a-zA-Z]+[^>]*\bid="%s"[^>]*>' % re.escape(elem_id), text)
    if not m:
        print(f"no element with id {elem_id!r} in {fname}")
        return 1
    dm = re.search(r'\bd="([^"]+)"', m.group(0))
    if not dm:
        print(f"element {elem_id!r} has no path data (not a path)")
        return 1
    d = dm.group(1)
    commands = re.findall(r"[A-Za-z]", d)
    numbers = re.findall(r"-?\d+\.?\d*", d)
    print(f"{fname} #{elem_id}: {len(commands)} commands, "
          f"{len(numbers) // 2} coordinate pairs, {len(d)} characters of path data")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
