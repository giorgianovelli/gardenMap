import numpy as np
import cv2

print(cv2.__version__)
# Definizione delle dimensioni della mappa e la dimensione delle celle (immagini)
map_width = 4
map_height = 4
cell_size = (224, 224)  # Dimensione delle immagini delle celle

# Inizializzazione della mappa come una matrice di immagini vuote
map_matrix = np.empty((map_height, map_width), dtype=object)

# Carica un'immagine di esempio per riempire la mappa
example_image = cv2.imread('img/long_oj.jpg')
example_image = cv2.resize(example_image, cell_size[:2])  # Ridimensiona l'immagine alla dimensione della cella

# Riempie la mappa con l'immagine di esempio
for i in range(map_height):
    for j in range(map_width):
        map_matrix[i, j] = example_image  # Ogni cella contiene l'immagine di esempio

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
