'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import nbody

if __name__ == '__main__':
    model = nbody.model.Model()
    model.add_particle(10 ** 7, [10, 10], [0, 0.02])
    model.add_particle(10 ** 9, [25, 25], [0.02, 0.01])
    model.add_particle(10 ** 5, [40, 10], [0.05, 0])

    model.set_dt(0.1)
    model.set_size((-100, 100))

    model.next_n_timesteps(10000)
    model.plot()
    # timesteps = 10
    # for t in range(timesteps):
    #     model.next_timestep()
    #     model.plot()
