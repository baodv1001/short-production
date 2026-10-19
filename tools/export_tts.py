#!/usr/bin/env python3
"""Export all Vietnamese dialogue lines for TTS.

File names match the shot numbers: audio/<EP>/<SHOT_ID>_<speaker>.mp3
Writes audio/<EP>/tts_manifest.csv and one .txt for each line.

Usage: python3 tools/export_tts.py --root . --episode E01
"""
import argparse
import csv
from pathlib import Path

from drama_lib import estimate_speech_seconds, load_assets, load_shotlist, to_float


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--episode", required=True)
    a = ap.parse_args()
    root = Path(a.root)
    shots = load_shotlist(root / "shotlists" / f"{a.episode}.csv")
    chars = load_assets(root / "characters")
    out_dir = root / "audio" / a.episode
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for s in shots:
        if not s["dialogue_vi"]:
            continue
        spk = s["speaker"]
        voice = chars.get(spk, {}).get("voice", {})
        stem = f'{s["shot_id"]}_{spk}'
        (out_dir / f"{stem}.txt").write_text(s["dialogue_vi"] + "\n", encoding="utf-8")
        est = estimate_speech_seconds(s["dialogue_vi"])
        rows.append({
            "file": f"{stem}.mp3", "shot_id": s["shot_id"], "speaker": spk,
            "voice_provider": voice.get("provider", ""), "voice_id": voice.get("voice_id", ""),
            "emotion": s["emotion"], "text_vi": s["dialogue_vi"],
            "est_speech_s": f"{est:.1f}", "shot_duration_s": s["duration_s"],
            "too_long": "YES" if est > to_float(s["duration_s"]) - 1 else "",
        })
    with open(out_dir / "tts_manifest.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["file"])
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} dialogue lines -> {out_dir / 'tts_manifest.csv'}")
    for r in rows:
        if r["too_long"]:
            print(f'WARN: {r["shot_id"]} line is probably longer than the shot')


if __name__ == "__main__":
    main()
