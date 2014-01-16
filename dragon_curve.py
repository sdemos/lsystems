###################################################
# dragon_curve.py
# lsystem representation of a dragon curve...?
# author: stphndemos
###################################################

import sys
from lsys import gen_lsys
import turtle

segment_length = 5
angle = 90

def draw_segment():
    turtle.forward(segment_length)

def turn_left():
    turtle.left(angle)

def turn_right():
    turtle.right(angle)

def init_turtle():
    turtle.ht()
    turtle.up()
    turtle.speed(0)
#    turtle.setpos(-600, -300)
    turtle.down()

alphabet = { 'A' : draw_segment,
             'B' : draw_segment,
             '+' : turn_left,
             '-' : turn_right,
           }
axiom    = 'A'
rules    = { 'A' : 'A+B',
             'B' : 'A-B'
           }

def main():
    init_turtle()
    gen_lsys(alphabet, axiom, rules, int(sys.argv[1]))
    print 'click to exit'
    turtle.exitonclick()

if __name__ == '__main__':
    main()
