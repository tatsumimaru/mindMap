#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from random import *

dead = 0
alive = 1
status = (dead, alive)

height = 10
width = 10
field = []

def init():
    for i in range(height):
        row = []
        for j in range(width):
            row.append(dead)
        field.append(row)
    draw()

#def rand_set():
#def reset():
def draw():
    canvas.delete("field")
    for i in range(height):
        for j in range(width):
            x0 = space + j * cell
            y0 = space + i * cell
            x1 = x0 + cell
            y1 = y0 + cell
            canvas.create_rectangle (x0, y0, x1, y1, fill = color [field[i][j]], tags = "field")
            

#def next():
#def count(x, y):
#def run():
#def start_stop():
#def alive_dead(event):

init()
#run()
root.mainloop()
