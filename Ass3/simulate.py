'''
File: simulate.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832
'''

import numpy as np
import integration.rungekutta as rk
import integration

if __name__ == '__main__':
    g = 6.67408 * 10 ** -11
    m1 = 10
    m2 = 20

    rk1 = rk.RungeKutta4([
        lambda (t, r11, r12, r21, r22): (-1 * g) * m2 * ((r1 - r2) / (r1 - r2) ** 3),
        lambda (t, r11, r12, r21, r22): (-1 * g) * m1 * ((r2 - r1) / (r2 - r1) ** 3)
    ], 0, [1, 2, 3, 4])

    rk1.generate_n(10)
    integration.integration.plot(rk1)
