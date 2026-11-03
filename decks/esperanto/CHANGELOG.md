# Changelog

Each version is a release tagged `esperanto-x.y.z` on the [releases page](https://github.com/ntfifwyb/anki-setup/releases). Major: importing it needs a step in Anki. Minor: new cards. Patch: fixes.

## 2.0.0 (2026-11-03)

- New subdeck **05 Verboj**: the 2,000 most common verbs from my study list (1,997 notes; three non-verbs left out), with an Esperanto definition, transitivity, a gapped sentence, the English as a hint and audio. Verbs ranked 501 and up also have a *Rekoni* card. Sentence fixes are listed in [verbs/README.md](verbs/README.md).
- **Vortprovizo** loses its 46 verbs (*pretendi*, *atendi*, *sopiri* …), which moved to Verboj with their definitions and notes; 9 adjectives and adverbs remain.
- **Step in Anki:** importing doesn't delete notes, so the 46 old Vortprovizo verb cards stay until you remove them. Before or after importing, open **Browse**, search
  `"deck:Languages::Esperanto::02 Vortprovizo" -Word:ekzemplero -Word:eventuala -Word:konscia -Word:konscienca -Word:simpatia -Word:kulpa -Word:verŝajne -Word:nepre -Word:kvankam`
  check that it finds 46 notes, select them all and delete them. Their review history goes with them; the same verbs start fresh in Verboj.

## 1.0.0 (2026-10-24)

- First release: 252 notes (343 cards) in `Languages::Esperanto`, with audio: Vortfarado, Vortprovizo, Korelativoj kaj partikloj and Gramatiko.
