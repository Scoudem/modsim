'''
File: seir.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

SEIR model
'''

import integration as ig
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 1000.0  # population
    beta = 0.96  # infection rate
    gamma = 1.0 / 9.0  # recovery rate
    sigma = 1.0 / 6.0  # conversion rate
    mu = 0.0  # death rate (0 for stable pop)
    nu = 0.0  # pass to resistant

    st = lambda (t, s, e, i, r): mu * (n - s) - beta * ((s * i) / n) - nu * s
    et = lambda (t, s, e, i, r): beta * ((s * i) / n) - (mu + sigma) * e
    it = lambda (t, s, e, i, r): sigma * e - (mu + gamma) * i
    rt = lambda (t, s, e, i, r): gamma * i - mu * r + nu * s

    m = ig.RungeKutta4([st, et, it, rt], 0, [999, 1, 0, 0], stepsize=0.01)
    m.generate_n(10000)

    plt.plot(m.get_y_values()[0], label="S")
    plt.plot(m.get_y_values()[1], label="E")
    plt.plot(m.get_y_values()[2], label="I")
    plt.plot(m.get_y_values()[3], label="R")
    plt.legend(loc='best')
    plt.show()
