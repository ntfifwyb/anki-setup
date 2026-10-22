"""Build the German Expressions Anki deck (.apkg) from data/*.txt, one file per subdeck.

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
DATA = os.path.join(HERE, "data")
ROOT = "Languages::German::Expressions"
OUT = os.path.join(HERE, "German_Expressions.apkg")
AUDIO = os.path.join(HERE, "audio")
LANG = "de"
PSITTACUS = os.path.join(HERE, "..", "..", "addons", "psittacus", "addon")

# data file -> (subdeck, label shown on the card)
SUBDECKS = {
    "01-funktionsverbgefuege.txt": ("01 Funktionsverbgefüge", "Funktionsverbgefüge"),
    "02-verb-praeposition.txt": ("02 Verb + Präposition", "Verb + Präposition"),
    "03-kollokationen.txt": ("03 Kollokationen", "Kollokation"),
    "04-diskutieren.txt": ("04 Diskutieren und Argumentieren", "Diskutieren"),
    "05-arbeit-emails.txt": ("05 Arbeit und E-Mails", "Arbeit und E-Mails"),
    "06-redewendungen.txt": ("06 Redewendungen", "Redewendung"),
}
# register (tag) -> label shown on the card
REGISTERS = {"neutral": "neutral", "formal": "formell", "colloquial": "umgangssprachlich", "vulgar": "derb"}

CSS = """
.card { font-family: -apple-system, "Segoe UI", Roboto, sans-serif; font-size: 20px;
        line-height: 1.5; text-align: center; max-width: 640px; margin: 0 auto; padding: 12px; }
.reg { display: inline-block; font-size: 12px; letter-spacing: .06em; text-transform: uppercase;
       opacity: .6; border: 1px solid currentColor; border-radius: 4px; padding: 1px 6px; }
.ctx { display: inline-block; font-size: 12px; letter-spacing: .06em; text-transform: uppercase; opacity: .6; margin-right: 6px; }
.meaning { font-size: 22px; margin: 18px 0 10px; }
.example { font-style: italic; opacity: .85; margin: 10px 0; }
.gap { font-style: normal; font-weight: 600; letter-spacing: .1em; opacity: .7; }
.hint { font-size: 14px; opacity: .55; }
.expr { font-size: 26px; font-weight: 700; margin: 10px 0; }
.en { font-size: 15px; opacity: .55; margin-top: 4px; }
.notes { font-size: 15px; opacity: .7; margin-top: 16px; }
a.hint { color: inherit; }
hr#answer { opacity: .3; }
"""

PRODUCE_Q = """<div class="ctx">{{Context}}</div> <div class="reg">{{Register}}</div>
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Gapped}}</div>
<div class="hint">{{Hint}}</div>
<div class="hint">{{hint:English}}</div>"""

PRODUCE_A = """{{FrontSide}}
<hr id="answer">
<div class="expr">{{Expression}}</div>
<div class="example">{{Example}}</div>
<div class="en">{{ExampleEnglish}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

RECOG_Q = """{{#Recognition}}<div class="ctx">{{Context}}</div> <div class="reg">{{Register}}</div>
<div class="expr">{{Expression}}</div>
<div class="hint">Was bedeutet das?</div>
{{ExpressionAudio}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Example}}</div>
<div class="en">{{English}} · {{ExampleEnglish}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

FIELDS = ["Expression", "Meaning", "Example", "Gapped", "Hint", "English", "ExampleEnglish", "Notes",
          "Register", "Recognition", "Context", "ExpressionAudio", "ExampleAudio"]
F = {name: i for i, name in enumerate(FIELDS)}

MODEL = genanki.Model(
    1589549670,
    "German Expression",
    fields=[{"name": n} for n in FIELDS],
    templates=[
        {"name": "Produce", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Recognise", "qfmt": RECOG_Q, "afmt": RECOG_A},
    ],
    css=CSS,
    sort_field_index=0,
)

DECKS = {}


def deck(file):
    """The subdeck for a data file. Its ID follows the file's position, so it stays stable."""
    name = f"{ROOT}::{SUBDECKS[file][0]}"
    if name not in DECKS:
        DECKS[name] = genanki.Deck(1703937062 + 1 + list(SUBDECKS).index(file), name)
    return DECKS[name]


def parse(path):
    rows = []
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 8:
            sys.exit(f"{os.path.basename(path)} line {ln}: expected 8 fields, got {len(parts)}: {line}")
        rows.append((ln, *parts))
    return rows


def notes():
    """(data file, fields, tags, guid) per note, the audio fields still empty."""
    files = sorted(os.listdir(DATA))
    if files != sorted(SUBDECKS):
        sys.exit(f"data/ files {files} don't match SUBDECKS")
    seen = set()
    out = []
    esc = lambda t: html.escape(t, quote=False)
    for name in files:
        label = SUBDECKS[name][1]
        for ln, expr, meaning, example, en, ex_en, note, register, recog in parse(os.path.join(DATA, name)):
            where = f"{name} line {ln}"
            segs = re.findall(r"\{\{(.+?)\}\}", example)
            if not segs:
                sys.exit(f"{where}: example has no {{{{ }}}} marker")
            if register not in REGISTERS:
                sys.exit(f"{where}: unknown register {register}")
            if recog not in ("", "R"):
                sys.exit(f"{where}: last field must be empty or R, not {recog}")
            if expr.lower() in seen:
                sys.exit(f"{where}: duplicate {expr}")
            seen.add(expr.lower())
            # html.escape leaves braces intact, so substitute on the escaped text
            ex_html = re.sub(r"\{\{(.+?)\}\}", r"<b>\1</b>", esc(example))
            gapped = re.sub(r"\{\{(.+?)\}\}", '<span class="gap">_____</span>', esc(example))
            words = sum(len(s.split()) for s in segs)
            hint = f"{words} Wort" if words == 1 else f"{words} Wörter"
            if len(segs) > 1:
                hint += f" in {len(segs)} Teilen"
            fields = [""] * len(FIELDS)
            fields[F["Expression"]] = esc(expr)
            fields[F["Meaning"]] = esc(meaning)
            fields[F["Example"]] = ex_html
            fields[F["Gapped"]] = gapped
            fields[F["Hint"]] = hint
            fields[F["English"]] = esc(en)
            fields[F["ExampleEnglish"]] = esc(ex_en)
            fields[F["Notes"]] = note  # may hold <i> markup
            fields[F["Register"]] = REGISTERS[register]
            fields[F["Recognition"]] = "y" if recog else ""
            fields[F["Context"]] = label
            tags = [f"register::{register}", f"type::{name[3:-4]}"]
            out.append((name, fields, tags, genanki.guid_for("german-expressions", expr.lower())))
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

    The expression is only spoken where a Recognise card plays it; every note's example is.
    """
    core = psittacus()
    _, engine, v = voice()
    sources = {F["ExampleAudio"]: fields[F["Example"]]}
    if fields[F["Recognition"]]:
        sources[F["ExpressionAudio"]] = fields[F["Expression"]]
    texts = {i: core.clean_text(f) for i, f in sources.items()}
    return {i: (t, core.cache_name(engine, v, t, 1.0)) for i, t in texts.items()}


def build():
    media, missing, n_recog = [], 0, 0
    for file, fields, tags, guid in notes():
        for i, (_, name) in clips(fields).items():
            path = os.path.join(AUDIO, name)
            missing += not os.path.exists(path)
            fields[i] = f"[sound:{name}]"
            media.append(path)
        n_recog += bool(fields[F["Recognition"]])
        deck(file).add_note(genanki.Note(model=MODEL, fields=fields, tags=tags, guid=guid))
    if missing:
        sys.exit(f"{missing} audio clips missing from {AUDIO}: run speak.py")
    package = genanki.Package(list(DECKS.values()))
    package.media_files = sorted(set(media))
    package.write_to_file(OUT)
    n = sum(len(d.notes) for d in DECKS.values())
    per = ", ".join(f"{name.split('::')[-1][:2]}: {len(d.notes)}" for name, d in sorted(DECKS.items()))
    print(f"{n} notes ({per}), {n + n_recog} cards ({n_recog} recognition), {len(set(media))} clips -> {OUT}")


if __name__ == "__main__":
    build()
