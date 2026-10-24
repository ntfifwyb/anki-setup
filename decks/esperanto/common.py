"""What the Esperanto subdecks share: the data-file parser, the card style, and the audio clips,
named as the Psittacus add-on names them.

Psittacus has no Esperanto voice, so this deck uses its own: eSpeak NG's `eo` (see speak.py).
Clips are still named by Psittacus's cache_name, with "espeak" as the engine.

Each subdeck's build.py returns rows (deck, model, fields, tags, guid, {audio field: text to speak});
add_notes() turns them into notes, filling the audio fields, and speak.py speaks the clips they name.
"""
import html
import importlib
import os
import re
import sys
import types

import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = "Languages::Esperanto"
AUDIO = os.path.join(HERE, "audio")
LANG = "eo"
PSITTACUS = os.path.join(HERE, "..", "..", "addons", "psittacus", "addon")
# The engine and voice data that name the clips (Psittacus's cache_name) and that speak.py speaks with.
ENGINE, VOICE = "espeak", {"voice": "eo"}

CSS = """
.card { font-family: -apple-system, "Segoe UI", Roboto, sans-serif; font-size: 20px;
        line-height: 1.5; text-align: center; max-width: 640px; margin: 0 auto; padding: 12px; }
.chip { display: inline-block; font-size: 12px; letter-spacing: .06em; text-transform: uppercase;
        opacity: .6; border: 1px solid currentColor; border-radius: 4px; padding: 1px 6px; margin: 0 2px; }
.ctx { display: inline-block; font-size: 12px; letter-spacing: .06em; text-transform: uppercase; opacity: .6; margin-right: 6px; }
.meaning { font-size: 22px; margin: 18px 0 10px; }
.example { font-style: italic; opacity: .85; margin: 10px 0; }
.gap { font-style: normal; font-weight: 600; letter-spacing: .1em; opacity: .7; }
.hint { font-size: 14px; opacity: .55; }
.expr { font-size: 26px; font-weight: 700; margin: 10px 0; }
.choice { font-style: normal; font-weight: 600; white-space: nowrap; }
.notes { font-size: 15px; opacity: .7; margin-top: 16px; }
hr#answer { opacity: .3; }
"""

esc = lambda t: html.escape(t, quote=False)


def parse(path, n):
    """(line number, fields) per data line of a `|`-separated file with n fields; # starts a comment."""
    rows = []
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != n:
            sys.exit(f"{os.path.basename(path)} line {ln}: expected {n} fields, got {len(parts)}: {line}")
        rows.append((ln, parts))
    return rows


def marked(text, where):
    """The {{ }}-marked segments of a text; stops if there are none."""
    segs = re.findall(r"\{\{(.+?)\}\}", text)
    if not segs:
        sys.exit(f"{where}: no {{{{ }}}} marker in {text}")
    return segs


def bold(text):
    """Escaped text with its {{ }} segments in bold."""
    return re.sub(r"\{\{(.+?)\}\}", r"<b>\1</b>", esc(text))


def gapped(text):
    """Escaped text with its {{ }} segments blanked out."""
    return re.sub(r"\{\{(.+?)\}\}", '<span class="gap">_____</span>', esc(text))


def word_hint(segs):
    """How much is missing: '2 vortoj en 2 partoj', or a lone word's first letter and length."""
    words = sum(len(s.split()) for s in segs)
    if words == 1 and len(segs) == 1:
        return f"1 vorto · komenciĝas per «{segs[0][0].lower()}» · {len(segs[0])} literoj"
    hint = f"{words} vortoj"
    if len(segs) > 1:
        hint += f" en {len(segs)} partoj"
    return hint


def psittacus(module="core"):
    """A module of the Psittacus add-on (submodule), loaded without its Anki-only __init__."""
    if "psittacus" not in sys.modules:
        pkg = types.ModuleType("psittacus")
        pkg.__path__ = [PSITTACUS]
        sys.modules["psittacus"] = pkg
    return importlib.import_module(f"psittacus.{module}")


def clip(source):
    """(text, clip file name) for a field's HTML, named as Psittacus names it."""
    core = psittacus()
    text = core.clean_text(source)
    return text, core.cache_name(ENGINE, VOICE, text, 1.0)


def add_notes(rows):
    """Add rows to their decks as notes, each audio field set to its clip; returns the decks and media files."""
    decks, media, missing = [], [], 0
    for deck, model, fields, tags, guid, sources in rows:
        for i, source in sources.items():
            _, name = clip(source)
            path = os.path.join(AUDIO, name)
            missing += not os.path.exists(path)
            fields[i] = f"[sound:{name}]"
            media.append(path)
        deck.add_note(genanki.Note(model=model, fields=fields, tags=tags, guid=guid))
        if deck not in decks:
            decks.append(deck)
    if missing:
        sys.exit(f"{missing} audio clips missing from {AUDIO}: run speak.py")
    return decks, media
