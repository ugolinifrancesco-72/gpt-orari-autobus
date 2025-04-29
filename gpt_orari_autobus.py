import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Orari Autobus GPT")

st.title("Orari Autobus - Linea 727 (Andata e Ritorno)")

# Fermate della linea 727
fermate_andata = [
    "Genova Brignole",
    "Genova Via Adua",
    "Genova Sampierdarena",
    "Busalla FS",
    "Casella Paese",
    "Avosso",
    "Montoggio",
    "Bromia"
]

fermate_ritorno = list(reversed(fermate_andata))

# Orari feriali e festivi (esempio base)
orari_feriali = {
    "andata": ["07:25", "08:10", "09:40", "11:20", "13:10", "15:20", "17:30"],
    "ritorno": ["06:30", "08:00", "10:00", "12:00", "14:30", "16:30", "18:00"]
}

orari_festivi = {
    "andata": ["08:00", "10:30", "13:00", "15:30", "18:00"],
    "ritorno": ["07:00", "09:30", "12:00", "14:30", "17:00"]
}

# Scelta direzione
direzione = st.radio("Scegli la direzione", ("Andata", "Ritorno"))

if direzione == "Andata":
    fermate = fermate_andata
else:
    fermate = fermate_ritorno

# Scelta fermate
partenza = st.selectbox("Seleziona la fermata di partenza", fermate)
indice_partenza = fermate.index(partenza)
fermate_possibili = fermate[indice_partenza+1:]

destinazione = st.selectbox("Seleziona la fermata di arrivo", fermate_possibili)

# Scelta giorno
giorno = st.selectbox(
    "Seleziona il giorno",
    ("Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica")
)

# Orario richiesto
ora_attuale = datetime.now().strftime("%H:%M")
ora_richiesta = st.text_input("Inserisci un orario di riferimento (HH:MM) oppure lascia vuoto per l'orario attuale:", "")

if ora_richiesta == "":
    ora_richiesta = ora_attuale

# Funzione per trovare gli orari successivi
def trova_prossimi_orari(lista_orari, ora_rif):
    return [o for o in lista_orari if o >= ora_rif]

if st.button("Cerca Orari"):
    tipo_giorno = "feriali" if giorno.lower() in ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì"] else "festivi"
    
    if tipo_giorno == "feriali":
        orari = orari_feriali["andata"] if direzione == "Andata" else orari_feriali["ritorno"]
    else:
        orari = orari_festivi["andata"] if direzione == "Andata" else orari_festivi["ritorno"]
    
    risultati = trova_prossimi_orari(orari, ora_richiesta)
    
    if risultati:
        st.success(f"Prossimi orari da {partenza} a {destinazione}: {', '.join(risultati)}")
    else:
        st.warning("Nessuna corsa disponibile a partire dall'orario selezionato.")
