import numpy as np
import cv2
import os
import random


# Seleziona casualmente un'immagine dalla cartella
def random_img():
    folder_path = "../img/"  # path della cartella che contiene le immagini
    image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # Seleziona casualmente un'immagine dalla lista
    random_image = random.choice(image_files)
    example_image = cv2.imread(f"{folder_path}" + random_image)
    example_image = cv2.resize(example_image, cell_size[:2])  # Ridimensiona l'immagine alla dimensione della cella

    return example_image


map_width = 4
map_height = 4
cell_size = (224, 224)  # Dimensione delle immagini delle celle

# Inizializzazione della mappa come una matrice di immagini vuote
map_matrix = np.empty((map_height, map_width), dtype=object)

# Definizione della griglia di posizioni nella mappa
#grid_positions = [(i, j) for i in range(map_height) for j in range(map_width)]


# Simulazione della raccolta delle immagini dal robot
def add_image(position, img):
    # Simulazione di un'immagine acquisita dal robot in base alla posizione nella mappa
    x,y = position
    map_matrix[x, y] = img


for i in range(map_height):
    for j in range(map_width):
        add_image([i, j], random_img())


#Per visualizzare:
# Crea una grande immagine che rappresenta l'intera mappa
map_image = np.zeros((map_height * cell_size[0], map_width * cell_size[1], 3), dtype=np.uint8)

# Riempie la grande immagine con le immagini delle celle
for i in range(map_height):
    for j in range(map_width):
        map_image[i * cell_size[0]: (i + 1) * cell_size[0], j * cell_size[1]: (j + 1) * cell_size[1]] = map_matrix[i, j]

# Visualizza l'intera mappa
cv2.imshow('Map', map_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Concatena le immagini lungo l'asse delle colonne per creare righe
rows = [np.concatenate(self.grid[i, :], axis=1) for i in range(self.width)]

# Concatena le righe per creare l'intera mappa
map_image = np.concatenate(rows, axis=0)

# Visualizza l'immagine della mappa
cv2.imshow("Mappa", map_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

