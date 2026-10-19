# AI short drama (Vietnamese, 9:16)

Start with the `short-drama` skill. It finds the current step and calls the step skills (`drama-1-script` ... `drama-6-edit`).

- Story first. Human approves the script and the shot list before any generation.
- Fixed character text in every prompt. One style (`style.json`).
- Image-to-video only. Generate each clip 1.2x longer than needed.
- Ask before you spend generation credits.
- Tools: `python3 tools/{init_project,validate,build_prompts,export_tts}.py --episode E01 [--root DIR]`.
- Example project: `examples/demo` (use `--root examples/demo`).
- Reply in ASD-STE100 simplified technical English. Vietnamese is used for dialogue, subtitles, and posts.
