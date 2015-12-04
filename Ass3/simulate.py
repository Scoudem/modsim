'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import nbody

if __name__ == '__main__':
    model = nbody.model.Model()
    model.add_particle(10, [10, 10], [10, 10])
    model.add_particle(5, [20, 20], [10, 10])
    print model
