# Verboj

The 2,000 most common Esperanto verbs, in frequency order, built from the 2000-verb list in my "Esperanto" study notes, the same way as the German [Verben](../../german/verbs/): 1,997 notes, each with the verb's transitivity, a definition in Esperanto, an example sentence, its English translation and usage notes (prepositions, *-ig*/*-iĝ* pairs, false friends). Part of the [Esperanto deck](../), in `Languages::Esperanto::05 Verboj`.

## Cards

The note type is **Esperanto Verb**. The cards are in Esperanto; the English is a tap-to-reveal hint on the front and a small line on the back.

- **Produkti** (every note): the front shows the rank, whether the verb is transitive, the definition and the example with the verb's form gapped, its first letter and length, and the English behind a *hint* link. You recall the verb in the form the sentence needs (*kuras*, *venu*, *aŭdiĝis*). The back shows the verb, the full sentence and the notes, and plays the verb and the sentence.
- **Rekoni** (only verbs ranked 501–2000): the front shows and plays the verb; you recall what it means. The first 500 are everyday verbs an intermediate speaker already understands, so they only get the Produkti card.

Definitions often share the verb's root (*validi*: "esti valida", *premii*: "doni premion al"), as Esperanto's own dictionaries do: the card then tests that the root works as a verb, and in which form. `build.py` doesn't check that; the script that wrote `verbs.txt` rejected definitions that contain the verb itself.

| Tag | Meaning |
|---|---|
| `freq::0001-0250` … `freq::1751-2000` | Frequency band |
| `verb::transitiva`, `verb::netransitiva` | Takes a direct object (*-n*) or not |
| `affix::ig`, `affix::iĝ` | Ends in *-igi* (makes something happen) or *-iĝi* (happens by itself) |

## Editing

One verb per line in `verbs.txt`: `rank | verb | tr. or ntr. | definition | example with {{the verb's form}} | English | English example | notes`. Mark the verb once per sentence. `build.py` stops on a malformed line, a duplicate, a rank out of order or a sentence without exactly one mark. A note's ID comes from the verb, so fixing anything else updates the card in place. Then make the audio and rebuild as in the [deck README](../README.md#editing-and-rebuilding).

## Changes from the source list

- Left out: *menciindi* (1003), not a verb in use (*estas menciinde* is the adjective *menciinda*); *povoscii* (862), non-standard, the word is *scipovi* (613); *alti* (1442), not a verb in use, the word is *altigi* (443).
- Corrected typos in the sentence: 975 *ampleksi*, 1501 *kolizii*, 1851 *dedukti*.
- Corrected *antaŭ* or *post* before an infinitive or a clause, which needs *antaŭ ol* or *post kiam*: 919, 921, 951, 993, 1243, 1298, 1356, 1361, 1551, 1561, 1575, 1600, 1699, 1718, 1737, 1756, 1795, 1820, 1962.
- Other corrected sentences: 177 (*skolon*), 226 (*preferi … al*), 255, 258, 305 (a preposition before an infinitive), 486 (*rezulti en*, an anglicism), 616 (*laptopon*), 621 (*ofero* for *oferto*), 679 (*al mi ekpensis ideo*), 890, 913 and 1233 (*pri tio, kiu*), 1107, 1369, 1399, 1448, 1579, 1638, 1806, 1878, 1910, 1948.
- The 46 verbs that were in Vortprovizo (*pretendi*, *agnoski*, *sopiri* …) moved here, with that subdeck's definition and notes; the sentence is the list's. The verbs also in Vortfarado (*plibonigi*, *ĝisdatigi*, *malhelpi* …) stay there too, as a word-building card, and share its definition.
