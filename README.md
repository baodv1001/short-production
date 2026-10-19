# Short production - AI short drama workflow

A skill set and tools to make a Vietnamese AI short drama (微短剧) with the Chinese production method.

## Workflow

```
1 Script -> 2 Characters + locations -> 3 Shot list -> 4 Video clips -> 5 Voice + lip sync -> 6 Edit
```

| Step | Skill | Tool | Output |
|---|---|---|---|
| 1 | `drama-1-script` | - | `script/E01.md` |
| 2 | `drama-2-characters` | - | `characters/`, `locations/`, `style.json` |
| 3 | `drama-3-storyboard` | `validate.py` | `shotlists/E01.csv` |
| 4 | `drama-4-video` | `build_prompts.py` | `prompts/`, `clips/` |
| 5 | `drama-5-voice` | `export_tts.py` | `audio/` |
| 6 | `drama-6-edit` | - | `edit/E01_final.mp4` |

## Quick start

```bash
python3 tools/init_project.py          # make folders and templates
# in Claude Code: /short-drama          # find the current step
python3 tools/validate.py --episode E01
python3 tools/build_prompts.py --episode E01 --model kling
python3 tools/export_tts.py --episode E01
```

Try the example: add `--root examples/demo` to each command.

## Shot list columns

`shot_id, shot_type, camera_move, duration_s, characters, action, first_frame, speaker, dialogue_vi, emotion, location_ref, twist, notes`

- `characters`: ids separated by `;`.
- `twist`: `hook` (shot 1), `twist`, `cliffhanger` (last shot).
- One speaker for each shot.

## Folders

```
script/      episode scripts (Vietnamese)       prompts/  image and video prompts
characters/  JSON + reference images            audio/    voice files and TTS list
locations/   JSON + reference images            clips/    generated video clips
shotlists/   one CSV for each episode           edit/     final edit and exports
```

## Not done yet

- Batch connection to video APIs (Kling and others). Prompts are in `prompts/<EP>.json` and are ready for a script.
- Automatic SRT subtitles. Timing depends on the final edit.
