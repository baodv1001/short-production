---
name: drama-4-video
description: Step 4 of the short drama workflow. Build image and video prompts for each shot, make first-frame images, and generate clips with image-to-video (Kling, Seedance, Jimeng). Use after the shot list is approved.
---

# Step 4 - Shot-by-shot video generation

## Procedure
1. Run `python3 tools/validate.py --episode E01`. Stop if there are errors.
2. Run `python3 tools/build_prompts.py --episode E01 --model kling` (or `seedance`, `jimeng`). Output: `prompts/E01.json` and `prompts/E01.md`.
3. For each shot:
   a. Make the first-frame still. Use `image_prompt` and the reference images in `first_frame_refs`.
   b. Check the face against the three-view. If the face is wrong, generate again.
   c. Animate it with image-to-video. Use `video_prompt` and `generate_duration_s` (1.2x the shot length). Use first-frame + last-frame control when the tool has it.
   d. Make 2-4 versions ("draw cards"). Delete bad clips: face change, wrong hands, wrong clothes, broken motion.
   e. Save the best clip as `clips/E01/E01-S01.mp4`. Write the choice in `notes`.
4. Before you spend credits, show the user the number of clips and the quote. If an MCP tool for image or video generation is available (for example Higgsfield), use it for one test shot first. Then do the batch.
5. Keep the style and prompt text the same in all shots. Do not rewrite the character text.
6. Show a contact sheet or list of the clips. The human approves.

## Done when
- One approved clip exists for every shot in `clips/E01/`.

Next: `drama-5-voice`.
