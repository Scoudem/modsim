'''
File: particle.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import numpy as np
import math


class Particle:
    '''
    '''
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.startpos = np.asarray(pos, dtype='float64')
        self.pos = np.asarray(pos, dtype='float64')
        self.startvel = np.asarray(vel, dtype='float64')
        self.vel = np.asarray(vel, dtype='float64')
        self.acc = np.zeros(len(pos), dtype='float64')
        self.acc_prev = np.zeros(len(pos), dtype='float64')
        self.jerk = np.zeros(len(pos), dtype='float64')
        self.path = np.asarray(pos, dtype='float64')
        self.circle = None
        self.active = True
        self.deathtime = -1

    def advance_pos(self, time):
        pos = self.startpos
        pos += self.vel * time
        pos += self.acc * time ** 2 / 2
        self.set_current_pos(pos)

    def compute_pos(self, time):
        self.compute_vel(time)
        pos = self.startpos
        pos += self.vel * time
        pos += self.acc * time ** 2 / 2
        pos += self.jerk * time ** 3 / 6
        self.set_pos(pos)

    def compute_vel(self, time):
        vel = self.startvel
        vel += self.acc * time
        vel += self.jerk * time ** 2 / 2
        self.vel = vel

    def estimate_jerk(self, dt):
        self.jerk = (self.acc - self.acc_prev) / dt

    def set_acc(self, acc, update_prev):
        if update_prev:
            self.prev_acc = acc
        self.acc = acc

    def set_pos(self, pos):
        ''' Set position and add it to the path '''
        self.pos = pos
        self.path = np.dstack((self.path, self.pos))

    def set_current_pos(self, pos):
        ''' Set position without adding it to the path '''
        self.pos = pos

    def get_path_x(self, i):
        return self.path[0][0][i]

    def get_path_y(self, i):
        return self.path[0][1][i]

    def get_path_at(self, i):
        if i >= len(self.path[0][0]):
            i = -1

        return (self.get_path_x(i), self.get_path_y(i))

    def get_mass_plotable(self):
        return math.log(self.mass) / 10

    def __str__(self):
        string = 'Particle@(M:{})(R:{})(V:{})'.format(
            self.mass, self.pos, self.vel
        )
        return string
