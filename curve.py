from matrix import *
from math import cos,sin,pi

def circle(edge, args): #[cx,cy,cz,r]
    cx = args[0]
    cy = args[1]
    cz = args[2]
    r = args[3]
    for t in range(100):
        x0 = r*cos(2*pi*t)+cx
        y0 = r*sin(2*pi*t)+cy
        z = 0
        x1 = r*cos(2*pi*(t+1)+cx
        y1 = r*sin(2*pi*(t+1)+cy
