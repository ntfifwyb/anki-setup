# English

My English deck, with audio: 444 notes in `Languages::English`, one subdeck per kind of card.

**Import:** download [`English.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/english-1.0.0/English.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/english-1.0.0) (version 1.0.0; [all versions](https://github.com/ntfifwyb/anki-setup/releases), [changelog](CHANGELOG.md)) and open it with Anki (or **File → Import**). It adds or updates every subdeck at once, with its audio. Notes keep stable IDs, so re-importing updates existing cards instead of duplicating them.

## Subdecks

| Subdeck | Notes | What's in it |
|---|---|---|
| [Expressions](expressions/) | 444 | Phrases, collocations and idioms by context: IELTS, work, emails, negotiating, emotions, friends and more |

Each folder has its source data, audio, `build.py` (its notes and checks) and a README on its cards and how to edit them.

## Rebuilding

Each publish is a new version on the releases page, tagged `english-x.y.z`: a major version when importing it needs a step in Anki (a renamed deck, say), a minor one for new cards, a patch for fixes. Before publishing, add the version and what changed to [`CHANGELOG.md`](CHANGELOG.md) and point the download link above at it; `scripts/check-release-links.sh` (part of `.local-ci`) fails until the links match. `scripts/publish-deck.sh english` then builds the `.apkg` and creates the release, with that changelog section as its notes.

After editing a subdeck (see its README), add a version to [`CHANGELOG.md`](CHANGELOG.md), commit, and once merged run `scripts/publish-deck.sh english` from the repository root. `build.py` here builds every subdeck in `PARTS` into `English.apkg`. To add a new kind of card, add a folder with its own `build.py` that returns its decks and clips from `build()`, and list it in `PARTS`.
