# Decisions

## 2026-10-20: Decks ship their audio

**Question:** should the English Expressions deck come with its audio, or leave the audio fields for the Psittacus add-on to fill after import?

**Choice:** ship it. `speak.py` makes each clip with Psittacus's own code and first voice for the language (Kokoro `af_heart` for English), and `build.py` packs the clips into the `.apkg`.

**Why:** filling the deck in Anki took 45–60 minutes, had to be redone after every re-import, and was easy to get wrong (one run read `Expression` into `ExampleAudio`). Shipped clips work on import, on the phone too, with or without the add-on. Using Psittacus's file names means clips a user already made aren't imported twice. This replaces the step, in Psittacus's `docs/DECISIONS.md` (2026-10-20, "First target deck is English Expressions"), of filling the fields in Anki after import; the fields and templates stay as decided there.

## 2026-10-20: The .apkg lives on a GitHub Release, not in git

**Question:** with the audio inside, the `.apkg` is about 14 MB. Commit it, or publish it as a release asset?

**Choice:** a release per deck, tagged with the deck's folder name and moved by `scripts/publish-deck.sh` on each publish, so the download link stays the same. The `.apkg` is git-ignored. The clips are committed, in the deck's `audio/`.

**Why:** a committed `.apkg` adds its full size to the history on every rebuild. Each clip is committed once, so the repository only grows when sentences change.

## 2026-10-20: Every deck with spoken content ships its audio

**Question:** the English Expressions deck makes its audio at build time. Is that a one-off, or the rule for new decks?

**Choice:** the rule. `FLASHCARD_GUIDE.md` §5.6 tells whoever builds a deck (language learning, pronunciation, anything meant to be heard) to make the clips with Psittacus's voices, following `decks/english-expressions/`.

**Why:** the owner builds their decks with Claude, so the audio should arrive with the deck rather than be added in Anki. The Psittacus add-on stays a standalone tool for cards written by hand (Psittacus `docs/DECISIONS.md`, same date).

## 2026-10-22: German Verbs tests a second meaning for common verbs

**Question:** many verbs have more than one meaning (*bestehen*: pass an exam / consist of), but each note's one sentence tests only one. Add second-meaning cards for all 529 verbs whose definition lists several meanings, or only for the top 1,000?

**Choice:** the top 1,000, and only where the second meaning is distinct enough to learn on its own: 174 verbs, listed in `decks/german-verbs/senses.txt`. Each is a third card type, *Produce 2*, on the verb's existing note, with fields appended to the note type.

**Why:** the verbs met most often are where a second meaning pays off; for rare verbs it would mostly add load. Keeping it on the same note keeps the GUIDs, so re-importing updates the deck (with **Merge note types** ticked) instead of adding notes. A semicolon in a definition often just rephrases one meaning (*beginnen*: starten; den Anfang machen), so those verbs got no card.

## 2026-10-22: German expressions get their own deck

**Question:** the verb deck tests single verbs, but most of the gap from B2 to C1 is in chunks: *eine Entscheidung treffen*, *sich verlassen auf + Akk.*, *zur Verfügung stellen*. Add those to the verb deck, or make a separate deck?

**Choice:** a separate deck, German Expressions (`Languages::German::Expressions`), 514 C1-focused notes, in subdecks by type like English Expressions: Funktionsverbgefüge, verb + preposition + case, collocations, discourse and work/email phrases, Redewendungen.

**Why:** an expression needs a different card than a verb (the whole chunk is the answer, not one verb in its forms), and subdecks let the owner study one kind at a time.
