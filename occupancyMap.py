import matplotlib.pyplot as plt
import numpy as np

# Parametri della mappa
map_size = 10  # Dimensioni della mappa in metri
resolution = 0.5  # Risoluzione della mappa in metri

# Creazione di una mappa vuota
grid_size = int(map_size / resolution)
occupancy_grid = np.zeros((grid_size, grid_size))

# Posizione iniziale del robot
robot_pose = np.array([5.0, 5.0])  # Inizializzato al centro della mappa


# Funzione per aggiornare la mappa con nuove letture
def update_map(sensor_data, robot_pose):
    # Aggiorna la mappa sulla base dei dati del sensore e della posizione del robot

    # Occupa la cella corrispondente alla posizione attuale del robot
    x, y = world_to_grid(robot_pose)
    occupancy_grid[x, y] = 1

    # Aggiorna la mappa con dati del sensore
    for measurement in sensor_data:
        # Converti le misurazioni in coordinate del mondo
        measurement_world = sensor_to_world(measurement, robot_pose)
        #print(measurement_world)
        # Converti le coordinate del mondo in coordinate della griglia
        x, y = world_to_grid(measurement_world)
        #print(x, y)
        # Occupa la cella corrispondente nella mappa
        occupancy_grid[x, y] = 1


# Funzione per convertire coordinate del mondo in coordinate della griglia
def world_to_grid(world_coordinates):
    return np.floor(world_coordinates / resolution).astype(int)


# Funzione per convertire misurazioni del sensore in coordinate del mondo
def sensor_to_world(sensor_measurement, robot_pose):
    return sensor_measurement + robot_pose


# Esempio di utilizzo, sostituire con ciclo, attenzione ai limiti
sensor_data = np.array([[0.5, 0.0], [1.0, 0.0], [1.5, 0.0], [2.0, 0.0], [2.5, 0.0]])  # Esempio di dati del sensore
update_map(sensor_data, robot_pose)


# Visualizzazione della mappa
plt.imshow(occupancy_grid, cmap='gray', origin='lower', extent=(0, map_size, 0, map_size))
plt.show()
