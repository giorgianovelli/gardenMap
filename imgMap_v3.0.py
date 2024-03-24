import cv2
import os
import random
import constants as c
import map
from datetime import datetime


# Seleziona casualmente un'immagine dalla cartella
def random_img():
    image_files = [file for file in os.listdir(c.FOLDER_PATH) if file.endswith(('.jpg', '.jpeg', '.png'))]
    random_image = random.choice(image_files)
    example_image = cv2.imread(f"{c.FOLDER_PATH}" + random_image)
    example_image = cv2.resize(example_image, c.CELL_SIZE)  # Ridimensiona l'immagine alla dimensione della cella

    return example_image


if __name__ == "__main__":
    #simulazione
    garden_map = map.Map(c.MAP_WIDTH, c.MAP_HEIGHT, c.CELL_SIZE)

    for i in range(c.MAP_HEIGHT):
        for j in range(c.MAP_WIDTH):
            tag_info = f'Timestamp: {(datetime.now()).strftime("%Y-%m-%d_%H-%M")}'
            garden_map.update_map(i, j, random_img(), tag_info)


    # Visualizza l'intera mappa con le immagini
    garden_map.display_map()


    """
    tag_info = f'Timestamp: {(datetime.now()).strftime("%Y-%m-%d_%H-%M")}'
    garden_map.update_map(0, 0, random_img(),tag_info)
    garden_map.update_map(1, 1, random_img(),tag_info)
    garden_map.update_map(2, 2, random_img(),tag_info)
    garden_map.display_images()
    """




