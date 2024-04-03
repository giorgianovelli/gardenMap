import numpy as np
import random
import time
import constants as c
import map
import cv2
import os

def random_img():
    image_files = [file for file in os.listdir(c.FOLDER_PATH) if file.endswith(('.jpg', '.jpeg', '.png'))]
    random_image = random.choice(image_files)
    example_image = cv2.imread(f"{c.FOLDER_PATH}" + random_image)
    example_image = cv2.resize(example_image, c.CELL_SIZE)  # Ridimensiona l'immagine alla dimensione della cella

    return example_image

def ingrandisci_matrice(matrice): # questo metoo può essere aggiunto nella classe per definire la mappa
    righe, colonne = len(matrice), len(matrice[0])
    print(righe, colonne)
    nuove_righe = 4 + righe  # 120+righe
    nuove_colonne = 4 + colonne  # 120+colonne

    nuova_matrice = np.zeros((nuove_righe, nuove_colonne), dtype=np.dtype('U1'))
    for i in range(righe):
        for j in range(colonne):
            nuova_matrice[i + 2][j + 2] = matrice[i][j]  # i+60,j+60

    return nuova_matrice




# --------------------------------------------------------------------------


def streamin(): # generatore dati
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
    #print(vettore)
    return a, b, c


#print(streamin())


def processData(data): # converte direzione e misura
    sens = 0

    # rimuove il prefisso "0b" e assicura che la rappresentazione
    # abbia una lunghezza di 8 bit riempiendo con zeri a sinistra
    bit_representation = bin(data)[2:].zfill(8)
    add_bit = bit_representation[0:2].zfill(8) # due bit per direzione
    measure_bit = bit_representation[2:].zfill(8) # sei bit per misurazione

    if (int(add_bit, 2) == 0): sens = 1  # left
    if (int(add_bit, 2) == 1): sens = 2  # front
    if (int(add_bit, 2) == 2): sens = 3  # right
    if (int(add_bit, 2) == 3): sens = 4  # back

    measure = int(measure_bit, 2)

    return sens, measure


if __name__ == "__main__":

    # inizializza la posizione del robot al centro
    i = 0
    j = 0

    cont = 3
    matrix_map = map.Map(c.MAP_WIDTH, c.MAP_HEIGHT, c.CELL_SIZE)

    while (cont > 0):
        start_time = time.time()  # Memorizza il tempo di inizio
        time.sleep(2)  # Attende un secondo
        timer = time.time()  # Memorizza il tempo di fine
        cont -= 1

        while (timer >= 2):
            timer = 0
            pacchetto_dati = streamin()

            if (pacchetto_dati[0] == 255 and pacchetto_dati[2] == 254):
                print(processData(pacchetto_dati[1]))
                byte_utile = processData(pacchetto_dati[1])  # Esegue la funzione e memorizza il risultato
                sens = byte_utile[0]  # direzione
                measure = byte_utile[1]  # distanza

                if i >= len(matrix_map.grid) - 3:
                    print("oltre indice 1")

                if i == 2:
                    print("oltre indice 2")

                if j >= len(matrix_map.grid) - 3:
                    print("oltre indice 3")

                if j == 2:
                    print("oltre indice 4")

                if (byte_utile[0] == 2):  # front
                    i -= 1
                    matrix_map.update_map(i,j,random_img())

                elif (byte_utile[0] == 4):  # back
                    i += 1
                    matrix_map.update_map(i, j, random_img())

                elif (byte_utile[0] == 1):  # left
                    j -= 1
                    matrix_map.update_map(i, j, random_img())

                elif (byte_utile[0] == 3):  # right
                    j += 1  # passo 1 da sostituire con measure
                    matrix_map.update_map(i, j, random_img())

        matrix_map.display_map()

    matrix_map.display_map()
