'''
File: particle.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import numpy as np


class Particle:
    '''
    '''
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos = np.asarray(pos)
        self.vel = np.asarray(vel)

    def __str__(self):
        string = 'Particle{}@(R:{})(V:{})'.format(self.mass, self.pos, self.vel)
        return string
