import cv2
import os
import random
import constants as c
import map


def random_img():
    folder_path = "img/"  # path della cartella che contiene le immagini
    image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # Seleziona casualmente un'immagine dalla lista
    random_image = random.choice(image_files)
    example_image = cv2.imread(f"{folder_path}" + random_image)
    example_image = cv2.resize(example_image, c.CELL_SIZE[:2])  # Ridimensiona l'immagine alla dimensione della cella

    return example_image


if __name__ == "__main__":

    garden_map = map.Map(c.MAP_WIDTH, c.MAP_HEIGHT, c.CELL_SIZE)

    for i in range(c.MAP_HEIGHT):
        for j in range(c.MAP_WIDTH):
            garden_map.update_cell(i, j, random_img())

    """
    garden_map.update_cell(0, 0, random_img())
    garden_map.update_cell(1, 1, random_img())
    garden_map.update_cell(2, 2, random_img())
    
    """

    # Visualizza l'intera mappa con le immagini
    garden_map.display_map()
