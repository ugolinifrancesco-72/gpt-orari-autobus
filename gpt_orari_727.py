import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Orari Autobus 727")
st.title("Orari Autobus - Linea 727")

# Fermate vere estratte dai file Excel
fermate_andata = [
    "GENOVA BRIGNOLE", "S.P.D'ARENA AUT.", "BUSALLA AUT.", "BUSALLA F.S.", "ISORELLE",
    "PONTE SAVIGNONE", "SAVIGNONE", "S. BARTOLOMEO", "CASELLA", "AVOSSO",
    "CASALINO", "MONTOGGIO", "BROMIA"
]

fermate_ritorno = list(reversed(fermate_andata))

# Orari completi estratti dai 4 file Excel
gorari = {
    "feriale": {
        "andata": [
            "06:20", "07:00", "07:25", "08:10", "09:40", "11:20", "13:10", "15:20", "17:30", "18:45"
        ],
        "ritorno": [
            "06:30", "08:00", "10:00", "12:00", "14:30", "16:30", "18:00", "19:15"
        ]
    },
    "festivo": {
        "andata": [
            "08:00", "10:30", "13:00", "15:30", "18:00"
        ],
        "ritorno": [
            "07:00", "09:30", "12:00", "14:30", "17:00"
        ]
    }
}

# UI
st.markdown("### Seleziona il viaggio")
direzione = st.radio("Direzione", ["Andata (Brignole ➔ Bromia)", "Ritorno (Bromia ➔ Brignole)"])

direzione_key = "andata" if "Andata" in direzione else "ritorno"
fermate = fermate_andata if direzione_key == "andata" else fermate_ritorno

partenza = st.selectbox("Fermata di partenza", fermate)
idx_partenza = fermate.index(partenza)
fermate_possibili = fermate[idx_partenza + 1:]

if fermate_possibili:
    destinazione = st.selectbox("Fermata di arrivo", fermate_possibili)
else:
    st.warning("Non ci sono fermate successive disponibili.")
    destinazione = None

st.markdown("### Seleziona il giorno e l'orario")
giorno = st.selectbox("Giorno della settimana", ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"])

ora_corrente = datetime.now().strftime("%H:%M")
ora_input = st.text_input("Orario di riferimento (HH:MM) - opzionale", "")
ora_riferimento = ora_input if ora_input else ora_corrente

def filtra_orari(lista_orari, ora):
    return [x for x in lista_orari if x >= ora]

if st.button("Cerca Orari") and destinazione:
    tipo = "feriale" if giorno in ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"] else "festivo"
    orari_disponibili = filtra_orari(orari[tipo][direzione_key], ora_riferimento)

    if orari_disponibili:
        st.success(f"Prossimi orari da {partenza} a {destinazione}: {', '.join(orari_disponibili)}")
    else:
        st.error("Nessuna corsa disponibile a partire dall'orario selezionato.")
