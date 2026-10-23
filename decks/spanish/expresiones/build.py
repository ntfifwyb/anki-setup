"""The Locuciones, Colocaciones and Vocabulario culto subdecks, from data/*.txt, one file per subdeck.
../build.py packages them."""
import os
import sys

import genanki

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import CSS, ROOT, bold, esc, gapped, labels, marked, parse, word_hint  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# data file -> (subdeck, label shown on the card); deck IDs follow the subdeck's number
SUBDECKS = {
    "02-locuciones.txt": ("02 Locuciones", "Locución"),
    "03-colocaciones.txt": ("03 Colocaciones", "Colocación"),
    "04-vocabulario-culto.txt": ("04 Vocabulario culto", "Vocabulario culto"),
}
DECKS = {file: genanki.Deck(1834560000 + int(file[:2]), f"{ROOT}::{deck}") for file, (deck, _) in SUBDECKS.items()}

HEAD = """<div class="ctx">{{Context}}</div><span class="chip">{{Register}}</span>{{#Region}}<span class="chip">{{Region}}</span>{{/Region}}"""

PRODUCE_Q = HEAD + """
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Gapped}}</div>
<div class="hint">{{Hint}}</div>"""

PRODUCE_A = """{{FrontSide}}
<hr id="answer">
<div class="expr">{{Expression}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

RECOG_Q = """{{#Recognition}}""" + HEAD + """
<div class="expr">{{Expression}}</div>
<div class="hint">¿Qué significa?</div>
{{ExpressionAudio}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

FIELDS = ["Expression", "Meaning", "Example", "Gapped", "Hint", "Notes", "Register", "Region",
          "Recognition", "Context", "ExpressionAudio", "ExampleAudio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1720154301,
    "Spanish Expression",
    fields=[{"name": n} for n in FIELDS],
    templates=[
        {"name": "Producir", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Reconocer", "qfmt": RECOG_Q, "afmt": RECOG_A},
    ],
    css=CSS,
    sort_field_index=0,
)


def rows():
    """(deck, model, fields, tags, guid, {audio field: text}) per expression.

    Every note's example is spoken; the expression only where a Reconocer card plays it.
    """
    files = sorted(os.listdir(DATA))
    if files != sorted(SUBDECKS):
        sys.exit(f"data/ files {files} don't match SUBDECKS")
    out, seen = [], set()
    for name in files:
        for ln, (expr, meaning, example, note, register, region, recog) in parse(os.path.join(DATA, name), 7):
            where = f"{name} line {ln}"
            segs = marked(example, where)
            register_label, region_label = labels(register, region, where)
            if recog not in ("", "R"):
                sys.exit(f"{where}: last field must be empty or R, not {recog}")
            if expr.lower() in seen:
                sys.exit(f"{where}: duplicate {expr}")
            seen.add(expr.lower())
            fields = [""] * len(FIELDS)
            fields[F["Expression"]] = esc(expr)
            fields[F["Meaning"]] = esc(meaning)
            fields[F["Example"]] = bold(example)
            fields[F["Gapped"]] = gapped(example)
            fields[F["Hint"]] = word_hint(segs)
            fields[F["Notes"]] = note  # may hold <i> markup
            fields[F["Register"]] = register_label
            fields[F["Region"]] = region_label
            fields[F["Recognition"]] = "y" if recog else ""
            fields[F["Context"]] = SUBDECKS[name][1]
            tags = [f"register::{register}", f"type::{name[3:-4]}"] + ([f"region::{region}"] if region else [])
            sources = {F["ExampleAudio"]: fields[F["Example"]]}
            if recog:
                sources[F["ExpressionAudio"]] = fields[F["Expression"]]
            guid = genanki.guid_for("spanish-expresiones", expr.lower())
            out.append((DECKS[name], MODEL, fields, tags, guid, sources))
    return out
