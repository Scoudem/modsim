'''
File: seir.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

SEIR model
'''

import integration as ig


if __name__ == '__main__':
    N = 1000.0
    t = 50.0 / N
    eps = 1.0 / 6.0
    mu = 1.0 / 9.0
    beta = 0.04
    b = 0.0

    st = lambda (t, s, e, i, r): N - beta * s * i - mu * s
    se = lambda (t, s, e, i, r): beta * s * i - (eps + mu) * e
    si = lambda (t, s, e, i, r): eps * e - (t + mu) * i
    sr = lambda (t, s, e, i, r): t * i - mu * r

    m = ig.RungeKutta4([st, se, si, sr], 0, [N - 1, 1, 0, 0])
    m.generate_n(10000)
    print m
    ig.plot(m)
