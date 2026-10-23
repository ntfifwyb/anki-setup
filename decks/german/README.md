# Deutsch

My German deck for B2→C1, with audio: 2,508 notes in `Languages::Deutsch`, one subdeck per kind of card.

**Import:** download [`Deutsch.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/german-2.0.0/Deutsch.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/german-2.0.0) (version 2.0.0; [all versions](https://github.com/ntfifwyb/anki-setup/releases), [changelog](CHANGELOG.md)) and open it with Anki (or **File → Import**). It adds or updates every subdeck at once, with its audio. Notes keep stable IDs, so re-importing updates existing cards instead of duplicating them.

**Updating from 1.x:** the deck is now named in German. Before importing 2.0.0, rename the decks in Anki (click the gear next to a deck → **Rename**): `Languages::German` → `Languages::Deutsch`, then `Verbs` → `Verben` and `Expressions` → `Ausdrücke` under it. Otherwise Anki creates the new decks next to the old ones, and your existing cards, with their reviews, stay in the old ones.

## Subdecks

| Subdeck | Notes | What's in it |
|---|---|---|
| [Verben](verbs/) | 1,994 | The 2,000 most common verbs by frequency: German definition, principal parts, gapped example sentence, a second meaning for 174 common verbs |
| [Ausdrücke](expressions/) | 514 | Funktionsverbgefüge, verb + preposition + case, collocations, discussion, work/email phrases and idioms, in 6 subdecks by type |

Each folder has its source data, audio, `build.py` (its notes and checks) and a README on its cards and how to edit them.

## Rebuilding

Each publish is a new version on the releases page, tagged `german-x.y.z`: a major version when importing it needs a step in Anki (a renamed deck, say), a minor one for new cards, a patch for fixes. Before publishing, add the version and what changed to [`CHANGELOG.md`](CHANGELOG.md) and point the download link above at it; `scripts/check-release-links.sh` (part of `.local-ci`) fails until the links match. `scripts/publish-deck.sh german` then builds the `.apkg` and creates the release, with that changelog section as its notes.

After editing a subdeck (see its README), add a version to [`CHANGELOG.md`](CHANGELOG.md), commit, and once merged run `scripts/publish-deck.sh german` from the repository root. `build.py` here builds every subdeck in `PARTS` into `Deutsch.apkg`. To add a new kind of card (nouns, say), add a folder with its own `build.py` that returns its decks and clips from `build()`, and list it in `PARTS`.
