# The Flashcard Master Guide

**Read this whole file before creating any card.** It is written for an AI (or a person) asked to build an Anki deck for the owner of this repository, on any subject. It sets out the evidence-based principles, the rules that turn them into cards, subject-specific playbooks, and the exact output format to deliver.

If a request conflicts with this guide, follow the request but say which rule you departed from and why.

---

## Contents

1. [How to use this guide (workflow for an AI)](#1-how-to-use-this-guide-workflow-for-an-ai)
2. [Why flashcards work: the evidence](#2-why-flashcards-work-the-evidence)
3. [The core rules for every card](#3-the-core-rules-for-every-card)
4. [Card types and when to use each](#4-card-types-and-when-to-use-each)
5. [Language learning playbook](#5-language-learning-playbook) (audio: [§5.6](#56-audio-ship-it-inside-the-deck))
6. [Playbooks for other subjects](#6-playbooks-for-other-subjects)
7. [Anti-patterns: cards to never make](#7-anti-patterns-cards-to-never-make)
8. [Deck structure, tags and size](#8-deck-structure-tags-and-size)
9. [Output format: delivering an importable deck](#9-output-format-delivering-an-importable-deck)
10. [Quality checklist before delivering](#10-quality-checklist-before-delivering)
11. [Recommended Anki settings](#11-recommended-anki-settings)
12. [Sources](#12-sources)

---

## 1. How to use this guide (workflow for an AI)

Follow these steps in order.

1. **Clarify the request.** Before writing cards, settle these points (ask if they are not stated and cannot be inferred):
   - **Subject and scope.** For example: "German B2→C1 vocabulary about work", "Chapter 3 of a machine-learning book", "AWS ML Engineer exam domains".
   - **The learner's current level.** This decides card language, difficulty and how much context to give.
   - **The goal.** Recognising something, producing it, passing a specific exam, or using it in real life. Production goals need production cards.
   - **Source material.** If the learner supplied a text, book, notes or a syllabus, build from it and cite it. Do not invent facts.
   - **Deck size.** Default to 20–60 notes per batch. A small set of excellent cards beats a large set of weak ones (see §8).
2. **Understand before you atomise.** Build an outline of the topic first: the main ideas and how they connect. Cards come from that outline, not from random facts (Wozniak rules 1–3).
3. **Choose reinforcement targets.** Decide *what* is worth remembering before deciding *how* to word it. Prioritise high-frequency, high-utility, foundational knowledge. Skip trivia unless asked.
4. **Write the cards** using the rules in §3, the card types in §4, and the relevant playbook (§5 or §6).
5. **Self-review** every card against the checklist in §10. Delete or rewrite failures.
6. **Deliver** in the format in §9, with a short summary: number of notes and cards, note types used, deck name, tags, and anything you left out or were unsure about.
7. **Save the deck to this repository** in `decks/<deck>/` (one deck per language or subject; a new kind of card for an existing deck is a subdeck folder in it), with its importable file, its source data and build script, and a short README. Add it to the Decks table in the root `README.md`, then commit and push. (Details in `CLAUDE.md`.)

---

## 2. Why flashcards work: the evidence

These are the principles every rule below depends on. They are among the most replicated findings in learning science.

| Principle | What it means | Implication for cards |
|---|---|---|
| **Retrieval practice (testing effect)** | Pulling an answer out of memory strengthens it far more than re-reading it (Roediger & Karpicke, 2006). Dunlosky et al. (2013) rated practice testing one of only two "high utility" study techniques. | Every card must force a real recall. If the answer can be guessed from the wording, the card is wasted. |
| **Spaced repetition (spacing effect)** | Reviews spread over growing intervals beat massed review for long-term retention (Cepeda et al., 2006). Distributed practice was the other "high utility" technique. | Anki handles the schedule. The card's job is to be quick and unambiguous so it can be reviewed hundreds of times without friction. |
| **Minimum information principle** | Simple items are remembered much better than complex ones, even when a complex item "contains" the same facts (Wozniak). | One fact per card. Split anything with more than one answer. |
| **Desirable difficulty** | Effortful recall strengthens memory more than easy recall, as long as it usually succeeds (Bjork). | Cards should take a moment of thought, but you should get them right most of the time. Add cues to cards that are too hard; don't make them trivial. |
| **Elaboration and the generation effect** | Connecting new facts to what you already know, and producing answers yourself, improves retention. | Add "why" and "how" cards, examples and personal connections, not just definitions. |
| **Dual coding** | Words plus a relevant image form two memory routes. | Use images where they carry meaning: anatomy, maps, concrete nouns, diagrams. Skip decorative images. |
| **Interference** | Similar items get confused with each other. | Make look-alike items explicitly contrastive (see §3, rule 9). |

---

## 3. The core rules for every card

These synthesise Wozniak's *Twenty Rules of Formulating Knowledge*, Matuschak's *How to Write Good Prompts*, and the Anki manual.

### Rule 1. Understand first, then memorise
Do not make cards for material the learner has not understood. Memorising things you do not understand is slow, and the knowledge has little value. If the learner is new to a topic, start with conceptual cards (what, why, how it connects) before detailed ones.

### Rule 2. One card, one fact (minimum information)
Each card asks for exactly one piece of knowledge, and there is one correct answer.

- ❌ *Q: What are the characteristics of the Dead Sea?* — *A: Salt lake on the border of Israel and Jordan, 400 m below sea level, ~67 km long, salinity ~30%…*
- ✅ *Q: The Dead Sea lies on the border between which two countries?* — *A: Israel and Jordan*
- ✅ *Q: The Dead Sea's shore is roughly how far below sea level?* — *A: More than 400 m (the lowest land on Earth)*

When in doubt, split. More small cards are cheaper to review than one big card that you keep half-failing.

### Rule 3. Be precise and unambiguous
The question must make only one answer acceptable. Add just enough context to rule out other correct answers.

- ❌ *Q: What does ReLU do?*
- ✅ *Q: (Neural networks) The ReLU activation outputs what for a negative input?* — *A: 0*

### Rule 4. Be consistent
The card should produce the same answer every time. If you could answer it a different "correct" way next week, rewrite it.

### Rule 5. Make it effortful but tractable
- The learner must retrieve the answer, not recognise it. Avoid yes/no and true/false cards, and avoid wording that gives the answer away.
- The learner should succeed most of the time. If a card would be failed again and again ("leech"), split it, add a cue, or add a mnemonic.

### Rule 6. Use cloze deletion for facts inside sentences
Cloze is the fastest way to turn prose into well-formed cards, and it keeps context.

- `{{c1::Mitochondria}} produce most of the cell's {{c2::ATP}}.`

Delete only the meaningful part. Don't delete filler words, and don't put several deletions with the same number in one card unless they really are one idea.

### Rule 7. Never ask for sets or unordered lists
"List the 7 OSI layers" is a terrible card: you'll always forget one, and the card can't be reviewed reliably. Instead:
- **Ordered lists** → overlapping clozes: one card per item, each showing its neighbours as context. (Example: *Layer 3 of OSI is {{c1::Network}}; layer 4 is Transport.*)
- **Unordered sets** → turn each member into its own card with a distinguishing question. ("Which AWS service is a fully managed NoSQL key-value database?" → DynamoDB.)
- If the whole set truly matters, add one extra card for its size: "How many layers does the OSI model have?" → 7.

### Rule 8. Use images, diagrams and image occlusion
- One meaningful image is often better than a sentence of description.
- For diagrams (anatomy, maps, architecture), use **Image Occlusion** (built into Anki since 23.10): hide one label per card.
- Never add images just to decorate a card.

### Rule 9. Fight interference
When items look alike (similar words, similar formulas, two neighbouring dates):
- Make a card that asks for the **difference**. ("*affect* vs *effect*: which is usually the verb?")
- Add a distinguishing cue to each card.
- Don't introduce two look-alike items in the same session if you can avoid it. Learn one well first.

### Rule 10. Optimise the wording
Short, plain, concrete. Cut every word that doesn't help retrieval. A card should be readable in 1–2 seconds.

### Rule 11. Connect to existing knowledge and personalise
Link to things the learner already knows: their life, work, previous cards, analogies. Personal connections ("my colleague says *Feierabend* every day at 17:00") are remembered much better than abstract ones. Leave a field free for the learner to add their own.

### Rule 12. Add "why" and "how" cards, not just "what"
Pure facts decay into trivia. For conceptual subjects, add:
- **Explanation cards**: "Why does gradient descent need a learning rate smaller than some threshold?"
- **Application cards**: "You have 10 000 labelled images and few compute resources. Which approach: train from scratch or fine-tune a pretrained model?"
- **Example/counterexample cards**: "Give an example of a non-convex loss function."
- **Implication cards**: "If the validation loss rises while the training loss falls, what is happening?"

### Rule 13. Provide sources and dates where it matters
Put the source in a non-tested field (a reference, a page number, a link). Mark facts that change over time ("As of 2026, …") so outdated cards can be found and updated.

### Rule 14. Prioritise
You can't learn everything. Make cards for what is most frequent, foundational, testable or useful first. Mark lower-priority cards with a tag (`priority::low`) or leave them out.

### Rule 15. Redundancy is allowed
Testing the same knowledge from two directions (term → definition and definition → term; recognition and production) does not break the minimum information principle. It builds a stronger, more flexible memory. Use it for important items.

---

## 4. Card types and when to use each

The note types below exist in the owner's Anki collection already (see `backup/settings/note_types.json`). Prefer them so cards import cleanly.

| Note type | Use for | Example |
|---|---|---|
| **Basic** | One-directional question → answer. The default for concepts. | *What problem does batch normalisation address?* → *Unstable layer input distributions during training (speeds up and stabilises training).* |
| **Basic (and reversed card)** | Pairs that should be recalled in **both** directions: term ↔ definition, symbol ↔ meaning. Makes 2 cards. | *IPA [ç]* ↔ *voiceless palatal fricative (as in German "ich")* |
| **Basic (optional reversed card)** | Like above, but you choose per note whether the reverse exists (fill the "Add Reverse" field). | |
| **Basic (type in the answer)** | Exact spelling, formulas, short code, word gender + spelling. The learner types; Anki shows the differences. | *Plural of "das Museum"* → *die Museen* |
| **Cloze** | Facts embedded in a sentence, ordered lists, grammar in context, definitions where the term itself is the thing to recall. | *Die Sitzung wurde {{c1::verschoben}}, weil der Chef krank war.* |
| **Image Occlusion** | Labelled diagrams, maps, anatomy, architecture charts. | Hide one label of a transformer architecture diagram per card. |

Rules of thumb:
- If you're not sure, prefer **Cloze** for knowledge that sits inside a sentence and **Basic** for a question you'd genuinely ask yourself.
- Create a reverse card only when recalling in that direction is a real goal.

---

## 5. Language learning playbook

### 5.1 Should cards be fully in the target language, or use translations?

**Short answer: it depends on the learner's level and on the word, so don't apply a rule blindly.**

What the research shows:
- **For beginners and intermediate learners, a native-language (L1) translation is fast and effective** for first learning a word. Studies of glosses (short explanations given alongside new words) find that intermediate learners retain more with L1 glosses, while **advanced learners do better with target-language (L2) glosses** (Vietnam National University study, see Sources). The vocabulary researcher Paul Nation also treats L1 translation as an efficient way to learn a word's basic meaning.
- **Monolingual (L2→L2) cards help more advanced learners** build direct links inside the new language. One flashcard experiment found faster word recognition after monolingual learning for participants who already knew the words well (Obermeier & Elgort).
- The "no translations" approach is strongly advocated by **Gabriel Wyner (*Fluent Forever*)**, who recommends using pictures, audio and personal connections instead of the native-language word, so you "think in the language". It's a popular, widely used method, but it comes from practitioner experience more than controlled studies.
- Translation's main weaknesses are real: translations are rarely exact (words have different ranges of meaning), and an L1 word on the card can become a crutch.

**Default policy for this deck owner:**

| Learner level | Front | Back |
|---|---|---|
| **A1–A2 (beginner)** | Target-language word + **picture** + audio | Picture/translation is acceptable. For concrete nouns, prefer a picture over a translation. |
| **B1–B2 (intermediate)** | Target-language word or a cloze sentence | **Mostly target language**: a simple L2 definition, an example sentence, collocations. Add the L1 translation in a small, separate field only when the L2 definition alone is ambiguous. |
| **C1+ (advanced)** | Target-language word or cloze sentence | **Target language only**: monolingual-dictionary-style definition, synonyms, register, example. No translation. |

The owner is at **B2 German working towards C1**, so for German: **use target-language-only cards by default** (monolingual definitions, example sentences, clozes), with an optional, non-tested "Translation (hint)" field for words whose meaning a German definition can't pin down.

For abstract words, a picture rarely works. Use a definition or an example sentence instead.

### 5.2 Vocabulary card recipe (B1 and up)

One **note** per word or phrase. Recommended fields:

1. **Word** – with article and plural for nouns (`die Besprechung, -en`), principal parts for strong verbs (`verschieben – verschob – hat verschoben`), the case or preposition it takes (`sich beschweren über + Akk.`).
2. **Definition (target language)** – short, simple wording, ideally from or modelled on a monolingual learner's dictionary (for German: Duden, DWDS, PONS Deutsch als Fremdsprache).
3. **Example sentence** – natural, from real usage where possible, showing typical collocations.
4. **Cloze sentence** – the example with the word deleted (used for the production card).
5. **Audio** – pronunciation of the word and, ideally, the sentence: `WordAudio` and `ExampleAudio`, made with the deck (§5.6).
6. **Image** – only for concrete, picturable meanings.
7. **Notes** – register (formal/colloquial), false friends, near-synonyms and how they differ, regional usage.
8. **Translation (hint)** – optional, not tested, only when needed (see 5.1).

Cards generated from that note:
- **Recognition**: word (+audio) → definition + example. *Do I understand it?*
- **Production**: definition or cloze sentence → word. *Can I produce it?* Production is the harder and more valuable direction for speaking and writing goals.
- **Listening** (optional): audio only → word + meaning.

### 5.3 Prefer sentences and context over isolated words
- Learn words in **collocations and chunks** (*eine Entscheidung treffen*, not just *Entscheidung*). Native speakers store language in phrases.
- **Sentence mining**: take sentences from material the learner actually reads or hears (articles, series, work emails) where they know everything except one new item ("i+1"). Make the unknown item a cloze.
- Keep sentences short (ideally under ~15 words) so the card stays fast.

### 5.4 Grammar
- Don't put grammar tables on cards. Turn each rule into many small **cloze examples**.
  - ✅ *Ich warte {{c1::auf den}} Bus.* (hint: warten + Präp. + Kasus)
  - ✅ *Wenn ich Zeit {{c1::hätte}}, würde ich mitkommen.* (Konjunktiv II)
- For **noun gender** (German, French, Spanish…), always learn the article with the noun. A type-in card or a consistent colour code (e.g. blue = der, red = die, green = das) helps. Wyner suggests a vivid image per gender.
- For irregular forms, make a card per form that's actually used, not per table.

### 5.5 Pronunciation
- Add audio to every vocabulary card: a native recording when the learner supplies one, otherwise the neural voices of §5.6, generated with the deck.
- Early on, learn the sound system: IPA symbols, minimal pairs (*Hölle / Hülle*, *Miete / Mitte*), and spelling-to-sound rules. The owner's collection already includes IPA and phonetics note types.

### 5.6 Audio: ship it inside the deck
Whenever a card's content is meant to be heard (any language deck, pronunciation, songs or poems), the deck comes with its own audio clips. Don't leave `{{tts}}` tags or empty audio fields to be filled in Anki later: that takes the owner up to an hour per deck, has to be redone after every re-import, and `{{tts}}` doesn't play on the phone.

**How.** Make the clips when the deck is built, with the voices of the owner's [Psittacus](https://github.com/ntfifwyb/psittacus) add-on, linked in this repository as the submodule `addons/psittacus` (`git submodule update --init addons/psittacus`). Its modules `core.py` and `engines.py` don't need Anki. Copy the pattern of `decks/english/` and its subdeck `decks/english/expressions/`:
- `build.py` loads Psittacus without its Anki-only `__init__` (`psittacus()`), takes the **first** voice Psittacus picks for the deck's language from `voices.json` (`voice()`), and names each clip with `core.cache_name`, so a clip the add-on already made isn't imported twice. It stops if a clip is missing. The deck's own `build.py` (`decks/english/build.py`) packages its subdecks into one `.apkg`.
- `speak.py` makes the missing clips into the deck's `audio/` with `core.Speaker` and only that first engine, so every clip has the name `build.py` expects. Clips already there are skipped, so rerunning it after editing a few notes is quick.
- The clips are committed in `audio/`; the `.apkg` with them goes on a new release of the deck (`scripts/publish-deck.sh <deck>`), never into git.

**Which voice.** Psittacus decides per language, from a listening test the owner did:

| Engine | Languages | Package for `speak.py` (`uv run --with …`) |
|---|---|---|
| Kokoro (local) | English (US, UK), Spanish, Portuguese (BR), French, Italian, Hindi | `kokoro-onnx==0.6.1` |
| Piper (local) | German, Dutch, Polish, Russian, Turkish, Arabic, Japanese, Korean | `piper-tts==1.8.0` |
| Edge TTS (online, unofficial Microsoft service) | Chinese, Portuguese (PT), anything else | `edge-tts==7.3.1` |

Every engine also needs `soundfile==0.13.1`; the exact versions are in the submodule's `requirements-addon.txt`. Models download once into `~/.cache/psittacus`. Use the language codes of `voices.json` (`en_US`, `de`, `pt-BR`…), the same ones as in a `{{tts}}` tag.

**Which fields and sides.** One audio field per spoken field, named after it (`Word` → `WordAudio`, `Example` → `ExampleAudio`), holding `[sound:<clip>.mp3]`, and placed in the template as `{{WordAudio}}`. Speak the plain text: strip HTML and cloze markers first. Play a clip only where it doesn't give the answer away: on a production card the front stays silent and the back plays the word and the example; on a recognition card the front may play the word. Fill an audio field only on notes whose cards play it.

**Check before delivering.** You can't listen, so check what you can: every audio field points to a clip that exists, no clip is empty or a fraction of a second long, and the clip count matches the fields. For a language you are less sure of, transcribe a sample of clips with Whisper and compare them with the text (Psittacus's `bench/` does this) to catch a voice reading the wrong words. Say in the delivery summary which voice spoke the deck.

### 5.7 What to choose to learn
- Prioritise by **frequency** (frequency lists, words met repeatedly in the learner's own reading) and by **personal relevance** (work, hobbies, upcoming exams).
- Don't make cards for words the learner already knows.
- Don't make cards for very rare words unless the learner asked for them.

---

## 6. Playbooks for other subjects

### 6.1 Technical and conceptual subjects (AI/ML, programming, science, engineering)
- Start with **concept cards**: the definition, the intuition, why it exists, what problem it solves.
- Add **mechanism cards**: "What happens to the gradient of a sigmoid at very large inputs?" → "It approaches 0 (vanishing gradient)."
- Add **comparison cards** between commonly confused concepts: "L1 vs L2 regularisation: which tends to produce sparse weights?"
- Add **application/scenario cards** with short, concrete situations.
- **Formulas**: one card for what each symbol means, one to recall the formula (type-in or cloze on one term at a time), and one for when to use it.
- **Code**: test what a short snippet does, the name of a specific API or function, or a single line to fill in. Never ask for whole programs to be recalled.
- Good cards here follow the learner's understanding. Base them on the learner's source (course, book, paper) and cite it in a source field.

### 6.2 Certification exams (e.g. AWS)
- Map cards to the **official exam guide's domains** and tag them by domain (`aws-mle::domain-2`).
- Focus on **"which service/option for this scenario"** cards, because that's how questions are asked.
- Include limits, defaults and distinctions that exams test ("SageMaker real-time vs serverless vs asynchronous inference: which suits large payloads with long processing time?").
- Mark changeable facts with a date (services and limits change).

### 6.3 Facts: history, geography, general knowledge
- Use **cloze** with context: *The Berlin Wall fell in {{c1::1989}}.*
- Turn dates into short, meaningful cards. Add a "why" or "what followed" card for important events.
- Use **maps with image occlusion** for geography.

### 6.4 Medicine, biology, anatomy
- Image occlusion for anatomy and pathways.
- One mechanism step per card.
- Cards for "most common cause of…", "first-line treatment for…", contraindications.

### 6.5 Procedures and skills
- Spaced repetition can't teach a physical or practical skill, but it can keep the **steps, cues and common errors** fresh.
- Make one card per step ("After X, what is the next step?"), plus cards for the common mistakes and why they happen.

---

## 7. Anti-patterns: cards to never make

| ❌ Anti-pattern | Why it fails | ✅ Fix |
|---|---|---|
| Long answer with several facts | Partial recall, inconsistent grading | Split into one fact per card |
| "List all X" | Always forget one item | Overlapping clozes, or one card per member |
| Yes/No or True/False | 50% guessable, weak retrieval | Ask for the thing itself |
| Vague question ("Tell me about…") | Many valid answers | Add context so only one answer fits |
| Answer hidden in the question wording | No real retrieval | Rephrase; remove cues that give it away |
| Isolated word with an English translation for an advanced learner | Weak, inexact links; L1 crutch | Definition, example, collocation in the target language |
| Copying a textbook paragraph onto a card | Not reviewable | Extract the 2–5 key facts as clozes |
| Cards on things not understood | Slow, fragile, low value | Explanation and concept cards first |
| Decorative images | Noise and media bloat | Only images that carry meaning |
| Near-duplicate cards worded differently | Interference, wasted reviews | Merge, or make them explicitly contrastive |
| Huge decks of trivia | Burnout, abandonment | Prioritise; fewer, better cards |

---

## 8. Deck structure, tags and size

- **Decks**: few and broad, using `::` for hierarchy. `Languages::Deutsch`, `Artificial Intelligence`, `Certifications::AWS ML Engineer`. Anki recommends using tags rather than lots of small decks. A language deck and its subdecks are named in that language, for immersion (`Languages::Deutsch::Verben`, `Languages::Español`).
- **Tags**: use for source, chapter, topic and priority. Lowercase, hyphenated, `::` for hierarchy: `source::deep-learning-book`, `chapter::03`, `topic::regularisation`, `priority::high`, `de::b2`.
- **Batch size**: 20–60 notes per batch. With the default limit of 20 new cards per day, 60 notes may already be 3–6 days of new cards, especially with reversed cards.
- **Ordering**: foundational cards first, so later cards build on them. Use the order in the file; Anki keeps it for new cards.
- **Consistency**: same field order, same style and same tags in a deck, so cards look and feel uniform.

---

## 9. Output format: delivering an importable deck

Pick one of the two formats below. In both cases, also give a short plain-text summary of what's in the deck.

### Option A (preferred for text-only decks, never for decks with audio): a tab-separated `.txt` file with Anki import headers

Anki 2.1.55+ reads these header lines, so the file imports with the right note type, deck and tags without any manual setup. Use **tab** as the separator (commas and semicolons occur in normal text).

```text
#separator:tab
#html:true
#notetype:Basic
#deck:Artificial Intelligence
#tags column:3
What does a neuron hold?	A number between 0 and 1 (its activation)	topic::neural-networks
Why does the digit network have 784 inputs?	One per pixel of a 28×28 image	topic::neural-networks
```

For cloze notes:

```text
#separator:tab
#html:true
#notetype:Cloze
#deck:Languages::Deutsch
#tags column:3
Die Sitzung wurde {{c1::verschoben}}, weil der Chef krank war.	verschieben – verschob – hat verschoben; <i>auf einen späteren Zeitpunkt legen</i>	de::b2 topic::arbeit
```

Rules for this format:
- One file per note type.
- The columns must match the note type's fields in order (Basic: Front, Back; Cloze: Text, Back Extra). The owner's note types can have extra fields (e.g. *Basic (and reversed card)* is Front, Example, Back), so always check the field order in `backup/settings/note_types.json`. Tags go in the column named by `#tags column`.
- Never put a literal tab or newline inside a field. Use `<br>` for line breaks (HTML is on).
- Escape nothing else; don't wrap fields in quotes unless they contain a tab.
- Multiple tags are separated by spaces.

Import: **File → Import**, choose the file, check the preview, click **Import**.

### Option B: an `.apkg` file (when you need custom note types, media, or several decks)

Generate it with the Python library [`genanki`](https://github.com/kerrickstaley/genanki):
- Give each model and deck a fixed, random 64-bit ID, and use `genanki.guid_for(...)` on a stable key (e.g. the word or question) so re-importing an updated deck updates notes instead of duplicating them.
- Add media files through `package.media_files`, and refer to them in fields by file name only: `[sound:verschieben.mp3]`, `<img src="besprechung.jpg">`. Audio clips are made as in §5.6.
- For a vocabulary note type, use the fields from §5.2 and generate a recognition template and a production template.

### General formatting rules
- Keep the front of a card short: ideally one line.
- Bold (`<b>`) the key term on the back only if it helps scanning.
- No styling that fights the owner's dark theme (the installed Anki Dashboard add-on uses a dark palette): don't hard-code black text or white backgrounds.
- Put sources, notes and translation hints in fields that aren't tested.

---

## 10. Quality checklist before delivering

Check **every** card. Rewrite or delete any card that fails.

- [ ] Does it test exactly **one** thing?
- [ ] Is there only **one** correct answer, and does the question make that clear?
- [ ] Does it require **real recall**, not recognition or guessing?
- [ ] Can it be answered in **under ~10 seconds** by someone who knows it?
- [ ] Is the wording as **short** as possible?
- [ ] Is it **factually correct** and consistent with the source? (When unsure, check, or leave it out and say so.)
- [ ] Is it something **worth remembering** for the learner's goal?
- [ ] Does it avoid **sets, lists, yes/no** and copied paragraphs?
- [ ] For look-alike items: is the **distinction** made explicit?
- [ ] For languages: is the card in the **target language** to the degree the learner's level calls for (§5.1)? Does it include **article/plural/forms**, an **example** and the deck's own **audio** clips (§5.6)?
- [ ] For conceptual topics: are there **why/how** cards, not only definitions?
- [ ] Is the **note type**, **deck** and **tag** format correct for import (§9)?
- [ ] No duplicates of existing cards? (The owner's current cards are listed in `backup/exports/all_notes.md`.)

---

## 11. Recommended Anki settings

The owner's current settings are in `backup/settings/`. General advice from the Anki manual and the FSRS project:

- **Turn on FSRS** (Deck Options → Advanced → FSRS) and click **Optimize** once the preset has a few hundred reviews (Anki tells you if there isn't enough data yet). FSRS schedules more accurately than the legacy SM-2 algorithm.
- **Desired retention: 0.90** is the standard default. Higher values (0.95) sharply increase the number of reviews; lower values (0.85) reduce work but you forget more.
- **New cards/day**: 10–20 for steady progress. Each new card produces several reviews per day for weeks, so the review load grows with the number of new cards.
- **Learning steps**: `1m 10m` (default) is fine. With FSRS, keep steps under one day.
- **Leeches**: keep "Tag only" and fix leech cards using the rules above (split, add a cue, add a mnemonic) instead of just pushing on.
- **Grade honestly**: use **Again** when you didn't recall the answer, and **Good** in most other cases. Don't use **Hard** for a failure.

---

## 12. Sources

Research and methods this guide is based on:

- Wozniak, P. (1999). [Effective learning: Twenty rules of formulating knowledge](https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge). SuperMemo.
- [Minimum information principle](https://supermemo.guru/wiki/Minimum_information_principle). supermemo.guru.
- Matuschak, A. [How to write good prompts: using spaced repetition to create understanding](https://andymatuschak.org/prompts/).
- Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255.
- Cepeda, N. J., et al. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380.
- Dunlosky, J., et al. (2013). Improving students' learning with effective learning techniques. *Psychological Science in the Public Interest*, 14(1), 4–58.
- Bjork, E. L., & Bjork, R. A. (2011). Making things hard on yourself, but in a good way: Creating desirable difficulties to enhance learning.
- Obermeier, A., & Elgort, I. [Integrating new vocabulary into the mental lexicon: Comparing the effects of monolingual and bilingual flashcard learning](https://openaccess.wgtn.ac.nz/articles/journal_contribution/Integrating_New_Vocabulary_into_the_Mental_Lexicon_Comparing_the_Effects_of_Monolingual_and_Bilingual_Flashcard_Learning/29133098/1). Victoria University of Wellington.
- [Effects of first language and second language glosses on learners' reading comprehension and vocabulary retention](https://jfs.ulis.vnu.edu.vn/index.php/fs/article/view/5052). VNU Journal of Foreign Studies.
- Nation, I. S. P. (2001). *Learning Vocabulary in Another Language*. Cambridge University Press.
- Wyner, G. (2014). *Fluent Forever: How to Learn Any Language Fast and Never Forget It*. ([summary notes](https://grahammann.net/book-notes/fluent-forever-gabriel-wyner))
- [The Anki Manual](https://docs.ankiweb.net/) — importing text files, note types, image occlusion, deck options and FSRS.
- [genanki](https://github.com/kerrickstaley/genanki) — Python library for generating `.apkg` files.
