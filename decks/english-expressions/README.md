# English Expressions

444 English expressions (487 cards) for a fluent speaker who wants a wider, more precise range of phrases. Every card is labelled with its context and register (academic, formal, neutral, informal, slang, vulgar).

**Import:** download `English_Expressions.apkg` and open it with Anki (or **File → Import**). It goes into `Languages::English::Expressions`.

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

## Editing and rebuilding

1. Edit `expressions.txt` or `contexts.txt`. One expression per line: `expression | meaning | example with {{the expression}} marked | notes | register | context | R` (R = also make a recognition card).
2. Run `pip install genanki` and then `python build.py`.
3. Re-import the new `.apkg`. Notes keep stable IDs, so existing cards are updated, not duplicated, and your review history is kept.

> Note: some cards in `10 With Friends` and `00 My Saved Phrases` are vulgar by design.
