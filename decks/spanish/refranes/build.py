"""The Refranes subdeck, from refranes.txt. ../build.py packages it."""
import os
import sys

import genanki

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import CSS, REGIONS, ROOT, bold, esc, gapped, marked, parse, word_hint  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "refranes.txt")
DECK = genanki.Deck(1834560001, f"{ROOT}::01 Refranes")

HEAD = """<div class="ctx">Refrán</div>{{#Region}}<span class="chip">{{Region}}</span>{{/Region}}"""

QUESTION = HEAD + """
<div class="refran">{{Gapped}}</div>
<div class="hint">{{Hint}} · complétalo y di qué significa</div>"""

ANSWER = HEAD + """
<div class="refran">{{Refran}}</div>
<hr id="answer">
<div class="meaning">{{Meaning}}</div>
{{#German}}<div class="equiv"><b>DE</b>{{German}}</div>{{/German}}
{{#English}}<div class="equiv"><b>EN</b>{{English}}</div>{{/English}}
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{Audio}}"""

FIELDS = ["Refran", "Gapped", "Hint", "Meaning", "German", "English", "Notes", "Region", "Audio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1720154302,
    "Spanish Refrán",
    fields=[{"name": n} for n in FIELDS],
    templates=[{"name": "Completar", "qfmt": QUESTION, "afmt": ANSWER}],
    css=CSS,
    sort_field_index=0,
)


def rows():
    """(deck, model, fields, tags, guid, {audio field: text}) per refrán; the full refrán is spoken."""
    out, seen = [], set()
    for ln, (refran, meaning, de, en, note, region) in parse(DATA, 6):
        where = f"refranes.txt line {ln}"
        segs = marked(refran, where)
        if region not in REGIONS:
            sys.exit(f"{where}: unknown region {region!r}")
        key = refran.replace("{{", "").replace("}}", "").lower()
        if key in seen:
            sys.exit(f"{where}: duplicate {refran}")
        seen.add(key)
        fields = [""] * len(FIELDS)
        fields[F["Refran"]] = bold(refran)
        fields[F["Gapped"]] = gapped(refran)
        fields[F["Hint"]] = word_hint(segs)
        fields[F["Meaning"]] = esc(meaning)
        fields[F["German"]] = esc(de)
        fields[F["English"]] = esc(en)
        fields[F["Notes"]] = note  # may hold <i> markup
        fields[F["Region"]] = REGIONS[region]
        tags = ["type::refran"] + ([f"region::{region}"] if region else [])
        guid = genanki.guid_for("spanish-refranes", key)
        out.append((DECK, MODEL, fields, tags, guid, {F["Audio"]: fields[F["Refran"]]}))
    return out
