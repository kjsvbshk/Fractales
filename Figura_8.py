import turtle
turtle.speed(0)
def dibujar_cuadrado(tortuga, lado):
    for _ in range(4):
        tortuga.forward(lado)
        tortuga.left(90)

def main():
    lado_cuadrado = 300
    angulo_giro = 65
    posicion_x = lado_cuadrado / 2

    tortuga = turtle.Turtle()
    tortuga.pencolor("black")
    tortuga.pensize(2)
    

    def Dibujar_cuadrado():
        for i in range(4):
            tortuga.forward(lado_cuadrado)
            tortuga.left(90)
        tortuga.forward(120)
        tortuga.left(90)
        tortuga.forward(lado_cuadrado)
        tortuga.right(90)
        tortuga.forward(60)
        tortuga.right(90)
        tortuga.forward(lado_cuadrado)
        tortuga.right(90)
        tortuga.forward(120)

    #Dibujar el primer cuadrado
    Dibujar_cuadrado()
    tortuga.hideturtle()

    # Levantar la pluma
    tortuga.penup()

    # Mover la tortuga a la posición inicial del segundo cuadrado
    tortuga.setposition(posicion_x - 78, 347)

    # Girar la tortuga
    tortuga.left(angulo_giro)

    # Bajar la pluma
    tortuga.pendown()

    # Dibujar el segundo cuadrado
    Dibujar_cuadrado()
    tortuga.hideturtle()

    tortuga.penup()
    tortuga.setposition(posicion_x - 200, 210)
    tortuga.right(angulo_giro + 65)

    tortuga.pendown()

    #Dibujar el tercer cuadrado
    Dibujar_cuadrado()
    tortuga.hideturtle()

    turtle.done()


main()
