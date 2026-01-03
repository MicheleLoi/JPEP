---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Technical Guide"
chunk: "1_yaml_problema_collegamenti"
topic: "YAML metadata: il problema dei collegamenti non automatici"
---

# YAML Metadata in Obsidian: Il Problema dei Collegamenti

## Il Problema Fondamentale

**Obsidian NON interpreta automaticamente i "metadati di connessione" come collegamenti**, a meno che non siano espressi in formato che Obsidian capisce.

Se i tuoi metadati sono solo testo strutturato, devi adattare i file o usare plugin.

## Cosa Obsidian Riconosce Automaticamente

### 1. Link Wiki-style (sempre nativi)

```markdown
[[NomeNota]]
```

✅ Compaiono nei backlink  
✅ Compaiono nel grafo  
✅ Non serve alcuna configurazione

### 2. Link Markdown standard

```markdown
[descrizione](NomeNota.md)
```

✅ Funzionano  
⚠️ Meno integrati (meno usati in Obsidian)

### 3. Tag

```markdown
#epistemic-trace
```

✅ Indicizzati  
✅ Usabili in ricerche  
❌ NON sono backlink tra note specifiche

## Metadati YAML: Cosa NON Funziona

### Esempio tipico (NON crea collegamenti)

```yaml
---
source_chat: 4.7.3
influences:
  - 5.3.1
  - 5.2.2
document_type: Epistemic Trace
---
```

**Risultato:**
- ❌ NON crea collegamenti
- ❌ NON appare nei backlink
- ❌ NON compare nel grafo

**Perché:** Per Obsidian questo è solo testo strutturato, non relazioni.

## Proprietà Annidate: Problema di Rendering

### ❌ Problematico

```yaml
derived_from:
  - type: Modification Log
    id: 4.2.4
    section: Section II
```

**Problemi:**
- Rendering difficile in Dataview
- Non sempre leggibile nelle proprietà Obsidian
- Query complesse

### ✅ Soluzione: Proprietà Flat

```yaml
derived_from_artifact_type: "Modification Log"
derived_from_artifact_id: "4.2.4"
derived_from_section: "Section II"
```

**Benefici:**
- ✅ Obsidian/Dataview friendly
- ✅ Indicizzabile, filtrabile, visualizzabile
- ✅ Query semplici possibili

**Esempio query:**
```dataview
LIST FROM ""
WHERE derived_from_artifact_type = "Modification Log"
```

## Come Trasformare Metadati in Collegamenti Reali

### Metodo 1: Metadati con Wiki-link (consigliato)

```yaml
---
influences:
  - [[5.3.1_Artifact_ontology_expansion]]
  - [[5.2.2_PDL_section_vii]]
---
```

✅ Obsidian li tratta come link reali  
✅ Compaiono in backlink e grafo  
✅ Soluzione più semplice e robusta

### Metodo 2: Plugin Dataview

```yaml
---
influences:
  - 5.3.1
  - 5.2.2
---
```

Con query Dataview:
```dataview
LIST FROM ""
WHERE contains(influences, "5.3.1")
```

✅ Vedi tutti i file collegati logicamente  
❌ Non sono backlink "nativi"  
➡️ Ottimo per sistemi complessi (ontologie, log)

### Metodo 3: Ibrido (best practice per sistemi complessi)

**YAML = semantica per query**  
**Wiki-link nel body = navigazione umana**

```yaml
---
document_type: Epistemic Trace
influences:
  - 5.3.1
  - 5.2.2
---

## Connessioni
- Influenza: [[5.3.1_Artifact_ontology_expansion]]
- Continua: [[4.7.4_PreliminaryChat_2]]
```

✅ Chiarezza concettuale  
✅ Massima compatibilità  
✅ Perfetto per archivi metodologici

## Conclusione

**Regola d'oro:** Obsidian non deduce relazioni dai metadati "concettuali". Devi:

1. **Usare wiki-links nei metadati YAML**, oppure
2. **Usare Dataview per query**, oppure
3. **Generare sezione "Connections" automatica con script Python**

La terza opzione è la più potente per sistemi di documentazione complessi.
