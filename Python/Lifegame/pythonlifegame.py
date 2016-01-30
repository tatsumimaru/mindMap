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

def rand_set():
    if is_run:
        return
    for i in range(height):
        for j in range(width):
            field[i][j] = random.choice(status)
    draw()
    
def reset():
    if is_run:
        return
    for i in range(height):
        for j in range(width):
            field[i][j] = dead
    draw()
    
def draw():
    canvas.delete("field")
    for i in range(height):
        for j in range(width):
            x0 = space + j * cell
            y0 = space + i * cell
            x1 = x0 + cell
            y1 = y0 + cell
            canvas.create_rectangle (x0, y0, x1, y1, fill = color [field[i][j]], tags = "field")
            

def next():
    global field
    new_field = []
    for i in range(height):
        row = []
        for j in range(width):
            num = count(i, j)
            if num == 3:
                row.append(alive)
            elif num == 2:
                row.append(field[i][j])
            else:
                row.append(dead)
        new_field.append(row)
    field = new_field
    draw()

def count(x, y):
    num = 0
    
    if x! = 0:
        num = num + field[y][x - 1]
        if y! = 0:
            num = num + field[y - 1][x - 1]
        if y! = height -1:
            num = num + field[y + 1][x + !] 
#def run():
#def start_stop():
#def alive_dead(event):

init()
#run()
root.mainloop()
