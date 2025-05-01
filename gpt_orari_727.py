import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Orari Autobus 727", page_icon="🚌")

st.markdown("""
    <style>
@media only screen and (max-width: 768px) {
  .stMarkdown p,
  .stMarkdown h1,
  .stMarkdown h2,
  .stMarkdown h3,
  .stMarkdown h4 {
    font-size: 18px !important;
    color: #000000 !important;
  }
  .block-container {
    font-size: 16px !important;
  }
  h1, h2, h3 {
    font-size: 18px !important;
  }
  .markdown-text-container p {
    font-size: 16px !important;
  }
  .stApp {
    padding-left: 0.5rem;
    padding-right: 0.5rem;
  }
  .block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
  }
  .stTextInput > div > input,
  .stSelectbox > div[data-baseweb="select"],
  .stTimeInput > div > input {
    font-size: 16px !important;
  }
  h1, h2, h3, h4 {
    font-size: 1.1rem !important;
  }
}
    body {
        background-color: #f0f4f8;
    }
    .stApp {
        background-color: #f0f4f8;
    }
    .stTextInput > div > input, .stSelectbox > div[data-baseweb="select"] {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
        border-radius: 6px !important;
        padding: 6px 10px !important;
    }
    .stTimeInput > div > input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
        border-radius: 6px !important;
        padding: 6px 10px !important;
    }
    .stTextInput input {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1) !important;
        border-radius: 6px !important;
        padding: 6px 10px !important;
    }
</style>
""", unsafe_allow_html=True)

st.image("https://github.com/ugolinifrancesco-72/gpt-orari-autobus/blob/main/corriera%20atp%20freccia%20turchino-2.jpg?raw=true", use_container_width=True)
st.title("Orari Autobus - Linea 727")

# Mostra la mappa del percorso della Linea 727
map_data = {
    "GENOVA BRIGNOLE": (44.40726, 8.93403),
    "S.P.D'ARENA AUT.": (44.44220, 8.89243),
    "BUSALLA AUT.": (44.56445, 8.94434),
    "ISORELLE": (44.56887, 9.00671),
    "PONTE SAVIGNONE": (44.55379, 9.01859),
    "S. BARTOLOMEO": (44.54721, 9.03258),
    "CASELLA": (44.53783, 9.04171),
    "AVOSSO": (44.52694, 9.04869),
    "CASALINO": (44.51936, 9.05742),
    "MONTOGGIO": (44.51511, 9.06431),
    "BROMIA": (44.50935, 9.07341)
}
import pandas as pd
import pydeck as pdk

mappa_df = pd.DataFrame(map_data.items(), columns=["fermata", "coords"])
mappa_df[["lat", "lon"]] = pd.DataFrame(mappa_df["coords"].tolist(), index=mappa_df.index)


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
    },
    "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
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
    "ora": "13:05",
    "fermate": {
      "GENOVA BRIGNOLE": "13:05",
      "S.P.D'ARENA AUT.": "13:25",
      "BUSALLA AUT.": "13:50",
      "ISORELLE": "13:52",
      "PONTE SAVIGNONE": "13:55",
      "S. BARTOLOMEO": "13:58",
      "CASELLA": "14:00",
      "AVOSSO": "14:05",
      "CASALINO": "14:07",
      "MONTOGGIO": "14:10",
      "BROMIA": "14:15"
    },
    "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
  },
  {
    "ora": "13:35",
    "fermate": {
      "GENOVA BRIGNOLE": "13:35",
      "S.P.D'ARENA AUT.": "13:55",
      "BUSALLA AUT.": "14:20",
      "ISORELLE": "14:22",
      "PONTE SAVIGNONE": "14:25",
      "S. BARTOLOMEO": "14:28",
      "CASELLA": "14:30",
      "AVOSSO": "14:35",
      "CASALINO": "14:37",
      "MONTOGGIO": "14:40",
      "BROMIA": "14:45"
    },
    "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
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
    },
    "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
  },
  {
    "ora": "14:35",
    "fermate": {
      "GENOVA BRIGNOLE": "14:35",
      "S.P.D'ARENA AUT.": "14:55",
      "BUSALLA AUT.": "15:20",
      "ISORELLE": "15:22",
      "PONTE SAVIGNONE": "15:25",
      "S. BARTOLOMEO": "15:28",
      "CASELLA": "15:30",
      "AVOSSO": "15:35",
      "CASALINO": "15:37",
      "MONTOGGIO": "15:40",
      "BROMIA": "15:45"
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
      "ora": "07:50",
      "fermate": {
        "PONTE SAVIGNONE": "07:50",
        "ISORELLE": "07:53",
        "BUSALLA AUT.": "07:55",
        "S.P.D'ARENA AUT.": "08:20",
        "GENOVA BRIGNOLE": "08:40"
      },
      "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
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
      },
      "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
    },
    {
      "ora": "07:15",
      "fermate": {
        "CASELLA": "07:15",
        "S. BARTOLOMEO": "07:17",
        "PONTE SAVIGNONE": "07:20",
        "ISORELLE": "07:23",
        "BUSALLA AUT.": "07:25",
        "S.P.D'ARENA AUT.": "07:50",
        "GENOVA BRIGNOLE": "08:10"
      },
      "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
    },
    {
      "ora": "06:45",
      "fermate": {
        "CASELLA": "06:45",
        "S. BARTOLOMEO": "06:47",
        "PONTE SAVIGNONE": "06:50",
        "ISORELLE": "06:53",
        "BUSALLA AUT.": "06:55",
        "S.P.D'ARENA AUT.": "07:20",
        "GENOVA BRIGNOLE": "07:40"
      },
      "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
    },
    
    
    
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
      },
      "note": "#ES: Giorni di scuola dal Lunedì al Venerdì"
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
      "ora": "07:00",
      "fermate": {
        "BROMIA": "07:00",
        "MONTOGGIO": "07:05",
        "CASALINO": "07:08",
        "AVOSSO": "07:10",
        "CASELLA": "07:15",
        "S. BARTOLOMEO": "07:17",
        "PONTE SAVIGNONE": "07:20",
        "ISORELLE": "07:23",
        "BUSALLA AUT.": "07:25",
        "S.P.D'ARENA AUT.": "07:50",
        "GENOVA BRIGNOLE": "08:10"
      }
    },
    {
      "ora": "07:30",
      "fermate": {
        "BROMIA": "07:30",
        "MONTOGGIO": "07:35",
        "CASALINO": "07:38",
        "AVOSSO": "07:40",
        "CASELLA": "07:45",
        "S. BARTOLOMEO": "07:47",
        "PONTE SAVIGNONE": "07:50",
        "ISORELLE": "07:53",
        "BUSALLA AUT.": "07:55",
        "S.P.D'ARENA AUT.": "08:20",
        "GENOVA BRIGNOLE": "08:40"
      }
    },
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
        "BUSALLA AUT.": "09:35",
        "S.P.D'ARENA AUT.": "10:00",
        "GENOVA BRIGNOLE": "10:20"
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

# Giorno e orario ora si definiscono prima della mappa
st.markdown("### Seleziona il giorno e l'orario")

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
                note = corsa.get("note", "")
                risultati.append({
                    "partenza": fermate[partenza],
                    "arrivo": fermate[destinazione],
                    "durata (minuti)": durata,
                    "note": note
                })
    return risultati

giorno = st.selectbox("Giorno della settimana", ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"])
ora_corrente = datetime.now().strftime("%H:%M")
corse_totali = orari.get("feriale", {}).get("andata", []) + orari.get("feriale", {}).get("ritorno", []) + orari.get("festivo", {}).get("andata", []) + orari.get("festivo", {}).get("ritorno", [])
all_ore = sorted(set(c["ora"] for c in corse_totali if "ora" in c))
ora_input = st.text_input("Orario di riferimento (HH:MM) - opzionale", "")
ora_riferimento = ora_input if ora_input else ora_corrente

if destinazione:
    st.button("Cerca Orari")
    # Mostra la mappa del percorso selezionato
import pydeck as pdk
if partenza and destinazione:
    mostra_mappa = st.checkbox("🗺️ Mostra mappa del percorso selezionato", value=False)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(f"### 🕒 Prossima corsa da {partenza} a {destinazione}:")
    tipo = "feriale" if giorno in ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"] else "festivo"
    corse = orari.get(tipo, {}).get(direzione_key, [])
    orari_disponibili = filtra_orari_completi(corse, partenza, destinazione, ora_riferimento)
    if orari_disponibili:
        st.markdown(f"<b>{orari_disponibili[0]['partenza']} ➝ {orari_disponibili[0]['arrivo']}</b>", unsafe_allow_html=True)
    else:
        st.markdown("<i>Nessuna corsa disponibile</i>", unsafe_allow_html=True)
with col2:
    st.markdown(f"### 🚏 Tratta selezionata:<br><b>{partenza} ➝ {destinazione}</b>", unsafe_allow_html=True)

if mostra_mappa:
        idx_start = list(map_data.keys()).index(partenza)
        idx_end = list(map_data.keys()).index(destinazione)
        fermate_tratte = list(map_data.items())[idx_start:idx_end + 1] if idx_start <= idx_end else list(map_data.items())[idx_end:idx_start + 1][::-1]
        tratta_df = pd.DataFrame(fermate_tratte, columns=["fermata", "coords"])
        tratta_df[["lat", "lon"]] = pd.DataFrame(tratta_df["coords"].tolist(), index=tratta_df.index)
        st.pydeck_chart(pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(latitude=tratta_df['lat'].mean(), longitude=tratta_df['lon'].mean(), zoom=11, pitch=0),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=tratta_df.assign(color=[
                        [0, 255, 0, 200] if f == partenza else [255, 0, 0, 200] if f == destinazione else [0, 150, 255, 180]
                        for f in tratta_df["fermata"]
                    ]),
                    get_position='[lon, lat]',
                    get_color='color',
                    get_radius=350,
                    pickable=True,
                ),
                pdk.Layer(
                    "LineLayer",
                    data=tratta_df,
                    get_source_position='[lon, lat]',
                    get_target_position='[lon, lat]',
                    get_color='[0, 100, 200]',
                    get_width=4,
                    pickable=False,
                    auto_highlight=True,
                )
            ],
            tooltip={"text": "{fermata}"}
        ))

st.markdown("""
<div style='font-size: 14px; padding-top: 10px;'>
  <b>Legenda:</b><br>
  🟢 Fermata di partenza<br>
  🔴 Fermata di arrivo<br>
  🔵 Fermate intermedie
</div>
""", unsafe_allow_html=True)

solo_scolastiche = st.checkbox("Mostra solo corse scolastiche")


if st.session_state.get("Cerca Orari") and destinazione:
    tipo = "feriale" if giorno in ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì"] else "festivo"
    corse = orari.get(tipo, {}).get(direzione_key, [])
    if solo_scolastiche:
        corse = [c for c in corse if '#ES' in c.get('note', '')]
    orari_filtrati = filtra_orari_completi(corse, partenza, destinazione, ora_riferimento)

    if orari_filtrati:
        st.markdown(f"### 🕒 Corse disponibili da **{partenza}** a **{destinazione}**")
        import pandas as pd
        for r in orari_filtrati:
            if '#ES' in r.get("note", ""):
                r["note"] = "🟡🚌 " + r["note"]
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
