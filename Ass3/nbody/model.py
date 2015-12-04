'''
File: model.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import numpy as np
import particle as pc


class Model:
    '''
    '''

    G = 6.67408 * 10 ** 11

    def __init__(self):
        '''
        '''
        self.particles = []
        self.timestep = 0

    def add_particle(self, mass, pos, vel):
        '''
        '''
        particle = pc.Particle(mass, pos, vel)
        self.particles.append(particle)

    def remove_particle(self, index):
        '''
        '''
        self.particles.remove(index)

    def next_timestep(self):
        '''
        '''
        pass

    def update_all_particles(self):
        '''
        '''
        for particle in self.particles:
            self.update_particle(particle)

    def update_particle(self, particle):
        '''
        '''
        self.compute_f(particle)
        self.compute_a(particle)

    def compute_f(self, p1):
        '''
        '''
        f = np.zeros(3)
        for p2 in self.particles:
            upper = self.G * (p1.mass * p2.mass) * (p2.pos - p1.pos)
            lower = np.linalg.norm((p2.pos - p1.pos)) ** 3
            f += upper / lower

    def compute_a(self, p1):
        '''
        '''
        a = np.zeros(3)
        for p2 in self.particles:
            upper = self.G * p2.mass * (p2.pos - p1.pos)
            lower = np.linalg.norm((p2.pos - p1.pos)) ** 3
            a += upper / lower

    def __str__(self):
        string = 'Timestep: {}\n'.format(self.timestep)
        for particle in self.particles:
            string += str(particle) + '\n'
        return string
