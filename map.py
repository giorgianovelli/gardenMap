import numpy as np
import cv2


class Map:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = np.empty((height, width), dtype=object)  # Matrice per memorizzare le immagini
        self.tags = np.empty((height, width), dtype=object)  # Matrice per memorizzare info aggiuntive

    # Aggiorna la cella della mappa con l'immagine acquisita dal robot
    def update_map(self, x, y, image, tag=None):
        self.grid[x][y] = image
        # self.tags[x][y] = {tag}


    # todo se aggiungo anche altre info, va ingrandita anche la tabella dei tag
    def ingrandisci_matrice(self): # test su una occupancy map
        righe, colonne = len(self.grid), len(self.grid[0])
        self.width = 4 + righe  # 120+righe
        self.height = 4 + colonne  # 120+colonne

        nuova_matrice = np.empty((self.width, self.height), dtype=object)
        for i in range(righe):
            for j in range(colonne):
                nuova_matrice[i + 2][j + 2] = self.grid[i][j]  # i+60,j+60

        self.grid = nuova_matrice


    # Mostra la singola immagine per cella
    def display_images(self):
        for x in range(self.width):
            for y in range(self.height):
                image = self.grid[x][y]
                tag_info = self.tags[x][y]
                print(tag_info)
                if image is not None:
                    cv2.imshow(f'Cella ({x}, {y})', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Visualizza l'intera mappa con le immagini
    def display_map(self):
        # controlla se nella matrice ci sono celle vuote senza immagini
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i, j] is None:
                    self.grid[i, j] = np.zeros((self.cell_size[0], self.cell_size[1], 3), dtype=np.uint8)  # Immagine nera
        """
        # Concatena le immagini lungo l'asse delle colonne per creare righe
        rows = [np.concatenate(self.grid[i, :], axis=1) for i in range(self.width)]

        # Concatena le righe per creare l'intera mappa
        map_image = np.concatenate(rows, axis=0)

        # Visualizza l'immagine della mappa
        cv2.imshow("Mappa SLAM", map_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        """
        # Crea una grande immagine che rappresenta l'intera mappa
        map_image = np.zeros((self.height * self.cell_size[0], self.width * self.cell_size[1], 3), dtype=np.uint8)

        # Riempie la grande immagine con le immagini delle celle
        for i in range(self.height):
            for j in range(self.width):
                map_image[i * self.cell_size[0]: (i + 1) * self.cell_size[0], j * self.cell_size[1]: (j + 1) * self.cell_size[1]] = self.grid[i, j]

        # Visualizza l'intera mappa
        cv2.imshow('Map', map_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






