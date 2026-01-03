---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Conversation Extract"
chunk_number: 3
topic: "Metadati YAML e collegamenti automatici"
---

# Metadati YAML e Collegamenti in Obsidian

## Problema: Obsidian e i Metadati

Obsidian NON interpreta automaticamente i "metadati di connessione" come collegamenti, a meno che non siano espressi in formato che Obsidian capisce.

### Cosa Obsidian riconosce automaticamente

**1. Link wiki (sempre)**
```markdown
[[NomeNota]]
```
✔ compaiono nei backlink  
✔ compaiono nel grafo  
✔ non serve alcuna impostazione

**2. Link Markdown**
```markdown
[descrizione](NomeNota.md)
```
✔ funzionano  
❌ meno integrati (meno usati in Obsidian)

**3. Tag**
```markdown
#epistemic-trace
```
✔ indicizzati  
✔ usabili in ricerche e grafi  
❌ non sono backlink tra note specifiche

## Metadati YAML: cosa succede davvero

### Esempio tipico (NON funziona per collegamenti)

```yaml
---
source_chat: 4.7.3
influences:
  - 5.3.1
  - 5.2.2
document_type: Epistemic Trace
---
```

**Stato di default:**
- ❌ NON crea collegamenti
- ❌ NON appare nei backlink
- ❌ NON nel grafo

👉 Per Obsidian questo è solo testo strutturato, non relazioni.

## Come trasformare i metadati in collegamenti veri

### ✅ Metodo 1 — Metadati con wiki-link (consigliato)

```yaml
---
influences:
  - [[5.3.1_Artifact_ontology_expansion]]
  - [[5.2.2_PDL_section_vii]]
---
```

✔ ora Obsidian li tratta come link reali  
✔ compaiono in backlink e grafo  
✔ soluzione più semplice e robusta

### ✅ Metodo 2 — Plugin Dataview (potentissimo)

Con Dataview, i metadati diventano queryabili.

**Esempio:**
```yaml
---
influences:
  - 5.3.1
  - 5.2.2
---
```

**Query:**
```dataview
LIST FROM ""
WHERE contains(influences, "5.3.1")
```

✔ vedi tutti i file collegati logicamente  
❌ non sono backlink "nativi"  
➡ ottimo per sistemi complessi (ontologie, log, tracce)

### ✅ Metodo 3 — Ibrido (molto usato in sistemi complessi)

**YAML = semantica ufficiale** (macchine / query)  
**Wiki-link nel testo = navigazione umana**

**Esempio:**
```yaml
---
document_type: Epistemic Trace
influences:
  - 5.3.1
---

## Connessioni
- Influenza: [[5.3.1_Artifact_ontology_expansion]]
- Continua: [[4.7.4_PreliminaryChat_2]]
```

✔ chiarezza concettuale  
✔ massima compatibilità  
✔ perfetto per archivi metodologici

## Proprietà annidate e rendering

**⚠️ IMPORTANTE:** Obsidian è "picky" con le proprietà annidate.

**Problema con nested properties:**
```yaml
derived_from:
  - type: Modification Log
    id: 4.2.4
```
❌ rendering difficile in Dataview  
❌ non sempre leggibile nelle proprietà

**Soluzione: usare chiavi flat**
```yaml
derived_from_artifact_type: "Modification Log"
derived_from_artifact_id: "4.2.4"
```
✔ Obsidian / Dataview friendly  
✔ indicizzabile, filtrabile, visualizzabile  
✔ query semplici possibili

## Conclusione

- ❌ Obsidian non deduce relazioni dai metadati "concettuali"
- ✔ Mostra collegamenti solo se sono link espliciti
- 🔧 Devi modificare i file oppure usare Dataview
- 🧠 Per sistemi complessi: YAML flat + wiki-link = best practice
