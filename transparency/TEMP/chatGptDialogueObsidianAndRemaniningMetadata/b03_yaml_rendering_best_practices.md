---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Technical Guide"
chunk: "3_yaml_rendering_best_practices"
topic: "YAML rendering: best practices per Obsidian"
---

# YAML Rendering: Best Practices per Obsidian

## Il Problema del Rendering Instabile

Obsidian e Dataview possono avere problemi con YAML mal formattato:
- Virgole finali negli array
- Parentesi e due-punti non quotati
- Proprietà annidate complesse

**Risultato:** Liste non visualizzate, query che falliscono, proprietà ignorate.

## Regole d'Oro per YAML Obsidian-Safe

### Regola 1: Niente Virgole Finali

#### ❌ Sbagliato

```yaml
inputs:
  - 4.4.5 ("Section VIII guidance"),
  - 4.7.3 (preliminary chat 1),
```

**Problema:** Virgola finale dopo ogni item.

#### ✅ Corretto

```yaml
inputs:
  - "4.4.5 (Section VIII guidance)"
  - "4.7.3 (preliminary chat 1)"
```

### Regola 2: Quota Caratteri Speciali

**Caratteri che richiedono quotatura:**
- Due-punti `:`
- Parentesi `( )`
- Virgolette interne `"` `'`
- Slash `/`

#### ✅ Sempre sicuro

```yaml
key_guidance_inputs:
  - "4.4.4 (Core principle: the paper embodies its own argument)"
  - "4.4.5 (Section VIII guidance)"
```

### Regola 3: Proprietà Flat, Non Annidate

#### ❌ Problematico

```yaml
derived_from:
  - type: Modification Log
    id: 4.2.4
    section: Section II
```

**Problemi:**
- Non indicizzabile facilmente
- Rendering instabile
- Query complesse

#### ✅ Obsidian-friendly

```yaml
derived_from_artifact_type: "Modification Log"
derived_from_artifact_id: "4.2.4"
derived_from_section: "Section II"
```

**Benefici:**
- Query semplici: `WHERE derived_from_artifact_type = "Modification Log"`
- Visualizzabile nelle proprietà
- Nessun parsing ambiguo

### Regola 4: Array di Stringhe Semplici

#### ✅ Sempre funziona

```yaml
sections_affected:
  - "Introduction"
  - "Section 6"

input_artifacts:
  - "4.4.4"
  - "4.4.5"
  - "4.7.3"
```

## Separare Riferimenti da Descrizioni

### ❌ Problema Comune: Misto

```yaml
inputs:
  - 4.4.5 ("Section VIII guidance")
  - 4.7.3 (preliminary chat 1)
  - 4.1 (complete prompt)
```

**Problemi:**
- Mescola ID + testo libero
- Non facilmente linkabile `[[...]]`
- Query difficili o impossibili

### ✅ Soluzione 1: Due Campi Separati

```yaml
input_artifacts:
  - "4.4.4"
  - "4.4.5"
  - "4.7.3"

input_notes:
  4.4.4: "Core principle"
  4.4.5: "Section VIII guidance"
  4.7.3: "Preliminary chat 1"
```

**Benefici:**
- `input_artifacts` → lista pulita, queryabile
- `input_notes` → spiegazione umana opzionale

**Query esempio:**
```dataview
LIST FROM ""
WHERE contains(input_artifacts, "4.4.5")
```

### ✅ Soluzione 2: Note nel Body

**YAML minimale:**
```yaml
input_artifacts:
  - "4.4.4"
  - "4.4.5"
```

**Nel documento:**
```markdown
## Input Rationale
- **4.4.4** — Core principle
- **4.4.5** — Section VIII guidance
```

**Quando usare:**
- File con molte descrizioni
- Note lunghe che appesantirebbero YAML
- Approccio "editorialmente pulito"

## Template Sicuro Standard

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"
title: "Document title"

sections_affected:
  - "Section 1"
  - "Section 2"

source_chat_name: "Chat name"
source_chat_id: "unique-id"
model: "Claude Sonnet 4.5"
date: "2025-10-15"

status: "complete"
---
```

## Checklist Pre-Commit

Prima di salvare YAML:

- [ ] Nessuna virgola finale negli array
- [ ] Valori con `:` o `()` sono quotati
- [ ] Nessuna proprietà annidata complessa
- [ ] Array contengono solo stringhe semplici
- [ ] Chiavi sono flat (no `.` nei nomi)
- [ ] Date in formato ISO (YYYY-MM-DD)

## Quando Quotare: Regola Pratica

**Sempre quota se contiene:**
- `:` → "Section 2: title"
- `()` → "4.4.5 (guidance)"
- `,` → "inputs, outputs"
- `/` → "input/output"
- `'` o `"` → "it's important"

**Regola generale:** Se in dubbio, quota tutto.

## Errori Comuni da Evitare

### Errore 1: Liste con oggetti inline

```yaml
# ❌ NON fare
inputs:
  - {id: 4.4.5, desc: "guidance"}
```

```yaml
# ✅ Usa flat
input_id_1: "4.4.5"
input_desc_1: "guidance"
```

### Errore 2: Valori multi-riga non quotati

```yaml
# ❌ NON fare
description: This is a long
  description spanning
  multiple lines
```

```yaml
# ✅ Usa blocco o quota
description: "This is a long description spanning multiple lines"
```

### Errore 3: Booleani/numeri non quotati quando ambigui

```yaml
# ⚠️ Ambiguo
status: complete

# ✅ Esplicito
status: "complete"
```

## Verifica Rendering

Dopo aver salvato YAML:

1. Apri nota in Obsidian
2. Controlla pannello proprietà (source mode)
3. Testa query Dataview se usi plugin
4. Verifica che liste si visualizzino correttamente

Se qualcosa non appare: probabilmente un problema di quotatura.

## Conclusione

**Principio fondamentale:** YAML è per macchine, Markdown è per umani.

Mantieni YAML:
- ✅ Minimale
- ✅ Flat
- ✅ Quotato quando necessario
- ✅ Array semplici

E metti descrizioni lunghe nel body del documento.
