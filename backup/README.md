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
| `addons/` | Add-ons installed on my computer, with their configs |
| `exports/all_notes.md`, `exports/all_notes.csv` | Every note in readable form |

## Installed add-ons

| Add-on | Version | Source | Config |
|---|---|---|---|
| Anki Dashboard (now [Ink](https://github.com/ntfifwyb/ink)) | 0.6.6 | My own | `addons/anki_dashboard/config.json` |

> Ink replaces Anki Dashboard. To switch: copy your settings from Anki Dashboard's Config, delete it in **Tools → Add-ons**, then install `ink.ankiaddon` from Ink's releases.

Not included: `prefs21.db` (contains the AnkiWeb sync login), logs, and media files that no card uses.

## Restoring

1. **Collection:** in Anki, **File → Import** and choose `collection/collection.colpkg`. ⚠️ This *replaces* the whole collection on that profile.
2. **Add-ons:** install each one from its source (see the table above), then paste in its saved config (**Tools → Add-ons → Config**).
3. **Settings:** deck options and preferences are inside the `.colpkg`. The files in `settings/` are a readable record in case anything needs to be set by hand.

## Refreshing

Anki keeps automatic backups in `%APPDATA%\Anki2\User 1\backups\`. To refresh: copy the newest `.colpkg` to `collection/collection.colpkg`, update `addons/` from `%APPDATA%\Anki2\addons21\`, regenerate `settings/` and `exports/`, and update the date above. Or ask Claude to do it.
