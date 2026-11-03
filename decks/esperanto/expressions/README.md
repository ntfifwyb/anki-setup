# 06 Esprimoj

199 Esperanto expressions (266 cards) for an intermediate speaker: the chunks single words don't teach. The preposition an adjective, noun or verb takes (*riĉa je*, *rajto je*, *peti iun pri*), collocations (*fari decidon*, *trapasi ekzamenon*, *kovri la tablon*), the words that structure speech and the set phrases of conversation (*unuflanke … aliflanke*, *interalie*, *ne dankinde*), and proverbs from Zamenhof's *Proverbaro Esperanta*. The companion to [05 Verboj](../verbs/), which teaches the verbs themselves. Part of the [Esperanto deck](../), in `Languages::Esperanto::06 Esprimoj`.

**Import:** download the deck's `.apkg` from the [deck README](../README.md) and open it with Anki (or **File → Import**); it adds this subdeck with its audio.

## Subdecks

| Subdeck | Notes | What's in it |
|---|---|---|
| 01 Prepozicioj | 40 | The preposition that goes with a word, where Spanish, English or German picks another: *riĉa je*, *tipa por*, *kolera kontraŭ*, *rajto je*, *malsaniĝi je*, *kapti iun je la brako* |
| 02 Kolokacioj | 45 | Words that belong together, and the calques to avoid: *fari decidon*, *havi sencon* (not *fari sencon*), *turni la atenton al* (not *pagi atenton*), *forta pluvo* |
| 03 Frazoj kaj diskursaj vortoj | 47 | Linking and structuring speech, and conversation: *ne nur … sed ankaŭ*, *alivorte*, *rilate al*, *dank' al*, *por tiel diri*, *ne dankinde*, *je via sano* |
| 04 Proverboj | 67 | Proverbs from the *Proverbaro Esperanta*: *Kiu ne riskas, tiu ne gajnas*, *Parolo estas arĝento, oron similas silento*, *Unu hirundo printempon ne alportas* |

Verb + preposition pairs already in a Verboj card's notes or sentence (*dependi de*, *kredi je*, *fieri pri*, *interesiĝi pri*, *plaĉi al*, *manki al* and about 200 more) are left out, so no pair is studied twice. Single linking words already in 03 Korelativoj kaj partikloj (*tamen*, *do*, *cetere*, *almenaŭ*) are left out too.

The proverbs are word for word from the second edition of the *Proverbaro Esperanta* (L. L. Zamenhof, 1925, public domain), as in the proofread transcription on [Esperanto Wikisource](https://eo.wikisource.org/wiki/Proverbaro_Esperanta_(L._Zamenhof,_2a_eld.)); each note gives the proverb's number there and, where one exists, the same proverb in Spanish, English or German. The rest was written by Claude for this deck. Every note is tagged with its subdeck (`type::prepozicioj`, `type::kolokacioj`, `type::frazoj`, `type::proverboj`).

## Cards

The note type is **Esperanto Word**, the same as Vortfarado's, with the expression in its *Word* field.

- **Produkti** (every note): the front shows the kind of expression, an Esperanto definition and the example with the expression's words gapped, plus a word count (*2 vortoj en 2 partoj*). You recall the whole chunk, preposition included. For a proverb, the example is the proverb itself with its second half gapped: you complete it from its first half and its meaning.
- **Rekoni** (the proverbs): the front shows and plays the proverb; you recall what it means.

The example sentence is spoken (eSpeak NG, as for the rest of the deck) on the back of every card; a proverb's Rekoni card plays it on the front.

## Editing

One expression per line in the file in `data/` for the subdeck: `expression | definition | example with {{the expression's words}} marked | notes | R`. The notes may hold `<i>` markup; a final `R` adds a Rekoni card. A proverb's example must be the proverb itself, with the part to recall marked. `build.py` stops on a malformed line, a duplicate, a sentence without a mark or a proverb whose example differs from it. A note's ID comes from the expression, so fixing anything else updates the card in place. Then make the audio and rebuild as in the [deck README](../README.md#editing-and-rebuilding).
