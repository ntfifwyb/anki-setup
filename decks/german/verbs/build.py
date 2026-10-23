"""The German Verbs subdeck, from verbs.txt and senses.txt. ../build.py packages it.

The audio clips come from audio/, which speak.py fills.
"""
import html
import importlib
import os
import re
import sys
import types
from pathlib import Path

import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "verbs.txt")
SENSES = os.path.join(HERE, "senses.txt")
DECK = "Languages::Deutsch::Verben"
AUDIO = os.path.join(HERE, "audio")
LANG = "de"
PSITTACUS = os.path.join(HERE, "..", "..", "..", "addons", "psittacus", "addon")
# Verbs ranked above this also get a Recognise card. The first 500 are everyday verbs a B2
# learner already understands; producing them is still worth practising, recognising is not.
RECOGNISE_FROM = 501

CSS = """
.card { font-family: -apple-system, "Segoe UI", Roboto, sans-serif; font-size: 20px;
        line-height: 1.5; text-align: center; max-width: 640px; margin: 0 auto; padding: 12px; }
.tag { display: inline-block; font-size: 12px; letter-spacing: .06em; text-transform: uppercase; opacity: .55; }
.def { font-size: 22px; margin: 18px 0 10px; }
.example { font-style: italic; opacity: .85; margin: 10px 0; }
.gap { font-style: normal; font-weight: 600; letter-spacing: .1em; opacity: .7; }
.hint { font-size: 14px; opacity: .55; }
.verb { font-size: 28px; font-weight: 700; margin: 10px 0 2px; }
.forms { font-size: 16px; opacity: .75; margin-bottom: 10px; }
.en { font-size: 15px; opacity: .55; margin-top: 4px; }
.notes { font-size: 15px; opacity: .7; margin-top: 16px; }
a.hint { color: inherit; }
hr#answer { opacity: .3; }
"""

PRODUCE_Q = """<div class="tag">Verb · Nr. {{Rank}}</div>
<div class="def">{{Definition}}</div>
<div class="example">{{Gapped}}</div>
<div class="hint">{{Hint}}</div>
<div class="hint">{{hint:English}}</div>"""

PRODUCE_A = """{{FrontSide}}
<hr id="answer">
<div class="verb">{{Verb}}</div>
<div class="forms">{{Forms}}</div>
<div class="example">{{Example}}</div>
<div class="en">{{ExampleEnglish}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{VerbAudio}} {{ExampleAudio}}"""

PRODUCE2_Q = """{{#Gapped2}}<div class="tag">Verb · Nr. {{Rank}} · 2. Bedeutung</div>
<div class="def">{{Definition2}}</div>
<div class="example">{{Gapped2}}</div>
<div class="hint">{{Hint2}}</div>
<div class="hint">{{hint:English2}}</div>{{/Gapped2}}"""

PRODUCE2_A = """{{FrontSide}}
<hr id="answer">
<div class="verb">{{Verb}}</div>
<div class="forms">{{Forms}}</div>
<div class="example">{{Example2}}</div>
<div class="en">{{ExampleEnglish2}}</div>
{{VerbAudio}} {{Example2Audio}}"""

RECOG_Q = """{{#Recognition}}<div class="tag">Verb · Nr. {{Rank}}</div>
<div class="verb">{{Verb}}</div>
<div class="hint">Was bedeutet das?</div>
{{VerbAudio}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="def">{{Definition}}</div>
<div class="forms">{{Forms}}</div>
<div class="example">{{Example}}</div>
<div class="en">{{English}} · {{ExampleEnglish}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

FIELDS = ["Verb", "Forms", "Definition", "Example", "Gapped", "Hint", "English", "ExampleEnglish",
          "Notes", "Rank", "Recognition", "VerbAudio", "ExampleAudio",
          # A second meaning (senses.txt), appended so Anki can merge the note type on import.
          "Definition2", "Example2", "Gapped2", "Hint2", "English2", "ExampleEnglish2", "Example2Audio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1580462913,
    "German Verb",
    fields=[{"name": n} for n in FIELDS],
    templates=[
        {"name": "Produce", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Recognise", "qfmt": RECOG_Q, "afmt": RECOG_A},
        {"name": "Produce 2", "qfmt": PRODUCE2_Q, "afmt": PRODUCE2_A},
    ],
    css=CSS,
    sort_field_index=0,
)


def parse():
    rows = []
    for ln, line in enumerate(open(SRC, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) == 7:
            parts.append("")
        if len(parts) != 8:
            sys.exit(f"line {ln}: expected 8 fields, got {len(parts)}: {line}")
        rows.append((ln, *parts))
    return rows


def parse_senses():
    """{verb: (definition, example, English, English example)} from senses.txt."""
    out = {}
    for ln, line in enumerate(open(SENSES, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) != 5:
            sys.exit(f"senses.txt line {ln}: expected 5 fields, got {len(parts)}: {line}")
        if parts[0] in out:
            sys.exit(f"senses.txt line {ln}: duplicate {parts[0]}")
        out[parts[0]] = tuple(parts[1:])
    return out


def gap(ln, example):
    """(example with the verb's words in bold, gapped example, hint) for an example with {{ }} marks."""
    segs = re.findall(r"\{\{(.+?)\}\}", example)
    if not segs:
        sys.exit(f"line {ln}: example has no {{{{ }}}} marker")
    esc = html.escape(example, quote=False)
    bold = re.sub(r"\{\{(.+?)\}\}", r"<b>\1</b>", esc)
    gapped = re.sub(r"\{\{(.+?)\}\}", '<span class="gap">_____</span>', esc)
    return bold, gapped, f"{len(segs)} Teile" if len(segs) > 1 else ""


def tags(rank, forms, notes):
    pres, past, perf = forms.split(" – ")
    band = (rank - 1) // 250 * 250
    out = [f"freq::{band + 1:04d}-{band + 250:04d}"]
    if " " in pres:
        out.append("verb::separable")
    if not re.search(r"te$", past.split("/")[0].split()[0]):  # strong: no -te in the Präteritum
        out.append("verb::strong")
    if perf.startswith("ist") or perf.startswith("hat/ist") or perf.startswith("ist/hat"):
        out.append("aux::sein")
    if re.search(r"\bsich \w", notes):
        out.append("verb::reflexive")
    low = notes.lower()
    if "vulgär" in low or "derb" in low:
        out.append("register::vulgar")
    elif "umgangssprachlich" in low or "jugendsprache" in low:
        out.append("register::colloquial")
    elif "gehoben" in low or "formell" in low or "amtssprache" in low:
        out.append("register::formal")
    return out


def notes():
    """(fields, tags, guid) per note, the audio fields still empty."""
    seen = set()
    out = []
    esc = lambda t: html.escape(t, quote=False)
    senses = parse_senses()
    for ln, rank, verb, forms, definition, example, en, ex_en, note in parse():
        rank = int(rank)
        if verb in seen:
            sys.exit(f"line {ln}: duplicate {verb}")
        seen.add(verb)
        ex_html, gapped, hint = gap(ln, example)
        fields = [""] * len(FIELDS)
        fields[F["Verb"]] = esc(verb)
        fields[F["Forms"]] = esc(forms)
        fields[F["Definition"]] = esc(definition)
        fields[F["Example"]] = ex_html
        fields[F["Gapped"]] = gapped
        fields[F["Hint"]] = hint
        fields[F["English"]] = esc(en)
        fields[F["ExampleEnglish"]] = esc(ex_en)
        fields[F["Notes"]] = note  # may hold <i> markup
        fields[F["Rank"]] = str(rank)
        fields[F["Recognition"]] = "y" if rank >= RECOGNISE_FROM else ""
        if verb in senses:
            definition2, example2, en2, ex_en2 = senses.pop(verb)
            ex2_html, gapped2, hint2 = gap(f"senses.txt {verb}", example2)
            fields[F["Definition2"]] = esc(definition2)
            fields[F["Example2"]] = ex2_html
            fields[F["Gapped2"]] = gapped2
            fields[F["Hint2"]] = hint2
            fields[F["English2"]] = esc(en2)
            fields[F["ExampleEnglish2"]] = esc(ex_en2)
        out.append((fields, tags(rank, forms, note), genanki.guid_for("german-verbs", verb)))
    if senses:
        sys.exit(f"senses.txt: not in verbs.txt: {', '.join(senses)}")
    return out


def psittacus(module="core"):
    """A module of the Psittacus add-on (submodule), loaded without its Anki-only __init__."""
    if "psittacus" not in sys.modules:
        pkg = types.ModuleType("psittacus")
        pkg.__path__ = [PSITTACUS]
        sys.modules["psittacus"] = pkg
    return importlib.import_module(f"psittacus.{module}")


def voice():
    """(voice data, engine, voice) Psittacus picks first for the deck's language."""
    core = psittacus()
    data = core.load_voices(Path(PSITTACUS) / "voices.json")
    engine, v = core.candidates(LANG, data)[0]
    return data, engine, v


def clips(fields):
    """{audio field index: (text, clip file name)} for a note, named as Psittacus names them.

    Every note speaks its verb (every card plays it), its example sentence and, if it has a
    second meaning, that meaning's example.
    """
    core = psittacus()
    _, engine, v = voice()
    sources = {F["VerbAudio"]: fields[F["Verb"]], F["ExampleAudio"]: fields[F["Example"]]}
    if fields[F["Example2"]]:
        sources[F["Example2Audio"]] = fields[F["Example2"]]
    texts = {i: core.clean_text(f) for i, f in sources.items()}
    return {i: (t, core.cache_name(engine, v, t, 1.0)) for i, t in texts.items()}


def build():
    """(decks, media files) of the subdeck."""
    deck = genanki.Deck(1716304582, DECK)
    media, missing, n_recog, n_second = [], 0, 0, 0
    for fields, note_tags, guid in notes():
        for i, (_, name) in clips(fields).items():
            path = os.path.join(AUDIO, name)
            missing += not os.path.exists(path)
            fields[i] = f"[sound:{name}]"
            media.append(path)
        n_recog += bool(fields[F["Recognition"]])
        n_second += bool(fields[F["Gapped2"]])
        deck.add_note(genanki.Note(model=MODEL, fields=fields, tags=note_tags, guid=guid))
    if missing:
        sys.exit(f"{missing} audio clips missing from {AUDIO}: run speak.py")
    n = len(deck.notes)
    print(f"Verbs: {n} notes, {n + n_recog + n_second} cards ({n_recog} recognition, {n_second} second meaning),"
          f" {len(set(media))} clips")
    return [deck], media

