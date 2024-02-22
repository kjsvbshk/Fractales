import turtle
import math

t = turtle.Turtle()
t.speed(0)

turtle.penup() 
turtle.goto(270, 30)  
turtle.dot(10, "blue")  
turtle.hideturtle()

#calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

def draw_rotated_square(t, angle, lado1,lado2, angle_test):

    t.penup()
    new_x, new_y = rotate_point(0, 0, angle)  # (Posicion inicial en x, posicion inicial en y, angulo a girar)
    
    t.goto(-100, -50)
    t.setheading(angle_test)
    t.pendown()

for i in range(1):
    t.forward(300)
    t.left(90)
    t.forward(300)
    t.left(90+45)
    t.forward(425)

turtle.done()