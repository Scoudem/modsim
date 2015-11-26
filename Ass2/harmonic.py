'''
File: harmonic.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Harmonic oscillator assignment
'''

import integration as ig
import matplotlib.pyplot as plt


if __name__ == '__main__':
    '''
    s''=-ks, s'=v and v'=-ks describe a harmonic oscillator.
    Writable as s=(v^2)/2 and v=(-ks^2)/2.
    Let s(0)=1.0 and v(0)=0.0.
    '''
    sl = lambda (t, s, v): v
    vl = lambda (t, s, v): -1 * s

    functions = [ig.Euler, ig.RungeKutta2, ig.RungeKutta4]
    for function in functions:
        result = function([sl, vl], 0, [1.0, 0.0], stepsize=0.5)
        result.generate_n(100)

        fig = plt.gcf()
        fig.suptitle(function.__name__, fontsize="x-large")

        plt.subplot(1, 3, 1)
        plt.title('s(t) vs t', fontsize="x-large")
        plt.plot(result.get_t_values(), result.get_y_values()[0])

        plt.subplot(1, 3, 2)
        plt.title('v(t) vs t', fontsize="x-large")
        plt.plot(result.get_t_values(), result.get_y_values()[1])

        plt.subplot(1, 3, 3)
        plt.title('s(t) vs v(t)', fontsize="x-large")
        plt.scatter(result.get_y_values()[0], result.get_y_values()[1])

        plt.show()
