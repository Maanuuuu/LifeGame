# LifeGame

## Juego de la Vida de Conway
El Juego de la Vida es un autómata celular diseñado por el matemático John Conway. Es un juego de cero jugadores que simula la evolución de una población de células en una cuadrícula basada en ciertas reglas.

### Estructuras Discretas II
Este proyecto forma parte del curso de Estructuras Discretas II, donde se exploran los conceptos de autómatas celulares y su aplicación en simulaciones.

### Manuel David Nava Díaz
Desarrollado por Manuel David Nava Díaz, estudiante de la sección 306C1.

## Descripción del Proyecto
El Juego de la Vida se basa en una cuadrícula bidimensional de células, donde cada célula puede estar viva o muerta. El estado de las células se actualiza en pasos discretos según reglas específicas.

### Reglas del Juego
1. **Supervivencia**: Una célula viva con 2 o 3 vecinos vivos permanece viva.
2. **Muerte**: Una célula viva con menos de 2 o más de 3 vecinos vivos muere.
3. **Nacimiento**: Una célula muerta con exactamente 3 vecinos vivos se convierte en una célula viva.

### Características
- Simulación visual del Juego de la Vida.
- Interfaz intuitiva para iniciar y detener la simulación.
- Configuración de patrones iniciales (como gliders y blinkers).

## Requisitos
- Python 3.8 o superior
- Biblioteca `turtle`, `matplotlib`, `numpy`  para los calculos y visualización gráfica

## Instalación
Para ejecutar el juego, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Maanuuuu/LifeGame

2. Instala las librerias Numpy, Matplotlib, Time, Turtle
   ```bash
   pip install numpy matplotlib turtle
