# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# python implementation by
# Abdur-Rahmaan Janhangeer

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/
from Vehicle import Vehicle

v = 0
def setup():
    global v
    size(640, 640)
    v = Vehicle(width/2, height/2)

def draw():
    global v
    background(255)
    mouse = PVector(mouseX, mouseY)
    
    # Draw an ellipse at the mouse position
    fill(200)
    stroke(0)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 48, 48)
    
    v.arrive(mouse);
    v.update();
    v.display();
    