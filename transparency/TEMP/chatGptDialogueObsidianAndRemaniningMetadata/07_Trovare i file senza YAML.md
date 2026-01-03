---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Conversation Extract"
chunk_number: 7
topic: "Workflow per aggiungere YAML frontmatter ai file"
---

# Workflow per Aggiungere YAML Frontmatter ai File

## Principio guida

> Non tutti i file devono avere lo stesso YAML.

Per esempio:
- `_INDEX.md`, `_PREAMBLE.md` → YAML molto leggero
- `SectionSummary` → YAML senza source_chat_id
- `Epistemic Trace` / `PDL` → YAML completo con source_chat_id

**Questo evita di "mentire" al sistema.**

## Metodo operativo

Per ogni file faremo sempre lo stesso ciclo:

### 1. Classificazione rapida

Che tipo di documento è:
- Pattern Summary
- Section Summary
- Section Guidance
- Modification Log
- Epistemic Trace
- Index / Structural

### 2. Template YAML minimo appropriato

Niente over-engineering: solo campi utili per:
- Navigazione
- Coerenza sistemica
- Riproducibilità

### 3. Decisione esplicita

- Cosa va nel YAML
- Cosa non va (e perché)
- Chat ID se disponibile e verificabile

### 4. Conferma e tracking

- Applica il YAML
- Marca come ✅ DONE
- Passa al prossimo

## Trovare i file senza YAML

### Script di diagnostic

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
    print(f"Markdown files without YAML frontmatter: {len(missing)}\n")
    for p in sorted(missing):
        print(p)

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
```

**Uso:**
```bash
python check_missing_yaml.py /path/to/vault
```

## Strategia per sezioni del progetto

### Alto valore (priorità)

**4.3 Pattern Summaries** + **4.4 Section Guidance**

Questi sono artefatti chiave che collegano processo a risultato.

### Alto volume (secondo)

**4.5 Section Summaries**

Molti file simili, facili da processare in batch.

### Strutturali (opzionale)

`_INDEX.md`, `_PREAMBLE.md`, `_DIAGNOSTIC.md`

Possono anche restare senza YAML se servono solo come navigation.

## Template per categorie comuni

### Pattern Summary

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

### Section Guidance

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

status: "complete"
---
```

## Tracking con checklist

Usa un file separato o un sistema come:

```markdown
## YAML Status Tracking

### 4.3 Pattern Summaries
- [x] 4.3.1 Section II
- [x] 4.3.2 Sections II–III
- [x] 4.3.3 Section IV
- [ ] 4.3.4 Section V
- [ ] 4.3.5 Section VIII

### 4.4 Section Guidance
- [x] 4.4.9 Consolidate Section 2
- [x] 4.4.10 Introduction tone
- [ ] 4.4.13 Appendix to Section 6
```

## Integrazioni durante il processo

✅ **Puoi suggerire integrazioni** per:
- Un file specifico
- Un pattern (più file)
- Un'eccezione documentata

❌ **Non propagare automaticamente** senza conferma

Questo evita:
- Retrofitting selvaggio
- YAML incoerente
- Falsi positivi nello script
