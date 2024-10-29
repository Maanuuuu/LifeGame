import turtle


def dibujar_triangulo(puntos, color):
    """Dibuja un triángulo con los puntos dados y el color especificado."""
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for punto in puntos:
        turtle.goto(punto)
        
        
    turtle.goto(puntos[0])  
    turtle.end_fill()

def sierpinski(puntos, profundidad):
    """Dibuja el triángulo de Sierpinski recursivamente."""
    if profundidad == 0:
        dibujar_triangulo(puntos, "blue")  # Se dibuja el triangulo
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
        
        
        turtle.penup()
        turtle.goto(puntos[1])  
        turtle.pendown()
        
        sierpinski([puntos[1], punto_medio1, punto_medio2], profundidad - 1)
        
       
        turtle.penup()
        turtle.goto(puntos[2])  
        turtle.pendown()
        
        sierpinski([puntos[2], punto_medio2, punto_medio3], profundidad - 1)

def main():
    """Función principal para configurar la tortuga y dibujar el triángulo."""
    turtle.speed(0)  
    
    # Puntos del triángulo inicial
    puntos = [(-200, -150), (0, 200), (200, -150)]
    
    
    turtle.penup()
    turtle.goto(puntos[0])  
    turtle.pendown()

    # Dibuja el triángulo de Sierpinski con profundidad 4
    sierpinski(puntos, profundidad=4)
    
    
    turtle.done()

if __name__ == "__main__":
    main()
