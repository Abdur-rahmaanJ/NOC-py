# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# python implementation by
# Abdur-Rahmaan janhangeer

# Seek_Arrive

# The "Vehicle" class

class Vehicle:
    def __init__(self, x, y):
        self.position = PVector(x,y)
        self.velocity = PVector(0,-2)
        self.acceleration = PVector(0,0)
        self.r = 6
        self.maxspeed = 4
        self.maxforce = 0.1
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) 
        
    def apply_force(self, force):
        self.acceleration.add(force)
        
    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    def arrive(self, target):
        desired = PVector.sub(target, self.position)
        d = desired.mag()
        # Scale with arbitrary damping within 100 pixels
        if (d < 100):
            m = map(d,0,100,0,self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)
        
        # Steering = Desired minus Velocity
        steer = PVector.sub(desired, self.velocity)
        steer.limit(self.maxforce)
        self.apply_force(steer)
        
    def display(self):
        theta = self.velocity.heading2D() + PI/2
        fill(127)
        stroke(0)
        strokeWeight(1)
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta);
        beginShape();
        vertex(0, -self.r*2);
        vertex(-self.r, self.r*2);
        vertex(self.r, self.r*2);
        endShape(CLOSE);
        popMatrix();