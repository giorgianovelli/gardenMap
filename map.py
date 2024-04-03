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
        self.tags[x][y] = {tag}

    # aggiungere metodo per ingrandire matrice

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

        # Concatena le immagini lungo l'asse delle colonne per creare righe
        rows = [np.concatenate(self.grid[i, :], axis=1) for i in range(self.width)]

        # Concatena le righe per creare l'intera mappa
        map_image = np.concatenate(rows, axis=0)

        # Visualizza l'immagine della mappa
        cv2.imshow("Mappa SLAM", map_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






