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

parse("good",edges,transform,screen,color)
