#!/usr/bin/env python3
"""Build one image prompt and one video prompt for each shot.

Reads  shotlists/<EP>.csv, characters/*.json, locations/*.json, style.json
Writes prompts/<EP>.json (for scripts and APIs) and prompts/<EP>.md (for people).

Usage: python3 tools/build_prompts.py --root . --episode E01 [--model kling]
"""
import argparse
import json
from pathlib import Path

from drama_lib import (MODEL_DURATIONS, character_description, gen_duration, load_assets,
                       load_shotlist, read_json, split_list, style_text, to_float)


FRAMING = {
    "close-up": "tight close-up, face fills most of the frame, background out of focus",
    "medium": "medium shot, waist up",
    "wide": "wide shot, full location visible",
    "over-the-shoulder": "over-the-shoulder shot, foreground shoulder out of focus",
}


def build(shot, chars, locs, style, model):
    names = split_list(shot["characters"])
    descs = [character_description(chars[n]) for n in names if n in chars]
    loc = locs.get(shot["location_ref"], {})
    loc_desc = loc.get("description_fixed", "")
    refs = []
    for n in names:
        imgs = chars.get(n, {}).get("reference_images", {})
        refs += [v for v in imgs.values() if v]
    if loc.get("reference_image"):
        refs.append(loc["reference_image"])

    st = style_text(style)
    frame = shot.get("first_frame") or shot["action"]
    image = " ".join(filter(None, [
        f'{st}.',
        f'{FRAMING.get(shot["shot_type"], shot["shot_type"] + " shot")}.',
        f'Location: {loc_desc}.' if loc_desc else "",
        f'Characters: {". ".join(descs)}.' if descs else "",
        f'Frame: {frame}.',
        f'Emotion: {shot["emotion"]}.' if shot["emotion"] else "",
        f'Aspect ratio {style.get("aspect", "9:16")}.',
        f'Avoid: {style["negative"]}.' if style.get("negative") else "",
    ]))

    duration = to_float(shot["duration_s"])
    speak = ""
    if shot["dialogue_vi"] and shot["speaker"]:
        speak = (f'{chars.get(shot["speaker"], {}).get("name", shot["speaker"])} speaks in Vietnamese, '
                 f'mouth moves naturally. Voice and lip sync are added later.')
    video = " ".join(filter(None, [
        f'{st}.',
        f'{FRAMING.get(shot["shot_type"], shot["shot_type"] + " shot")}, camera: {shot["camera_move"]}.',
        f'Location: {loc_desc}.' if loc_desc else "",
        f'Characters: {". ".join(descs)}.' if descs else "",
        f'Action: {shot["action"]}.',
        f'Emotion: {shot["emotion"]}.' if shot["emotion"] else "",
        speak,
        "Keep face and clothes the same as the first frame. No subtitles, no text, no watermark.",
    ]))
    return {
        "shot_id": shot["shot_id"],
        "first_frame_refs": refs,
        "image_prompt": image,
        "video_prompt": video,
        "video_negative": style.get("negative", ""),
        "target_duration_s": duration,
        "generate_duration_s": gen_duration(duration, model),
        "aspect": style.get("aspect", "9:16"),
        "dialogue_vi": shot["dialogue_vi"],
        "speaker": shot["speaker"],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--episode", required=True)
    ap.add_argument("--model", default="kling", choices=sorted(MODEL_DURATIONS))
    a = ap.parse_args()
    root = Path(a.root)

    shots = load_shotlist(root / "shotlists" / f"{a.episode}.csv")
    chars = load_assets(root / "characters")
    locs = load_assets(root / "locations")
    style = read_json(root / "style.json")
    out = [build(s, chars, locs, style, a.model) for s in shots]

    (root / "prompts").mkdir(exist_ok=True)
    (root / "prompts" / f"{a.episode}.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    md = [f"# Prompts {a.episode} (model: {a.model})\n"]
    for p in out:
        md += [f'## {p["shot_id"]}  (need {p["target_duration_s"]}s, generate {p["generate_duration_s"]}s)',
               f'**Reference images:** {", ".join(p["first_frame_refs"]) or "none yet"}\n',
               f'**Image prompt**\n\n{p["image_prompt"]}\n',
               f'**Video prompt**\n\n{p["video_prompt"]}\n']
    (root / "prompts" / f"{a.episode}.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {len(out)} shot prompts to {root / 'prompts' / a.episode}.json and .md")


if __name__ == "__main__":
    main()
