# Decisions

## 2026-10-20: Decks ship their audio

**Question:** should the English Expressions deck come with its audio, or leave the audio fields for the Psittacus add-on to fill after import?

**Choice:** ship it. `speak.py` makes each clip with Psittacus's own code and first voice for the language (Kokoro `af_heart` for English), and `build.py` packs the clips into the `.apkg`.

**Why:** filling the deck in Anki took 45–60 minutes, had to be redone after every re-import, and was easy to get wrong (one run read `Expression` into `ExampleAudio`). Shipped clips work on import, on the phone too, with or without the add-on. Using Psittacus's file names means clips a user already made aren't imported twice. This replaces the step, in Psittacus's `docs/DECISIONS.md` (2026-10-20, "First target deck is English Expressions"), of filling the fields in Anki after import; the fields and templates stay as decided there.

## 2026-10-20: The .apkg lives on a GitHub Release, not in git

**Question:** with the audio inside, the `.apkg` is about 14 MB. Commit it, or publish it as a release asset?

**Choice:** a release per deck, tagged with the deck's folder name and moved by `scripts/publish-deck.sh` on each publish, so the download link stays the same. The `.apkg` is git-ignored. The clips are committed, in the deck's `audio/`.

**Why:** a committed `.apkg` adds its full size to the history on every rebuild. Each clip is committed once, so the repository only grows when sentences change.
