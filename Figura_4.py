import turtle
turtle.pensize(2)
turtle.speed(0)
def interna():
    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()

    for i in range(12):
        turtle.forward(350)
        turtle.right(150)
        print("Coordenadas: ",turtle.position())
def externa(angle):
    turtle.penup()
    turtle.goto(-75,-10)
    turtle.pendown()
    turtle.setheading(angle)
    for i in range (3):
        turtle.forward(300)
        turtle.left(120)
        turtle.forward(200)
        turtle.left(120)

#interna()
   
externa(0)
turtle.done()