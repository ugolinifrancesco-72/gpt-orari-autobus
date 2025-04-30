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
        "andata":[
  {
    "ora": "06:05",
    "fermate": {
      "GENOVA BRIGNOLE": "06:05",
      "S.P.D'ARENA AUT.": "06:25",
      "BUSALLA AUT.": "06:50",
      "ISORELLE": "06:52",
      "PONTE SAVIGNONE": "06:55",
      "S. BARTOLOMEO": "06:58",
      "CASELLA": "07:00",
      "AVOSSO": "07:05",
      "CASALINO": "07:07",
      "MONTOGGIO": "07:10",
      "BROMIA": "07:15"
    }
  },
  {
    "ora": "07:05",
    "fermate": {
      "GENOVA BRIGNOLE": "07:05",
      "S.P.D'ARENA AUT.": "07:25",
      "BUSALLA AUT.": "07:50",
      "ISORELLE": "07:52",
      "PONTE SAVIGNONE": "07:55",
      "S. BARTOLOMEO": "07:58",
      "CASELLA": "08:00",
      "AVOSSO": "08:05",
      "CASALINO": "08:07",
      "MONTOGGIO": "08:10",
      "BROMIA": "08:15"
    }
  },
  {
    "ora": "08:05",
    "fermate": {
      "GENOVA BRIGNOLE": "08:05",
      "S.P.D'ARENA AUT.": "08:25",
      "BUSALLA AUT.": "08:50",
      "ISORELLE": "08:52",
      "PONTE SAVIGNONE": "08:55",
      "S. BARTOLOMEO": "08:58",
      "CASELLA": "09:00",
      "AVOSSO": "09:05",
      "CASALINO": "09:07",
      "MONTOGGIO": "09:10",
      "BROMIA": "09:15"
    }
  },
  {
    "ora": "09:05",
    "fermate": {
      "GENOVA BRIGNOLE": "09:05",
      "S.P.D'ARENA AUT.": "09:25",
      "BUSALLA AUT.": "09:50",
      "ISORELLE": "09:52",
      "PONTE SAVIGNONE": "09:55",
      "S. BARTOLOMEO": "09:58",
      "CASELLA": "10:00",
      "AVOSSO": "10:05",
      "CASALINO": "10:07",
      "MONTOGGIO": "10:10",
      "BROMIA": "10:15"
    }
  }
  {
    "ora": "14:05",
    "fermate": {
      "GENOVA BRIGNOLE": "14:05",
      "S.P.D'ARENA AUT.": "14:25",
      "BUSALLA AUT.": "14:50",
      "ISORELLE": "14:52",
      "PONTE SAVIGNONE": "14:55",
      "S. BARTOLOMEO": "14:58",
      "CASELLA": "15:00",
      "AVOSSO": "15:05"
    }
  },
  {
    "ora": "17:35",
    "fermate": {
      "GENOVA BRIGNOLE": "17:35",
      "S.P.D'ARENA AUT.": "17:55",
      "BUSALLA AUT.": "18:20",
      "ISORELLE": "18:22",
      "PONTE SAVIGNONE": "18:25",
      "S. BARTOLOMEO": "18:28",
      "CASELLA": "18:30",
      "AVOSSO": "18:35",
      "CASALINO": "18:37",
      "MONTOGGIO": "18:40",
      "BROMIA": "18:45"
    }
  },
  {
    "ora": "18:05",
    "fermate": {
      "GENOVA BRIGNOLE": "18:05",
      "S.P.D'ARENA AUT.": "18:25",
      "BUSALLA AUT.": "18:50",
      "ISORELLE": "18:52",
      "PONTE SAVIGNONE": "18:55",
      "S. BARTOLOMEO": "18:58",
      "CASELLA": "19:00",
      "AVOSSO": "19:05",
      "CASALINO": "19:07",
      "MONTOGGIO": "19:10",
      "BROMIA": "19:15"
    }
  },
  {
    "ora": "18:35",
    "fermate": {
      "GENOVA BRIGNOLE": "18:35",
      "S.P.D'ARENA AUT.": "18:55",
      "BUSALLA AUT.": "19:20",
      "ISORELLE": "19:22",
      "PONTE SAVIGNONE": "19:25",
      "S. BARTOLOMEO": "19:28",
      "CASELLA": "19:30",
      "AVOSSO": "19:35",
      "CASALINO": "19:37",
      "MONTOGGIO": "19:40",
      "BROMIA": "19:45"
    }
  },
  {
    "ora": "20:35",
    "fermate": {
      "GENOVA BRIGNOLE": "20:35",
      "S.P.D'ARENA AUT.": "20:50",
      "BUSALLA AUT.": "21:15",
      "BUSALLA F.S.": "21:20",
      "ISORELLE": "21:27",
      "PONTE SAVIGNONE": "21:30",
      "S. BARTOLOMEO": "21:33",
      "CASELLA": "21:35",
      "AVOSSO": "21:40",
      "CASALINO": "21:42",
      "MONTOGGIO": "21:45",
      "BROMIA": "21:50"
    }
  }
]

        "ritorno": [
            # ⬇⬇⬇ INCOLLA QUI GLI ORARI COMPLETI FERIALI RITORNO (Bromia ➜ Brignole) ⬇⬇⬇
        ]
    },
    "festivo": {
        "andata": [
            # ⬇⬇⬇ INCOLLA QUI GLI ORARI COMPLETI FESTIVI ANDATA (Brignole ➜ Bromia) ⬇⬇⬇
        ],
        "ritorno": [
            # ⬇⬇⬇ INCOLLA QUI GLI ORARI COMPLETI FESTIVI RITORNO (Bromia ➜ Brignole) ⬇⬇⬇
        ]
    }
}
        # ⬇⬇⬇ INCOLLA QUI GLI ORARI COMPLETI FESTIVI RITORNO (Bromia ➜ Brignole) ⬇⬇⬇
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
    corse = orari.get(tipo, {}).get(direzione_key, [])
    orari_filtrati = filtra_orari_completi(corse, partenza, destinazione, ora_riferimento)

    if orari_filtrati:
        st.success(f"Prossimi orari da {partenza} a {destinazione}: {', '.join(orari_filtrati)}")
    else:
        st.error("Nessuna corsa disponibile a partire dall'orario selezionato.")
