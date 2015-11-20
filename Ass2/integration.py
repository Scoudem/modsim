'''
File: integration.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains Euler and second and fourth order Runge-Kutta integration methods.
'''


from math import isinf
import numpy as np


class Euler:
    def __init__(self, function, time, y0, stepsize=1):
        '''
        Constructor, takes a function, initial timestep, initial y value.
        Optional: stepsize
        '''
        if time < 0:
            raise ValueError('Time should be equal or greater than 0')
        if not isinstance(function, type(lambda: 0)):
            raise ValueError('Given variable is not a lambda or function')
        if stepsize <= 0:
            raise ValueError('Stepsize should be greater than 0')

        self._function = function
        self._timestep = time
        self._x_values = [0] * (time + 1)
        self._y_values = [0] * time + [y0]
        self._stepsize = stepsize

    def get_x_values(self):
        '''
        Returns the current list of x values
        '''
        return self._x_values

    def get_y_values(self):
        '''
        Returns the current list of y values
        '''
        return self._y_values

    def generate_n(self, n):
        '''
        Generates the next n values of the given function
        '''
        for n in range(n):
            self.get_next()

    def get_next(self):
        '''
        Generates the next value of the given function
        '''
        an = self._function(self._x_values[self._timestep],
                            self._y_values[self._timestep])
        self._x_values.append(self._x_values[self._timestep] + self._stepsize)
        self._y_values.append(self._y_values[self._timestep] +
                              self._stepsize * an)

        if isinf(self._y_values[-1]):
            raise OverflowError(
                "y reached infinity. Stopping generation at {}".format(
                    self._timestep
                )
            )

        self._timestep += 1

    def __str__(self):
        '''
        Returns a string containing all variables
        '''
        return "Current timestep: {}.\nStepsize: {}.\nx: {}.\ny: {}.".format(
            self._timestep,
            self._stepsize,
            self._x_values,
            self._y_values
        )


if __name__ == '__main__':
    '''
    Tests
    '''
    import matplotlib.pyplot as plt

    euler1 = Euler(lambda x, y: 1, 0, 0)
    euler2 = Euler(lambda x, y: y, 0, 0)
    euler3 = Euler(lambda x, y: y, 0, 1)
    euler4 = Euler(lambda x, y: y * y, 1, 1)

    euler1.generate_n(10)
    euler2.generate_n(10)
    euler3.generate_n(5)
    euler4.generate_n(10)

    plt.subplot(221)
    plt.plot(euler1.get_x_values(), euler1.get_y_values())
    plt.subplot(222)
    plt.plot(euler2.get_x_values(), euler2.get_y_values())
    plt.subplot(223)
    plt.plot(euler3.get_x_values(), euler3.get_y_values())
    plt.subplot(224)
    plt.plot(euler4.get_x_values(), euler4.get_y_values())

    plt.show()
