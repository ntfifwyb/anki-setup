"""Build the English Expressions Anki deck (.apkg) from expressions.txt and contexts.txt.

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
SRC_SAVED = os.path.join(HERE, "expressions.txt")
SRC_NEW = os.path.join(HERE, "contexts.txt")
ROOT = "Languages::English::Expressions"

# context -> (subdeck, label shown on the card)
CONTEXTS = {
    "ielts-writing": ("01 IELTS Writing", "IELTS Writing Task 2"),
    "ielts-task1": ("01 IELTS Writing", "IELTS Writing Task 1"),
    "ielts-speaking": ("02 IELTS Speaking", "IELTS Speaking"),
    "work": ("03 Work and Email", "Work and meetings"),
    "email": ("03 Work and Email", "Formal emails"),
    "diplomacy": ("04 Disagreeing and Negotiating", "Disagreeing and negotiating"),
    "precision": ("05 Saying It Precisely", "Saying it precisely"),
    "emotions": ("06 Emotions", "Describing emotions"),
    "social": ("07 Social Life and Dating", "Social life and dating"),
    "support": ("08 Support and Apologies", "Support and apologies"),
    "admin": ("09 Services and Admin", "Services, landlords, offices"),
    "friends": ("10 With Friends", "With friends"),
}
SAVED_DECK = "00 My Saved Phrases"
SAVED_LABELS = {
    "banter": "Banter", "work": "Work", "conversation": "Conversation", "reactions": "Reacting",
    "disagreement": "Disagreeing", "warnings": "Warnings", "situations": "Describing situations",
    "money": "Money", "feelings": "Feelings", "sayings": "Sayings and proverbs",
}
OUT = os.path.join(HERE, "English_Expressions.apkg")
AUDIO = os.path.join(HERE, "audio")
LANG = "en_US"
PSITTACUS = os.path.join(HERE, "..", "..", "addons", "psittacus", "addon")

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
.notes { font-size: 15px; opacity: .7; margin-top: 16px; }
hr#answer { opacity: .3; }
"""

PRODUCE_Q = """<div class="ctx">{{Context}}</div> <div class="reg">{{Register}}</div>
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Gapped}}</div>
<div class="hint">{{Hint}}</div>"""

PRODUCE_A = """{{FrontSide}}
<hr id="answer">
<div class="expr">{{Expression}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

RECOG_Q = """{{#Recognition}}<div class="ctx">{{Context}}</div> <div class="reg">{{Register}}</div>
<div class="expr">{{Expression}}</div>
<div class="hint">What does it mean?</div>
{{ExpressionAudio}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}
{{ExampleAudio}}"""

MODEL = genanki.Model(
    1844176211,
    "English Expression",
    fields=[{"name": n} for n in
            ["Expression", "Meaning", "Example", "Gapped", "Hint", "Notes", "Register", "Recognition", "Context",
              "ExpressionAudio", "ExampleAudio"]],
    templates=[
        {"name": "Produce", "qfmt": PRODUCE_Q, "afmt": PRODUCE_A},
        {"name": "Recognise", "qfmt": RECOG_Q, "afmt": RECOG_A},
    ],
    css=CSS,
    sort_field_index=0,
)

DECKS = {}


def deck(sub):
    name = f"{ROOT}::{sub}"
    if name not in DECKS:
        DECKS[name] = genanki.Deck(1739284057 + 1 + len(DECKS), name)
    return DECKS[name]


def parse(src):
    rows = []
    for ln, line in enumerate(open(src, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 6 or len(parts) > 7:
            sys.exit(f"line {ln}: expected 6-7 fields, got {len(parts)}: {line}")
        parts += [""] * (7 - len(parts))
        rows.append((ln, *parts[:7]))
    return rows


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


def notes():
    """(subdeck, fields, tags, guid) per note, the audio fields still empty."""
    seen = set()
    out = []
    rows = [("saved", r) for r in parse(SRC_SAVED)] + [("new", r) for r in parse(SRC_NEW)]
    for origin, (ln, expr, meaning, example, notes, register, topic, recog) in rows:
        if origin == "saved":
            sub, label = SAVED_DECK, f"Saved · {SAVED_LABELS[topic]}"
            tags = [f"register::{register}", f"topic::{topic}", "source::saved-phrases"]
        else:
            if topic not in CONTEXTS:
                sys.exit(f"contexts line {ln}: unknown context {topic}")
            sub, label = CONTEXTS[topic]
            tags = [f"register::{register}", f"context::{topic}", "source::claude"]
        segs = re.findall(r"\{\{(.+?)\}\}", example)
        if not segs:
            sys.exit(f"line {ln}: example has no {{{{ }}}} marker")
        if expr.lower() in seen:
            sys.exit(f"{origin} line {ln}: duplicate {expr}")
        seen.add(expr.lower())
        esc = lambda t: html.escape(t, quote=False)
        # html.escape leaves braces intact, so substitute on the escaped text
        ex_html = re.sub(r"\{\{(.+?)\}\}", r"<b>\1</b>", esc(example))
        gapped = re.sub(r"\{\{(.+?)\}\}", '<span class="gap">_____</span>', esc(example))
        words = sum(len(s.split()) for s in segs)
        hint = f"{words} word{'s' if words != 1 else ''}"
        if len(segs) > 1:
            hint += f" in {len(segs)} parts"
        r = "y" if recog.upper() == "R" else ""
        fields = [esc(expr), esc(meaning), ex_html, gapped, hint, esc(notes), register, r, label, "", ""]
        out.append((sub, fields, tags, genanki.guid_for("english-expressions", expr.lower())))
    return out


def clips(fields):
    """{audio field index: (text, clip file name)} for a note, named as Psittacus names them.

    The expression is only spoken where a Recognise card plays it; every note's example is.
    """
    core = psittacus()
    _, engine, v = voice()
    sources = {10: fields[2]} | ({9: fields[0]} if fields[7] else {})
    texts = {i: core.clean_text(f) for i, f in sources.items()}
    return {i: (t, core.cache_name(engine, v, t, 1.0)) for i, t in texts.items()}


def build():
    media, missing, n_recog = [], 0, 0
    for sub, fields, tags, guid in notes():
        for i, (_, name) in clips(fields).items():
            path = os.path.join(AUDIO, name)
            missing += not os.path.exists(path)
            fields[i] = f"[sound:{name}]"
            media.append(path)
        n_recog += bool(fields[7])
        deck(sub).add_note(genanki.Note(model=MODEL, fields=fields, tags=tags, guid=guid))
    if missing:
        sys.exit(f"{missing} audio clips missing from {AUDIO}: run speak.py")
    package = genanki.Package(list(DECKS.values()))
    package.media_files = sorted(set(media))
    package.write_to_file(OUT)
    n = sum(len(d.notes) for d in DECKS.values())
    print(f"{n} notes, {n + n_recog} cards ({n_recog} recognition), {len(set(media))} clips -> {OUT}")


if __name__ == "__main__":
    build()
