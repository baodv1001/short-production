# Prompt rules

## Always
- Use the fixed character text word for word in every prompt. `tools/build_prompts.py` does this.
- Use exact details: age, face shape, skin tone, hair color and style, clothes type and color, accessories.
- Keep the same style words, lens, and light in all shots (`style.json`).
- Use the first-frame image (with the character reference) as the input. Then animate it.
- Use first-frame + last-frame control when the tool has it, for smooth cuts.
- Describe one action for each shot. Short and physical: "Lan puts the cup down and looks up".
- Say what the camera does: static, slow push-in, pan left.

## Never
- Do not write vague words: "handsome", "beautiful", "cool".
- Do not mix realistic, 3D, and anime.
- Do not put text or subtitles in the generated video. Subtitles are added in the edit.
- Do not describe two big actions in one 5-10 s shot.

## Vietnamese setting details (use in location text)
Vietnamese street, motorbikes, nhà ống (tube house), street coffee shop with low plastic stools, chợ (market), rice field, áo dài, Vietnamese shop signs, hanging electric wires, tropical plants, humid air.

## Duration
- Generate 1.2x the shot length. The tool rounds to the model's allowed length (see `MODEL_DURATIONS` in `tools/drama_lib.py`).
- Cut the extra frames in the edit.

## Draw cards (抽卡)
- Make 2-4 versions of each shot. Keep the best.
- Delete clips with face change, wrong hands, broken motion, wrong clothes.
- Record the chosen file in the shot list `notes` column.
