'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import nbody

if __name__ == '__main__':
    model = nbody.model.Model()
    model.add_particle(10 ** 2, [9, 10], [10, 10])
    model.add_particle(10 ** 5, [20, 20], [0, 0])
    model.add_particle(10 ** 2, [30, 30], [-10, -10])

    model.set_dt(0.1)

    # model.next_n_timesteps(10)
    timesteps = 10
    for t in range(timesteps):
        model.next_timestep()
        model.plot()
