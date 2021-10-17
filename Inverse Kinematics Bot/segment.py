import math

class Segment():
    """class creates joint segment objects, robot arm pieces that will fit together in the simulation"""
    def __init__(self, length, starting_coords, angle, parent, child):
        self.length = length
        self.start = starting_coords
        self.angle = angle
        self.parent = parent
        self.child = child

        angle = angle * (math.pi/180) # degrees to radians
        self.end = (length * math.cos(angle) + self.start[0], length * math.sin(angle) + self.start[1])    # rad from 0 degrees

    
    def update_start(self, new_coords):
        self.start = new_coords

    def update_angle(self, new_angle):
        self.angle = new_angle