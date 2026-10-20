# Instructions for AI assistants

If you're asked to create Anki flashcards or a deck from this repository:

1. Read `FLASHCARD_GUIDE.md` in full first and follow it.
2. Check `exports/all_notes.md` so you don't duplicate existing cards.
3. Use the note types listed in `settings/note_types.json` where possible.
4. Deliver the deck in one of the formats in section 9 of the guide.
5. **Save every deck you create to this repository**, in its own folder `decks/<deck-name>/` (lowercase, hyphenated). Include:
   - the importable file (`.apkg`, or the `.txt` import files),
   - the source data and any build script, so the deck can be edited and rebuilt,
   - a short `README.md`: what the deck covers, its subdecks, how to import and rebuild it.
   Then add the deck to the "Decks" table in the root `README.md`, commit and push.
6. When you update an existing deck, keep note GUIDs stable so re-importing updates cards instead of duplicating them.
