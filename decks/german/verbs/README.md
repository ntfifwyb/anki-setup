# Verben

The 2,000 most common German verbs, in frequency order, for a B2 learner working towards C1. Built from the 2000-verb list in my "Deutsch" study notes: 1,994 notes (3,662 cards), each with the verb's principal parts, a German definition, an example sentence, its English translation and usage notes (prepositions, case, reflexive use, register). 174 of the top 1,000 verbs also have a second meaning with its own example.

**Import:** this is a subdeck of the [Deutsch deck](../): download its `.apkg` from there and open it with Anki (or **File → Import**). This part goes into `Languages::Deutsch::Verben`, with its audio. When you update a version imported before the second-meaning cards were added, tick **Merge note types** in the import dialog: the note type gained fields, and without merging Anki won't update the existing notes.

## Structure

One deck, no subdecks: new cards come in frequency order (the most useful verbs first), and everything else is a tag, so you can build filtered decks from them.

| Tag | Meaning |
|---|---|
| `freq::0001-0250` … `freq::1751-2000` | Frequency band |
| `verb::separable` | Separable verb (*anrufen → ruft an*) |
| `verb::strong` | Strong verb: the Präteritum has no *-te* (*gehen → ging*) |
| `aux::sein` | Perfekt with *sein* (or either auxiliary) |
| `verb::reflexive` | Usually or often used with *sich* |
| `register::colloquial`, `register::formal`, `register::vulgar` | Register, when it isn't neutral |

`Languages::Deutsch` is the German deck. Other kinds of cards (expressions, nouns) go next to this one as `Languages::Deutsch::<Name>`, named in German, each in its own folder under `decks/german/`, since each needs its own note type and card layout.

## Card types

The note type is **German Verb**. Following the guide's policy for B2→C1, the cards are German first: the English is a tap-to-reveal hint on the front and a small line on the back.

- **Produce** (every note): the front shows the German definition and the example sentence with the verb's words gapped (`2 Teile` when the verb is split, as separable verbs are), plus the English verb behind a *hint* link. You recall the verb in the form the sentence needs. The back shows the verb, *er/sie/es* present – Präteritum – Perfekt, the full sentence and the notes.
- **Produce 2** (174 of the top 1,000 verbs): the same, for a second meaning distinct enough to learn on its own (*bestehen*: pass an exam → *bestehen aus*, consist of; *merken*: notice → *sich merken*, remember). The front is labelled *2. Bedeutung* and shows that meaning's definition and its own gapped sentence.
- **Recognise** (only verbs ranked 501–2000): the front shows the verb and plays it; you recall what it means. The first 500 are everyday verbs a B2 learner already understands, so they only get the Produce card.

## Audio

Every note has two clips, the verb (`VerbAudio`) and the example sentence (`ExampleAudio`), plus `Example2Audio` for the second meaning's sentence, spoken by Piper's `de_DE-thorsten-high`, the voice the [Psittacus](https://github.com/ntfifwyb/psittacus) add-on uses for German. They're ordinary MP3s, so they play on desktop, AnkiDroid and AnkiMobile without any add-on.

| Card | Front | Back |
|---|---|---|
| Produce | silent (audio would give the answer away) | verb, then sentence |
| Produce 2 | silent | verb, then the second sentence |
| Recognise | the verb | the sentence |

## Editing and rebuilding

1. Edit `verbs.txt`. One verb per line: `rank | verb | present – Präteritum – Perfekt | definition | example with {{the verb's words}} marked | English | English example | notes`. Second meanings go in `senses.txt`: `verb | definition | example | English | English example`; `build.py` stops if a verb there isn't in `verbs.txt`.
2. Make the audio for new or changed text (it needs the Psittacus submodule, `git submodule update --init`); clips already in `audio/` are skipped:
   ```
   uv run --no-project -p 3.13 --with genanki==0.13.1 --with piper-tts==1.8.0 --with soundfile==0.13.1 python speak.py
   ```
3. Add a version to the deck's [`CHANGELOG.md`](../CHANGELOG.md) (see the [deck README](../README.md#rebuilding)), commit, then run `scripts/publish-deck.sh german` from the repository root. It builds `Deutsch.apkg` (`../build.py` packages this folder's `build.py`, which stops if a clip is missing) and publishes it as a new release.
4. Re-import the new `.apkg`. Notes keep stable IDs (from the verb), so existing cards are updated, not duplicated.

## Changes from the source list

- Left out, because the example sentence used a different verb or the verb is too rare to be worth a card: *frischen* (517), *kapseln* (1481), *schliefen* (1597), *listen* (1684), *beulen* (1712), *heuern* (1977).
- Corrected example sentences (they used a different verb or were ungrammatical): 496 *doppeln*, 747 *bescheißen*, 809 *anliegen*, 847 *kleben*, 925 *aufhängen*, 944 *laden*, 1430 *angucken*, 1448 *hingehören*, 1464 *anführen*, 1713 *abschleppen*, 1990 *herziehen*.
- Replaced example sentences that used a compound instead of the verb itself (*knallen* had *zuknallen*, *pfeifen* had *abpfeifen*): 28 *nehmen*, 147 *werfen*, 425 *pfeifen*, 444 *bewahren*, 475 *senden*, 483 *rühren*, 591 *locken*, 688 *wiegen*, 750 *knallen*, 895 *zünden*, 1213 *knöpfen*, 1751 *fauchen*, 1999 *zwinkern*. The notes point to the compound (*Vgl.*).
- Some verbs are vulgar by design (tagged `register::vulgar`).
