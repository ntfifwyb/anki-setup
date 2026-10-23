"""The Norma y dudas subdeck, from dudas.txt. ../build.py packages it."""
import hashlib
import os
import re
import sys

import genanki

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import CSS, ROOT, esc, marked, parse  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "dudas.txt")
DECK = genanki.Deck(1834560005, f"{ROOT}::05 Norma y dudas")
TOPICS = {"dequeismo": "dequeísmo", "concordancia": "concordancia", "verbos": "verbos",
          "pronombres": "pronombres", "preposiciones": "preposiciones", "paronimos": "parónimos",
          "lexico": "léxico", "ortografia": "ortografía"}

HEAD = """<div class="ctx">Norma</div><span class="chip">{{Topic}}</span>"""

QUESTION = HEAD + """
<div class="meaning">{{Choice}}</div>
<div class="hint">¿Qué forma recomienda la norma culta?</div>"""

ANSWER = HEAD + """
<div class="meaning">{{Sentence}}</div>
<hr id="answer">
<div class="notes">{{Rule}}</div>
{{Audio}}"""

FIELDS = ["Sentence", "Choice", "Rule", "Topic", "Audio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1720154303,
    "Spanish Norma",
    fields=[{"name": n} for n in FIELDS],
    templates=[{"name": "Elegir", "qfmt": QUESTION, "afmt": ANSWER}],
    css=CSS,
    sort_field_index=0,
)

MARK = r"\{\{(.+?)\}\}"


def choice(m):
    """[ a / b ] for a {{correct/wrong…}} marker, in an order fixed by the options but not by which is right."""
    options = m.group(1).split("/")
    shown = sorted(options, key=lambda o: hashlib.sha1(o.encode()).hexdigest())
    return '<span class="choice">[ ' + " / ".join(o or "∅" for o in shown) + " ]</span>"


def rows():
    """(deck, model, fields, tags, guid, {audio field: text}) per sentence; the correct sentence is spoken."""
    out, seen = [], set()
    for ln, (sentence, rule, topic) in parse(DATA, 3):
        where = f"dudas.txt line {ln}"
        for seg in marked(sentence, where):
            if "/" not in seg:
                sys.exit(f"{where}: {{{{{seg}}}}} needs a wrong option after /")
        if topic not in TOPICS:
            sys.exit(f"{where}: unknown topic {topic!r}")
        right = re.sub(MARK, lambda m: m.group(1).split("/")[0], sentence)
        if right.lower() in seen:
            sys.exit(f"{where}: duplicate {right}")
        seen.add(right.lower())
        fields = [""] * len(FIELDS)
        # html.escape leaves braces and / intact, so substitute on the escaped text
        fields[F["Sentence"]] = re.sub(MARK, lambda m: f"<b>{m.group(1).split('/')[0]}</b>", esc(sentence))
        fields[F["Sentence"]] = re.sub(r"\s+", " ", fields[F["Sentence"]].replace("<b></b>", ""))
        fields[F["Choice"]] = re.sub(MARK, choice, esc(sentence))
        fields[F["Rule"]] = rule  # may hold <i> markup
        fields[F["Topic"]] = TOPICS[topic]
        guid = genanki.guid_for("spanish-norma", right.lower())
        out.append((DECK, MODEL, fields, [f"topic::{topic}"], guid, {F["Audio"]: fields[F["Sentence"]]}))
    return out
