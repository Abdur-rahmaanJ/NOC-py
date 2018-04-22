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
        self.history = []
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0) 
        history.add(position.get())
        if (len(history) > 100):
            history.pop(0)
        
    def apply_force(self, force):
        self.acceleration.add(force)
        
    def seek(self, target): # steer = desired - velocity
        desired = PVector.sub(target,self.position)
        desired.setMag(self.maxspeed)
        steer = PVector.sub(desired,self.velocity)
        steer.limit(self.maxforce)
        self.apply_force(steer)
        
    def display(self):
        beginShape();
        stroke(0);
        strokeWeight(1);
        noFill();
        for(v in history):
            vertex(v.x,v.y)
        endShape();
        
        # triangle
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