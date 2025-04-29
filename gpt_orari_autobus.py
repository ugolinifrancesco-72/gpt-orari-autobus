import streamlit as st

st.set_page_config(page_title="Orari Autobus GPT", page_icon="🚍")

st.title("Orari Autobus - Mini GPT")


# Dati degli orari incorporati direttamente nel codice
orari_data = {
    "feriale": {
        "727": {
            "Genova Brignole -> Bromia": ["7:25", "8:10", "8:40", "10:20"]
        },
        "740": {
            "Busalla FS -> Bromia": ["5:30", "6:15", "7:00", "7:30"]
        },
        "822": {
            "Busalla FS -> Savignone": ["6:10", "7:10", "8:30", "9:30"]
        }
    },
    "festivo": {
        "727": {
            "Genova Brignole -> Bromia": ["7:35", "10:30", "13:30", "16:30"]
        },
        "822": {
            "Busalla FS -> Savignone": ["7:15", "8:30", "10:30", "13:40"]
        }
    }
}

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

