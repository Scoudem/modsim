'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import nbody

if __name__ == '__main__':
    model = nbody.model.Model()
    # model.add_particle(10 ** 12, [100, 100], [-0.1, 0])
    # model.add_particle(10 ** 13, [0, 0], [0.1, 0])
    # model.add_particle(10 ** 10, [-50, 0], [0, 3])
    # model.add_particle(10 ** 10, [50, 0], [0, -3])
    # model.add_particle(10 ** 10, [0, -50], [3, 0])
    # model.add_particle(10 ** 10, [0, 50], [-3, 0])
    # # model.add_particle(10 ** 9, [25, 25], [0.02, 0.01])
    # # model.add_particle(10 ** 5, [40, 10], [0.05, 0])
    # # model.add_particle(10 ** 2, [-30, -50], [0.05, 0.03])

    model.set_dt(0.1)
    model.set_size((-50, 50))

    model.generate_random(3)

    model.next_n_timesteps(10000)
    model.plot(drawpath=True, autoscale=False)
