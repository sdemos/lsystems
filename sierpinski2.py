###################################################
# sierpinski2.py
# lsystem representation of a sierpinski's triangle
# author: stphndemos
###################################################

import sys
import lsys
import turtle

segment_length = 5
angle = 120

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

alphabet = { 'F' : draw_segment,
             'G' : draw_segment,
             '+' : turn_right,
             '-' : turn_left,
           }
axiom    = 'F-G-G'
rules    = { 'F' : 'F-G+F+G-F',
             'G' : 'GG'
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
