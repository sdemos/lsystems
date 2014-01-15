########################################
# koch_curve.py
# lsystem representation of a koch curve
# author: stphndemos
########################################

import sys
import lsys
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

def turn_right():
    turtle.right(angle)

def init_turtle():
    turtle.ht()
    turtle.up()
    turtle.speed(0)
    turtle.setpos(-500, 0)
    turtle.down()

alphabet = { 'F' : draw_segment,
             'f' : draw_blank_segment,
             '+' : turn_left,
             '-' : turn_right,
           }
axiom    = 'F-F-F-F'
rules    = { 'F' : 'F-F+F+FF-F-F+F' }

def main():
    init_turtle()
    koch_curve = lsys.lsystem(alphabet, axiom, rules)
    tree = koch_curve.apply_rules(int(sys.argv[1]))
    koch_curve.perform_actions(tree)
    print 'click to exit'
    turtle.exitonclick()

if __name__ == '__main__':
    main()
