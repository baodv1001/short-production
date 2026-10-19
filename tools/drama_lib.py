"""Shared helpers for the short-drama tools. Standard library only."""
import csv
import json
import re
from pathlib import Path

FIELDS = [
    "shot_id", "shot_type", "camera_move", "duration_s", "characters",
    "action", "first_frame", "speaker", "dialogue_vi", "emotion",
    "location_ref", "twist", "notes",
]
SHOT_ID_RE = re.compile(r"^E\d{2}-S\d{2}$")
TWIST_VALUES = {"", "hook", "twist", "cliffhanger"}

# Clip lengths (seconds) that each tool accepts. Edit when a tool changes.
MODEL_DURATIONS = {
    "kling": [5, 10],
    "seedance": [5, 10],
    "jimeng": [5, 10],
    "any": None,
}
GEN_MARGIN = 1.2  # generate each clip 1.2x longer than the shot needs
VI_WORDS_PER_SEC = 4.0  # rough Vietnamese speech rate (one word = one syllable)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_assets(folder):
    """Load every *.json in folder. Files that start with '_' are templates."""
    assets = {}
    for p in sorted(Path(folder).glob("*.json")):
        if p.name.startswith("_"):
            continue
        assets[p.stem] = read_json(p)
    return assets


def load_shotlist(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return [{k: (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f)]


def split_list(value):
    return [x.strip() for x in re.split(r"[;,]", value) if x.strip()]


def character_description(c):
    """Fixed text description. Use description_fixed if the author wrote one."""
    if c.get("description_fixed"):
        return c["description_fixed"]
    parts = [
        f'{c.get("age", "")}'.strip(),
        f'{c["face_shape"]} face' if c.get("face_shape") else "",
        f'{c["skin_tone"]} skin' if c.get("skin_tone") else "",
        c.get("hair", ""),
        f'wearing {c["clothes"]}' if c.get("clothes") else "",
        c.get("accessories", ""),
    ]
    return f'{c.get("name", "")}: ' + ", ".join(p for p in parts if p)


def style_text(style):
    bits = list(style.get("style", [])) + [style.get("lens", ""), style.get("lighting", "")]
    return ", ".join(b for b in bits if b)


def gen_duration(target, model):
    """Target shot length x 1.2, then rounded up to a length the model accepts."""
    want = target * GEN_MARGIN
    allowed = MODEL_DURATIONS.get(model)
    if not allowed:
        return round(want, 1)
    for d in allowed:
        if d >= want:
            return d
    return allowed[-1]


def estimate_speech_seconds(text):
    return len(text.split()) / VI_WORDS_PER_SEC if text else 0.0


def to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default
