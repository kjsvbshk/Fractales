import turtle
import math
t = turtle.Turtle()
t.pensize(2)
t.speed(0)
#calcular nuevas coordenadas después de la rotación
def rotate_point(x, y, angle):
    angle = math.radians(angle)
    new_x = x * math.cos(angle) - y * math.sin(angle)
    new_y = x * math.sin(angle) + y * math.cos(angle)
    return new_x, new_y

# dibujar la siguiente figura en la misma posicion
def draw_rotated_square(t, angle, lado):
    t.penup()
    new_x, new_y = rotate_point(-100, -100, angle)  # (Posicion inicial en x, posicion inicial en y, angulo a girar)
    t.goto(new_x, new_y)
    t.setheading(angle)
    t.pendown()
    for i in range(4):
        t.forward(lado)
        t.left(90)

    t.left(90)
    t.forward(60)#abajo alto
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(60)

    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(75)

    t.left(180)
    t.forward(lado)

    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(75)
    t.left(90)
    t.forward(60)

    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(75)

    t.left(180)
    t.forward(lado)
 
  

    

#parametros
lado = 200 #estatico si lo mueve la caga
incremento_angulo = 36
cantidad_figuras = 5

# Dibujar figura
for i in range(cantidad_figuras):
    
    draw_rotated_square(t, i * incremento_angulo, lado)


turtle.done()
