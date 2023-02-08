#the author's name: saerin bong

import turtle
func = turtle.Turtle()

def draw_sq(x):
    func.color(x)
    func.forward(100)
    func.right(90)
    func.forward(100)
    func.right(90)
    func.forward(100)
    func.right(90)
    func.forward(100)

draw_sq("yellow")
