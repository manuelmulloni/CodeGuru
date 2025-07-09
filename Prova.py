def calcola_media(lista_numeri):
    somma = sum(lista_numeri)
    conta = len(lista_numeri)
    if conta == 0:
        return 0
    return somma / conta


def stampa_risultato(valore):
    print(f"La media è: {valore}")


# ⚠️ ERRORE DI BATTITURA: funzione chiamata in modo errato
media = calcoola_media([4, 8, 15, 16, 23, 42])  # <-- errore: 'calcoola' invece di 'calcola'
stampa_risultato(media)