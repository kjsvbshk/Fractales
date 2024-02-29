import turtle
import colorsys
turtle.pensize(2)
def dibujo(tam, profund):
    if profund == 0:
        return
    else:
        turtle.forward(tam)
        turtle.left(45)
        dibujo(tam*2/3, profund-1)
        turtle.right(90)
        dibujo(tam*2/3, profund-1)
        turtle.left(45)
        turtle.backward(tam)


turtle.speed(0)  
turtle.penup()  
turtle.goto(-100, 0)  
turtle.pendown()  

for i in range (1):
    hue = i/125.0
    color  = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    dibujo(100, 10)  

turtle.done()
