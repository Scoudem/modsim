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
    def __init__(self, functions, time, y0, stepsize=1):
        '''
        Constructor, takes a function, initial timestep, initial y value.
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
        #TODO: check if lengths if functions list and y0 list are equal
        #TODO: check if initial values are numeric

        for f in functions:
            if not isinstance(f, type(lambda: 0)):
                raise ValueError('Given variable is not a lambda or function')

        self._functions = functions
        self._timestep = 0
        self._t_values = [time]
        self._y_values = np.swapaxes(np.array(y0, ndmin=2), 0, 1)
        self._stepsize = stepsize

        print self

    def get_t_values(self):
        '''
        Returns the current list of t values
        '''
        return self._t_values

    def get_y_values(self, index=0):
        '''
        Returns the current list of y values for the function with the given index
        '''
        print self._y_values[index, :]
        return self._y_values[index,:]

    def generate_n(self, n):
        '''
        Generates the next n values of the given function
        '''
        for n in range(n):
            self.get_next()

    def get_next(self):
        '''
        Generates the next value for each of the functions
        '''
        an = []
        args = tuple([self._t_values[self._timestep]] + self._y_values[:,self._timestep].tolist())

        for function in self._functions:
            an.append(function(args))

        for i, val in enumerate(an):
            an[i] = self._y_values[i,self._timestep] + self._stepsize * an[i]

            #TODO: should this inf check be after appending y and t to their arrays? (so the value will be included?)
            if isinf(an[i]):
                raise OverflowError(
                    "y{} reached infinity. Stopping generation at t={}".format(
                        i,
                        self._t_values[self._timestep]
                    )
                )

        self._y_values = np.append(self._y_values, np.swapaxes(np.array([an]), 0, 1), axis=1)
        self._t_values.append(self._t_values[self._timestep] + self._stepsize)

        self._timestep += 1

    def __str__(self):
        '''
        Returns a string containing all variables
        '''
        return "Current timestep: {}.\nStepsize: {}.\nx: {}.\ny: {}.".format(
            self._timestep,
            self._stepsize,
            self._t_values,
            self._y_values
        )


if __name__ == '__main__':
    '''
    Tests
    '''
    import matplotlib.pyplot as plt

    euler1 = Euler(lambda (t, x): 1, 0, 0)
    euler2 = Euler(lambda (t, x): x, 0, 0)
    euler3 = Euler(lambda (t, x): x, 0, 1)
    euler4 = Euler(lambda (t, x): x * x, 1, 1)

    euler1.generate_n(10)
    euler2.generate_n(10)
    euler3.generate_n(5)
    euler4.generate_n(10)

    plt.subplot(221)
    plt.plot(euler1.get_t_values(), euler1.get_y_values())
    plt.subplot(222)
    plt.plot(euler2.get_t_values(), euler2.get_y_values())
    plt.subplot(223)
    plt.plot(euler3.get_t_values(), euler3.get_y_values())
    plt.subplot(224)
    plt.plot(euler4.get_t_values(), euler4.get_y_values())

    plt.show()
    plt.close()

    '''
    Euler test with multiple functions
    '''
    euler6 = Euler([lambda (t, x, y): 0.5 * x, lambda (t, x, y): 0.5 * x - 1], 0, [1, 2])
    euler6.generate_n(10)
    plt.plot(euler6.get_t_values(), euler6.get_y_values(0), 'r')
    plt.plot(euler6.get_t_values(), euler6.get_y_values(1), 'b')

    plt.show()
