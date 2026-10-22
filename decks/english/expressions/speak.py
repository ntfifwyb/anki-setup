"""Speak the deck's audio clips into audio/ with Psittacus's voice, skipping clips already there.

uv run --no-project -p 3.13 --with genanki==0.13.1 --with kokoro-onnx==0.6.1 --with soundfile==0.13.1 python speak.py

The voice model downloads once, into ~/.cache/psittacus. Expect a few seconds per clip.
"""
from pathlib import Path

from build import AUDIO, LANG, clips, notes, psittacus, voice

MODELS = Path.home() / ".cache" / "psittacus"


def main():
    core, engines = psittacus(), psittacus("engines")
    data, engine, _ = voice()
    # Only the first engine, so every clip has the name build.py expects.
    speaker = core.Speaker({engine: engines.ENGINES[engine](MODELS, print)}, data, Path(AUDIO))
    todo = {name: text for _, fields, _, _ in notes() for text, name in clips(fields).values()}
    todo = {name: text for name, text in todo.items() if not (Path(AUDIO) / name).exists()}
    for i, (name, text) in enumerate(todo.items(), 1):
        print(f"{i}/{len(todo)} {text}")
        path = speaker.speak(text, LANG)
        assert path.name == name, (path.name, name)


if __name__ == "__main__":
    main()
