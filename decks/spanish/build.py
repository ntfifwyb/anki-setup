"""Build the Spanish Anki deck (Spanish.apkg): every subdeck folder here, packaged into one file.

Each subdeck's build.py checks its source and returns its notes as rows; common.add_notes fills
their audio and adds them to Languages::Spanish, so one import adds or updates the whole deck.
"""
import importlib.util
import os

import genanki

from common import add_notes

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = ["refranes", "expresiones", "norma"]
OUT = os.path.join(HERE, "Spanish.apkg")


def part(name):
    """A subdeck's build module, loaded under its own name (every subdeck's file is build.py)."""
    spec = importlib.util.spec_from_file_location(f"{name}_build", os.path.join(HERE, name, "build.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rows():
    return [row for name in PARTS for row in part(name).rows()]


def build():
    decks, media = add_notes(rows())
    for d in sorted(decks, key=lambda d: d.name):
        print(f"{d.name}: {len(d.notes)} notes")
    package = genanki.Package(decks)
    package.media_files = sorted(set(media))
    package.write_to_file(OUT)
    print(f"{sum(len(d.notes) for d in decks)} notes, {len(set(media))} clips -> {OUT}")


if __name__ == "__main__":
    build()
