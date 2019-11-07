"""
UMass ECE 241 - Advanced Programming
Homework #4     Fall 2019
hw4_q1_2019.py - Recursice fern with turtle
"""

import turtle

pen = turtle.Turtle()
mywin = turtle.Screen()
pen.color('blue')
pen.width(3)


""""
Tree code is only in this file for reference.
It is not needed fr solving the assignment!!!
"""

def tree(n,l):
    if n==0 or l<2:
        return
    pen.down()

    pen.forward(l)
    pen.left(45)
    tree(n-1, l/2)
    pen.right(90)
    tree(n-1, l/2)
    pen.left(45)
    pen.backward(l)

#tree(3,100)
#mywin.exitonclick()

def fern(n,l):
    if n == 0 or l < 2:
        return

    pen.down()
    pen.forward(0.3*l)
    pen.left(55)
    fern(n-1,l/2)
    pen.right(55)
    pen.forward(0.3*l)
    pen.right(45)
    fern(n-1,l/2)
    pen.left(45)
    pen.forward(0.3*l)
    pen.left(5)
    fern(n-1,l)
    pen.right(5)
    pen.backward(l*0.9)


fern(5, 100)
mywin.exitonclick()