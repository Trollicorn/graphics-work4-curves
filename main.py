from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians

screen = new_screen()
color = [ 0, 127, 255 ]
edges = []
transform = new_matrix()
ident(transform)
"""
f = open("gif.sh",'w')
f.write("#!/bin/bash\n\n")
f.write("convert -delay 0.1 -loop 0 ")
for i in range(110):
    f.write("use"+str(i)+".png ")
f.write("art.gif")
"""

parse("script",edges,transform,screen,color)
