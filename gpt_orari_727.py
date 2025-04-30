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
  },
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
        ],
        "ritorno": [
            {
  "ora": "06:15",
  "fermate": {
    "BROMIA": "06:15",
    "MONTOGGIO": "06:20",
    "CASALINO": "06:23",
    "AVOSSO": "06:25",
    "CASELLA": "06:30",
    "S. BARTOLOMEO": "06:32",
    "PONTE SAVIGNONE": "06:35",
    "ISORELLE": "06:38",
    "BUSALLA AUT.": "06:40",
    "S.P.D'ARENA AUT.": "07:05",
    "GENOVA BRIGNOLE": "07:25"
  }
},
{
  "ora": "06:30",
  "fermate": {
    "CASELLA": "06:30",
    "S. BARTOLOMEO": "06:32",
    "PONTE SAVIGNONE": "06:35",
    "ISORELLE": "06:38",
    "BUSALLA AUT.": "06:40",
    "S.P.D'ARENA AUT.": "07:05",
    "GENOVA BRIGNOLE": "07:25"
  }
},
{
  "ora": "06:30",
  "fermate": {
    "BROMIA": "06:30",
    "MONTOGGIO": "06:35",
    "CASALINO": "06:38",
    "AVOSSO": "06:40",
    "CASELLA": "06:45",
    "S. BARTOLOMEO": "06:47",
    "PONTE SAVIGNONE": "06:50",
    "ISORELLE": "06:53",
    "BUSALLA AUT.": "06:55",
    "S.P.D'ARENA AUT.": "07:20",
    "GENOVA BRIGNOLE": "07:40"
  }
},
{
  "ora": "15:00",
  "fermate": {
    "BROMIA": "15:00",
    "MONTOGGIO": "15:05",
    "CASALINO": "15:08",
    "AVOSSO": "15:10",
    "CASELLA": "15:15",
    "S. BARTOLOMEO": "15:17",
    "PONTE SAVIGNONE": "15:20",
    "ISORELLE": "15:23",
    "BUSALLA AUT.": "15:25",
    "S.P.D'ARENA AUT.": "15:50",
    "GENOVA BRIGNOLE": "16:10"
  }
},
{
  "ora": "16:00",
  "fermate": {
    "BROMIA": "16:00",
    "MONTOGGIO": "16:05",
    "CASALINO": "16:08",
    "AVOSSO": "16:10",
    "CASELLA": "16:15",
    "S. BARTOLOMEO": "16:17",
    "PONTE SAVIGNONE": "16:20",
    "ISORELLE": "16:23",
    "BUSALLA AUT.": "16:25",
    "S.P.D'ARENA AUT.": "16:50",
    "GENOVA BRIGNOLE": "17:10"
  }
},
{
  "ora": "17:00",
  "fermate": {
    "BROMIA": "17:00",
    "MONTOGGIO": "17:05",
    "CASALINO": "17:08",
    "AVOSSO": "17:10",
    "CASELLA": "17:15",
    "S. BARTOLOMEO": "17:17",
    "PONTE SAVIGNONE": "17:20",
    "ISORELLE": "17:23",
    "BUSALLA AUT.": "17:25",
    "S.P.D'ARENA AUT.": "17:50",
    "GENOVA BRIGNOLE": "18:10"
  }
},
{
  "ora": "19:00",
  "fermate": {
    "BROMIA": "19:00",
    "MONTOGGIO": "19:05",
    "CASALINO": "19:08",
    "AVOSSO": "19:10",
    "CASELLA": "19:15",
    "S. BARTOLOMEO": "19:17",
    "PONTE SAVIGNONE": "19:20",
    "ISORELLE": "19:23",
    "BUSALLA AUT.": "19:25",
    "S.P.D'ARENA AUT.": "19:50",
    "GENOVA BRIGNOLE": "20:10"
  }
}
        ]
    },
    "festivo": {
        "andata": [
            {
  "ora": "07:35",
  "fermate": {
    "GENOVA BRIGNOLE": "07:35",
    "S.P.D'ARENA AUT.": "07:55",
    "BUSALLA AUT.": "08:20",
    "ISORELLE": "08:22",
    "PONTE SAVIGNONE": "08:25",
    "S. BARTOLOMEO": "08:28",
    "CASELLA": "08:30",
    "AVOSSO": "08:35",
    "CASALINO": "08:37",
    "MONTOGGIO": "08:40",
    "BROMIA": "08:45"
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
}
        ],
        "ritorno": [
            {
  "ora": "09:00",
  "fermate": {
    "BROMIA": "09:00",
    "MONTOGGIO": "09:05",
    "CASALINO": "09:08",
    "AVOSSO": "09:10",
    "CASELLA": "09:15",
    "S. BARTOLOMEO": "09:17",
    "PONTE SAVIGNONE": "09:20",
    "ISORELLE": "09:23",
    "BUSALLA AUT.": "09:25",
    "S.P.D'ARENA AUT.": "09:50",
    "GENOVA BRIGNOLE": "10:10"
  }
},
{
  "ora": "17:00",
  "fermate": {
    "BROMIA": "17:00",
    "MONTOGGIO": "17:05",
    "CASALINO": "17:08",
    "AVOSSO": "17:10",
    "CASELLA": "17:15",
    "S. BARTOLOMEO": "17:17",
    "PONTE SAVIGNONE": "17:20",
    "ISORELLE": "17:23",
    "BUSALLA AUT.": "17:25",
    "S.P.D'ARENA AUT.": "17:50",
    "GENOVA BRIGNOLE": "18:10"
  }
}
        ]
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
                from datetime import datetime as dt

                ora_partenza = dt.strptime(fermate[partenza], "%H:%M")
                ora_arrivo = dt.strptime(fermate[destinazione], "%H:%M")
                durata = int((ora_arrivo - ora_partenza).total_seconds() // 60)
                risultati.append({
                    "partenza": fermate[partenza],
                    "arrivo": fermate[destinazione],
                    "durata (minuti)": durata
                })
    return risultati

if st.button("Cerca Orari") and destinazione:
    tipo = "feriale" if giorno in ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"] else "festivo"
    corse = orari.get(tipo, {}).get(direzione_key, [])
    orari_filtrati = filtra_orari_completi(corse, partenza, destinazione, ora_riferimento)

    if orari_filtrati:
        st.success(f"Prossimi orari da {partenza} a {destinazione}:")
        import pandas as pd
        df = pd.DataFrame(orari_filtrati)
        st.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Scarica orari in CSV",
            data=csv,
            file_name=f"orari_{partenza}_{destinazione}.csv",
            mime='text/csv'
        )
    else:
        st.error("Nessuna corsa disponibile a partire dall'orario selezionato.")

st.caption("App realizzata da Francesco per la Linea 727 – Tutti i diritti riservati")
