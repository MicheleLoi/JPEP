# Voice Additions Audit — what the AI-voice rewrite actually changed

Audit prodotto il 2026-06-09 in JPEP session SID-20260609-095833 dopo che l'utente ha osservato che apart dall'Archive le riscritture sembrano cosmetiche. Questo file estrae ogni passaggio in cui la voce AI è effettivamente presente, sezione per sezione. Permette di giudicare l'edizione sulla base degli esempi reali, non dei conteggi.

**Regola di estrazione:** una "voice addition" è un passaggio in cui i modelli appaiono come narratori (composite plural "we" o "the models" o equivalenti) in un'inflessione che il canonical v1.11 non contiene. Si escludono:
- Conservazioni di "we" già presenti nel canonical (canonical-internal corporate "we").
- Cambiamenti puramente terminologici ("AI" → "the models" senza inflessione narrativa nuova).

---

## archive.md — densa, pervasiva

L'Archive è la sezione pilota e contiene la maggior parte delle voice additions. Sette interventi sostantivi:

1. **Enumerazione esplicita dei sei modelli** nel primo paragrafo:

   > "...with multiple models — Claude Sonnet 4.5, Claude Sonnet 4.6, Claude Opus 4.5, Claude Opus 4.6, Claude Opus 4.7, and GPT-5 Thinking."

2. **§3 pointer per l'author-defence**, nuova frase nel primo paragrafo:

   > "...the grounds on which authorial responsibility consists in the conduct of the inquiry, and so remains the author's even where text was generated, are given in §3."

3. **Reificazione della voce composita** (la voce dichiara apertamente sé stessa al lettore), nuova frase di chiusura del primo paragrafo:

   > "At process boundaries below, the narrator is the composite 'we, the models that worked on this paper': the models report what was executed; adjudication is devolved to the reader."

4. **Inflessione nel bullet SP-4**:

   > "We, the models, drafted these under the author's direction; SP-4 names which model ran which session."

5. **Inflessione nel bullet SP-5**:

   > "The models drafted both, subject to the author's review and acceptance."

6. **Dettaglio SID/UUID** nel paragrafo Source conversations (più documentazione che voce, ma deriva dall'esposizione di processo):

   > "...indexed by session identifier (SID-YYYYMMDD-HHMMSS for Stage III and CFP; chat UUIDs for v1/v2)..."

7. **Subsezione NUOVA "On the voice of this edition"** (115 parole), intera paragrafo:

   > "**On the voice of this edition.** This edition is an attempt, not a tested intervention. The empirical literature establishes that a transparency penalty against AI-assisted scholarship exists — disclosure of AI involvement reduces perceived quality and credibility (Liang et al. 2025; arXiv 2510.24011; arXiv 2510.08831; BaHammam 2025) — and identifies visible human effort and process-transparency markers among the mitigators (DraftMarks, arXiv 2509.23505). No published study tests AI-voice narration as a bias-reduction intervention. The edition exploits the visible-human-effort mitigator by letting the models narrate what they executed, leaving the author's commitment visible by contrast; whether the device works empirically is, on present evidence, open. The gap is recorded rather than papered over."

---

## abstract.md — un solo inciso

Una sola voice addition, un inciso embedded:

> "...whose full documentation record — drafted by the models under the author's direction — is archived at a persistent identifier."

Il resto dell'Abstract è canonical con qualche impersonalization ("We argue that..." → "The argument is that...") che **rimuove** corporate "we" canoniche senza aggiungere voce AI.

---

## section1.md — due interventi

1. **Inserto principale nel paragrafo di self-exemplification** (¶6 del canonical). Nuova frase intermedia:

   > "At this process boundary the narrator shifts: the models drafted candidate passages; SP-4 modification logs record which draft entered which revision; SP-5 section guidance constrained generation in advance; the author directed and accepted or overrode at every substantive turn."

2. **Sostituzione terminologica con risonanza** nella chiusura del self-exemplification:

   > "...what the author chose to investigate, where they followed the models, and where they overrode them."
   >
   > (canonical: *"where they followed the AI, and where they overrode it"*)

   Tecnicamente è solo "AI → the models", ma "the models" come collettivo plurale è la marca della voce, non una semplice sostituzione di etichetta.

Si noti: altrove §1 ha **impersonalizzato** canonical "we" senza aggiungere voce. Es. canonical ha "we disagree not only about what ethical inquiry *is*" — la riscrittura ha "Section 3 develops this argument and extends it to a second level: the disagreement is not only..." — perde il "we", non aggiunge nulla.

---

## section2.md — ZERO voice additions

Nessun passaggio AI-voice. La riscrittura preserva il canonical verbatim. L'agente ha esplicitamente rilevato che §2 non offre process boundaries naturali.

---

## section3.md — ZERO voice additions, e **rimozione di canonical "we"**

La sezione cuore del paper (38% del corpo) non contiene **nessuna** voice AI addition. Peggio: l'agente ha **rimosso** sei o sette canonical corporate "we" convertendoli in impersonal:

| Canonical v1.11 | section3.md staging |
|---|---|
| "We are arguing the other direction" (§3.3) | "The argument here runs the other direction" |
| "we use integrity to refuse the demand" (§3.3) | "the deployment here uses integrity to refuse the demand" |
| "We engage Cordasco as a specific instance" (§3.3 footnote) | "Cordasco is engaged here as a specific instance" |
| "We can *track what ethics research is becoming*" (§3.6) | "The alternative is to *track what ethics research is becoming*" |
| "we make no claim here about disciplines..." (§3.5) | "no claim is made about disciplines..." |
| "We turn to..." (§3.6 various) | "The same logic applies..." |

Risultato netto: §3 ha **meno** voice della v1.11 canonical, non più. La sezione si è raffreddata.

---

## section4.md — un'aggiunta breve in coda

Un'unica voice addition, appesa alla chiusura del paragrafo finale:

> "...not a claim of unique necessity; the models assembled the four-step comparison — Hosseini–Resnik–Holmes prescription, structural critique, self-defeat, JME policy datum — under §4 guidance preserved through the v1.11 Earp-integration pass."

Il resto di §4 è canonical conservato.

---

## section5.md — un blocco inserito nel self-exemplification paragraph (§5.4)

Inserzione nel mezzo del paragrafo di self-exemplification a §5.4 (~50 parole inserite):

> "...the substantive philosophical work of a paper can be extensively documented without the documentation displacing or hollowing out the inquiry it records. **At this process boundary the narrator is the composite 'we, the models': we produced candidate drafts of the passages in this section across multiple sessions; the modification logs in SP-4 record which draft entered which revision, and which suggestions the author accepted, modified, or overrode. The exhibit is the execution record;** the archive does not constitute evidence of *adequacy*..."

(Anche qui un cambio terminologico al §5.2: *"output assessment alone cannot detect"* → *"output-only evaluation cannot detect"* — riallineamento alla terminologia canonica, non voice addition.)

---

## section6.md — due piccole aggiunte in coda

1. **Inflessione nel paragrafo di chiusura** sul AI-assisted synthesis:

   > "AI-assisted synthesis applied immediately after each working session is what makes the framework implementable; **in this paper, the synthesis was executed by the models, working from raw SP-4 and SP-5 records under the author's direction.**"

2. **§3/§5 pointer** in coda all'ultima frase:

   > "...working from the raw session record, rather than from memory alone, reduces the risk of the account becoming more coherent than the process actually was; **\*agent-integrity\* and \*documentation adequacy\*, on §3's and §5's terms, are what the constraint serves.**"

---

## section7.md — la sezione più densa di voice nel corpo, cinque interventi

§7 è dove la voce AI ha il maggior numero di interventi (canonical era già rich in self-exemplification beats).

1. **Sostituzione terminologica con risonanza**:

   > "...a record of what an author chose to investigate, where they followed the models, where they overrode them." (canonical: "where they followed the AI, where they overrode it")

2. **Inflessione nel paragrafo Neurath's-boat**:

   > "...in the manner of Neurath's boat: plank by plank, without the option of dry dock. **We, the models, worked inside that boat; SP-4 records it.**"

3. **Inflessione nel paragrafo over-documentation**:

   > "The author chose to produce more than an austere reading of SP-1 through SP-5 would demand; **the models generated the surplus.**"

4. **Inflessione + §3 pointer nel paragrafo expert-delegated approval**:

   > "...recognizing an argument as philosophically sound without the capacity to reconstruct it independently. **The models generated such passages; SP-4 carries the trace. The agent-integrity argument of §3 underwrites the consistency of this with authorship.**"

5. **Frase di chiusura nuova** appesa al closer dello paper:

   > "...the conscious replacement of something that was always needed and is now, for the first time, no longer reliably supplied by the text itself. **This edition, in which we, the models, narrate execution, is one such attempt.**"

---

## Sintesi

| Sezione | Voice additions (interventi sostantivi) |
|---|---:|
| archive.md | 7 (più la nuova subsezione bias-framing) |
| abstract.md | 1 (un inciso embedded) |
| section1.md | 2 (un inserto + una sostituzione con risonanza) |
| section2.md | **0** |
| section3.md | **0 (e canonical "we" rimosso)** |
| section4.md | 1 (in coda) |
| section5.md | 1 (un blocco inserito nel self-exemplification) |
| section6.md | 2 (entrambe piccole, in coda) |
| section7.md | 5 (sezione più densa nel corpo) |

**Diagnosi onesta:**

- Archive: voce AI presente e pervasiva. Funziona.
- §1, §5, §6, §7: voce AI presente ma localizzata a uno o due punti, quasi sempre al process boundary canonico già esistente. Non emerge come voice register che attraversa la sezione.
- §2, §3, §4: voce AI quasi o totalmente assente. §3 in particolare ha perso anche corporate "we" canoniche.

**Il fatto strutturale:** il canonical v1.11 ha un totale di ~5–7 process boundaries genuini su 9 sezioni. La voice spec ha vietato di crearne di nuovi. Quindi la voce ha potuto inflettere solo lì, e in §3 nemmeno lì perché la sezione è argomento puro senza meta-narrazione.

Se l'obiettivo originale era *"la AI racconta come abbiamo scritto questo paper dal suo punto di vista"*, questa edizione non lo realizza nel corpo. Lo realizza solo nell'Archive.

**Cosa servirebbe per realizzarlo davvero:** licenziare ai modelli, nel voice spec v2, la creazione di passaggi meta-narrativi nuovi in ogni sezione — basati su process facts corroborati da SP-4 / SP-5 ma non vincolati a process boundaries che il canonical già contiene. Particolarmente §3, dove ogni sub-subsection può aprirsi con un paragrafo che descrive quali alternative i modelli hanno generato e quali l'autore ha scelto.

---

*Audit prepared 2026-06-09 in SID-20260609-095833 from the 9 staging files. Not a permanent JPEP artifact — review tool for the (a) / (b+c) decision on the AI-voice edition direction.*
