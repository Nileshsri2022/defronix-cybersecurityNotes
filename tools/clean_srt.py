#!/usr/bin/env python3
"""Clean a YouTube auto-caption .srt into plain running text.

Removes indices/timestamps and collapses the rolling-caption duplication
that YouTube produces (each cue repeats the tail of the previous cue).
"""
import sys, os, re


def clean(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        raw = fh.read()

    lines = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.isdigit() or "-->" in line:
            continue
        line = re.sub(r"<[^>]+>", "", line).strip()
        if line:
            lines.append(line)

    merged = []
    for line in lines:
        if merged and (line in merged[-1] or merged[-1] in line):
            if len(line) > len(merged[-1]):
                merged[-1] = line
            continue
        merged.append(line)

    return " ".join(merged)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        text = clean(p)
        sys.stdout.write(text + "\n")
