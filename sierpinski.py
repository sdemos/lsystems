###################################################
# sierpinski.py
# lsystem representation of a sierpinski's triangle
# author: stphndemos
###################################################

import sys
import lsys
import turtle

segment_length = 5
angle = 60

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
    turtle.setpos(-600, -300)
    turtle.down()

alphabet = { 'A' : draw_segment,
             'B' : draw_segment,
             '+' : turn_left,
             '-' : turn_right,
           }
axiom    = 'A'
rules    = { 'A' : 'B-A-B',
             'B' : 'A+B+A'
           }

def main():
    init_turtle()
    triangle = lsys.lsystem(alphabet, axiom, rules)
    tree = triangle.apply_rules(int(sys.argv[1]))
    triangle.perform_actions(tree)
    print 'click to exit'
    turtle.exitonclick()

if __name__ == '__main__':
    main()
