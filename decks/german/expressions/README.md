# German Expressions

514 German expressions (629 cards) for a B2 learner working towards C1: the chunks that single words don't teach. Funktionsverbgefüge (*eine Entscheidung treffen*), verbs with their preposition and case (*sich verlassen auf + Akk.*), collocations, phrases for discussing and arguing, work and email phrases, and everyday idioms. The companion to [German Verbs](../verbs/), which teaches the verbs themselves.

**Import:** this is a subdeck of the [German deck](../): download [`German.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/german/German.apkg) from its [release](https://github.com/ntfifwyb/anki-setup/releases/tag/german) and open it with Anki (or **File → Import**). This part goes into `Languages::German::Expressions`, with its audio.

## Subdecks

| Subdeck | Notes | What's in it |
|---|---|---|
| 01 Funktionsverbgefüge | 110 | Noun + light verb that mean one thing: *in Frage kommen*, *zur Verfügung stellen*, *Rücksicht nehmen auf* |
| 02 Verb + Präposition | 112 | Verbs with a fixed preposition and case: *sich gewöhnen an + Akk.*, *verzichten auf + Akk.*, *bestehen auf + Dat.* |
| 03 Kollokationen | 88 | Words that belong together: *einen Termin vereinbaren*, *eine Frist einhalten*, *starker Verkehr*, *ein triftiger Grund* |
| 04 Diskutieren und Argumentieren | 72 | Opinion, agreeing, disagreeing, structuring and hedging: *meines Erachtens*, *es liegt auf der Hand, dass …*, *angesichts + Gen.* |
| 05 Arbeit und E-Mails | 58 | Formal emails, meetings and the workplace: *für Rückfragen stehe ich gern zur Verfügung*, *Rücksprache halten*, *krankgeschrieben sein* |
| 06 Redewendungen | 74 | Idioms, neutral to colloquial: *ins Fettnäpfchen treten*, *die Kirche im Dorf lassen*, *das ist nicht mein Bier* |

All written by Claude for this deck. Verb + preposition pairs already on a German Verbs card (*bestehen aus*, *sich beziehen auf*, *stoßen auf* and others, listed at the top of `data/02-verb-praeposition.txt`) are left out.

Every note is tagged with its register (`register::neutral`, `register::formal`, `register::colloquial`) and its type (`type::funktionsverbgefuege`, …), so you can build filtered decks, for example formal phrases only before writing an application.

## Card types

The note type is **German Expression**. Like German Verbs, the cards are German first: the English is a tap-to-reveal hint on the front and a small line on the back.

- **Produce** (every note): the front shows the subdeck, the register, a German definition and the example sentence with the expression's words gapped, plus a word count (*3 Wörter in 2 Teilen*). You recall the whole chunk. In verb + preposition sentences the gap includes the preposition and its article, so you also recall the case.
- **Recognise** (115 notes, most of them idioms): the front shows the expression and plays it; you recall what it means. Idioms are worth recognising when you hear them, even ones you rarely say.

## Audio

Spoken by Piper's `de_DE-thorsten-high`, the voice the [Psittacus](https://github.com/ntfifwyb/psittacus) add-on uses for German. Ordinary MP3s, so they play on desktop, AnkiDroid and AnkiMobile without any add-on.

| Card | Front | Back |
|---|---|---|
| Produce | silent (audio would give the answer away) | the example sentence (`ExampleAudio`) |
| Recognise | the expression (`ExpressionAudio`) | the example sentence |

`ExpressionAudio` is only filled on notes with a Recognise card, since no other card plays it.

## Editing and rebuilding

1. Edit the file in `data/` for the subdeck. One expression per line: `expression | German meaning | example with {{the expression's words}} marked | English | English example | notes | register | R`. `register` is `neutral`, `formal`, `colloquial` or `vulgar`; a final `R` adds a Recognise card. A new subdeck needs a new file and an entry in `SUBDECKS` in `build.py`.
2. Make the audio for new or changed text (it needs the Psittacus submodule, `git submodule update --init`); clips already in `audio/` are skipped:
   ```
   uv run --no-project -p 3.13 --with genanki==0.13.1 --with piper-tts==1.8.0 --with soundfile==0.13.1 python speak.py
   ```
3. Commit, then run `scripts/publish-deck.sh german` from the repository root. It builds `German.apkg` (`../build.py` packages this folder's `build.py`, which stops on a malformed line, a duplicate or a missing clip) and uploads it to the deck's release.
4. Re-import the new `.apkg`. Notes keep stable IDs (from the expression), so existing cards are updated, not duplicated. Changing an expression's wording gives it a new ID.
