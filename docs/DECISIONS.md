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

## 2026-10-22: One deck per language, with subdecks

**Question:** English Expressions, German Verbs and German Expressions were three folders, three `.apkg` files and three releases. Keep one deck per topic, or one per language with the topics as subdecks?

**Choice:** one per language: `decks/german/` (subdecks `verbs/`, `expressions/`) and `decks/english/` (`expressions/`), each with a `build.py` that packages its subdecks into one `.apkg` (`German.apkg`, `English.apkg`) on one release (`german`, `english`). Anki's deck names don't change (`Languages::German::Verbs` …), nor do GUIDs, deck IDs or note types: the combined files hold exactly the notes of the old ones.

**Why:** in Anki they already were one deck per language; the repository now matches. A new kind of card is a subdeck folder, not a new deck, release and README row. The cost is a bigger download: re-importing after a fix to one subdeck re-imports the whole language, which updates unchanged notes in place.

## 2026-10-23: A Spanish deck for a native speaker

**Question:** the owner is a native Spanish speaker and wants an advanced deck. What should it teach, in which variety, and how big?

**Choice:** the cultured register natives rarely master, in five subdecks: Refranes, Locuciones, Colocaciones, Vocabulario culto (with Latin phrases) and Norma y dudas (the RAE's *Diccionario panhispánico de dudas*). Panhispanic, with regionalisms tagged by region and their equivalents elsewhere noted. About 600 notes to start (676 shipped).

**Why:** a translation deck teaches a native nothing; the gap is in precision (*zanjar*, not *terminar*, a polémica), set phrases, refranes and the norma culta. Cards are all in Spanish. Refranes show their German and English equivalent, which links to the owner's other two decks. Panhispanic because the owner reads and hears Spanish from everywhere; a tag still lets them filter one region.

**Also decided by Claude (pending review):** three note types (Spanish Expression, Spanish Refrán, Spanish Norma), because each asks a different question; a single `audio/` and `common.py` at the language level, shared by the three subdeck folders, instead of copying the Psittacus helpers into each.

## 2026-10-23: Decks named in their language; a release per version

**Question:** the owner wants deck and subdeck names in the deck's own language (Spanish → Español), for immersion, and every published version kept on the releases page as a track record. How should versions be numbered and linked?

**Choice:** Anki names in the deck's language under the shared `Languages::` parent, which stays as is because it spans languages: `Languages::Deutsch::Verben`, `Languages::Deutsch::Ausdrücke`, `Languages::Español` (its subdecks already had Spanish names); English is unchanged. Each publish creates a release tagged `<deck>-x.y.z` (SemVer: major when importing needs a step in Anki, minor for new cards, patch for fixes), titled with the native name and version (`Deutsch 2.0.0`), with the section of the deck's new `CHANGELOG.md` as notes. The READMEs link to the current version's download, and `scripts/check-release-links.sh` in `.local-ci` fails when they don't match the changelog. The former moving releases became 1.0.0; German and Spanish are 2.0.0, since the rename needs the decks renamed in Anki before importing. This replaces the moving tag of 2026-10-20 ("The .apkg lives on a GitHub Release").

**Why:** a moving tag kept no history. GitHub's `releases/latest` is one per repository, not per deck, so a stable per-deck link to the newest file would need a second, duplicated release on every publish; a link bumped in the PR, guarded by CI, is simpler. Folders keep English names (`decks/german/`): they're for the repository, not for study.

**Also decided by Claude (pending review):** `Ausdrücke` for German Expressions; the files are named `Deutsch.apkg` and `Espanol.apkg`, without the accent, because GitHub replaces non-ASCII characters in asset names; Anki shows the deck names from inside the file, so the accent there is intact.

## 2026-10-24: An Esperanto deck, with an eSpeak voice

**Question:** the owner wants an Esperanto deck. At what level, in which language, and spoken by what, given that no Psittacus engine (Kokoro, Piper, Edge) has an Esperanto voice?

**Choice (the owner's):** intermediate and up, entirely in Esperanto, about 200 notes to start (252 shipped), with audio from eSpeak NG's `eo` voice.

**Why:** eSpeak NG is the only freely available voice that reads Esperanto by its own rules (ĉ, ĝ, ĥ, ĵ, ŝ, ŭ, penultimate stress); the other option, an Italian voice reading a respelled text, sounds more natural but gets several sounds wrong. eSpeak is robotic, but correct.

**Also decided by Claude (pending review):** four subdecks, Vortfarado, Vortprovizo, Korelativoj kaj partikloj and Gramatiko, because an intermediate speaker's gaps are in productive word building, precision, the small words and a few grammar points, not in basic vocabulary; two note types (Esperanto Word, Esperanto Choice) after the Spanish deck's Expression and Norma. eSpeak NG runs from the `espeakng-loader` package through its C library, in the deck's own `speak.py`, rather than as a new Psittacus engine: the deck needs no system install, and the add-on stays as it is. Clips are still named with Psittacus's `cache_name` (engine `espeak`), so Psittacus could adopt the voice later without renaming them.
