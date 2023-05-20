"""
    Below file starts the simulation after implementation.
    The below file contains a "World" object specifying the world settings and a set of particles.
    Whenever we move the Robot with our keyboard key directions, it generates the random observations used to update the particle sets to estimate 
    the robot path as well as the landmarks locations.
"""
import sys
import random
import math
from copy import deepcopy
from world import World
from particle2 import Particle2
from Fast_Slam import Fast_Slam

class Fast_Slam2(Fast_Slam):
    """Inherited from FastSlam"""
    def __init__(self, x, y, orien, particle_size = 50):
        self.world = World()
        self.particles = [Particle2(x, y, random.random()* 2.*math.pi) for i in range(particle_size)]
        self.robot = Particle2(x, y, orien, is_robot=True)
        self.particle_size = particle_size

if __name__=="__main__":
    random.seed(5)
    simulator = Fast_Slam2(80, 140, 0, particle_size=200)
    simulator.run_simulation()
