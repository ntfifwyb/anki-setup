# Spanish

My Spanish deck: not a course but the cultured register of my own language, with audio. 676 notes (810 cards) in `Languages::Spanish`, one subdeck per kind of card. Panhispanic: regionalisms are tagged with their region (España, América, Río de la Plata, México) and their equivalents elsewhere noted on the card.

**Import:** download [`Spanish.apkg`](https://github.com/ntfifwyb/anki-setup/releases/download/spanish/Spanish.apkg) from the deck's [release](https://github.com/ntfifwyb/anki-setup/releases/tag/spanish) and open it with Anki (or **File → Import**). It adds or updates every subdeck at once, with its audio. Notes keep stable IDs, so re-importing updates existing cards instead of duplicating them.

## Subdecks

| Subdeck | Notes | What's in it | Folder |
|---|---|---|---|
| 01 Refranes | 173 | Complete the refrán and say what it means; the back gives its German and English equivalent where one exists | [refranes/](refranes/) |
| 02 Locuciones | 151 | Set phrases from the cultured to the colloquial: *a la postre*, *sin solución de continuidad*, *de higos a brevas*, *tomar las de Villadiego* | [expresiones/](expresiones/) |
| 03 Colocaciones | 116 | The precise word that goes with another: *zanjar una polémica*, *subsanar un error*, *error garrafal*, *miedo cerval* | [expresiones/](expresiones/) |
| 04 Vocabulario culto | 144 | Precise, mostly written words and Latin phrases: *abstruso*, *perentorio*, *conminar*, *ex profeso*, *statu quo* | [expresiones/](expresiones/) |
| 05 Norma y dudas | 92 | Choose the form the norma culta prefers, and learn why: *hubo/hubieron*, *infligir/infringir*, *detrás de mí/mío*, dequeísmo | [norma/](norma/) |

All written by Claude for this deck: meanings in the style of the RAE's *Diccionario de la lengua española*, refranes among the best known (as in the Instituto Cervantes' *Refranero multilingüe*), and the rules in Norma y dudas from the RAE's *Diccionario panhispánico de dudas*, *Ortografía* (2010) and *Nueva gramática*.

Cards are entirely in Spanish. Every note is tagged with its type and, where it applies, its register (`register::culto`, `register::coloquial`, …) and region (`region::esp`, `region::am`, `region::rioplatense`, `region::mex`).

## Audio

Spoken by Kokoro's `ef_dora`, the voice the [Psittacus](https://github.com/ntfifwyb/psittacus) add-on uses first for Spanish. Ordinary MP3s in `audio/`, shared by every subdeck, so they play on desktop, AnkiDroid and AnkiMobile without any add-on.

## Editing and rebuilding

1. Edit the subdeck's data (see its README).
2. Make the audio for new or changed text (it needs the Psittacus submodule, `git submodule update --init`); clips already in `audio/` are skipped:
   ```
   uv run --no-project -p 3.13 --with genanki==0.13.1 --with kokoro-onnx==0.6.1 --with soundfile==0.13.1 python speak.py
   ```
3. Commit, then run `scripts/publish-deck.sh spanish` from the repository root. `build.py` packages every subdeck in `PARTS` into `Spanish.apkg` (each subdeck's `build.py` stops on a malformed line or a duplicate, and `common.py` on a missing clip) and uploads it to the release.
4. Re-import the new `.apkg`. A note's ID comes from its text (the expression, the refrán, the correct sentence), so changing that text gives it a new ID; changing anything else updates it in place.

`common.py` holds what the subdecks share: the data parser, the register and region labels, the card style and the audio clips. To add a new kind of card, add a folder with a `build.py` whose `rows()` returns its notes, and list it in `PARTS`.
