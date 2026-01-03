---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Conversation Extract"
chunk_number: 6
topic: "YAML best practices e problemi di rendering"
---

# YAML Best Practices per Obsidian

## Problema: rendering instabile

Obsidian (e Dataview) possono avere problemi di rendering con YAML mal formattato:
- Virgole finali negli array
- Parentesi e due-punti non quotati
- Proprietà annidate complesse

## Regole d'oro per YAML Obsidian-safe

### 1. Niente virgole finali

❌ **Sbagliato:**
```yaml
inputs:
  - 4.4.5 ("Section VIII guidance"),
  - 4.7.3 (preliminary chat 1),
```

✅ **Corretto:**
```yaml
inputs:
  - "4.4.5 (Section VIII guidance)"
  - "4.7.3 (preliminary chat 1)"
```

### 2. Quota tutto ciò che contiene caratteri speciali

**Caratteri che richiedono quotatura:**
- Due-punti `:`
- Parentesi `( )`
- Virgolette interne
- Slash `/`

✅ **Sempre sicuro:**
```yaml
key_guidance_inputs:
  - "4.4.4 (Core principle: the paper embodies its own argument)"
  - "4.4.5 (Section VIII guidance)"
```

### 3. Proprietà flat, non annidate

❌ **Problematico in Obsidian:**
```yaml
derived_from:
  - type: Modification Log
    id: 4.2.4
    section: Section II
```

✅ **Obsidian-friendly:**
```yaml
derived_from_artifact_type: "Modification Log"
derived_from_artifact_id: "4.2.4"
derived_from_section: "Section II"
```

**Benefici flat:**
- ✔ Indicizzabile in Dataview
- ✔ Visualizzabile nelle proprietà Obsidian
- ✔ Query semplici possibili
- ✔ Nessun problema di parsing

### 4. Array di stringhe semplici

✅ **Sempre funziona:**
```yaml
sections_affected:
  - "Introduction"
  - "Section 6"
```

✅ **Con ID:**
```yaml
input_artifacts:
  - "4.4.4"
  - "4.4.5"
  - "4.7.3"
```

## Separare riferimenti e descrizioni

### ❌ Problema comune

```yaml
inputs:
  - 4.4.5 ("Section VIII guidance")
  - 4.7.3 (preliminary chat 1)
  - 4.1 (complete prompt)
```

**Problemi:**
- Mescola ID + testo libero nello stesso item
- Non facilmente linkabile
- Query difficili

### ✅ Soluzione 1: Due campi separati

```yaml
input_artifacts:
  - "4.4.4"
  - "4.4.5"
  - "4.7.3"

input_notes:
  4.4.4: "Core principle – the paper embodies its own argument"
  4.4.5: "Section VIII guidance"
  4.7.3: "Preliminary chat 1"
```

**Benefici:**
- `input_artifacts` → lista pulita, queryabile
- `input_notes` → spiegazione umana
- Separazione funzioni chiara

### ✅ Soluzione 2: Note nel body

**YAML minimale:**
```yaml
input_artifacts:
  - "4.4.4"
  - "4.4.5"
  - "4.7.3"
```

**Nel documento:**
```markdown
## Input Rationale
- **4.4.4** — Core principle: the paper embodies its own argument
- **4.4.5** — Section VIII guidance
- **4.7.3** — Preliminary chat 1
```

## Template sicuro standard

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"
title: "Titolo del documento"

sections_affected:
  - "Section 1"
  - "Section 2"

source_chat_name: "Nome chat"
source_chat_id: "id-univoco"
model: "Claude Sonnet 4.5"
date: "2025-10-15"

status: "complete"
---
```

## Checklist pre-commit

Prima di salvare YAML, verifica:
- [ ] Nessuna virgola finale negli array
- [ ] Tutti i valori con `:` o `()` sono quotati
- [ ] Nessuna proprietà annidata complessa
- [ ] Array contengono solo stringhe semplici
- [ ] Tutte le chiavi sono flat (no `.` nei nomi chiave)

## Quando quotare (regola pratica)

**Sempre quota se il valore contiene:**
- Due-punti `:` (es. "Section 2: title")
- Parentesi `()` (es. "4.4.5 (guidance)")
- Virgole `,` (es. "inputs, outputs")
- Slash `/` (es. "input/output")
- Apici `'` o `"`

**Sicurezza generale:** se in dubbio, quota tutto.
