# Anki setup

My complete Anki setup: cards and review history, settings, add-ons, and a master guide for making excellent flashcards.

**Asking an AI to make a deck?** Point it at this repository and tell it the subject. It should start with [`FLASHCARD_GUIDE.md`](FLASHCARD_GUIDE.md).

## What's in here

| Path | Contents |
|---|---|
| [`FLASHCARD_GUIDE.md`](FLASHCARD_GUIDE.md) | Evidence-based guide to writing ideal flashcards, for any subject, with output formats an AI can use directly |
| `collection/collection.colpkg` | Full backup of the collection (all decks, notes, cards, note types, deck options and review history). Importable in Anki |
| `exports/all_notes.md`, `exports/all_notes.csv` | Every note in readable form, for browsing on GitHub or giving to an AI |
| `settings/deck_options.json` | Deck option presets (new/review limits, learning steps, FSRS settings) |
| `settings/preferences.txt` | App preferences (scheduling, reviewing, backups) |
| `settings/collection_config.json` | Collection-level configuration |
| `settings/note_types.json`, `settings/decks.json` | Note types (with fields and card templates) and decks |
| `decks/` | Decks made with AI using the guide, each with its source files (see below) |
| `addons/anki_dashboard/` | Installed add-on: [Anki Dashboard](https://github.com/montinaops/anki-dashboard) v0.6.6, including my `config.json` |

Not included: `prefs21.db` (it contains the AnkiWeb sync login) and log files.

## Decks

| Deck | Notes | Description |
|---|---|---|
| [English Expressions](decks/english-expressions/) | 444 | Phrases, collocations and idioms by context: IELTS, work, emails, negotiating, emotions, friends and more |

## Restoring

1. **Collection**: in Anki, **File → Import**, choose `collection/collection.colpkg`. ⚠️ This *replaces* the whole collection on that profile.
2. **Add-on**: copy `addons/anki_dashboard/` into Anki's add-ons folder (**Tools → Add-ons → View Files**), then restart Anki. Or install it from its homepage. `config.json` holds my settings.
3. **Settings**: deck options and preferences are included in the `.colpkg`. The JSON/text files in `settings/` are a readable record in case they need to be set by hand.

## Updating the backup

Anki keeps automatic backups in `%APPDATA%\Anki2\User 1\backups\`. To refresh this repo, copy the newest `.colpkg` to `collection/collection.colpkg`, copy `addons21/` over `addons/`, and regenerate the exports, or ask Claude to do it.
