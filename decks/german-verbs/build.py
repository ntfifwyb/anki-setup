"""Build the German Verbs Anki deck (.apkg) from verbs.txt.

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
DECK = "Languages::German::Verbs"
OUT = os.path.join(HERE, "German_Verbs.apkg")
AUDIO = os.path.join(HERE, "audio")
LANG = "de"
PSITTACUS = os.path.join(HERE, "..", "..", "addons", "psittacus", "addon")
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
          "Notes", "Rank", "Recognition", "VerbAudio", "ExampleAudio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1580462913,
    "German Verb",
    fields=[{"name": n} for n in FIELDS],
    templates=[
        {"name": "Produce", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Recognise", "qfmt": RECOG_Q, "afmt": RECOG_A},
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
    for ln, rank, verb, forms, definition, example, en, ex_en, note in parse():
        rank = int(rank)
        segs = re.findall(r"\{\{(.+?)\}\}", example)
        if not segs:
            sys.exit(f"line {ln}: example has no {{{{ }}}} marker")
        if verb in seen:
            sys.exit(f"line {ln}: duplicate {verb}")
        seen.add(verb)
        ex_html = re.sub(r"\{\{(.+?)\}\}", r"<b>\1</b>", esc(example))
        gapped = re.sub(r"\{\{(.+?)\}\}", '<span class="gap">_____</span>', esc(example))
        hint = f"{len(segs)} Teile" if len(segs) > 1 else ""
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
        out.append((fields, tags(rank, forms, note), genanki.guid_for("german-verbs", verb)))
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

    Every note speaks its verb (both cards play it) and its example sentence.
    """
    core = psittacus()
    _, engine, v = voice()
    sources = {F["VerbAudio"]: fields[F["Verb"]], F["ExampleAudio"]: fields[F["Example"]]}
    texts = {i: core.clean_text(f) for i, f in sources.items()}
    return {i: (t, core.cache_name(engine, v, t, 1.0)) for i, t in texts.items()}


def build():
    deck = genanki.Deck(1716304582, DECK)
    media, missing, n_recog = [], 0, 0
    for fields, note_tags, guid in notes():
        for i, (_, name) in clips(fields).items():
            path = os.path.join(AUDIO, name)
            missing += not os.path.exists(path)
            fields[i] = f"[sound:{name}]"
            media.append(path)
        n_recog += bool(fields[F["Recognition"]])
        deck.add_note(genanki.Note(model=MODEL, fields=fields, tags=note_tags, guid=guid))
    if missing:
        sys.exit(f"{missing} audio clips missing from {AUDIO}: run speak.py")
    package = genanki.Package(deck)
    package.media_files = sorted(set(media))
    package.write_to_file(OUT)
    n = len(deck.notes)
    print(f"{n} notes, {n + n_recog} cards ({n_recog} recognition), {len(set(media))} clips -> {OUT}")


if __name__ == "__main__":
    build()
