---
name: drama-1-script
description: Step 1 of the short drama workflow. Write the series bible and the Vietnamese episode script (scene list, dialogue, plot twists, cliffhanger). Use when the user wants an idea, a story, a script, or a new episode.
---

# Step 1 - Script

The human controls the story. Ask, propose options, then write what the human picks.

## Procedure
1. If `script/_series_bible.md` is empty, ask the user (one short message) for: genre, setting, main characters, big secret, number of episodes. Offer 2-3 concept options with a logline. Read `../short-drama/references/genres.md`.
2. Fill `script/_series_bible.md`. Get approval.
3. For each episode, copy `script/_episode_template.md` to `script/E01.md` and write:
   - Hook for the first 3-5 s.
   - Scene list (location, characters, what happens, twist).
   - Vietnamese dialogue. Short lines (5-12 words), one speaker for each line, correct kinship terms.
   - 2-3 plot twists.
   - Cliffhanger in the last shot. The next episode starts from it.
4. Check the length: 1-3 min means about 8-15 shots and 150-350 Vietnamese words of dialogue at most.
5. Show a summary. Get approval.

## Done when
- `script/_series_bible.md` is complete.
- `script/E01.md` exists and the human approved it.

Next: `drama-2-characters`.
