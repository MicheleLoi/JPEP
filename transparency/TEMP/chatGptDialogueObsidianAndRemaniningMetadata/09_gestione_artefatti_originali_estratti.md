---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Conversation Extract"
chunk_number: 9
topic: "Gestione artefatti originali vs estratti"
---

# Gestione Artefatti Originali vs Estratti

## Il problema dello split editoriale

Durante la riorganizzazione di un progetto complesso:
1. Artefatti originali sono prodotti direttamente in chat (MD chat-direct)
2. Vengono poi splittati/estratti per adattarsi alla struttura del progetto
3. La provenienza può diventare ambigua

**Rischio:** perdere traccia di quale è l'artefatto canonico.

## Esempio concreto: Section Guidance

### Artefatto originale (chat-direct)

**File:** `section_guidance_1_and_6.md`

**Contenuto:**
- Section Guidance per Introduction (Section 1)
- Section Guidance per Section 6
- Tutto in un unico artefatto MD
- Prodotto direttamente nella chat "JPEP whole paper audit"

### Estratti derivati (post-processing)

**File 1:** `4.4.10_Section_Guidance_Introduction_tone_changes`
- Contiene solo la parte Introduction
- Rinominato per struttura SP4

**File 2:** `4.4.8_Section_6_Revision_Guidance`
- Contiene solo la parte Section 6
- Rinominato per struttura SP4

## Strategia: artefatti canonici in SP5

### Principio

**SP5 = Note** contenente artefatti canonici originali

**SP4 = Process Documentation** contenente estratti organizzati

### Struttura consigliata

```
SP5_DevelopmentRecords/
├── 5.3_Notes_Type11/
│   ├── 5.3.12_section_guidance_1_and_6.md  ← CANONICO
│   └── ...
```

```
SP4_ProcessDocumentation/
├── 4.4_SectionGuidance/
│   ├── 4.4.8_Section_6_Revision_Guidance.md  ← ESTRATTO
│   ├── 4.4.10_Introduction_tone_changes.md   ← ESTRATTO
│   └── ...
```

## YAML per artefatto canonico (SP5)

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

status: "complete"
---
```

## YAML per estratto (SP4)

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"

title: "Section Guidance: Introduction (tone changes) and Section IV"

sections_affected:
  - "Introduction"
  - "Section IV"

source_artifact_original: "5.3.12_section_guidance_1_and_6.md"

source_chat_name: "JPEP whole paper audit"
source_chat_id: "e5ec43be-0e81-4fdb-946a-4286bfc743d6"
model: "Claude Sonnet 4.5"
date: "2025-10-18"

provenance_status: "extracted_from_chat_direct_artifact"
status: "complete"
---
```

## Campi chiave per tracciabilità

### Nel canonico (SP5)

```yaml
note_type: "Canonical source artifact (chat-direct)"

related_extracted_artifacts:
  - "4.4.10_Section_Guidance_Introduction_tone_changes"
  - "4.4.8_Section_6_Revision_Guidance"
```

### Nell'estratto (SP4)

```yaml
source_artifact_original: "5.3.12_section_guidance_1_and_6.md"
provenance_status: "extracted_from_chat_direct_artifact"
```

## Benefici del sistema

### 1. Nessuna perdita di informazione

Artefatto originale completo resta disponibile come riferimento.

### 2. Flessibilità organizzativa

Puoi riorganizzare SP4 senza toccare SP5.

### 3. Tracciabilità bidirezionale

- Da estratto → canonico (via `source_artifact_original`)
- Da canonico → estratti (via `related_extracted_artifacts`)

### 4. Reversibilità

Se uno split si rivela sbagliato, puoi sempre risalire all'originale.

## Caso speciale: artefatti rinominati (non splittati)

### Quando NON c'è stato split

Artefatto chat-direct semplicemente rinominato per SP4.

**Esempio:**
- Originale: `feedforward_guidance_conclusion.md`
- Rinominato: `4.4.7_For_Conclusion.md`

### YAML appropriato

```yaml
---
document_type: "Section Guidance"

title: "4.4.7 From Section IX (now 7) to Conclusion"

original_artifact_filename: "feedforward_guidance_conclusion"
original_artifact_title: "Feed-Forward Guidance - Conclusion"

source_chat_name: "JPEP section 9 writing"
source_chat_id: "..."

provenance_status: "chat_direct_original_md_renamed_for_sp4"
status: "complete"
---
```

**Nota:** Qui NON serve `source_artifact_original` perché non c'è un file separato in SP5.

## Provenance status: vocabolario controllato

```yaml
# Artefatto originale mai modificato
provenance_status: "chat_direct_original_md"

# Artefatto rinominato ma non modificato nel contenuto
provenance_status: "chat_direct_original_md_renamed_for_sp4"

# Estratto da artefatto più grande
provenance_status: "extracted_from_chat_direct_artifact"

# Derivato da più fonti/iterazioni
provenance_status: "derived_from_multiple_sources"

# Provenienza da verificare
provenance_status: "source_chat_unknown_verify"
```

## Workflow pratico

### Quando trovi un possibile split

1. **Verifica:** Confronta testi per confermare corrispondenza
2. **Salva originale in SP5:** Se non già presente, aggiungi come 5.3.X
3. **Aggiorna YAML estratto:** Aggiungi `source_artifact_original`
4. **Aggiorna YAML canonico:** Aggiungi `related_extracted_artifacts`
5. **Documenta:** Note su perché è stato fatto lo split

### Checklist finale

- [ ] Artefatto originale salvato in SP5?
- [ ] YAML estratto punta al canonico?
- [ ] YAML canonico lista gli estratti?
- [ ] Provenance status corretto?
- [ ] Chat ID presente in entrambi?

Questo garantisce che la catena di provenienza sia sempre ricostruibile.
