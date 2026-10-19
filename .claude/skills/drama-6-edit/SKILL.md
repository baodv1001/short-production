---
name: drama-6-edit
description: Step 6 of the short drama workflow. Edit in CapCut/Jianying or DaVinci - timeline order, audio alignment, color match, Vietnamese subtitles, export 9:16 1080p, final QA. Use after voice and lip sync are done.
---

# Step 6 - Edit and finish

Editing is done by the human in CapCut / 剪映 (or DaVinci Resolve, Premiere). Claude prepares the plan and checks the result.

## Procedure
1. Make `edit/E01_edit_plan.md` from the shot list: order of clips, in and out points (cut the extra 20 %), voice file, SFX, music, subtitle text.
2. Give the user this edit order:
   1. Put clips in order on the timeline.
   2. Align voice and effects with each clip.
   3. Make color temperature and contrast the same in all clips.
   4. Add Vietnamese subtitles. One font, one color, one position. Use the exact `dialogue_vi` text.
   5. Add music under the voice. Set the same loudness.
   6. Export 9:16, 1080p to `edit/E01_final.mp4`.
3. Do the QA with `../short-drama/references/qa-checklist.md`. If a shot is bad, return to step 4 for that shot only.
4. Remind the user: AI label if the platform asks, no real person's face or voice, check tool terms for commercial use.
5. Write the post text (title, hook line, hashtags in Vietnamese) if the user asks.
6. Start the next episode at `drama-1-script`. Use the cliffhanger.

## Done when
- `edit/E01_final.mp4` exists and passes the QA checklist.
