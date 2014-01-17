Lindenmayer Systems
===================

I was bored last night so I looked at something I found a while back called lindenmayer systems, which are basically a way to formally define string rewriting, developed by some guy whose last name was Lindenmayer, who was a biologist or something, and invented them as a mathematical way to model plant growth in the 1960s.
I programmed a bunch of different systems in python, as well as a basic library for creating and displaying these systems pretty easily. All of my examples use turtle, but the library can really do anything, as long as it is wrapped in a function with no arguments

The order of the created files (so that you can see the progress, and also because they generally go from less to more complicated/cool):
*  stupid\_tree.py
*  lsys.py
*  koch\_curve.py
*  sierpinski.py
*  sierpinski2.py
*  koch\_island.py
*  cool\_square\_thing.py
*  fractal\_wheat.py

I got it down to a pretty general system, but there are somethings that need to be explicitly programmed everytime for flexability overall. 
Maybe if I made a libary with some general functions, it would be cool. Maybe that really woudn't do that much though, I don't know. 

Added ability for stochastic lsystems. They are used by having an uppercase and a lowercase letter in the rules, if this happens it automatically chooses between them. I think I am going to reimplement this, using a list of dictionaries of possible values. I was going to let you pass in a weight for the randomness, but that doesn't work yet. 
