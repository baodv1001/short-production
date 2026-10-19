#!/usr/bin/env python3
"""Create the project folders and copy the templates.

Usage: python3 tools/init_project.py [--root .]
"""
import argparse
import shutil
from pathlib import Path

FOLDERS = ["script", "characters", "locations", "shotlists", "prompts", "audio", "clips", "edit"]
HERE = Path(__file__).resolve().parent.parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    for f in FOLDERS:
        (root / f).mkdir(parents=True, exist_ok=True)
        keep = root / f / ".gitkeep"
        if not any((root / f).iterdir()):
            keep.touch()
    copies = {
        "style.json": "style.json",
        "series_bible.md": "script/_series_bible.md",
        "character.json": "characters/_template.json",
        "location.json": "locations/_template.json",
        "shotlist.csv": "shotlists/_template.csv",
        "episode_script.md": "script/_episode_template.md",
    }
    for src, dst in copies.items():
        target = root / dst
        if not target.exists():
            shutil.copy(HERE / "templates" / src, target)
            print("created", target)
    print("Project folders ready in", root.resolve())


if __name__ == "__main__":
    main()
