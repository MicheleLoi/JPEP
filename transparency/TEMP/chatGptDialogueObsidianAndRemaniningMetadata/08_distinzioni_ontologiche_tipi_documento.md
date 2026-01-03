---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Conversation Extract"
chunk_number: 8
topic: "Distinzioni ontologiche tra tipi di documenti"
---

# Distinzioni Ontologiche: Pattern Summary vs Process Note

## Problema: non tutti i documenti sono "puri"

Un documento può sembrare un Pattern Summary ma avere funzione diversa. Serve precisione ontologica per evitare categorizzazioni sbagliate.

## Pattern Summary (Type 4) - Standard

### Caratteristiche

- **Funzione:** Estrarre pattern argomentativi o metodologici
- **Origine:** Derivato da Modification Logs
- **Focus:** "Cosa ha funzionato" dal punto di vista contenutistico
- **Chat:** Può avere o non avere source_chat_id

### YAML tipico

```yaml
---
document_type: "Pattern Summary"

pattern_scope: "Old Section X (now Section Y)"
derived_from_artifact: "4.2.X_ModificationLog"

source_chat_name: "..."
source_chat_id: "..."
status: "complete"
---
```

## Process Note - Variante riflessiva

### Caratteristiche

- **Funzione:** Documentare processo e auto-correzione AI
- **Origine:** Derivato da Modification Logs con focus metacognitivo
- **Focus:** "Come si è arrivati a questo risultato" (trasparenza procedurale)
- **Funzione normativa:** Dimostra il metodo (non solo lo descrive)

### Esempio concreto: Section IV

**Process Note su Section IV** documenta:
- MOD-20: AI identifies epistemic overreach (auto-correzione)
- MOD-21: Two rounds of redundancy elimination
- **Claim metodologico:** "This transparency models what the paper advocates"

### YAML per Process Note

```yaml
---
document_type: "Process Note"
document_role: "Pattern extraction and methodological transparency"

process_scope: "Old Section IV (now Section 2)"
section_final_number: 2

derived_from_artifact: "4.2.4_ModificationLog_Section_IV"
derived_from_process:
  - "MOD-20 (AI identification of epistemic overreach)"
  - "MOD-21 (two rounds of redundancy elimination)"

methodological_claim: "Transparency of AI self-correction as epistemic signal"
status: "complete"
---
```

### Differenze chiave

| Aspetto | Pattern Summary | Process Note |
|---------|----------------|--------------|
| **Focus** | Contenuto/argomenti | Processo/metacognizione |
| **Funzione** | Estrazione lezioni | Dimostrazione metodologica |
| **Valore** | Riuso pattern | Trasparenza epistemica |
| **Origine** | Mod Log (output) | Mod Log (procedura) |

## Relazioni non causali: evitare ambiguità

### Problema con "used_in"

```yaml
used_in_artifact:
  - 4.4.9_Section_Guidance
```

❌ **Problema:** Suggerisce causalità downstream (A alimenta B)

### Soluzioni alternative

```yaml
# Opzione 1: Documenta processo iniziato altrove
documents_process_initiated_by:
  - "4.4.9_Section_Guidance"

# Opzione 2: Contesto non causale
process_context_artifact:
  - "4.4.9_Section_Guidance"

# Opzione 3: Descrittiva (più sicura)
process_context: "Consolidation of Sections II–IV per Section Guidance 4.4.9"
```

**Regola:** Se la relazione NON è input/output operativo, usa linguaggio non-causale.

## Section Guidance: ulteriori distinzioni

### Section Guidance "pura"

**Caratteristiche:**
- Coordinamento strutturale/editoriale
- NON nasce da singola chat
- Deriva da riflessione multi-artefatto

```yaml
---
document_type: "Section Guidance"
guidance_scope: "Consolidation of multiple sections"

role_in_process: "Editorial coordination and tone alignment"
status: "complete"
---
```

### Section Guidance chat-direct

**Caratteristiche:**
- Prodotta direttamente in chat
- Artefatto originale MD dalla conversazione
- Può essere rinominata per struttura SP

```yaml
---
document_type: "Section Guidance"

original_artifact_filename: "section_guidance_section9"
original_artifact_title: "Section Guidance – Section 9"

source_chat_name: "JPEP section 8 writing"
source_chat_id: "..."

provenance_status: "chat_direct_original_md_renamed_for_sp4"
status: "complete"
---
```

## Regola generale

> Il document_type deve riflettere la **funzione epistemica**, non solo la posizione nella cartella.

**Conseguenze:**
- Non tutto in `4.3_PatternSummaries/` è un Pattern Summary "puro"
- Alcuni possono essere Process Notes
- Altri possono essere derivati di secondo ordine

**Beneficio:** Query e analisi successive sono semanticamente corrette.

## Checklist rapida

Prima di assegnare `document_type`, chiedi:

1. **Questo documento estrae pattern argomentativi?** → Pattern Summary
2. **Documenta processo/auto-correzione con valore metodologico?** → Process Note
3. **Coordina struttura/editing multi-sezione?** → Section Guidance
4. **Documenta modifiche forensicamente?** → Modification Log
5. **Traccia sviluppo conversazionale preliminare?** → Epistemic Trace

Rispondere correttamente garantisce ontologia pulita e query affidabili.
