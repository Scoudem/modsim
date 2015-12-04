'''
File: particle.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''


class Particle:
    '''
    '''
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.x, self.y, self.z = pos,
        self.vx, self.vy, self.vz = vel,

    def __str__(self):
        str = 'mass: {}\n'.format(self.mass)
        return str
