'''
File: integration.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains Euler and second and fourth order Runge-Kutta integration methods.
'''


import numpy as np
import numbers


class IntegrationTechnique:
    '''
    Base class containing methods used for integration
    '''
    def __init__(self, functions, time, y0, stepsize=1):
        '''
        Constructor, takes functions, initial timestep, initial y values.
        Optional: stepsize
        '''
        if time < 0:
            raise ValueError('Time should be equal or greater than 0')
        if stepsize <= 0:
            raise ValueError('Stepsize should be greater than 0')

        if not isinstance(functions, list):
            functions = [functions]
        if not isinstance(y0, list):
            y0 = [y0]
        if len(y0) != len(functions):
            raise ValueError('Amount of functions should be equal to amount ' +
                             'of initial values')

        for f in functions:
            if not isinstance(f, type(lambda: 0)):
                raise ValueError('Given variable is not a lambda or function')

        for v in y0:
            if not isinstance(v, numbers.Real):
                raise ValueError('Initial values should be real numbers')

        self._functions = functions
        self._timestep = 0
        self._t_values = [time]
        self._y_values = np.swapaxes(np.array(y0, ndmin=2), 0, 1)
        self._stepsize = stepsize

    def get_t_values(self):
        '''
        Returns the current list of t values
        '''
        return self._t_values

    def get_y_values(self):
        '''
        Returns the current list of values for the function
        '''
        return self._y_values

    def generate_n(self, n):
        '''
        Generates the next n values of the given function
        '''
        try:
            for n in range(n):
                self.get_next()
        except OverflowError, e:
            print e

    def __str__(self):
        '''
        Returns a string containing all variables
        '''
        s = "Current timestep: {}.\nStepsize: {}.\nx: {}.\ny: {}.".format(
            self._timestep,
            self._stepsize,
            self._t_values,
            self._y_values
        )

        return s


def plot(objects, xscales={}, yscales={}, title=""):
    from matplotlib.pyplot import plot, show, close, subplot,\
        xscale, yscale, gcf
    '''
    Plots current state of objects in subplots.
    Define xscales and yscales as dict of indexes.
    '''
    if not isinstance(objects, list):
            objects = [objects]

    l = len(objects)
    first = round(l / 2.0) + 1
    second = round(l / 2.0)
    for i in range(0, l):
        subplot(first, second, i + 1)
        if i in xscales:
            xscale(xscales[i])
        if i in yscales:
            yscale(yscales[i])
        fig = gcf()
        fig.suptitle(title, fontsize="x-large")

        values = objects[i].get_y_values()
        x, y = values.shape

        for j in range(x):
            plot(objects[i].get_t_values(), values[j, :])

    show()
    close()

if __name__ == '__main__':
    '''
    Tests for integration techniques
    '''
    from euler import Euler
    from rungekutta import RungeKutta2, RungeKutta4

    functions = [Euler, RungeKutta2, RungeKutta4]
    for function in functions:
        results = [
            function(lambda (t, x): 1, 0, 0),
            function(lambda (t, x): x, 0, 0),
            function(lambda (t, x): x, 0, 1),
            function(lambda (t, x): x * x, 1, 1),
            function([
                lambda (t, x, y): 0.5 * x,
                lambda (t, x, y): 0.5 * x - 1
            ], 0, [1, 2])
        ]

        for object in results:
            object.generate_n(10)

        plot(results,
             yscales={3: 'log'}, title=function.__name__)
