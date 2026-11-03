"""The Verboj subdeck: the 2,000 most common verbs, from verbs.txt. ../build.py packages it."""
import os
import sys

import genanki

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import CSS, ROOT, bold, esc, gapped, marked, parse  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "verbs.txt")
DECK = genanki.Deck(1938270005, f"{ROOT}::05 Verboj")
# Verbs ranked from here on also get a Rekoni card. The first 500 are everyday verbs an
# intermediate speaker already understands; producing them is still worth practising.
RECOGNISE_FROM = 501

HEAD = """<div class="ctx">Verbo · n-ro {{Rank}} · {{Grammar}}</div>"""

PRODUCE_Q = HEAD + """
<div class="meaning">{{Definition}}</div>
<div class="example">{{Gapped}}</div>
<div class="hint">{{Hint}}</div>
<div class="hint">{{hint:English}}</div>"""

PRODUCE_A = """{{FrontSide}}
<hr id="answer">
<div class="expr">{{Verb}}</div>
<div class="example">{{Example}}</div>
<div class="hint">{{ExampleEnglish}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{VerbAudio}} {{ExampleAudio}}"""

RECOG_Q = """{{#Recognition}}""" + HEAD + """
<div class="expr">{{Verb}}</div>
<div class="hint">Kion ĝi signifas?</div>
{{VerbAudio}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="meaning">{{Definition}}</div>
<div class="example">{{Example}}</div>
<div class="hint">{{English}} · {{ExampleEnglish}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

FIELDS = ["Verb", "Grammar", "Definition", "Example", "Gapped", "Hint", "English", "ExampleEnglish",
          "Notes", "Rank", "Recognition", "VerbAudio", "ExampleAudio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1720154403,
    "Esperanto Verb",
    fields=[{"name": n} for n in FIELDS],
    templates=[
        {"name": "Produkti", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Rekoni", "qfmt": RECOG_Q, "afmt": RECOG_A},
    ],
    css=CSS,
    sort_field_index=0,
)

GRAMMAR = {"tr.": "transitiva", "ntr.": "netransitiva"}


def hint(segs):
    """The gap's first letter and length: the verb is known from the definition, its form from the sentence."""
    seg = segs[0]
    return f"komenciĝas per «{seg[0].lower()}» · {len(seg)} literoj"


def tags(rank, verb, grammar):
    band = (rank - 1) // 250 * 250
    out = [f"freq::{band + 1:04d}-{band + 250:04d}", f"verb::{GRAMMAR[grammar]}"]
    for suffix in ("ig", "iĝ"):
        if verb.endswith(suffix + "i"):
            out.append(f"affix::{suffix}")
    return out


def rows():
    """(deck, model, fields, tags, guid, {audio field: text}) per verb; every note speaks its verb and sentence."""
    out, seen, last = [], set(), 0
    for ln, (rank, verb, grammar, definition, example, en, ex_en, note) in parse(SRC, 8):
        where = f"verbs.txt line {ln}"
        rank = int(rank)
        if rank <= last:
            sys.exit(f"{where}: rank {rank} not after {last}")
        last = rank
        if grammar not in GRAMMAR:
            sys.exit(f"{where}: grammar must be tr. or ntr., not {grammar}")
        if verb in seen:
            sys.exit(f"{where}: duplicate {verb}")
        seen.add(verb)
        segs = marked(example, where)
        if len(segs) != 1:
            sys.exit(f"{where}: mark the verb once, not {len(segs)} times")
        fields = [""] * len(FIELDS)
        fields[F["Verb"]] = esc(verb)
        fields[F["Grammar"]] = grammar
        fields[F["Definition"]] = esc(definition)
        fields[F["Example"]] = bold(example)
        fields[F["Gapped"]] = gapped(example)
        fields[F["Hint"]] = hint(segs)
        fields[F["English"]] = esc(en)
        fields[F["ExampleEnglish"]] = esc(ex_en)
        fields[F["Notes"]] = note  # may hold <i> markup
        fields[F["Rank"]] = str(rank)
        fields[F["Recognition"]] = "y" if rank >= RECOGNISE_FROM else ""
        sources = {F["VerbAudio"]: fields[F["Verb"]], F["ExampleAudio"]: fields[F["Example"]]}
        guid = genanki.guid_for("esperanto-verbs", verb)
        out.append((DECK, MODEL, fields, tags(rank, verb, grammar), guid, sources))
    return out
