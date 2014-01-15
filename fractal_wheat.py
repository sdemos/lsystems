########################################
# koch_curve.py
# lsystem representation of a koch curve
# author: stphndemos
########################################

import sys
from lsys import gen_lsys
import turtle

segment_length = 10
angle = 24
pos_stack = []

def draw_segment():
    turtle.forward(segment_length)

def do_nothing():
    pass

def turn_left():
    turtle.left(angle)

def turn_right():
    turtle.right(angle)

def init_turtle():
    turtle.ht()
    turtle.up()
    turtle.speed(0)
    turtle.setpos(-500, -300)
    turtle.left(60)
    turtle.colormode(255)
    turtle.pencolor((150,150,0))
    turtle.down()

def push_pos():
    pos_stack.append((turtle.xcor(), turtle.ycor(), turtle.heading()))

def pop_pos():
    turtle.up()
    x,y,h = pos_stack.pop()
    turtle.setpos(x,y)
    turtle.seth(h)
    turtle.down()

alphabet = { 'F' : draw_segment,
             'X' : do_nothing,
             '+' : turn_right,
             '-' : turn_left,
             '[' : push_pos,
             ']' : pop_pos,
           }
axiom    = 'X'
rules    = { 'F' : 'FF',
             'X' : 'F-[[X]+X]+[X]+F[+FX]-X',
           }

def main():
    init_turtle()
    gen_lsys(alphabet, axiom, rules, int(sys.argv[1]))
    print 'click to exit'
    turtle.exitonclick()

if __name__ == '__main__':
    main()
