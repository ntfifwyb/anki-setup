"""Regenerate backup/settings and backup/exports from a collection.anki2 file.

Usage: python regenerate.py path/to/collection.anki2
Requires: pip install anki
"""
import csv
import json
import os
import re
import shutil
import sys
import tempfile

from anki.collection import Collection

BACKUP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS = os.path.join(BACKUP, "settings")
EXPORTS = os.path.join(BACKUP, "exports")


def main(src):
    os.makedirs(SETTINGS, exist_ok=True)
    os.makedirs(EXPORTS, exist_ok=True)
    tmp = os.path.join(tempfile.mkdtemp(), "collection.anki2")
    shutil.copy(src, tmp)  # never open the original
    col = Collection(tmp)
    try:
        dump = lambda name, obj: json.dump(obj, open(os.path.join(SETTINGS, name), "w", encoding="utf-8"),
                                          indent=2, ensure_ascii=False, sort_keys=True, default=str)
        dump("deck_options.json", col.decks.all_config())
        dump("decks.json", [{"id": d.id, "name": d.name} for d in col.decks.all_names_and_ids()])
        dump("note_types.json", [{"id": m["id"], "name": m["name"],
                                  "fields": [f["name"] for f in m["flds"]],
                                  "card_templates": [t["name"] for t in m["tmpls"]]}
                                 for m in col.models.all()])
        config = {}
        for key in col.all_config():
            config[key] = col.get_config(key)
        dump("collection_config.json", config)
        open(os.path.join(SETTINGS, "preferences.txt"), "w").write(str(col.get_preferences()))

        rows = []
        for nid in col.find_notes(""):
            note = col.get_note(nid)
            deck = col.decks.name(note.cards()[0].did)
            model = note.note_type()
            rows.append((deck, model["name"], " ".join(note.tags),
                         [f["name"] for f in model["flds"]], list(note.fields)))
        rows.sort(key=lambda r: (r[0], r[1]))
        with open(os.path.join(EXPORTS, "all_notes.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["deck", "note_type", "tags", "fields..."])
            for deck, nt, tags, _, vals in rows:
                w.writerow([deck, nt, tags] + vals)
        md = ["# All notes (readable export)", "",
              "Generated from the collection. The importable backup is `backup/collection/collection.colpkg`.", ""]
        current = None
        for deck, nt, tags, names, vals in rows:
            if deck != current:
                md += ["", f"## Deck: {deck}", ""]
                current = deck
            md.append(f"- **{nt}**" + (f" · tags: `{tags}`" if tags else ""))
            for n, v in zip(names, vals):
                md.append(f"  - *{n}:* {re.sub(r'\s+', ' ', v)}")
        open(os.path.join(EXPORTS, "all_notes.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
        print(f"{len(rows)} notes, {col.card_count()} cards, {len(col.decks.all_names_and_ids())} decks")
    finally:
        col.close()


if __name__ == "__main__":
    main(sys.argv[1])
