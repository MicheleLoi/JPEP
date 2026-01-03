---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Technical Guide"
chunk: "8_esempi_completi_yaml"
topic: "Esempi completi di YAML per tutti i casi"
---

# Esempi Completi di YAML per Tutti i Casi

## Pattern Summary - Singola Chat

### Scenario
Pattern estratto da Section V, derivato da un solo Modification Log con una chat.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Pattern Summary"

pattern_scope: "Old Section V – Why Engage (now final Section 3)"
section_final_number: 3

derived_from_artifact: "4.2.6_ModificationLog_Section_V__S03"

source_chat_name: "JPEP section 5 writing"
source_chat_id: "240f00db-62f9-4dcf-86f3-de1257562310"
model: "Claude Sonnet 4.5"
date: "2025-10-14"

status: "complete"
---
```

## Pattern Summary - Multi-Chat (Consolidation)

### Scenario
Pattern che consolida Section II e III, ciascuna con chat distinta.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Pattern Summary"

pattern_scope: "Sections II–III (later consolidated into Section 2)"
section_final_number: 2

derived_from_sections:
  - "Old Section II – Incentives"
  - "Old Section III – Contiguous Approaches"
derived_from_artifact_type: "Modification Logs"

source_chat_name:
  - "JPEP section 2 writing"
  - "JPEP section 3 writing"
source_chat_id:
  - "4177422b-27c3-44d4-a52e-f065de4e72ab"
  - "6e92907a-03f7-413f-b99f-2983f8f44b22"

model: "Claude Sonnet 4.5"
date_range: "2025-10-12 → 2025-12-10"

status: "complete"
---
```

## Process Note

### Scenario
Documentazione processo con auto-correzione AI (Section IV).

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Process Note"
document_role: "Pattern extraction and methodological transparency"

process_scope: "Old Section IV – Unfair Reviews (now Section 2)"
section_final_number: 2

derived_from_artifact: "4.2.4_ModificationLog_Section_IV__S02"
derived_from_process:
  - "MOD-20 (AI identification of epistemic overreach)"
  - "MOD-21 (two rounds of redundancy elimination)"

documents_process_initiated_by:
  - "4.4.9_Section_Guidance_Consolidate_Section_2"

methodological_claim: "Transparency of AI self-correction as epistemic signal"
status: "complete"
---
```

**Nota:** NO source_chat_id (è già nel ModLog derivato).

## Section Guidance - Chat-Direct (Original MD)

### Scenario
Guidance prodotta direttamente come MD in chat, rinominata per SP4.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"

title: "4.4.6 For Section IX (now 7) from Section VIII"

sections_affected:
  - "Section 7"

original_artifact_filename: "section_guidance_section9"
original_artifact_title: "Section Guidance – Section 9"

source_chat_name: "JPEP section 8 writing"
source_chat_id: "3b4ee4d7-939e-4cb7-8830-571952d5b5a4"
model: "Claude Sonnet 4.5"
date: "2025-10-15"

provenance_status: "chat_direct_original_md_renamed_for_sp4"
status: "complete"
---
```

## Section Guidance - Estratta da Canonico

### Scenario
Guidance estratta da artefatto più grande salvato in SP5.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"

title: "Section 6 Revision Guidance"

sections_affected:
  - "Section 6"

source_artifact_original: "5.3.12_section_guidance_1_and_6.md"

source_chat_name: "JPEP whole paper audit"
source_chat_id: "e5ec43be-0e81-4fdb-946a-4286bfc743d6"
date: "2025-10-18"
model: "Claude Sonnet 4.5"

provenance_status: "extracted_from_chat_direct_artifact"
status: "complete"
---
```

## Section Guidance - Derivata (Non Chat-Direct)

### Scenario
Guidance che emerge dall'audit, implementata poi in altra chat.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"

title: "Consolidate Section 2: Systemic Barriers"

sections_affected:
  - "Section 2"
  - "Section 3"
  - "Section 4"

source_chat_name: "JPEP whole paper audit"
source_chat_id: "e5ec43be-0e81-4fdb-946a-4286bfc743d6"
date: "2025-10-18"

related_modification_log: "4.2.5_ModificationLog_Consolidation"

status: "complete"
---
```

**Nota:** ModLog separato documenta l'execution in altra chat.

## Modification Log - Fase Singola

### Scenario
Drafting e revisione in una chat, fase unica.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Modification Log"

section_scope: "Old Section V – Why Engage (now Section 3)"
section_final_number: 3

source_chat_name: "JPEP section 5 writing"
source_chat_id: "240f00db-62f9-4dcf-86f3-de1257562310"
model: "Claude Sonnet 4.5"
date: "2025-10-14"

status: "complete"
---
```

## Modification Log - Multi-Fase

### Scenario
Drafting in una chat, revisione post-editorial in altra chat.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Modification Log"

section_scope: "Old Section IV – Unfair Reviews (now Section 2)"
section_final_number: 2

guided_by_artifact: "4.4.9_Section_Guidance_Consolidate_Section_2"

phase1_description: "Initial drafting and redundancy elimination"
phase1_chat_name: "JPEP section 4 writing"
phase1_chat_id: "17c34bca-3050-4825-908a-599adfa9f8c0"
phase1_model: "Claude Sonnet 4.5"
phase1_date: "2025-10-12"

phase2_description: "Post-editorial logical correction"
phase2_chat_name: "JPEP post-editorial review of Section 4[2]"
phase2_chat_id: "277c8d57-07af-45b2-9a83-a36a6d9b4d0d"
phase2_model: "Claude Sonnet 4.5"
phase2_date: "2025-10-18"

provenance_status: "verified_distinct_chats"
status: "complete"
---
```

## Canonical Artifact (SP5)

### Scenario
Artefatto originale chat-direct salvato in SP5, con estratti in SP4.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP5"
document_type: "Note"
note_type: "Canonical source artifact (chat-direct)"

title: "Section Guidance: Introduction (1) and Section 6"

scope_sections:
  - "Introduction"
  - "Section 6"

source_chat_name: "JPEP whole paper audit"
source_chat_id: "e5ec43be-0e81-4fdb-946a-4286bfc743d6"
date: "2025-10-18"
model: "Claude Sonnet 4.5"

related_extracted_artifacts:
  - "4.4.10_Introduction_tone_changes"
  - "4.4.8_Section_6_Revision_Guidance"

status: "complete"
---
```

## Epistemic Trace

### Scenario
Conversazione preliminare che precede drafting formale.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Epistemic Trace"

trace_scope: "Preliminary design conversation for Section VIII methodology"
trace_number: "4.7.3"

source_chat_name: "JPEP section 8 preliminary"
source_chat_id: "fb6251ae-9ce3-4e5e-8b3f-4ef67aa42092"
model: "Claude Sonnet 4.5"
date: "2025-10-12"

influenced_artifacts:
  - "4.4.4_Section_VIII_Guidance"
  - "5.2.1_PDL_Section_VIII"

status: "complete"
---
```

## Index / Structural (Minimale)

### Scenario
File strutturale di navigazione, YAML leggero.

### YAML Completo

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Index"
index_scope: "Pattern Summaries for all sections"
status: "maintained"
---
```

## File Senza YAML (Opzionale)

### Quando accettabile

**Casi OK senza YAML:**
- `README.md` (documentazione)
- `_PREAMBLE.md` (introduttivo)
- File temporanei/draft

**Non accettabile senza YAML:**
- Artefatti di processo
- Documenti citati da altri
- Qualunque cosa con source_chat_id

## Provenance Status: Reference Rapido

```yaml
# Originale MD dalla chat
provenance_status: "chat_direct_original_md"

# Originale rinominato
provenance_status: "chat_direct_original_md_renamed_for_sp4"

# Estratto da più grande
provenance_status: "extracted_from_chat_direct_artifact"

# Multi-source
provenance_status: "derived_from_multiple_sources"

# Multi-fase verificata
provenance_status: "verified_distinct_chats"

# Singola chat con audit upstream
provenance_status: "guidance_from_single_chat"

# Da verificare
provenance_status: "source_chat_unknown_verify"
```

## Checklist per Ogni Tipo

### Prima di salvare YAML, verifica:

**Tutti:**
- [ ] Nessuna virgola finale
- [ ] Caratteri speciali quotati
- [ ] Proprietà flat
- [ ] `status` presente

**Con chat:**
- [ ] `source_chat_id` verificato
- [ ] `date` in formato ISO
- [ ] `model` specificato

**Derivati:**
- [ ] `derived_from_*` corretto
- [ ] NO duplicazione chat da originale
- [ ] `provenance_status` appropriato

**Multi-fase:**
- [ ] `phase1_*` / `phase2_*` completi
- [ ] Chat distinte verificate
- [ ] Date in ordine cronologico

## Conclusione

Questi template coprono tutti i casi principali. Per casi edge:

1. Parte dal template più simile
2. Adatta campi specifici
3. Verifica con query Dataview
4. Documenta eccezione se necessario

**Principio:** Meglio YAML minimale corretto che complesso incompleto.
