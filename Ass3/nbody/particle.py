'''
File: particle.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''


class Particle:
    '''
    '''
    def __init__(self, mass):
        self.mass = mass

    def __str__(self):
        str = 'mass: {}\n'.format(self.mass)
        return str
