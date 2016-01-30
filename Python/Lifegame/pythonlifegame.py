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

#def next():
#def count(x, y):
#def run():
#def start_stop():
#def alive_dead(event):

init()
#run()
root.mainloop()
