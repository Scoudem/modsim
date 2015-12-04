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
        self.pos = np.asarray(pos, dtype='float64')
        self.vel = np.asarray(vel, dtype='float64')
        self.acc = np.zeros(len(pos), dtype='float64')
        self.path = np.asarray(pos, dtype='float64')

    def update_pos(self, dt):
        self.pos += self.vel * dt
        # should we still add it if the position remains the same?
        self.path = np.dstack((self.path, self.pos))

    def update_vel(self, dt):
        self.vel += self.acc * dt

    def __str__(self):
        string = 'Particle@(M:{})(R:{})(V:{})'.format(
            self.mass, self.pos, self.vel
        )
        return string
