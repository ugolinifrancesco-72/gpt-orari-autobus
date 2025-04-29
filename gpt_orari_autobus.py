import streamlit as st
import json
from pathlib import Path

st.set_page_config(page_title="Orari Autobus GPT", page_icon="🚍")

st.title("\ud83d\ude8d Orari Autobus - Mini GPT")

# Caricamento sicuro del file JSON con Pathlib
def carica_orari():
    file_path = Path(__file__).parent / "orari_autobus.json"
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return None

orari_data = carica_orari()

if orari_data is None:
    st.error("⚠️ Errore: File degli orari non trovato. Carica 'orari_autobus.json' nel repository.")
else:
    def trova_orari(partenza, destinazione, giorno_settimana, ora_richiesta=None):
        giorno_settimana = giorno_settimana.lower()
        if giorno_settimana in ["sabato", "domenica"]:
            tipo_giorno = "festivo"
        else:
            tipo_giorno = "feriale"

        risultati = []

        for linea, tratte in orari_data.get(tipo_giorno, {}).items():
            for tratta, orari in tratte.items():
                if partenza.lower() in tratta.lower() and destinazione.lower() in tratta.lower():
                    if ora_richiesta:
                        prossime_corse = [o for o in orari if o >= ora_richiesta]
                        if prossime_corse:
                            risultati.append((linea, prossime_corse[0]))
                    else:
                        risultati.append((linea, orari))

        if risultati:
            risposte = []
            for linea, orari in risultati:
                if isinstance(orari, list):
                    risposte.append(f"Linea {linea}: Orari disponibili -> {', '.join(orari)}")
                else:
                    risposte.append(f"Linea {linea}: Prossima corsa alle {orari}")
            return "\n".join(risposte)
        else:
            return "Nessuna corsa trovata per la tratta richiesta."

    # UI dell'app
    partenza = st.text_input("Da dove parti?", "Genova Brignole")
    destinazione = st.text_input("Dove vuoi andare?", "Bromia")

    giorno = st.selectbox(
        "Che giorno della settimana?",
        ("luned\u00ec", "marted\u00ec", "mercoled\u00ec", "gioved\u00ec", "venerd\u00ec", "sabato", "domenica")
    )

    ora = st.text_input("A che ora? (Formato HH:MM, opzionale)", "")

    if st.button("Cerca Orari"):
        ora = ora if ora else None
        risposta = trova_orari(partenza, destinazione, giorno, ora)
        st.subheader("Risultato:")
        st.text(risposta)
