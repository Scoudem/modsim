'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import nbody

if __name__ == '__main__':
    model = nbody.model.Model()
    model.add_particle(10 ** 3, [5, 5], [0, 0])
    model.add_particle(10 ** 2, [6, 29], [0.01, -0.1])
    model.add_particle(10 ** 7, [10, 15], [0, 0])
    model.add_particle(10 ** 9, [25, 25], [0, 0])
    model.add_particle(10 ** 3, [20, 20], [0, 0])

    model.set_dt(0.1)

    model.next_n_timesteps(2000)
    model.plot()
    # timesteps = 10
    # for t in range(timesteps):
    #     model.next_timestep()
    #     model.plot()
