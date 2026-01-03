---
source_chat_name: "Usi e vantaggi Obsidian"
source_chat_id: "g-p-6909e266ae5c8191895a6360a7d67828-roba-seria/c/6957afa7-c6a0-8333-bb60-c4c81de70885"
model: "ChatGPT 5.2"
date: "2026-01-02"
document_type: "Conversation Extract"
chunk_number: 2
topic: "Backlink e navigazione in Obsidian"
---

# Come Vedere Chi Cita Una Nota: Backlink in Obsidian

## Metodo 1 — Pannello Backlink (il più usato)

1. Apri la nota che ti interessa
2. In alto a destra clicca sui tre puntini (⋯)
3. Seleziona "Backlink"
4. Si apre un pannello che mostra:
   - Note che linkano esplicitamente questa nota ([[NomeNota]])
   - Menzioni non collegate (se attive)

👉 Ogni voce è cliccabile: vai subito alla nota che cita.

## Metodo 2 — Backlink fissi nella nota

Puoi far comparire i backlink in basso alla nota, automaticamente.

**Impostazioni → Backlink**
- Attiva "Mostra backlink nel documento"
- (Opzionale) Attiva "Mostra menzioni non collegate"

**Risultato:** quando apri una nota, vedi subito chi la cita, senza pannelli extra.

## Metodo 3 — Vista a grafo (visuale)

1. Apri la Vista a grafo
2. Clicca su una nota
3. Le connessioni evidenziate sono le note che la citano o che essa cita

Utile per esplorare reti di concetti, meno per il dettaglio testuale.

## Tip utili

- Le **menzioni non collegate** ti permettono di trasformare un riferimento testuale in link con un clic
- I backlink funzionano solo se il nome della nota è unico (buona pratica)
- Rinominare una nota aggiorna tutti i link automaticamente

## Cosa Obsidian NON fa automaticamente

👉 **IMPORTANTE:** Obsidian NON interpreta automaticamente i "metadati di connessione" come collegamenti, a meno che non siano espressi in un formato che Obsidian capisce.

Se i tuoi metadati sono solo testo strutturato (YAML senza link espliciti), devi adattare i file o usare plugin come Dataview.
