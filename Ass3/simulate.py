'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import nbody

if __name__ == '__main__':
    model = nbody.model.Model()
    model.add_particle(10 ** 12, [0, 0], [0.2, 0])
    model.add_particle(10 ** 7, [10, 2], [-0.5, 3])
    # model.add_particle(10 ** 8, [20, 7], [1, 0.1])

    model.set_dt(0.1)
    model.set_size((-100, 100))

    # model.generate_random(3)

    model.next_n_timesteps(5000)
    model.plot(drawpath=True, autoscale=False)
