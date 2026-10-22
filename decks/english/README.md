# English

My English deck, with audio: 444 notes in `Languages::English`, one subdeck per kind of card.

**Import:** download [`English.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/english/English.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/english) and open it with Anki (or **File → Import**). It adds or updates every subdeck at once, with its audio. Notes keep stable IDs, so re-importing updates existing cards instead of duplicating them.

## Subdecks

| Subdeck | Notes | What's in it |
|---|---|---|
| [Expressions](expressions/) | 444 | Phrases, collocations and idioms by context: IELTS, work, emails, negotiating, emotions, friends and more |

Each folder has its source data, audio, `build.py` (its notes and checks) and a README on its cards and how to edit them.

## Rebuilding

After editing a subdeck (see its README), commit and run `scripts/publish-deck.sh english` from the repository root. `build.py` here builds every subdeck in `PARTS` into `English.apkg` and uploads it to the release. To add a new kind of card, add a folder with its own `build.py` that returns its decks and clips from `build()`, and list it in `PARTS`.
