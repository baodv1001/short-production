---
name: short-drama
description: Run the full AI short drama (微短剧) production workflow for a Vietnamese 9:16 series. Use when the user wants to start a short drama, plan an episode, or asks "what is the next step". It checks project state, then sends the work to the correct step skill.
---

# Short drama workflow (Chinese method, Vietnamese film)

Format: 9:16, 1080p, 1-3 min for each episode, 10-30 episodes, 2-3 plot twists for each episode, hook in the first 3-5 s, 8-15 shots of 5-10 s.

## Rules

1. Story first. Do not open a video tool before the script and shot list are approved by the human.
2. The human controls the story. You propose, the human decides.
3. Character consistency is the main risk. Never write a prompt that does not use the fixed character text.
4. One visual style for the full series. It is locked in `style.json`.
5. Use image-to-video. Do not use text-to-video.
6. Do not use the face or voice of a real person. Tell the user to check each tool's commercial terms and each platform's AI label rules.

## Steps and skills

| Step | Skill | Output |
|---|---|---|
| 0 | this skill | folders, `style.json`, series bible |
| 1 | `drama-1-script` | `script/E01.md` |
| 2 | `drama-2-characters` | `characters/*.json`, `locations/*.json`, reference images |
| 3 | `drama-3-storyboard` | `shotlists/E01.csv` (validated) |
| 4 | `drama-4-video` | `prompts/E01.*`, `clips/E01/*.mp4` |
| 5 | `drama-5-voice` | `audio/E01/*.mp3`, lip-synced clips |
| 6 | `drama-6-edit` | `edit/E01_final.mp4` |

## What to do when this skill starts

1. Read the project state:
   - `ls script characters locations shotlists prompts audio clips edit`
   - If the folders do not exist: `python3 tools/init_project.py`
2. Find the first step that is not complete (see "Done when" in each step skill).
3. Tell the user the current step in 2-3 short lines. Then run that step skill.
4. At the end of each step, stop. Ask the human to approve before the next step.

## Tools in `tools/` (Python 3, no packages)

- `init_project.py` makes folders and copies templates.
- `validate.py --episode E01` checks the shot list (columns, refs, duration, twist rhythm, dialogue length).
- `build_prompts.py --episode E01 --model kling` writes image and video prompts for each shot.
- `export_tts.py --episode E01` writes the TTS list with file names that match shot IDs.

Add `--root <folder>` to work on a different project. Example: `--root examples/demo`.

## Reference files

- `references/genres.md` - genre patterns and hook formulas.
- `references/prompting.md` - prompt rules and Vietnamese setting details.
- `references/qa-checklist.md` - checks before you export each episode.
- `references/tool-notes.md` - tool roles (Kling, Seedance, Jimeng, ElevenLabs, CapCut) and legal notes.
