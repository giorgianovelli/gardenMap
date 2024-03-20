import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# Parametri della mappa
map_size = 10  # Dimensioni della mappa in metri
resolution = 0.5  # Risoluzione della mappa in metri

# Creazione di una mappa vuota
grid_size = int(map_size / resolution)
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# Posizione iniziale del robot
robot_pose = np.array([5.0, 5.0])  # Inizializzato al centro della mappa


# Funzione per aggiornare la mappa con nuove letture
def update_map(sensor_data, robot_pose, start_img, img):

    x, y = world_to_grid(robot_pose)
    grid[y][x] = start_img

    for measurement in sensor_data:
        measurement_world = sensor_to_world(measurement, robot_pose)
        # print(measurement_world)
        x, y = world_to_grid(measurement_world)
        # print(x, y)
        grid[y][x] = img



# Funzione per convertire coordinate del mondo in coordinate della griglia
def world_to_grid(world_coordinates):
    return np.floor(world_coordinates / resolution).astype(int)


# Funzione per convertire misurazioni del sensore in coordinate del mondo
def sensor_to_world(sensor_measurement, robot_pose):
    return sensor_measurement + robot_pose


# Esempio di utilizzo, sostituire con ciclo, attenzione ai limiti
#sensor_data = np.array([[0.5, 0.0], [1.0, 0.0], [1.5, 0.0], [2.0, 0.0], [2.5, 0.0]])  # Esempio di dati del sensore
sensor_data = np.array([[0.5, 0.0]])
# Carica l'immagine JPEG

img = Image.open('img/cropped_cutgrass.jpg')

# Converte l'immagine in una matrice NumPy
image_matrix = img.load()


larghezza, altezza = img.size
# Stampa le dimensioni dell'immagine
print("Dimensioni dell'immagine:", larghezza, "x", altezza)

update_map(sensor_data, robot_pose, image_matrix, image_matrix)

for row in grid:
    print(row)
