########################################
# koch_curve.py
# lsystem representation of a koch curve
# author: stphndemos
########################################

import sys
from lsys import gen_lsys
import turtle

segment_length = 5
angle = 90

def draw_segment():
    turtle.forward(segment_length)

def draw_blank_segment():
    turtle.up()
    draw_segment()
    turtle.down()

def turn_left():
    turtle.left(angle)

def turn_half_left():
    turtle.left(angle/2)

def turn_right():
    turtle.right(angle)

def init_turtle():
    turtle.ht()
    turtle.up()
    turtle.speed(0)
    turtle.setpos(-500, 0)
    turtle.down()

alphabet = { 'F' : draw_segment,
             'G' : draw_blank_segment,
             '+' : turn_left,
             '-' : turn_right,
             '/' : turn_half_left,
           }
axiom    = 'F+F+F+F'
rules    = { 'F' : 'F+G-FF+F+FF+FG+FF-G+FF-F-FF-FG-FFF',
             'f' : 'F/G-FF/F/FF/FG/FF-G/FF-F-FF-FG-FFF',
             'G' : 'GGGGGG',
             'g' : 'GGFFGG',
           }

def main():
    init_turtle()
    gen_lsys(alphabet, axiom, rules, int(sys.argv[1]), rw = 's')
    print 'click to exit'
    turtle.exitonclick()

if __name__ == '__main__':
    main()
