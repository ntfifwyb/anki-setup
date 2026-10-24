# Esperanto

My Esperanto deck, for an intermediate speaker going further: not the basics, but word building, precise vocabulary, the small words and the grammar points where speakers of Spanish, English and German go wrong. 252 notes (343 cards) in `Languages::Esperanto`, one subdeck per kind of card, with audio.

**Import:** download [`Esperanto.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/esperanto-1.0.0/Esperanto.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/esperanto-1.0.0) (version 1.0.0; [all versions](https://github.com/ntfifwyb/anki-setup/releases), [changelog](CHANGELOG.md)) and open it with Anki (or **File → Import**). It adds or updates every subdeck at once, with its audio. Notes keep stable IDs, so re-importing updates existing cards instead of duplicating them.

## Subdecks

| Subdeck | Notes | What's in it | Folder |
|---|---|---|---|
| 01 Vortfarado | 90 | Build the word from its root with the right affixes: *malsanulejo*, *vidinda*, *pagenda*, *kandelingo*, *ĝisdatigi*, *eksedzino* | [words/](words/) |
| 02 Vortprovizo | 55 | Precise verbs and adjectives, and false friends: *pretendi*, *ekzemplero*, *eventuala*, *atendi*/*esperi*, *prunti*, *agnoski* | [words/](words/) |
| 03 Korelativoj kaj partikloj | 44 | The rarer correlatives and the small words: *ties*, *ial*, *ĉiom*, *ajn*, *ja*, *plu*, *ju … des*, *nek … nek* | [words/](words/) |
| 04 Gramatiko | 63 | Choose the right form, and learn why: accusative of direction, time and measure, predicative, *si*/*lia*, *-ig*/*-iĝ*, participles, *-us*/*-u*, reported speech, *da*/*de* | [grammar/](grammar/) |

All written by Claude for this deck: definitions in the style of the *Plena Ilustrita Vortaro* (PIV), the grammar rules after the *Fundamento* and Bertilo Wennergren's *Plena Manlibro de Esperanta Gramatiko* (PMEG). Cards are entirely in Esperanto; where a word is a false friend, its note names the Spanish, English or German word it is confused with. Every note is tagged with its type (`type::vortfarado`, …) or grammar topic (`topic::akuzativo`, …).

## Audio

None of the voices of the [Psittacus](https://github.com/ntfifwyb/psittacus) add-on speaks Esperanto, so this deck has its own: [eSpeak NG](https://github.com/espeak-ng/espeak-ng)'s `eo` voice. It is robotic, but reads Esperanto by its own rules (ĉ, ĝ, ĥ, ĵ, ŝ, ŭ, stress on the next-to-last syllable). Every example sentence is spoken, and the word on notes with a *Rekoni* card. Ordinary MP3s in `audio/`, shared by every subdeck, named as Psittacus names its clips, so they play on desktop, AnkiDroid and AnkiMobile without any add-on.

## Editing and rebuilding

Each publish is a new version on the releases page, tagged `esperanto-x.y.z`: a major version when importing it needs a step in Anki (a renamed deck, say), a minor one for new cards, a patch for fixes. Before publishing, add the version and what changed to [`CHANGELOG.md`](CHANGELOG.md) and point the download link above at it; `scripts/check-release-links.sh` (part of `.local-ci`) fails until the links match. `scripts/publish-deck.sh esperanto` then builds the `.apkg` and creates the release, with that changelog section as its notes.

1. Edit the subdeck's data (see its README).
2. Make the audio for new or changed text (it needs the Psittacus submodule for the clip names, `git submodule update --init`); clips already in `audio/` are skipped. eSpeak NG comes from the `espeakng-loader` package, so nothing needs installing system-wide:
   ```
   uv run --no-project -p 3.13 --with genanki==0.13.1 --with espeakng-loader==0.2.4 --with soundfile==0.13.1 --with numpy python speak.py
   ```
3. Add a version to [`CHANGELOG.md`](CHANGELOG.md) (see above), commit, and once merged run `scripts/publish-deck.sh esperanto` from the repository root. `build.py` packages every subdeck in `PARTS` into `Esperanto.apkg` (each subdeck's `build.py` stops on a malformed line or a duplicate, and `common.py` on a missing clip).
4. Re-import the new `.apkg`. A note's ID comes from its word (or, in Gramatiko, its correct sentence), so changing that gives it a new ID; changing anything else updates it in place.

`common.py` holds what the subdecks share: the data parser, the card style and the clip names. To add a new kind of card, add a folder with a `build.py` whose `rows()` returns its notes, and list it in `PARTS`.
