---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Technical Guide"
chunk: "4_workflow_aggiungere_yaml"
topic: "Workflow pratico per aggiungere YAML frontmatter"
---

# Workflow Pratico: Aggiungere YAML Frontmatter ai File

## Principio Guida

> Non tutti i file devono avere lo stesso YAML.

**Esempi:**
- `_INDEX.md` → YAML molto leggero (o nessuno)
- Section Summary → YAML senza source_chat_id
- Epistemic Trace → YAML completo con chat

**Questo evita di "mentire" al sistema.**

## Script Diagnostico: Trovare File Senza YAML

### check_missing_yaml.py

```python
#!/usr/bin/env python3
from pathlib import Path

def has_yaml_frontmatter(text: str) -> bool:
    if not text.startswith("---"):
        return False
    end = text.find("\n---", 3)
    return end != -1

def main(root: str = ".") -> None:
    root_path = Path(root).resolve()
    missing = []

    for p in root_path.rglob("*.md"):
        try:
            txt = p.read_text(encoding="utf-8")
        except Exception:
            missing.append(p)
            continue

        if not has_yaml_frontmatter(txt):
            missing.append(p)

    print(f"Scanned: {root_path}")
    print(f"Files without YAML: {len(missing)}\n")
    for p in sorted(missing):
        print(f"  - {p.relative_to(root_path)}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
```

### Uso

```bash
cd /path/to/vault
python check_missing_yaml.py .
```

**Output esempio:**
```
Scanned: /path/to/vault
Files without YAML: 38

  - SP4_ProcessDocumentation/4.3_PatternSummaries/4.3.1_Section_II.md
  - SP4_ProcessDocumentation/4.4_SectionGuidance/4.4.10_Introduction.md
  ...
```

## Metodo Operativo: Ciclo per Ogni File

### 1. Classificazione Rapida

Determina il tipo:
- **Pattern Summary** (Type 4)
- **Section Guidance** (Type 3)
- **Modification Log** (Type 2)
- **Process Note** (variante riflessiva)
- **Epistemic Trace** (Type 8)

### 2. Template YAML Appropriato

Scegli template basato su:
- Tipo documento
- Presenza di source_chat_id
- Complessità (singola fase vs multi-fase)

### 3. Verifica Chat ID

**Metodi:**
- Controllare Modification Log correlato
- Cercare nella chat con RAG di Claude
- Controllare documentazione esistente

**Domanda tipo per Claude:**
```
Can you identify the chat where we created 
[describe the artifact]? Please give chat name, 
chat ID, and date.
```

### 4. Tracking con Checklist

**File separato:** `_YAML_STATUS.md`

```markdown
## YAML Status Tracking

### 4.3 Pattern Summaries
- [x] 4.3.1 Section II
- [x] 4.3.2 Sections II–III
- [ ] 4.3.3 Section IV
- [ ] 4.3.4 Section V

### 4.4 Section Guidance
- [x] 4.4.9 Consolidate Section 2
- [ ] 4.4.10 Introduction tone
```

## Template per Categorie Comuni

### Pattern Summary (singola chat)

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Pattern Summary"

pattern_scope: "Old Section X (now Section Y)"
section_final_number: Y

derived_from_artifact: "4.2.X_ModificationLog"

source_chat_name: "Chat name"
source_chat_id: "chat-id"
model: "Claude Sonnet 4.5"
date: "2025-XX-XX"

status: "complete"
---
```

### Pattern Summary (multi-chat / consolidation)

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Pattern Summary"

pattern_scope: "Sections II–III (consolidated into Section 2)"
section_final_number: 2

derived_from_sections:
  - "Old Section II"
  - "Old Section III"

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

### Section Guidance (chat-direct)

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Section Guidance"

sections_affected:
  - "Section X"

source_chat_name: "Chat name"
source_chat_id: "chat-id"
date: "2025-XX-XX"

provenance_status: "chat_direct_original_md_renamed_for_sp4"
status: "complete"
---
```

### Modification Log (fase singola)

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Modification Log"

section_scope: "Section X description"
section_final_number: X

source_chat_name: "Chat name"
source_chat_id: "chat-id"
model: "Claude Sonnet 4.5"
date: "2025-XX-XX"

status: "complete"
---
```

### Modification Log (multi-fase)

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Modification Log"

section_scope: "Section X description"
section_final_number: X

phase1_description: "Initial drafting"
phase1_chat_name: "Chat name 1"
phase1_chat_id: "chat-id-1"
phase1_date: "2025-XX-XX"

phase2_description: "Post-editorial revision"
phase2_chat_name: "Chat name 2"
phase2_chat_id: "chat-id-2"
phase2_date: "2025-XX-XX"

provenance_status: "verified_distinct_chats"
status: "complete"
---
```

### Process Note

```yaml
---
project: "JPEP"
sp: "SP4"
document_type: "Process Note"
document_role: "Pattern extraction and methodological transparency"

process_scope: "Old Section X (now Section Y)"
section_final_number: Y

derived_from_artifact: "4.2.X_ModificationLog"
derived_from_process:
  - "MOD-20 (AI self-correction)"
  - "MOD-21 (redundancy elimination)"

methodological_claim: "Transparency as epistemic signal"
status: "complete"
---
```

## Strategie di Prioritizzazione

### Alto Valore (priorità 1)

**4.3 Pattern Summaries + 4.4 Section Guidance**

Questi collegano processo a risultato - fondamentali per comprensione.

### Alto Volume (priorità 2)

**4.5 Section Summaries**

Molti file simili, batch processing efficiente.

### Strutturali (opzionale)

**_INDEX.md, _PREAMBLE.md, _DIAGNOSTIC.md**

Possono restare senza YAML se servono solo per navigation.

## Integrazioni Durante il Processo

### Puoi suggerire

✅ Integrazioni per file specifico  
✅ Pattern per più file  
✅ Eccezioni documentate

### Non propagare automaticamente

❌ Cambi senza conferma  
❌ Retrofit su tutto il vault

**Questo evita:**
- YAML incoerente
- Falsi positivi
- Perdita di semantica

## Checklist File-by-File

Per ogni file:

- [ ] Tipo documento classificato correttamente
- [ ] Template appropriato selezionato
- [ ] Chat ID verificato (se applicabile)
- [ ] Tutti i campi obbligatori compilati
- [ ] Nessuna virgola finale
- [ ] Valori speciali quotati
- [ ] Status aggiornato in tracking
- [ ] File salvato e verificato in Obsidian

## Conclusione

Il workflow sistematico garantisce:
- ✅ Coerenza ontologica
- ✅ Tracciabilità completa
- ✅ YAML corretto al primo colpo
- ✅ Facile manutenzione futura
