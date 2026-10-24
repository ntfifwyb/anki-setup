# Vortfarado, Vortprovizo, Korelativoj kaj partikloj

Three subdecks of the [Esperanto deck](../) that share one note type, one file each in `data/`:

| Subdeck | Notes | File |
|---|---|---|
| 01 Vortfarado | 90 | `data/01-vortfarado.txt`: words built with affixes (*-ig-*, *-iĝ-*, *-ebl-*, *-ind-*, *-end-*, *-ej-*, *-ing-*, *-um-*, *mal-*, *ek-*, *bo-*, *fi-*, *mis-* …) and prepositions as prefixes |
| 02 Vortprovizo | 55 | `data/02-vortprovizo.txt`: precise verbs and adjectives (*aserti*, *agnoski*, *elteni*, *sopiri*) and false friends (*pretendi*, *eventuala*, *kompromiti*) |
| 03 Korelativoj kaj partikloj | 44 | `data/03-korelativoj-kaj-partikloj.txt`: the rarer correlatives (*ties*, *nenial*, *ĉiom*) and particles (*ja*, *plu*, *ajn*, *ju … des*) |

## Cards

Note type **Esperanto Word**:

- **Produkti** (every note): the front shows the subdeck, a definition and the example sentence with the word gapped. In Vortfarado the hint names the base word (*el «lerni»*), so you choose the affixes; elsewhere it gives the gap's first letter and length. The back shows the word and plays the sentence.
- **Rekoni** (notes marked `R`, the less obvious ones): the front shows and plays the word; you recall its meaning.

## Editing

One word per line: `word | definition | example with {{the gapped form}} | notes | base word | R`. The base word fills the Vortfarado hint; leave it empty elsewhere. A final `R` adds a Rekoni card. A new subdeck needs a new file numbered after the others and an entry in `SUBDECKS` in `build.py`. Then rebuild as in the [deck README](../README.md#editing-and-rebuilding).
