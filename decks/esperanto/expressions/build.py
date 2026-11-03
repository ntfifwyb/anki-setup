"""The 06 Esprimoj subdecks, from data/*.txt, one file per subdeck. ../build.py packages them.

Notes use the Esperanto Word note type of ../words/ (the expression in its Word field), so the
cards look and work like the other subdecks'. Proverbs come from Zamenhof's Proverbaro Esperanta:
their example is the proverb itself, with its second half gapped.
"""
import importlib.util
import os
import sys

import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from common import ROOT, bold, esc, gapped, marked, parse, word_hint  # noqa: E402

DATA = os.path.join(HERE, "data")
DECK = f"{ROOT}::06 Esprimoj"

# data file -> (subdeck, label shown on the card); deck IDs follow the subdeck's number
SUBDECKS = {
    "01-prepozicioj.txt": ("01 Prepozicioj", "Prepozicio"),
    "02-kolokacioj.txt": ("02 Kolokacioj", "Kolokacio"),
    "03-frazoj.txt": ("03 Frazoj kaj diskursaj vortoj", "Frazo"),
    "04-proverboj.txt": ("04 Proverboj", "Proverbo"),
}
DECKS = {file: genanki.Deck(1938270600 + int(file[:2]), f"{DECK}::{deck}") for file, (deck, _) in SUBDECKS.items()}


def words():
    """../words/build.py, for its note type."""
    spec = importlib.util.spec_from_file_location("words_build", os.path.join(HERE, "..", "words", "build.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rows():
    """(deck, model, fields, tags, guid, {audio field: text}) per expression.

    Every note's example is spoken; the expression only where a Rekoni card plays it.
    """
    w = words()
    F = w.F
    files = sorted(os.listdir(DATA))
    if files != sorted(SUBDECKS):
        sys.exit(f"data/ files {files} don't match SUBDECKS")
    out, seen = [], set()
    for name in files:
        for ln, (expr, meaning, example, note, recog) in parse(os.path.join(DATA, name), 5):
            where = f"{name} line {ln}"
            segs = marked(example, where)
            if recog not in ("", "R"):
                sys.exit(f"{where}: last field must be empty or R, not {recog}")
            if expr.lower() in seen:
                sys.exit(f"{where}: duplicate {expr}")
            seen.add(expr.lower())
            if name.startswith("04") and example.replace("{{", "").replace("}}", "") != expr:
                sys.exit(f"{where}: a proverb's example must be the proverb itself")
            fields = [""] * len(w.FIELDS)
            fields[F["Word"]] = esc(expr)
            fields[F["Meaning"]] = esc(meaning)
            fields[F["Example"]] = bold(example)
            fields[F["Gapped"]] = gapped(example)
            fields[F["Hint"]] = word_hint(segs)
            fields[F["Notes"]] = note  # may hold <i> markup
            fields[F["Recognition"]] = "y" if recog else ""
            fields[F["Context"]] = SUBDECKS[name][1]
            tags = [f"type::{name[3:-4]}"]
            sources = {F["ExampleAudio"]: fields[F["Example"]]}
            if recog:
                sources[F["WordAudio"]] = fields[F["Word"]]
            guid = genanki.guid_for("esperanto-expressions", expr.lower())
            out.append((DECKS[name], w.MODEL, fields, tags, guid, sources))
    return out
