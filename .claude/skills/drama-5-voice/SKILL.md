---
name: drama-5-voice
description: Step 5 of the short drama workflow. Make Vietnamese voice with TTS, one fixed voice for each character, then lip sync, sound effects, and music. Use after the video clips are approved.
---

# Step 5 - Vietnamese voice and lip sync

## Procedure
1. Run `python3 tools/export_tts.py --episode E01`. Output: `audio/E01/tts_manifest.csv` and one `.txt` for each line. File names match shot IDs.
2. Make the voice for each line (ElevenLabs or CapCut voices). Use the `voice_id` from the character file. Never change a character's voice during the series. Save to `audio/E01/<file>.mp3`.
3. Listen to each line. Check Vietnamese tones, names, and pause. Fix the text if the tone is wrong. Add a short pause for emotion.
4. Test lip sync on ONE short clip first (Kling lip sync, HeyGen, or Magic Hour). Vietnamese has tones, so check the mouth. Only then run all the clips.
5. Lip sync after the final voice track is fixed. Not before. Save to `clips/E01/lipsync/E01-S01.mp4`.
6. Add sound effects and background music. Save in `audio/E01/sfx/` and `audio/E01/music/`. Use only music you have the right to use.
7. Check that each voice line is shorter than its clip.

## Done when
- A voice file exists for each dialogue line.
- Lip-synced clips exist for all shots that have dialogue.
- Music and effects are chosen.

Next: `drama-6-edit`.
