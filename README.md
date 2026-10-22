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
| [English Expressions](decks/english-expressions/) ([download](https://github.com/ntfifwyb/anki-setup/releases/download/english-expressions/English_Expressions.apkg)) | 444 | Phrases, collocations and idioms by context: IELTS, work, emails, negotiating, emotions, friends and more, with audio |
| [German Verbs](decks/german-verbs/) ([download](https://github.com/ntfifwyb/anki-setup/releases/download/german-verbs/German_Verbs.apkg)) | 1,994 | The 2,000 most common German verbs by frequency: German definition, principal parts, gapped example sentence, with audio |

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
