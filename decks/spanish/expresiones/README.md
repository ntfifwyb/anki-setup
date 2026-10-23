# Locuciones, Colocaciones, Vocabulario culto

Three subdecks of the [Español deck](../) that share one note type, one file each in `data/`:

| Subdeck | Notes | File |
|---|---|---|
| 02 Locuciones | 151 | `data/02-locuciones.txt`: set phrases, from the cultured (*a la sazón*, *por ende*) to colloquial and regional (*de prepo*, *ni modo*) |
| 03 Colocaciones | 116 | `data/03-colocaciones.txt`: the precise verb or adjective for a noun (*esgrimir un argumento*, *ignorancia supina*) |
| 04 Vocabulario culto | 144 | `data/04-vocabulario-culto.txt`: precise written words (*soslayar*, *aquiescencia*) and Latin phrases (*grosso modo*, *ex profeso*) |

## Cards

Note type **Spanish Expression**:

- **Producir** (every note): the front shows the subdeck, register and region, a definition and the example sentence with the expression gapped. The hint gives the word count, or for a single word its first letter and length (of the form in the sentence). You recall it; the back shows it and plays the sentence. In Colocaciones only the precise word is gapped, the noun stays visible.
- **Reconocer** (notes marked `R`, the rarer ones): the front shows and plays the expression; you recall its meaning.

## Editing

One expression per line: `expression | definition | example with {{the gapped words}} | notes | register | region | R`. `register` is `neutral`, `culto`, `formal`, `coloquial` or `vulgar`; `region` is empty (general), `esp`, `am`, `rioplatense` or `mex`; a final `R` adds a Reconocer card. A new subdeck needs a new file numbered after the others and an entry in `SUBDECKS` in `build.py`. Then rebuild as in the [deck README](../README.md#editing-and-rebuilding).
