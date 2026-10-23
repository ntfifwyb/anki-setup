# Anki setup

Everything Anki in one place: the decks I make, the add-ons I build, and a backup of my local Anki setup. Plus a master guide for making excellent flashcards.

**Asking an AI to make a deck?** Point it at this repository and tell it the subject. It should start with [`FLASHCARD_GUIDE.md`](FLASHCARD_GUIDE.md) and [`CLAUDE.md`](CLAUDE.md).

## Layout

| Folder | Contents |
|---|---|
| [`decks/`](decks/) | Decks I've made, each with its source data, build script and audio. The importable `.apkg` is on the deck's [releases](https://github.com/ntfifwyb/anki-setup/releases), one per version |
| [`addons/`](addons/) | Add-ons I develop, linked to their own repositories |
| [`backup/`](backup/) | Snapshot of my local Anki: collection, settings, installed add-ons and readable exports |
| [`FLASHCARD_GUIDE.md`](FLASHCARD_GUIDE.md) | Evidence-based guide to writing ideal flashcards, for any subject |

## Decks

Each deck and subdeck is named in its own language, for immersion. Every version stays on the [releases page](https://github.com/ntfifwyb/anki-setup/releases); each deck's `CHANGELOG.md` says what changed.

| Deck | Notes | Description |
|---|---|---|
| [English](decks/english/) ([download 1.0.0](https://github.com/ntfifwyb/anki-setup/releases/download/english-1.0.0/English.apkg)) | 444 | **Expressions:** phrases, collocations and idioms by context: IELTS, work, emails, negotiating, emotions, friends and more, with audio |
| [Deutsch](decks/german/) (German, [download 2.0.0](https://github.com/ntfifwyb/anki-setup/releases/download/german-2.0.0/Deutsch.apkg)) | 2,508 | **Verben** (1,994): the 2,000 most common German verbs by frequency: German definition, principal parts, gapped example sentence, a second meaning for 174 common verbs. **Ausdrücke** (514): Funktionsverbgefüge, verb + preposition + case, collocations, discussion, work/email phrases and idioms for B2→C1, in subdecks by type, with audio |
| [Español](decks/spanish/) (Spanish, [download 2.0.0](https://github.com/ntfifwyb/anki-setup/releases/download/spanish-2.0.0/Espanol.apkg)) | 676 | For a native speaker, all in Spanish: **Refranes** (173) to complete, with German and English equivalents; **Locuciones** (151), **Colocaciones** (116) and **Vocabulario culto** (144) to produce from a definition and a gapped sentence; **Norma y dudas** (92) from the RAE's DPD. Panhispanic, regionalisms tagged, with audio |

## Add-ons

| Add-on | Description |
|---|---|
| [Ink](https://github.com/ntfifwyb/ink) | Minimal, information-dense redesign of the deck list, overview, reviewer and stats page (formerly Anki Dashboard) |

## Cloning

`addons/` uses git submodules, so clone with:

```
git clone --recurse-submodules https://github.com/ntfifwyb/anki-setup
```

In an existing clone, run `git submodule update --init` to fetch them.
