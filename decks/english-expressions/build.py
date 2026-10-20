"""Build the English Expressions Anki deck (.apkg) from expressions.txt."""
import html
import os
import re
import sys

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
{{tts en_US:Expression}}"""

RECOG_Q = """{{#Recognition}}<div class="ctx">{{Context}}</div> <div class="reg">{{Register}}</div>
<div class="expr">{{Expression}}</div>
<div class="hint">What does it mean?</div>
{{tts en_US:Expression}}{{/Recognition}}"""

RECOG_A = """{{FrontSide}}
<hr id="answer">
<div class="meaning">{{Meaning}}</div>
<div class="example">{{Example}}</div>
{{#Notes}}<div class="notes">{{Notes}}</div>{{/Notes}}"""

MODEL = genanki.Model(
    1844176211,
    "English Expression",
    fields=[{"name": n} for n in
            ["Expression", "Meaning", "Example", "Gapped", "Hint", "Notes", "Register", "Recognition", "Context"]],
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


def build():
    seen = set()
    n_recog = 0
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
        n_recog += bool(r)
        deck(sub).add_note(genanki.Note(
            model=MODEL,
            fields=[esc(expr), esc(meaning), ex_html, gapped, hint, esc(notes), register, r, label],
            tags=tags,
            guid=genanki.guid_for("english-expressions", expr.lower()),
        ))
    genanki.Package(list(DECKS.values())).write_to_file(OUT)
    print(f"{len(seen)} notes, {len(seen) + n_recog} cards ({n_recog} recognition) -> {OUT}")


if __name__ == "__main__":
    build()
