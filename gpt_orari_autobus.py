
import json
from datetime import datetime

# Caricamento del file JSON degli orari
with open('orari_autobus.json', 'r', encoding='utf-8') as f:
    orari_data = json.load(f)

def trova_orari(partenza, destinazione, giorno_settimana, ora_richiesta=None):
    # Capire se giorno feriale o festivo
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
                    # Cerca la corsa successiva all'ora richiesta
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

# Esempi di utilizzo
if __name__ == "__main__":
    print("Benvenuto nel Mini-GPT degli orari Autobus!")
    partenza = input("Da dove parti? ")
    destinazione = input("Dove vuoi andare? ")
    giorno = input("Che giorno della settimana? (es: lunedì, domenica) ")
    ora = input("A che ora (formato HH:MM, opzionale)? Lascia vuoto se non ti interessa: ")

    ora = ora if ora else None
    risposta = trova_orari(partenza, destinazione, giorno, ora)
    print("\nRisultato:")
    print(risposta)
