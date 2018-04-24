# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# python implementation by
# Abdur-Rahmaan Janhangeer

from Vehicle import Vehicle

v = 0
debug = True
d = 25

def setup():
    global v
    size(640, 640)
    v = Vehicle(width/2, height/2)

def draw():
    global v, d
    background(255)
    mouse = PVector(mouseX, mouseY)
    
    if (debug):
        stroke(175)
        noFill()
        rectMode(CENTER)
        rect(width/2, height/2, width-d*2, height-d*2)
    
    v.boundaries(d)
    v.run()
    
def mousePressed():
    global debug
    debug = not debug
    