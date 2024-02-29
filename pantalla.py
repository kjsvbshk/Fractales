import turtle
import colorsys
turtle.speed(0)
windows = turtle.Screen()
windows.bgcolor("black")
for i in range(500000000):
    hue = i/125.0
    color  = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    turtle.pencolor(color)
    turtle.forward(50+i)
    turtle.right(91)
turtle.done()