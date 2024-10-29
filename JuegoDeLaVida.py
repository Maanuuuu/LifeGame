import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuración de la cuadrícula
GRID_SIZE = 50  # Tamaño de la cuadrícula (50x50)
ON = 1          # Representación de una célula viva
OFF = 0         # Representación de una célula muerta

def random_grid(size):
    
    # Solo el 10% de las células totales estarán vivas
    return np.random.choice([ON, OFF], size*size, p=[0.2, 0.8]).reshape(size, size)


# Inicialización del juego
def main():
    grid = random_grid(GRID_SIZE)

    # Figura donde aparecerá el diagrama
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='gray')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, GRID_SIZE),
                                frames=10, interval=200, save_count=50)
    plt.show()

# Ejecución del juego
main()
