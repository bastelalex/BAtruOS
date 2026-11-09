"""Validated placement v1 -> OpenSCAD anchors (standard library only)."""
import csv
import json
import math
import sys
from pathlib import Path


def convert(source, target, width=100, height=80):
    points = []
    seen = set()
    with Path(source).open(newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != ["reference", "x_mm", "y_mm", "rotation_deg", "side"]:
            raise ValueError("placement v1 header required")
        for row in reader:
            ref = row["reference"]
            if not ref or ref in seen or row["side"] != "top":
                raise ValueError("unique reference and top side required")
            x, y, angle = (float(row[k]) for k in ("x_mm", "y_mm", "rotation_deg"))
            if not all(math.isfinite(v) for v in (x, y, angle)):
                raise ValueError("non-finite coordinate")
            if not (0 <= x <= width and 0 <= y <= height):
                raise ValueError("coordinate outside board")
            seen.add(ref)
            points.append([x, y, angle % 360])
    if not points:
        raise ValueError("empty placement")
    Path(target).write_text("// Synthetic/example anchors unless verified externally.\nplacements = " + json.dumps(points) + ";\n")


if __name__ == "__main__":
    convert(*sys.argv[1:])
