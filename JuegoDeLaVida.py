import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Configuración de la cuadrícula
GRID_SIZE = 50  # Tamaño de la cuadrícula (50x50)
ON = 1          # Representación de una célula viva
OFF = 0         # Representación de una célula muerta

def Determinar_Celulas_Vivas(size):
    
    # Solo el 10% de las células totales estarán vivas
    return np.random.choice([ON, OFF], size*size, p=[0.2, 0.8]).reshape(size, size)

def ActualizacionDeGeneraciones(frame_num, img, grid, size):
    """Actualiza la cuadrícula en cada generación"""
    new_grid = grid.copy()
    for i in range(size):
        for j in range(size):
            total = (grid[i, (j-1)%size] + grid[i, (j+1)%size] +
                        grid[(i-1)%size, j] + grid[(i+1)%size, j] +
                        grid[(i-1)%size, (j-1)%size] + grid[(i-1)%size, (j+1)%size] +
                        grid[(i+1)%size, (j-1)%size] + grid[(i+1)%size, (j+1)%size])
                
            # Aplicamos las Reglas del Juego de la Vida
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF  # Muerte por soledad o sobrepoblación
            else:
                if total == 3:
                    new_grid[i, j] = ON  # Nacimiento de la celula

    # Actualización del diagrama
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Inicialización del juego
def main():
    grid = Determinar_Celulas_Vivas(GRID_SIZE)

    # Figura donde aparecerá el diagrama
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap='gray')
    ani = animation.FuncAnimation(fig, ActualizacionDeGeneraciones, fargs=(img, grid, GRID_SIZE),
                                frames=10, interval=200, save_count=50)
    plt.show()

# Ejecución del juego
main()
