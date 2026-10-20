# English Expressions

444 English expressions (487 cards) for a fluent speaker who wants a wider, more precise range of phrases. Every card is labelled with its context and register (academic, formal, neutral, informal, slang, vulgar).

**Import:** download [`English_Expressions.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/english-expressions/English_Expressions.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/english-expressions) and open it with Anki (or **File → Import**). It goes into `Languages::English::Expressions`, with its audio.

## Subdecks

| Subdeck | Source |
|---|---|
| 00 My Saved Phrases | My own list of phrases collected over the years (`expressions.txt`) |
| 01 IELTS Writing | Added by Claude (`contexts.txt`) |
| 02 IELTS Speaking | Added by Claude |
| 03 Work and Email | Added by Claude |
| 04 Disagreeing and Negotiating | Added by Claude |
| 05 Saying It Precisely | Added by Claude |
| 06 Emotions | Added by Claude |
| 07 Social Life and Dating | Added by Claude |
| 08 Support and Apologies | Added by Claude |
| 09 Services and Admin | Added by Claude |
| 10 With Friends | Added by Claude |

## Card types

- **Produce** (every note): the front shows the meaning and an example sentence with a gap, plus a word count; you recall the expression.
- **Recognise** (only for less common expressions): the front shows the expression; you recall the meaning.

## Audio

The deck comes with its audio, spoken by Kokoro (voice `af_heart`), the voice the [Psittacus](https://github.com/ntfifwyb/psittacus) add-on uses for English. The clips are ordinary MP3s, so they play on desktop, AnkiDroid and AnkiMobile without any add-on.

| Card | Front | Back |
|---|---|---|
| Produce | silent (audio would give the answer away) | the example sentence (`ExampleAudio`) |
| Recognise | the expression (`ExpressionAudio`) | the example sentence (`ExampleAudio`) |

`ExpressionAudio` is only filled on notes with a Recognise card, since no other card plays it. The clips are in `audio/`, named as Psittacus names them, so a clip Psittacus already made for you isn't imported twice.

## Editing and rebuilding

1. Edit `expressions.txt` or `contexts.txt`. One expression per line: `expression | meaning | example with {{the expression}} marked | notes | register | context | R` (R = also make a recognition card).
2. Make the audio for new or changed sentences (it needs the Psittacus submodule, `git submodule update --init`); clips already in `audio/` are skipped:
   ```
   uv run --no-project -p 3.13 --with genanki==0.13.1 --with kokoro-onnx==0.6.1 --with soundfile==0.13.1 python speak.py
   ```
3. Commit, then run `scripts/publish-deck.sh english-expressions` from the repository root. It builds the `.apkg` (`build.py`, which stops if a clip is missing) and uploads it to the deck's release.
4. Re-import the new `.apkg`. Notes keep stable IDs, so existing cards are updated, not duplicated, and your review history is kept.

Clips for removed or reworded sentences stay in `audio/`; delete those not listed in the built deck if they pile up.

If you changed the note type's fields or templates, tick **Merge note types** in the import dialog, so the existing notes are updated instead of skipped.

> Note: some cards in `10 With Friends` and `00 My Saved Phrases` are vulgar by design.
