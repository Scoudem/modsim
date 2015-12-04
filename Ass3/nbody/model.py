'''
File: model.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import numpy as np
import particle as pc
import math


class Model:
    '''
    '''

    G = 6.67408 * 10 ** -11

    def __init__(self):
        '''
        '''
        self.particles = []
        self.timestep = 0
        self.dt = 0.01

    def set_dt(self, dt):
        '''
        '''
        self.dt = dt

    def add_particle(self, mass, pos, vel):
        '''
        '''
        particle = pc.Particle(mass, pos, vel)
        self.particles.append(particle)

    def remove_particle(self, index):
        '''
        '''
        self.particles.remove(index)

    def next_n_timesteps(self, timesteps):
        '''
        '''
        for t in range(timesteps):
            self.next_timestep()

    def next_timestep(self):
        '''
        '''
        self.update_all_particles()
        # draw
        self.timestep += 1

    def update_all_particles(self):
        '''
        '''
        for particle in self.particles:
            self.update_particle(particle)

        for particle in self.particles:
            particle.update_pos(self.dt)
            particle.update_vel(self.dt)

        print self

    def update_particle(self, particle):
        '''
        '''
        self.compute_f(particle)
        self.compute_a(particle)

    def compute_f(self, p1):
        '''
        '''
        f = np.zeros(2)
        for p2 in self.particles:
            if p1 is p2:
                continue

            upper = self.G * (p1.mass * p2.mass) * (p2.pos - p1.pos)
            lower = np.abs(p2.pos - p1.pos) ** 3
            f += np.asarray(upper) / np.asarray(lower)

    def compute_a(self, p1):
        '''
        '''
        a = np.zeros(2)
        for p2 in self.particles:
            if p1 is p2:
                continue

            upper = self.G * p2.mass * (p2.pos - p1.pos)
            lower = np.abs(p2.pos - p1.pos) ** 3
            print upper, lower
            a += np.asarray(upper) / np.asarray(lower)

        p1.acc = a

    def plot(self):
        import matplotlib.pyplot as plt
        fig = plt.gcf()
        plt.xlim((0, 30))
        plt.ylim((0, 30))
        for particle in self.particles:
            circle = plt.Circle(particle.pos, math.log(particle.mass) / 10)
            print circle
            fig.gca().add_artist(circle)
        plt.show()

    def __str__(self):
        string = 'Timestep: {}\n'.format(self.timestep)
        for particle in self.particles:
            string += str(particle) + '\n'
        return string
