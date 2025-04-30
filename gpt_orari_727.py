import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Orari Autobus 727")
st.title("Orari Autobus - Linea 727")

fermate_andata = [
    "GENOVA BRIGNOLE", "S.P.D'ARENA AUT.", "BUSALLA AUT.", "ISORELLE",
    "PONTE SAVIGNONE", "S. BARTOLOMEO", "CASELLA", "AVOSSO",
    "CASALINO", "MONTOGGIO", "BROMIA"
]

fermate_ritorno = list(reversed(fermate_andata))

# Orari ufficiali aggiornati da file Excel
orari = {
    "feriale": {
        "andata": [
            {
                "ora": "06:05",
                "fermate": {
                    "GENOVA BRIGNOLE": "06:05", "S.P.D'ARENA AUT.": "06:25", "BUSALLA AUT.": "06:50", "ISORELLE": "07:00",
                    "PONTE SAVIGNONE": "07:03", "S. BARTOLOMEO": "07:06", "CASELLA": "07:09", "AVOSSO": "07:14",
                    "CASALINO": "07:17", "MONTOGGIO": "07:20", "BROMIA": "07:25"
                }
            },
            {
                "ora": "07:05",
                "fermate": {
                    "GENOVA BRIGNOLE": "07:05", "S.P.D'ARENA AUT.": "07:25", "BUSALLA AUT.": "07:50", "ISORELLE": "08:00",
                    "PONTE SAVIGNONE": "08:03", "S. BARTOLOMEO": "08:06", "CASELLA": "08:09", "AVOSSO": "08:14",
                    "CASALINO": "08:17", "MONTOGGIO": "08:20", "BROMIA": "08:25"
                }
            },
            {
                "ora": "08:05",
                "fermate": {
                    "GENOVA BRIGNOLE": "08:05", "S.P.D'ARENA AUT.": "08:25", "BUSALLA AUT.": "08:50", "ISORELLE": "09:00",
                    "PONTE SAVIGNONE": "09:03", "S. BARTOLOMEO": "09:06", "CASELLA": "09:09", "AVOSSO": "09:14",
                    "CASALINO": "09:17", "MONTOGGIO": "09:20", "BROMIA": "09:25"
                }
            },
            {
                "ora": "09:05",
                "fermate": {
                    "GENOVA BRIGNOLE": "09:05", "S.P.D'ARENA AUT.": "09:25", "BUSALLA AUT.": "09:50", "ISORELLE": "10:00",
                    "PONTE SAVIGNONE": "10:03", "S. BARTOLOMEO": "10:06", "CASELLA": "10:09", "AVOSSO": "10:14",
                    "CASALINO": "10:17", "MONTOGGIO": "10:20", "BROMIA": "10:25"
                }
            },
            {
                "ora": "13:05",
                "fermate": {
                    "GENOVA BRIGNOLE": "13:05", "S.P.D'ARENA AUT.": "13:25", "BUSALLA AUT.": "13:50", "ISORELLE": "14:00",
                    "PONTE SAVIGNONE": "14:03", "S. BARTOLOMEO": "14:06", "CASELLA": "14:09", "AVOSSO": "14:14",
                    "CASALINO": "14:17", "MONTOGGIO": "14:20", "BROMIA": "14:25"
                }
            }
            # ...continua con tutte le corse da file
        ]
    }
    # Le sezioni "ritorno" e "festivo" saranno aggiunte nei prossimi step
}

st.markdown("### Seleziona il viaggio")
direzione = st.radio("Direzione", ["Andata (Brignole ➔ Bromia)", "Ritorno (Bromia ➔ Brignole)"])
direzione_key = "andata" if "Andata" in direzione else "ritorno"
fermate = fermate_andata if direzione_key == "andata" else fermate_ritorno

partenza = st.selectbox("Fermata di partenza", fermate)
idx_partenza = fermate.index(partenza)
fermate_possibili = fermate[idx_partenza + 1:]

destinazione = st.selectbox("Fermata di arrivo", fermate_possibili) if fermate_possibili else None
if not destinazione:
    st.warning("Non ci sono fermate successive disponibili.")

st.markdown("### Seleziona il giorno e l'orario")
giorno = st.selectbox("Giorno della settimana", ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"])
ora_corrente = datetime.now().strftime("%H:%M")
ora_input = st.text_input("Orario di riferimento (HH:MM) - opzionale", "")
ora_riferimento = ora_input if ora_input else ora_corrente

def filtra_orari_completi(corse, partenza, destinazione, ora):
    risultati = []
    for corsa in corse:
        fermate = corsa.get("fermate", {})
        if partenza in fermate and destinazione in fermate:
            if fermate[partenza] <= fermate[destinazione] and fermate[partenza] >= ora:
                risultati.append(fermate[partenza])
    return risultati

if st.button("Cerca Orari") and destinazione:
    tipo = "feriale" if giorno in ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"] else "festivo"
    corse = orari.get(tipo, {}).get(direzione_key, [])
    orari_filtrati = filtra_orari_completi(corse, partenza, destinazione, ora_riferimento)

    if orari_filtrati:
        st.success(f"Prossimi orari da {partenza} a {destinazione}: {', '.join(orari_filtrati)}")
    else:
        st.error("Nessuna corsa disponibile a partire dall'orario selezionato.")
