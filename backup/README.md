# Backup of my local Anki

A snapshot of my Anki installation (profile "User 1"). Only the latest snapshot is kept; earlier versions are in the git history.

**Last updated:** 2026-10-20

| Path | Contents |
|---|---|
| `collection/collection.colpkg` | Full collection: all decks, notes, cards, note types, deck options and review history |
| `settings/deck_options.json` | Deck option presets (limits, learning steps, FSRS settings) |
| `settings/preferences.txt` | App preferences (scheduling, reviewing, backups) |
| `settings/collection_config.json` | Collection-level configuration |
| `settings/note_types.json`, `settings/decks.json` | Note types (fields and card templates) and decks |
| `addons/` | Configs of the add-ons installed on my computer (code comes from each add-on's own source) |
| `tools/regenerate.py` | Rebuilds `settings/` and `exports/` from a `collection.anki2` file |
| `exports/all_notes.md`, `exports/all_notes.csv` | Every note in readable form |

## Installed add-ons

| Add-on | Version | Source | Config |
|---|---|---|---|
| [Ink](https://github.com/ntfifwyb/ink) | 0.8.0 | My own ([`../addons/ink`](../addons/ink)), installed from its [releases](https://github.com/ntfifwyb/ink/releases) | `addons/ink/config.json` |

Not included: `prefs21.db` (contains the AnkiWeb sync login), logs, and media files that no card uses.

## Restoring

1. **Collection:** in Anki, **File → Import** and choose `collection/collection.colpkg`. ⚠️ This *replaces* the whole collection on that profile.
2. **Add-ons:** install each one from its source (see the table above), then paste in its saved config (**Tools → Add-ons → Config**).
3. **Settings:** deck options and preferences are inside the `.colpkg`. The files in `settings/` are a readable record in case anything needs to be set by hand.

## Refreshing

Anki keeps automatic backups in `%APPDATA%\Anki2\User 1\backups\`. To refresh: copy the newest `.colpkg` to `collection/collection.colpkg`, copy each add-on's `config.json` and `meta.json` from `%APPDATA%\Anki2\addons21\<add-on>\` into `addons/<add-on>/`, run `python tools/regenerate.py "%APPDATA%\Anki2\User 1\collection.anki2"` (needs `pip install anki`), and update the date above. Or ask Claude to do it.
