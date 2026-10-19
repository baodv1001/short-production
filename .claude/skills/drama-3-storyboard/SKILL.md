---
name: drama-3-storyboard
description: Step 3 of the short drama workflow. Turn the approved script into a validated shot list CSV (分镜) with shot type, camera move, duration, characters, action, Vietnamese dialogue, emotion, and location reference. Use before video generation.
---

# Step 3 - Storyboard / shot list

## Procedure
1. Read `script/E01.md`, `characters/*.json`, `locations/*.json`.
2. Write `shotlists/E01.csv`. Start from `shotlists/_template.csv`. Columns:
   `shot_id, shot_type, camera_move, duration_s, characters, action, first_frame, speaker, dialogue_vi, emotion, location_ref, twist, notes`
   - `shot_id`: `E01-S01`, `E01-S02`, ...
   - `shot_type`: close-up, medium, wide, over-the-shoulder.
   - `camera_move`: static, slow push-in, pan left, ...
   - `duration_s`: 5-10. This is the time you need in the final edit.
   - `characters`: ids separated by `;` (`lan;minh`).
   - `action`: one physical action. `first_frame`: optional, the still image at the start.
   - `speaker` + `dialogue_vi`: one speaker for each shot. Split a long exchange into more shots.
   - `location_ref`: file name of the location without `.json`.
   - `twist`: `hook` on shot 1, `twist` on twist shots, `cliffhanger` on the last shot. Else empty.
3. Rules: 8-15 shots, a small twist every 3-5 shots, dialogue must fit the shot (about 4 words/second, leave 1 s of margin).
4. Run `python3 tools/validate.py --episode E01`. Fix all ERROR lines. Fix WARN lines or tell the user why they stay.
5. Show the shot list as a table. A human checks it. Get approval.

## Done when
- `validate.py` has no ERROR.
- The human approved the shot list.

Next: `drama-4-video`.
