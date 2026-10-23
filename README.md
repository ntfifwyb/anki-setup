# Anki setup

Everything Anki in one place: the decks I make, the add-ons I build, and a backup of my local Anki setup. Plus a master guide for making excellent flashcards.

**Asking an AI to make a deck?** Point it at this repository and tell it the subject. It should start with [`FLASHCARD_GUIDE.md`](FLASHCARD_GUIDE.md) and [`CLAUDE.md`](CLAUDE.md).

## Layout

| Folder | Contents |
|---|---|
| [`decks/`](decks/) | Decks I've made, each with its source data, build script and audio. The importable `.apkg` is on the deck's [release](https://github.com/ntfifwyb/anki-setup/releases) |
| [`addons/`](addons/) | Add-ons I develop, linked to their own repositories |
| [`backup/`](backup/) | Snapshot of my local Anki: collection, settings, installed add-ons and readable exports |
| [`FLASHCARD_GUIDE.md`](FLASHCARD_GUIDE.md) | Evidence-based guide to writing ideal flashcards, for any subject |

## Decks

| Deck | Notes | Description |
|---|---|---|
| [English](decks/english/) ([download](https://github.com/ntfifwyb/anki-setup/releases/download/english/English.apkg)) | 444 | **Expressions:** phrases, collocations and idioms by context: IELTS, work, emails, negotiating, emotions, friends and more, with audio |
| [German](decks/german/) ([download](https://github.com/ntfifwyb/anki-setup/releases/download/german/German.apkg)) | 2,508 | **Verbs** (1,994): the 2,000 most common German verbs by frequency: German definition, principal parts, gapped example sentence, a second meaning for 174 common verbs. **Expressions** (514): Funktionsverbgefüge, verb + preposition + case, collocations, discussion, work/email phrases and idioms for B2→C1, in subdecks by type, with audio |
| [Spanish](decks/spanish/) ([download](https://github.com/ntfifwyb/anki-setup/releases/download/spanish/Spanish.apkg)) | 676 | For a native speaker, all in Spanish: **Refranes** (173) to complete, with German and English equivalents; **Locuciones** (151), **Colocaciones** (116) and **Vocabulario culto** (144) to produce from a definition and a gapped sentence; **Norma y dudas** (92) from the RAE's DPD. Panhispanic, regionalisms tagged, with audio |

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
