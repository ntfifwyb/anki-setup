# Instructions for AI assistants

If you're asked to create Anki flashcards or a deck from this repository:

1. Read `FLASHCARD_GUIDE.md` in full first and follow it.
2. Check `backup/exports/all_notes.md` so you don't duplicate existing cards.
3. Use the note types listed in `backup/settings/note_types.json` where possible.
4. Deliver the deck in one of the formats in section 9 of the guide.
5. **Save every deck you create to this repository**: one deck per language or subject, `decks/<deck>/` (lowercase, hyphenated, e.g. `german`), whose `build.py` packages its subdeck folders `decks/<deck>/<subdeck>/` into one `.apkg`. A new kind of card for an existing deck is a new subdeck folder there (listed in that `build.py`'s `PARTS`), not a new deck. Include:
   - the `.txt` import files, or a `build.py` that writes the `.apkg` (git-ignored: publish it on the deck's GitHub Release with `scripts/publish-deck.sh <deck>`),
   - the source data and any build script, so the deck can be edited and rebuilt,
   - a short `README.md` for the deck and for each subdeck: what it covers, how to import and rebuild it.
   Then add the deck to the "Decks" table in the root `README.md`, commit and push.
6. When you update an existing deck, keep note GUIDs stable so re-importing updates cards instead of duplicating them.

## Repository layout

- `decks/` — decks made for the owner (see rule 5 above).
- `addons/` — add-ons the owner develops, each linked as a git submodule to its own repository. Never copy an add-on's source in here; to add a new one, run `git submodule add <repo-url> addons/<name>` and list it in `addons/README.md`.
- `backup/` — a snapshot of the owner's local Anki: collection, settings, the configs of installed add-ons, and readable exports. Regenerate `settings/` and `exports/` with `backup/tools/regenerate.py`. Keep only the latest snapshot and overwrite it (git history keeps old versions). Never commit `prefs21.db` (it holds the AnkiWeb login) or media from third-party decks. Never copy add-on code into `backup/addons/`, only each add-on's `config.json` and `meta.json`; record every installed add-on (name, version, source, AnkiWeb code if any) in the "Installed add-ons" table of `backup/README.md` rather than copying their code.
