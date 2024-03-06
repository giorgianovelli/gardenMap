import random
import numpy as np
import time


# codice che stampa ogni 2 secondi un aggiornamento randomico della mappa in termini di direzione
# non ho aggiunto l'aggiornamento di distanza per leggibilità del codice in fase di print
# measure = byte_utile[1]  -----> distanza rilevata
# è sufficiente aggiungere uno spostamento di measure anziché di uno in riga 113,121,128,135 ed adattare la funzione ingrandisci matrice
# al momento ingrandisci matrice aumenta di due caselle ogni lato, deve farlo di 60 caselle ci sono dei commenti dove questo andrebbe fatto
# es riga 16


def ingrandisci_matrice(matrice):
    righe, colonne = len(matrice), len(matrice)
    nuove_righe = 4 + righe  # 120+righe
    nuove_colonne = 4 + colonne  # 120+colonne

    nuova_matrice = np.zeros((nuove_righe, nuove_colonne), dtype=np.dtype('U1'))
    for i in range(righe):
        for j in range(colonne):
            nuova_matrice[i + 2][j + 2] = matrice[i][j]  # i+60,j+60

    return nuova_matrice


def streamin():
    vettore = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
    a = 0
    b = 0
    c = 0
    for i in range(8, 15):
        bit = random.randint(0, 1)
        vettore[i] = bit

    for i in range(0, 8):
        a += vettore[7 - i] * 2 ** i

    for i in range(8, 16):
        b += vettore[23 - i] * 2 ** (i - 8)

    for i in range(16, 24):
        c += vettore[39 - i] * 2 ** (i - 16)

    return a, b, c


def processData(data):
    sens = 0
    bit_representation = bin(data)[2:].zfill(8)

    add_bit = bit_representation[0:2].zfill(8)
    measure_bit = bit_representation[2:].zfill(8)

    if (int(add_bit, 2) == 0): sens = 1  # left
    if (int(add_bit, 2) == 1): sens = 2  # front
    if (int(add_bit, 2) == 2): sens = 3  # right
    if (int(add_bit, 2) == 3): sens = 4  # back

    measure = int(measure_bit, 2)

    return sens, measure


row = 9
coloumn = 9
i = 4
j = 4
matrice = np.zeros((row, coloumn), dtype=np.dtype('U1'))
matrice[i, j] = chr(35)

while (True):
    start_time = time.time()  # Memorizza il tempo di inizio
    time.sleep(2)  # Attende un secondo
    timer = time.time()  # Memorizza il tempo di fine

    while (timer >= 2):
        timer = 0
        pacchetto_dati = streamin()

        if (pacchetto_dati[0] == 255 and pacchetto_dati[2] == 254):
            print(processData(pacchetto_dati[1]))
            byte_utile = processData(pacchetto_dati[1])  # Esegue la funzione e memorizza il risultato
            sens = byte_utile[0]  # direzione
            measure = byte_utile[1]  # distanza

            if i >= len(matrice) - 3:
                matrice[i, j] = ''
                matrice = ingrandisci_matrice(matrice)  # ingrandisco la matrice di 4 quindi riporto il cursore dov'era
                i += 2
                j += 2  # +60 anziché +2 in ogni if

            if i == 2:
                matrice[i, j] = ''
                matrice = ingrandisci_matrice(matrice)
                i += 2
                j += 2

            if j >= len(matrice) - 3:
                matrice[i, j] = ''  # aggiunto
                matrice = ingrandisci_matrice(matrice)
                i += 2
                j += 2

            if j == 2:
                matrice[i, j] = ''
                matrice = ingrandisci_matrice(matrice)
                i += 2
                j += 2

            if (byte_utile[0] == 2):  # front

                i -= 1
                matrice[i + 1, j] = ''
                matrice[i, j] = chr(35)



            elif (byte_utile[0] == 4):  # back

                i += 1
                matrice[i - 1, j] = ''
                matrice[i, j] = chr(35)


            elif (byte_utile[0] == 1):  # left

                j -= 1
                matrice[i, j + 1] = ''
                matrice[i, j] = chr(35)


            elif (byte_utile[0] == 3):  # right

                j += 1  # passo 1 da sostituire con measure
                matrice[i, j - 1] = ''
                matrice[i, j] = chr(35)

            print(matrice)


