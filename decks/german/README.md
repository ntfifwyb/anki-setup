# German

My German deck for B2→C1, with audio: 2,508 notes in `Languages::German`, one subdeck per kind of card.

**Import:** download [`German.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/german/German.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/german) and open it with Anki (or **File → Import**). It adds or updates every subdeck at once, with its audio. Notes keep stable IDs, so re-importing updates existing cards instead of duplicating them.

## Subdecks

| Subdeck | Notes | What's in it |
|---|---|---|
| [Verbs](verbs/) | 1,994 | The 2,000 most common verbs by frequency: German definition, principal parts, gapped example sentence, a second meaning for 174 common verbs |
| [Expressions](expressions/) | 514 | Funktionsverbgefüge, verb + preposition + case, collocations, discussion, work/email phrases and idioms, in 6 subdecks by type |

Each folder has its source data, audio, `build.py` (its notes and checks) and a README on its cards and how to edit them.

## Rebuilding

After editing a subdeck (see its README), commit and run `scripts/publish-deck.sh german` from the repository root. `build.py` here builds every subdeck in `PARTS` into `German.apkg` and uploads it to the release. To add a new kind of card (nouns, say), add a folder with its own `build.py` that returns its decks and clips from `build()`, and list it in `PARTS`.
