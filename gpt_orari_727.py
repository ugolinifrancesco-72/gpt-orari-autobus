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

# Orari: includono ora + mappa fermata -> orario preciso
orari = {
    "feriale": {
        "andata": [
            {"ora": "06:00", "fermate": {"GENOVA BRIGNOLE": "06:00", "S.P.D'ARENA AUT.": "06:10", "BUSALLA AUT.": "06:30", "ISORELLE": "06:40", "PONTE SAVIGNONE": "06:43", "S. BARTOLOMEO": "06:46", "CASELLA": "06:49", "AVOSSO": "06:54", "CASALINO": "06:57", "MONTOGGIO": "07:00", "BROMIA": "07:05"}},
            {"ora": "07:00", "fermate": {"GENOVA BRIGNOLE": "07:00", "S.P.D'ARENA AUT.": "07:10", "BUSALLA AUT.": "07:30", "ISORELLE": "07:40", "PONTE SAVIGNONE": "07:43", "S. BARTOLOMEO": "07:46", "CASELLA": "07:49", "AVOSSO": "07:54", "CASALINO": "07:57", "MONTOGGIO": "08:00", "BROMIA": "08:05"}},
            {"ora": "08:00", "fermate": {"GENOVA BRIGNOLE": "08:00", "S.P.D'ARENA AUT.": "08:10", "BUSALLA AUT.": "08:30", "ISORELLE": "08:40", "PONTE SAVIGNONE": "08:43", "S. BARTOLOMEO": "08:46", "CASELLA": "08:49", "AVOSSO": "08:54", "CASALINO": "08:57", "MONTOGGIO": "09:00", "BROMIA": "09:05"}},
            {"ora": "09:00", "fermate": {"GENOVA BRIGNOLE": "09:00", "S.P.D'ARENA AUT.": "09:10", "BUSALLA AUT.": "09:30", "ISORELLE": "09:40", "PONTE SAVIGNONE": "09:43", "S. BARTOLOMEO": "09:46", "CASELLA": "09:49", "AVOSSO": "09:54", "CASALINO": "09:57", "MONTOGGIO": "10:00", "BROMIA": "10:05"}},
            {"ora": "10:00", "fermate": {"GENOVA BRIGNOLE": "10:00", "S.P.D'ARENA AUT.": "10:10", "BUSALLA AUT.": "10:30", "ISORELLE": "10:40", "PONTE SAVIGNONE": "10:43", "S. BARTOLOMEO": "10:46", "CASELLA": "10:49", "AVOSSO": "10:54", "CASALINO": "10:57", "MONTOGGIO": "11:00", "BROMIA": "11:05"}},
            {"ora": "11:00", "fermate": {"GENOVA BRIGNOLE": "11:00", "S.P.D'ARENA AUT.": "11:10", "BUSALLA AUT.": "11:30", "ISORELLE": "11:40", "PONTE SAVIGNONE": "11:43", "S. BARTOLOMEO": "11:46", "CASELLA": "11:49", "AVOSSO": "11:54", "CASALINO": "11:57", "MONTOGGIO": "12:00", "BROMIA": "12:05"}},
            {"ora": "12:00", "fermate": {"GENOVA BRIGNOLE": "12:00", "S.P.D'ARENA AUT.": "12:10", "BUSALLA AUT.": "12:30", "ISORELLE": "12:40", "PONTE SAVIGNONE": "12:43", "S. BARTOLOMEO": "12:46", "CASELLA": "12:49", "AVOSSO": "12:54", "CASALINO": "12:57", "MONTOGGIO": "13:00", "BROMIA": "13:05"}},
            {"ora": "13:00", "fermate": {"GENOVA BRIGNOLE": "13:00", "S.P.D'ARENA AUT.": "13:10", "BUSALLA AUT.": "13:30", "ISORELLE": "13:40", "PONTE SAVIGNONE": "13:43", "S. BARTOLOMEO": "13:46", "CASELLA": "13:49", "AVOSSO": "13:54", "CASALINO": "13:57", "MONTOGGIO": "14:00", "BROMIA": "14:05"}},
            {"ora": "14:00", "fermate": {"GENOVA BRIGNOLE": "14:00", "S.P.D'ARENA AUT.": "14:10", "BUSALLA AUT.": "14:30", "ISORELLE": "14:40", "PONTE SAVIGNONE": "14:43", "S. BARTOLOMEO": "14:46", "CASELLA": "14:49", "AVOSSO": "14:54", "CASALINO": "14:57", "MONTOGGIO": "15:00", "BROMIA": "15:05"}},
            {"ora": "15:00", "fermate": {"GENOVA BRIGNOLE": "15:00", "S.P.D'ARENA AUT.": "15:10", "BUSALLA AUT.": "15:30", "ISORELLE": "15:40", "PONTE SAVIGNONE": "15:43", "S. BARTOLOMEO": "15:46", "CASELLA": "15:49", "AVOSSO": "15:54", "CASALINO": "15:57", "MONTOGGIO": "16:00", "BROMIA": "16:05"}},
            {"ora": "16:00", "fermate": {"GENOVA BRIGNOLE": "16:00", "S.P.D'ARENA AUT.": "16:10", "BUSALLA AUT.": "16:30", "ISORELLE": "16:40", "PONTE SAVIGNONE": "16:43", "S. BARTOLOMEO": "16:46", "CASELLA": "16:49", "AVOSSO": "16:54", "CASALINO": "16:57", "MONTOGGIO": "17:00", "BROMIA": "17:05"}},
            {"ora": "17:00", "fermate": {"GENOVA BRIGNOLE": "17:00", "S.P.D'ARENA AUT.": "17:10", "BUSALLA AUT.": "17:30", "ISORELLE": "17:40", "PONTE SAVIGNONE": "17:43", "S. BARTOLOMEO": "17:46", "CASELLA": "17:49", "AVOSSO": "17:54", "CASALINO": "17:57", "MONTOGGIO": "18:00", "BROMIA": "18:05"}},
            {"ora": "18:00", "fermate": {"GENOVA BRIGNOLE": "18:00", "S.P.D'ARENA AUT.": "18:10", "BUSALLA AUT.": "18:30", "ISORELLE": "18:40", "PONTE SAVIGNONE": "18:43", "S. BARTOLOMEO": "18:46", "CASELLA": "18:49", "AVOSSO": "18:54", "CASALINO": "18:57", "MONTOGGIO": "19:00", "BROMIA": "19:05"}}
        ]
    }
    # Ritorno e festivo ancora da aggiungere...
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
    corse = orari[tipo][direzione_key]
    orari_filtrati = filtra_orari_completi(corse, partenza, destinazione, ora_riferimento)

    if orari_filtrati:
        st.success(f"Prossimi orari da {partenza} a {destinazione}: {', '.join(orari_filtrati)}")
    else:
        st.error("Nessuna corsa disponibile a partire dall'orario selezionato.")
