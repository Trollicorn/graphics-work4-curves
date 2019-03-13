from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians
from os import remove
#""" delete/add # to enable/disable
for i in range(110):
    screen = new_screen()
    color = [ 0, 127, 255 ]
    edges = []
    transform = new_matrix()
    ident(transform)
    f = open("epic"+str(i)+".txt",'w')
    f.write("circle\n250 250 0 200\ncircle\n")
    if i < 56:
        f.write(str(200-i)+" 325 0 10\ncircle\n"+str(350-i)+" 325 0 10\n")
    else:
        f.write(str(145+(i-55))+" 325 0 10\ncircle\n"+str(295+(i-55))+" 325 0 10\n")
    f.write("hermite\n150 150 350 150 -100 -100 100 150\nbezier\n136 323 137 355 204 355 210 324\n")
    f.write("bezier\n286 323 287 355 354 355 360 324\nline\n250 275 0 250 325 0\nbezier\n250 215 300 195 300 295 250 275\n")
    f.write("apply\nsave\nuse"+str(i)+".png\n")
    f.close()
    parse("epic"+str(i)+".txt",edges,transform,screen,color)
    remove("epic"+str(i)+".txt")
"""
screen = new_screen()
color = [ 0, 127, 255 ]
edges = []
transform = new_matrix()
ident(transform)
#"""
parse("good",edges,transform,screen,color)
