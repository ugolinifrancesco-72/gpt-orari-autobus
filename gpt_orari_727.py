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
        "andata": [...],  # tutte 14 corse andata
        "ritorno": [...],  # tutte 14 corse ritorno
    },
    "festivo": {
        "andata": [...],  # 2 corse andata
        "ritorno": [...]   # 2 corse ritorno
    }
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
