"""The Vortfarado, Vortprovizo and Korelativoj kaj partikloj subdecks, from data/*.txt, one file per subdeck.
../build.py packages them."""
import os
import sys

import genanki

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import CSS, ROOT, bold, esc, gapped, marked, parse, word_hint  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# data file -> (subdeck, label shown on the card); deck IDs follow the subdeck's number
SUBDECKS = {
    "01-vortfarado.txt": ("01 Vortfarado", "Vortfarado"),
    "02-vortprovizo.txt": ("02 Vortprovizo", "Vortprovizo"),
    "03-korelativoj-kaj-partikloj.txt": ("03 Korelativoj kaj partikloj", "Korelativo, partiklo"),
}
DECKS = {file: genanki.Deck(1938270000 + int(file[:2]), f"{ROOT}::{deck}") for file, (deck, _) in SUBDECKS.items()}

HEAD = """<div class="ctx">{{Context}}</div>"""

PRODUCE_Q = HEAD + """
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Gapped}}</div>
<div class="hint">{{Hint}}</div>"""

PRODUCE_A = """{{FrontSide}}
<hr id="answer">
<div class="expr">{{Word}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

RECOG_Q = """{{#Recognition}}""" + HEAD + """
<div class="expr">{{Word}}</div>
<div class="hint">Kion ĝi signifas?</div>
{{WordAudio}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

FIELDS = ["Word", "Meaning", "Example", "Gapped", "Hint", "Notes", "Recognition", "Context",
          "WordAudio", "ExampleAudio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1720154401,
    "Esperanto Word",
    fields=[{"name": n} for n in FIELDS],
    templates=[
        {"name": "Produkti", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Rekoni", "qfmt": RECOG_Q, "afmt": RECOG_A},
    ],
    css=CSS,
    sort_field_index=0,
)


def rows():
    """(deck, model, fields, tags, guid, {audio field: text}) per word.

    Every note's example is spoken; the word only where a Rekoni card plays it.
    The hint names the base word where one is given (Vortfarado), else the gap's first letter and length.
    """
    files = sorted(os.listdir(DATA))
    if files != sorted(SUBDECKS):
        sys.exit(f"data/ files {files} don't match SUBDECKS")
    out, seen = [], set()
    for name in files:
        for ln, (word, meaning, example, note, base, recog) in parse(os.path.join(DATA, name), 6):
            where = f"{name} line {ln}"
            segs = marked(example, where)
            if recog not in ("", "R"):
                sys.exit(f"{where}: last field must be empty or R, not {recog}")
            if word.lower() in seen:
                sys.exit(f"{where}: duplicate {word}")
            seen.add(word.lower())
            fields = [""] * len(FIELDS)
            fields[F["Word"]] = esc(word)
            fields[F["Meaning"]] = esc(meaning)
            fields[F["Example"]] = bold(example)
            fields[F["Gapped"]] = gapped(example)
            fields[F["Hint"]] = f"el «{esc(base)}»" if base else word_hint(segs)
            fields[F["Notes"]] = note  # may hold <i> markup
            fields[F["Recognition"]] = "y" if recog else ""
            fields[F["Context"]] = SUBDECKS[name][1]
            tags = [f"type::{name[3:-4]}"]
            sources = {F["ExampleAudio"]: fields[F["Example"]]}
            if recog:
                sources[F["WordAudio"]] = fields[F["Word"]]
            guid = genanki.guid_for("esperanto-words", word.lower())
            out.append((DECKS[name], MODEL, fields, tags, guid, sources))
    return out
