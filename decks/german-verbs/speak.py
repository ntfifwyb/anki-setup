"""Speak the deck's audio clips into audio/ with Psittacus's voice, skipping clips already there.

uv run --no-project -p 3.13 --with genanki==0.13.1 --with piper-tts==1.8.0 --with soundfile==0.13.1 python speak.py

German is spoken by Piper (de_DE-thorsten-high). The voice model (about 110 MB) downloads once,
from Hugging Face, into ~/.cache/psittacus. Piper is fast: about 4,000 clips take a few minutes.
"""
from pathlib import Path

from build import AUDIO, LANG, clips, notes, psittacus, voice

MODELS = Path.home() / ".cache" / "psittacus"


def main():
    core, engines = psittacus(), psittacus("engines")
    data, engine, _ = voice()
    # Only the first engine, so every clip has the name build.py expects.
    speaker = core.Speaker({engine: engines.ENGINES[engine](MODELS, print)}, data, Path(AUDIO))
    todo = {name: text for fields, _, _ in notes() for text, name in clips(fields).values()}
    todo = {name: text for name, text in todo.items() if not (Path(AUDIO) / name).exists()}
    for i, (name, text) in enumerate(todo.items(), 1):
        print(f"{i}/{len(todo)} {text}")
        path = speaker.speak(text, LANG)
        assert path.name == name, (path.name, name)


if __name__ == "__main__":
    main()
