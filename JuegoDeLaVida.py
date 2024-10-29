import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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
