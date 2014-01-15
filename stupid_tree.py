###################################################
# Playing around with lindenmeyer systems in turtle
# main.py
# author: stphndemos
###################################################

import sys
import turtle

rules = { '0' : '1[0]0',
		  '1' : '11'
		}

# possible actions

segment_length = 2
pos_stack = []

def draw_segment(length):
	turtle.forward(length)

def draw_segment_half():
	draw_segment(segment_length/2)

def draw_segment_full():
	draw_segment(segment_length)

def push_left():
	pos_stack.append((turtle.xcor(), turtle.ycor(), turtle.heading()))
	turtle.left(45)

def pop_right():
	x,y,h = pos_stack.pop()
	turtle.up()
	turtle.setpos(x,y)
	turtle.seth(h)
	turtle.right(45)
	turtle.down()

actions = { '0' : draw_segment_half,
			'1' : draw_segment_full,
			'[' : push_left,
			']' : pop_right
		  }

def apply_rules(tree):
	out_tree = ''
	for c in tree:
		if c in rules:
			out_tree += rules[c]
		else:
			out_tree += c
	return out_tree

def draw_tree(tree):
	for c in tree:
		actions[c]()

def turtle_init():
	turtle.ht()
	turtle.up()
	turtle.speed(0)
	turtle.left(90)
	turtle.backward(350)
	turtle.down()

def main():
	turtle_init()
	depth = int(sys.argv[1])
	tree = '0'
	while depth > 0:
		tree = apply_rules(tree)
		depth -= 1
	draw_tree(tree)
	turtle.exitonclick()

if __name__ == '__main__':
	main()
