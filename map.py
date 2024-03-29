import numpy as np
import cv2

import constants as c


class Map:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.empty((height, width), dtype=object)  # Matrice per memorizzare le immagini
        self.tags = np.empty((height, width), dtype=object)

    # Aggiorna la cella della mappa con l'immagine acquisita dal robot
    def update_map(self, x, y, image, tag=None):
        self.grid[y][x] = image
        self.tags[y][x] = {tag}

    # Mostra la singola immagine per cella
    def display_images(self):
        for y in range(self.height):
            for x in range(self.width):
                image = self.grid[y][x]
                tag_info = self.tags[y][x]
                print(tag_info)
                if image is not None:
                    cv2.imshow(f'Cella ({x}, {y})', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



    # Visualizza l'intera mappa con le immagini, da sistemare se le celle sono vuote
    def display_map(self):
        # Crea una grande immagine che rappresenta l'intera mappa
        map_image = np.zeros((c.MAP_HEIGHT * c.CELL_SIZE[0], c.MAP_WIDTH * c.CELL_SIZE[1], 3), dtype=np.uint8)

        # Riempie la grande immagine con le immagini delle celle
        for i in range(self.height):
            for j in range(self.width):
                map_image[i * self.cell_size[0]: (i + 1) * self.cell_size[0], j * self.cell_size[1]: (j + 1) * self.cell_size[1]] = self.grid[i, j]

        # Visualizza l'intera mappa
        cv2.imshow('Map', map_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



