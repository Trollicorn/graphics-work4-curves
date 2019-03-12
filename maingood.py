from display import *
from draw import *
from matrix import *
from parse import *
from transform import *
from math import cos,sin,tan,radians
from os import remove

for i in range(110):
    screen = new_screen()
    color = [ 0, 127, 255 ]
    edges = []
    transform = new_matrix()
    ident(transform)
    f = open("epic"+str(i)+".txt",'w')
    f.write("circle\n250 250 0 200\ncircle\n")
    if i < 56:
        f.write(str(190-i)+" 325 0 10\ncircle\n"+str(340-i)+" 325 0 10\n")
    else:
        f.write(str(135+(i-55))+" 325 0 10\ncircle\n"+str(340-i)+" 325 0 10\n")
    f.write("hermite\n150 150 350 150 -100 -100 100 150\nbezier\n126 323 127 355 194 355 200 324\n")
    f.write("bezier\n276 323 277 355 344 355 350 324\nline\n250 275 0 250 325 0\nbezier\n250 215 300 195 300 295 250 275\n")
    f.write("apply\nsave\nuse"+str(i)+".png\n")
    f.close()
    parse("epic"+str(i)+".txt",edges,transform,screen,color)
#    remove("epic"+str(i)+".txt")

#parse("good",edges,transform,screen,color)
