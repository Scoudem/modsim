'''
File: particle.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import numpy as np
import matplotlib.animation as anm
import matplotlib.pyplot as plt
import math


class Particle:
    '''
    '''
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos = np.asarray(pos, dtype='float64')
        self.vel = np.asarray(vel, dtype='float64')
        self.acc = np.zeros(len(pos), dtype='float64')
        self.path = np.asarray(pos, dtype='float64')
        self.circle = None

    def update_pos(self, dt):
        self.pos += self.vel * dt
        # should we still add it if the position remains the same?
        self.path = np.dstack((self.path, self.pos))

    def update_vel(self, dt):
        self.vel += self.acc * dt

    def plot(self, fig, ax, frames, animated=True):
        self.circle = plt.Circle(([], []), self.get_mass_plotable())
        self.ax = ax

        self.anim = anm.FuncAnimation(
            fig, self.animate, init_func=self.init_animation,
            frames=frames, interval=1, blit=False
        )

    def get_path_x(self, i):
        return self.path[0][0][i]

    def get_path_y(self, i):
        return self.path[0][1][i]

    def get_path_at(self, i):
        return (self.get_path_x(i), self.get_path_y(i))

    def get_mass_plotable(self):
        return math.log(self.mass) / 10

    def init_animation(self):
        self.circle.center = self.get_path_at(0)
        self.ax.add_patch(self.circle)
        return self.circle,

    def animate(self, i):
        self.circle.center = self.get_path_at(i)
        return self.circle,

    def __str__(self):
        string = 'Particle@(M:{})(R:{})(V:{})'.format(
            self.mass, self.pos, self.vel
        )
        return string
