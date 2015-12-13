'''
File: model.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import random as rd
import numpy as np
import particle as pc
from scipy.spatial import distance
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import sys


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
        self.size = None
        self.plots = None
        self.circles = []

    def set_dt(self, dt):
        '''
        '''
        self.dt = dt

    def set_size(self, size):
        '''
        '''
        self.size = size

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
        print('Simulating {} timesteps with {} particles...'.format(
            timesteps, len(self.particles)
        ))
        for t in range(timesteps):
            sys.stdout.write('\r{}/{}. dt={}...'.format(
                t + 1, timesteps, self.dt
            ))
            self.next_timestep()
        print(' done.\nPlotting...')

    def next_timestep(self):
        '''
        '''
        self.update_all_particles()
        # draw
        self.timestep += 1

    def update_all_particles(self):
        '''
        '''
        dts = 0
        for particle in self.particles:
            dist = self.update_particle(particle)
            vel = np.mean(np.abs(particle.vel))
            dts += vel / dist

        self.set_dt(dts / (len(self.particles) + 1))

        for particle in self.particles:
            particle.update_pos(self.dt)
            particle.update_vel(self.dt)

    def update_particle(self, particle):
        '''
        '''
        # self.compute_f(particle)
        return self.compute_a(particle)

    def compute_f(self, p1):
        '''
        '''
        f = np.zeros(2)
        for p2 in self.particles:
            if p1 is p2:
                continue

            upper = self.G * (p1.mass * p2.mass) * (p2.pos - p1.pos)
            lower = distance.euclidean(p2.pos, p1.pos) ** 3
            f += np.asarray(upper) / np.asarray(lower)

    def compute_a(self, p1):
        '''
        '''
        dists = 0

        a = np.zeros(2)
        for p2 in self.particles:
            if p1 is p2:
                continue

            dist = distance.euclidean(p2.pos, p1.pos)
            dists += dist

            upper = self.G * p2.mass * (p2.pos - p1.pos)
            lower = dist ** 3
            a += np.asarray(upper) / np.asarray(lower)

        p1.acc = a

        return dists / (len(self.particles) - 1)

    def generate_random(self, n):
        for i in range(n):
            mass = 10 ** (10 + rd.uniform(-3, 3))
            position = [
                rd.randint(self.size[0], self.size[1]),
                rd.randint(self.size[0], self.size[1])
            ]
            velocity = [rd.uniform(-1, 1), rd.uniform(-1, 1)]
            self.add_particle(mass, position, velocity)
            print self.particles[-1]

    def plot(self, drawpath=True, autoscale=False, animated=True):
        '''
        Plot the particles and their paths
        '''

        fig = plt.figure()
        self.ax = plt.axes()

        self.ax.set_xlim(self.size, auto=autoscale)
        self.ax.set_ylim(self.size, auto=autoscale)
        self.ax.axis('equal')

        # self.ax.axis('equal')

        for particle in self.particles:
            if drawpath:
                path = particle.path
                self.ax.plot(path[:, 0][0], path[:, 1][0], '--')

            if animated:
                c = plt.Circle(
                    ([], []), particle.get_mass_plotable(), visible=False
                )
                c.center = particle.get_path_at(0)
                self.circles.append(c)

        self.anim = anm.FuncAnimation(
            fig, self.animate, init_func=self.init_animation,
            frames=self.timestep, interval=1, blit=True
        )

        plt.show()
        print(' done.')

    def init_animation(self):
        for circle in self.circles:
            circle.set_visible(False)
            self.ax.add_patch(circle)
        return self.circles

    def animate(self, i):
        for item in zip(self.circles, self.particles):
            item[0].center = item[1].get_path_at(i)
            item[0].set_visible(True)

            sys.stdout.write('\rTimestep {}/{}...'.format(
                i + 1, self.timestep)
            )
        return self.circles

    def __str__(self):
        string = 'Timestep: {}\n'.format(self.timestep)
        for particle in self.particles:
            string += str(particle) + '\n'
        return string
