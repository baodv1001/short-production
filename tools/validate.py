#!/usr/bin/env python3
"""Check an episode shot list before you spend credits on generation.

Usage: python3 tools/validate.py --root . --episode E01
Exit code 1 if there are errors. Warnings do not change the exit code.
"""
import argparse
import sys
from pathlib import Path

from drama_lib import (FIELDS, SHOT_ID_RE, TWIST_VALUES, estimate_speech_seconds,
                       load_assets, load_shotlist, split_list, to_float)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--episode", required=True)
    a = ap.parse_args()
    root = Path(a.root)
    path = root / "shotlists" / f"{a.episode}.csv"
    if not path.exists():
        sys.exit(f"ERROR: {path} not found")

    shots = load_shotlist(path)
    chars = load_assets(root / "characters")
    locs = load_assets(root / "locations")
    errors, warns = [], []

    missing_cols = [f for f in FIELDS if f not in (shots[0] if shots else {})]
    if missing_cols:
        errors.append(f"missing columns: {', '.join(missing_cols)}")

    seen = set()
    for s in shots:
        sid = s.get("shot_id", "?")
        if not SHOT_ID_RE.match(sid):
            errors.append(f"{sid}: shot_id must look like E01-S05")
        elif not sid.startswith(a.episode + "-"):
            errors.append(f"{sid}: shot_id does not match episode {a.episode}")
        if sid in seen:
            errors.append(f"{sid}: duplicate shot_id")
        seen.add(sid)
        d = to_float(s.get("duration_s"))
        if not 5 <= d <= 10:
            warns.append(f"{sid}: duration {d}s is outside 5-10 s")
        for c in split_list(s.get("characters", "")):
            if c not in chars:
                errors.append(f"{sid}: character '{c}' has no file in characters/")
        if s.get("location_ref") not in locs:
            errors.append(f"{sid}: location '{s.get('location_ref')}' has no file in locations/")
        if s.get("twist") not in TWIST_VALUES:
            errors.append(f"{sid}: twist must be one of hook, twist, cliffhanger or empty")
        if s.get("dialogue_vi"):
            if s.get("speaker") not in chars:
                errors.append(f"{sid}: dialogue has no valid speaker")
            need = estimate_speech_seconds(s["dialogue_vi"])
            if need > d - 1:
                warns.append(f"{sid}: dialogue needs about {need:.1f}s, shot is {d}s. Shorten the line or split the shot")
        if not s.get("action"):
            errors.append(f"{sid}: action is empty")

    n = len(shots)
    if not 8 <= n <= 15:
        warns.append(f"{n} shots. A typical episode has 8-15 shots")
    total = sum(to_float(s.get("duration_s")) for s in shots)
    if not 60 <= total <= 180:
        warns.append(f"total length {total:.0f}s. Target is 60-180 s")
    if shots and shots[0].get("twist") != "hook":
        warns.append("first shot is not marked 'hook'. The hook must be in the first 3-5 s")
    if shots and shots[-1].get("twist") != "cliffhanger":
        warns.append("last shot is not marked 'cliffhanger'")
    marks = [i for i, s in enumerate(shots) if s.get("twist") in ("twist", "cliffhanger")]
    if len(marks) < 2:
        warns.append("fewer than 2 plot twists in this episode")
    gap, last = 0, -1
    for i in marks + [n - 1]:
        gap = max(gap, i - last)
        last = i
    if gap > 5:
        warns.append(f"{gap} shots without a twist. Add a small twist every 3-5 shots")

    print(f"{a.episode}: {n} shots, {total:.0f}s")
    for w in warns:
        print("WARN :", w)
    for e in errors:
        print("ERROR:", e)
    if not errors and not warns:
        print("OK: no problems found")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
