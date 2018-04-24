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
        
    def run(self):
        self.update()
        self.display()
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) 
        
    def boundaries(self, d):
        desired = None
        if (self.position.x < d):
             desired = PVector(self.maxspeed, self.velocity.y)
        elif (self.position.x > width-d):
            desired = PVector(-self.maxspeed, self.velocity.y)
        if (self.position.y < d):
            desired = PVector(self.velocity.x, self.maxspeed)
        elif (self.position.y > height-d):
            desired = PVector(self.velocity.x, -self.maxspeed)
            
        if desired != None:
            desired.normalize()
            desired.mult(self.maxspeed)
            steer = PVector.sub(desired, self.velocity)
            steer.limit(self.maxforce)
            self.apply_force(steer)
        
    def apply_force(self, force):
        self.acceleration.add(force)
        
    def seek(self, target): # steer = desired - velocity
        desired = PVector.sub(target,self.position)
        desired.setMag(self.maxspeed)
        steer = PVector.sub(desired,self.velocity)
        steer.limit(self.maxforce)
        self.apply_force(steer)
        
    def display(self):
        theta = self.velocity.heading2D() + PI/2
        fill(127)
        stroke(0)
        strokeWeight(1)
        pushMatrix()
        translate(self.position.x, self.position.y)
        rotate(theta)
        beginShape()
        vertex(0, -self.r*2)
        vertex(-self.r, self.r*2)
        vertex(self.r, self.r*2)
        endShape(CLOSE)
        popMatrix()