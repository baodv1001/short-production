---
name: drama-2-characters
description: Step 2 of the short drama workflow. Make the character and location package - fixed text descriptions, three-view images, expression sheets, location references, and the locked series style. Use before any storyboard or video work. This is the most important step.
---

# Step 2 - Character and scene package

If a face changes between shots, the viewer stops believing the story. Do this step with care.

## Procedure
1. Fill `style.json` from the series bible. Use one style only. Do not mix realistic, 3D, and anime.
2. For each character in the script, write `characters/<id>.json` (copy `characters/_template.json`). Use the id in lower case without accents (`lan`, `minh`).
   - Required: age, face_shape, skin_tone, hair (color and style), clothes (type and color), accessories.
   - Do not use "handsome" or "beautiful". Use exact facts.
   - Set `voice` (provider, voice_id, note). One fixed voice for each character.
   - Optional: `description_fixed` replaces the auto text. Once the images are made, do not change it.
3. For each location, write `locations/loc_NN_<name>.json`. Add Vietnamese details (see `../short-drama/references/prompting.md`).
4. Make the images (ask the user before you spend credits):
   - Three-view: front, side, back, neutral pose, plain background. Save `characters/<id>_three_view.png`.
   - Expression sheet: neutral, happy, angry, sad, surprised. Save `characters/<id>_expressions.png`.
   - One wide reference for each location. Save `locations/<id>.png`.
   Image prompt pattern: `<style from style.json>. <fixed character text>. three-view character sheet, front, side and back, plain light gray background, same face in all views.`
5. Ask the human to check: same face in all views, clothes match the text. Fix the text or regenerate. Then freeze the files.

## Done when
- `style.json`, every `characters/*.json`, and every `locations/*.json` are complete.
- All reference image paths in the JSON files exist.
- The human approved the faces.

Next: `drama-3-storyboard`.

## Tool notes (learned from TopView tests)
- Submit at most 3 image tasks at once. A 5th task fails with error 5105 (not charged).
- A full-body three-view makes small faces. Always make the expression sheet (close-up faces) from the approved three-view. It is the real face reference.
- Do not rely on small accessories (watch, mole). The model does not keep the wrist side. Use big, clear costume features (colors, headband, embroidery).
- Signs and text in generated images are often garbled. Say "no readable text" in the location text.
- Build the prompts with `python3 tools/build_asset_prompts.py`. Output: `prompts/assets.json`.
