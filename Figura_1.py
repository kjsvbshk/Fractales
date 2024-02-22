import turtle
turtle.speed(0)
turtle.pensize(2)
lado1=250
lado2=65
def dibujar_Rectangulo(angulo):
    turtle.setheading(angulo)

    for i in range(5):
        turtle.forward(lado1)
        turtle.left(90) 
        turtle.forward(lado2)     
        turtle.left(90)    
        turtle.forward(lado1)
        turtle.left(90)    
        turtle.forward(lado2)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(lado2)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(lado2)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(144)

        


# Ángulo inicial
angulo_inicial = 0
angulo_final = angulo_inicial+36


turtle.penup()
turtle.goto(0,0)
turtle.pendown()
dibujar_Rectangulo(angulo_inicial)

turtle.penup()
turtle.goto(0,-69)
turtle.down()
dibujar_Rectangulo(angulo_final)


turtle.done()
    