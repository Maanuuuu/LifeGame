import turtle
import time

def dibujar_triangulo(puntos, color):
    """Dibuja un triángulo con los puntos dados y el color especificado."""
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for punto in puntos:
        turtle.goto(punto)
        time.sleep(0.1)  # Retraso para la animación
        
    turtle.goto(puntos[0])  # Regresa al inicio
    turtle.end_fill()

def sierpinski(puntos, profundidad):
    """Dibuja el triángulo de Sierpinski recursivamente."""
    if profundidad == 0:
        dibujar_triangulo(puntos, "blue")  # Dibuja un triángulo sólido
    else:
        # Calcula los puntos medios
        punto_medio1 = (
            (puntos[0][0] + puntos[1][0]) / 2, 
            (puntos[0][1] + puntos[1][1]) / 2
        )
        punto_medio2 = (
            (puntos[1][0] + puntos[2][0]) / 2, 
            (puntos[1][1] + puntos[2][1]) / 2
        )
        punto_medio3 = (
            (puntos[2][0] + puntos[0][0]) / 2, 
            (puntos[2][1] + puntos[0][1]) / 2
        )
        
        # Llamadas recursivas para los triángulos más pequeños
        sierpinski([puntos[0], punto_medio1, punto_medio3], profundidad - 1)
        
        # Levanta el lápiz antes de mover a la siguiente posición
        turtle.penup()
        turtle.goto(puntos[1])  # Mueve a la segunda esquina
        turtle.pendown()
        
        sierpinski([puntos[1], punto_medio1, punto_medio2], profundidad - 1)
        
        # Levanta el lápiz antes de mover a la siguiente posición
        turtle.penup()
        turtle.goto(puntos[2])  # Mueve a la tercera esquina
        turtle.pendown()
        
        sierpinski([puntos[2], punto_medio2, punto_medio3], profundidad - 1)

def main():
    """Función principal para configurar la tortuga y dibujar el triángulo."""
    turtle.speed(0)  # Velocidad más rápida
    turtle.hideturtle()  # Oculta el cursor
    
    # Vértices iniciales del triángulo
    puntos = [(-200, -150), (0, 200), (200, -150)]
    
    # Posiciona la tortuga sin dibujar
    turtle.penup()
    turtle.goto(puntos[0])  # Mueve a la primera esquina
    turtle.pendown()

    # Dibuja el triángulo de Sierpinski con profundidad 4
    sierpinski(puntos, profundidad=4)
    
    # Finaliza la animación y espera a que se cierre la ventana
    turtle.done()

if __name__ == "__main__":
    main()
