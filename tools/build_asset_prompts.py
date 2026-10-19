#!/usr/bin/env python3
"""Build image prompts for character sheets and location references.

Reads  characters/*.json, locations/*.json, style.json
Writes prompts/assets.json  (one entry for each three-view, expression sheet, and location)

Usage: python3 tools/build_asset_prompts.py --root .
"""
import argparse
import json
from pathlib import Path

from drama_lib import character_description, load_assets, read_json, style_text

EXPRESSIONS = "neutral, happy, angry, sad, surprised"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    style = read_json(root / "style.json")
    st = style_text(style)
    avoid = style.get("negative", "")
    out = []
    for cid, c in load_assets(root / "characters").items():
        desc = character_description(c)
        out.append({
            "id": f"{cid}_three_view", "kind": "three_view", "aspect": "16:9",
            "output": f"characters/{cid}_three_view.png",
            "prompt": (f"{st}. Character design reference sheet, three-view turnaround: front view, "
                       f"side view in profile, back view, full body, standing in a neutral pose, plain light "
                       f"gray studio background, even soft light, the same person in all three views. {desc}. "
                       f"Avoid: {avoid}, labels, captions."),
        })
        out.append({
            "id": f"{cid}_expressions", "kind": "expression_sheet", "aspect": "16:9",
            "output": f"characters/{cid}_expressions.png",
            "input": f"characters/{cid}_three_view.png",
            "prompt": (f"{st}. Expression sheet of the same person as the reference image: five close-up "
                       f"head-and-shoulders portraits in a row, expressions: {EXPRESSIONS}. Same face, same hair, "
                       f"same clothes in every portrait, plain light gray background. {desc}. "
                       f"Avoid: {avoid}, labels, captions."),
        })
    for lid, loc in load_assets(root / "locations").items():
        out.append({
            "id": lid, "kind": "location", "aspect": style.get("aspect", "9:16"),
            "output": loc.get("reference_image", f"locations/{lid}.png"),
            "prompt": (f"{st}. Wide establishing shot of an empty location, no people. "
                       f"{loc['description_fixed']}. Avoid: people, {avoid}."),
        })
    (root / "prompts").mkdir(exist_ok=True)
    (root / "prompts" / "assets.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(out)} asset prompts to {root / 'prompts' / 'assets.json'}")


if __name__ == "__main__":
    main()
