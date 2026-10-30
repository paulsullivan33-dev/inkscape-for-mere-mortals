#!/usr/bin/env python3
"""Report what is actually inside a PNG exported from Inkscape.

Usage: python3 check-png.py FILE.png [FILE2.png ...]

Prints the pixel size, how many distinct colours the picture
uses, how many pixels are not fully transparent, and the three
most common colours. A vector export that went wrong usually
shows up here as a blank (all transparent) or flat picture.
"""
import sys
from collections import Counter

from PIL import Image


def main(argv):
    for name in argv[1:]:
        im = Image.open(name).convert("RGBA")
        px = list(im.getdata())
        colours = Counter(px)
        solid = sum(1 for p in px if p[3] > 0)
        print(f"{name}: {im.size[0]}x{im.size[1]} px, "
              f"{len(colours)} distinct colours, "
              f"{solid} of {len(px)} pixels not transparent")
        for colour, count in colours.most_common(3):
            print(f"    {colour}: {count} px")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
