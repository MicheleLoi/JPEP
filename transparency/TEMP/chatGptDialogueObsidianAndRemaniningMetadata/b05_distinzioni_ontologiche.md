---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Technical Guide"
chunk: "5_distinzioni_ontologiche"
topic: "Distinzioni ontologiche: document_type precisi"
---

# Distinzioni Ontologiche: Document Type Precisi

## Il Problema della Categorizzazione Imprecisa

Non tutti i documenti in una cartella `PatternSummaries/` sono necessariamente Pattern Summary "puri". Serve precisione ontologica.

**Conseguenza:** Se categorizzi male, le query Dataview restituiscono risultati sbagliati.

## Pattern Summary (Type 4) - Standard

### Caratteristiche

**Funzione:** Estrarre pattern argomentativi o metodologici  
**Origine:** Derivato da Modification Logs  
**Focus:** "Cosa ha funzionato" - contenuto  
**Chat:** Può avere o non avere source_chat_id

### YAML Tipico

```yaml
---
document_type: "Pattern Summary"

pattern_scope: "Old Section X (now Section Y)"
section_final_number: Y

derived_from_artifact: "4.2.X_ModificationLog"

source_chat_name: "JPEP section X writing"
source_chat_id: "..."
model: "Claude Sonnet 4.5"
date: "2025-XX-XX"

status: "complete"
---
```

### Esempio Concreto

**File:** `4.3.1_Section_II_Pattern_Summary.md`

**Contenuto tipico:**
- Pattern emersi durante drafting Section II
- Lezioni su struttura argomentativa
- Strategie che hanno funzionato

## Process Note - Variante Riflessiva

### Caratteristiche

**Funzione:** Documentare processo e auto-correzione AI  
**Origine:** Derivato da Modification Logs con focus metacognitivo  
**Focus:** "Come si è arrivati" - procedura  
**Claim:** Dimostra il metodo (non solo lo descrive)

### Esempio Concreto: Section IV

**File:** `4.3.3_Section_IV_Process_Note.md`

**Process Note documenta:**

```markdown
## MOD-20: AI Identifies Epistemic Overreach

During drafting, Claude independently flagged 
that claim X was too strong given evidence Y.

## MOD-21: Two Rounds of Redundancy Elimination

First pass: paragraph-level cuts
Second pass: sentence-level refinement

## Methodological Claim

This transparency models what the paper advocates:
making AI decision-making visible for evaluation.
```

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

### Tabella Comparativa

| Aspetto | Pattern Summary | Process Note |
|---------|----------------|--------------|
| **Focus** | Contenuto/argomenti | Processo/metacognizione |
| **Funzione** | Estrazione lezioni | Dimostrazione metodologica |
| **Valore** | Riuso pattern | Trasparenza epistemica |
| **Origine** | Mod Log (output) | Mod Log (procedura) |
| **Claim** | "Cosa funziona" | "Come è stato fatto" |

## Section Guidance: Ulteriori Distinzioni

### Section Guidance "Pura" (editoriale)

**Caratteristiche:**
- Coordinamento strutturale/editoriale
- NON nasce da singola chat
- Deriva da riflessione multi-artefatto

**YAML:**
```yaml
---
document_type: "Section Guidance"

guidance_scope: "Consolidation of multiple sections"
sections_affected:
  - "Section 2"
  - "Section 3"

role_in_process: "Editorial coordination"
status: "complete"
---
```

**Nota:** NO source_chat_id (è sintesi, non conversazione).

### Section Guidance Chat-Direct (originale)

**Caratteristiche:**
- Prodotta direttamente in chat come MD
- Artefatto originale dalla conversazione
- Può essere rinominata per struttura SP4

**YAML:**
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

## Relazioni Non Causali: Evitare Ambiguità

### Problema con "used_in"

```yaml
used_in_artifact:
  - "4.4.9_Section_Guidance"
```

❌ **Problema:** Suggerisce causalità downstream (A alimenta B come input).

### Soluzioni Alternative

```yaml
# Opzione 1: Documenta processo iniziato altrove
documents_process_initiated_by:
  - "4.4.9_Section_Guidance"

# Opzione 2: Contesto non causale
process_context_artifact:
  - "4.4.9_Section_Guidance"

# Opzione 3: Descrittiva (più sicura)
process_context: "Consolidation per Section Guidance 4.4.9"
```

**Regola:** Se la relazione NON è input→output operativo, usa linguaggio non-causale.

## Checklist di Classificazione

Prima di assegnare `document_type`, rispondi:

### 1. Questo documento estrae pattern argomentativi?
✅ → Pattern Summary

### 2. Documenta processo/auto-correzione con valore metodologico?
✅ → Process Note

### 3. Coordina struttura/editing multi-sezione?
✅ → Section Guidance (pura)

### 4. È artefatto originale MD da chat?
✅ → Section Guidance (chat-direct)  
**Aggiungi:** `provenance_status: "chat_direct_..."`

### 5. Documenta modifiche forensicamente?
✅ → Modification Log

### 6. Traccia sviluppo conversazionale preliminare?
✅ → Epistemic Trace

## Casi Ambigui: Come Decidere

### Caso 1: File in `4.3_PatternSummaries/` ma contenuto riflessivo

**Sintomo:** Parla più di "come" che di "cosa".

**Soluzione:**
```yaml
document_type: "Process Note"
```

**Non cambiare cartella** (pragmatico), ma correggi type.

### Caso 2: Guidance che sembra Pattern

**Sintomo:** Estrae lezioni ma è directive (non descrittiva).

**Test:** Contiene "Objective" / "Required Input" / "Do this"?

**Se sì:** Section Guidance (anche se estrae pattern nel processo).

### Caso 3: Mod Log che è anche Epistemic Trace

**Sintomo:** Documenta processo MA è preliminare (non post-hoc).

**Regola:** Data è decisiva.
- **Prima del drafting:** Epistemic Trace
- **Dopo completion:** Modification Log

## Regola Generale

> Il document_type deve riflettere la **funzione epistemica**, non solo la posizione nella cartella.

**Benefici:**
- ✅ Query semanticamente corrette
- ✅ Distinzioni chiare tra ruoli
- ✅ Sistema auto-documentante

## Query Dataview per Verifica

```dataview
# Tutti i Process Note
LIST document_role
FROM ""
WHERE document_type = "Process Note"

# Pattern Summary vs Process Note
TABLE document_type, pattern_scope, process_scope
FROM "4.3_PatternSummaries"

# Section Guidance per tipo
TABLE provenance_status
FROM ""
WHERE document_type = "Section Guidance"
```

## Conclusione

Categorizzazione precisa è foundational:
- Senza, query falliscono
- Con, sistema è interrogabile correttamente
- Vale la pena investire tempo nella classificazione iniziale
