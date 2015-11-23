'''
File: integration.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains Euler and second and fourth order Runge-Kutta integration methods.
'''


from math import isinf
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

    def get_y_values(self, index=0):
        '''
        Returns the current list of values for the function at the given index
        '''
        return self._y_values[index, :]

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


class Euler(IntegrationTechnique):

    def get_next(self):
        '''
        Generates the next value for each of the functions
        '''
        an = []
        h = self._stepsize
        args = tuple([self._t_values[self._timestep]]
                     + self._y_values[:, self._timestep].tolist())

        for function in self._functions:
            an.append(function(args))

        for i, val in enumerate(an):
            an[i] = self._y_values[i, self._timestep] + h * an[i]

            if isinf(an[i]):
                raise OverflowError(
                    "y{} reached infinity. Stopping generation at t={}".
                    format(
                        i,
                        self._t_values[self._timestep]
                    )
                )

        an = np.swapaxes(np.array([an]), 0, 1)
        self._y_values = np.append(self._y_values, an, axis=1)
        self._t_values.append(self._t_values[self._timestep] + h)

        self._timestep += 1


class RungeKutta2:
    '''
    The second order Runge-Kutta method
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

    def get_y_values(self, index=0):
        '''
        Returns the current list of values for the function at the given index
        '''
        return self._y_values[index, :]

    def generate_n(self, n):
        '''
        Generates the next n values of the given function
        '''
        try:
            for n in range(n):
                self.get_next()
        except OverflowError, e:
            print e

    def get_next(self):
        '''
        Generates the next value for each of the functions
        '''
        t = self._timestep
        h = self._stepsize
        y_values = self._y_values[:, t].tolist()

        k1_args = tuple([self._t_values[t]]
                      + y_values)
        k1 = []
        for function in self._functions:
            k1.append(function(k1_args))

        k2_args = tuple([self._t_values[t] + (h / 2.0)]
                      + [current_y + h*k1[i] for i, current_y in enumerate(y_values)])
        k2 = []
        for function in self._functions:
            k2.append(function(k2_args))

        an = []
        for i, current_y in enumerate(y_values):
            k_parts = current_y + h * ((k1[i] + k2[i]) / 2)
            next_y = current_y + (h / 6.0) * k_parts
            an.append(next_y)

            if isinf(next_y):
                raise OverflowError(
                    "y{} reached infinity. Stopping generation at t={}".format(
                        i,
                        self._t_values[t]
                    )
                )

        an = np.swapaxes(np.array([an]), 0, 1)
        self._y_values = np.append(self._y_values, an, axis=1)
        self._t_values.append(self._t_values[t] + h)

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


class RungeKutta4:
    '''
    The classical Runge-Kutta method
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

    def get_y_values(self, index=0):
        '''
        Returns the current list of values for the function at the given index
        '''
        return self._y_values[index, :]

    def generate_n(self, n):
        '''
        Generates the next n values of the given function
        '''
        try:
            for n in range(n):
                self.get_next()
        except OverflowError, e:
            print e

    def get_next(self):
        '''
        Generates the next value of the given function
        '''
        t = self._timestep
        h = self._stepsize
        # c_y = self._y_values[t]
        y_values = self._y_values[:, t].tolist()

        # k1 = self._function(t, c_y)
        k1_args = tuple([self._t_values[t]]
                      + y_values)
        k1 = []
        for function in self._functions:
            k1.append(function(k1_args))

        # y1 = c_y + 0.5 * k1 * h
        # k2 = self._function(t + 0.5 * h, y1)
        k2_args = tuple([self._t_values[t] + (h / 2.0)]
                      + [current_y + 0.5 * h*k1[i] for i, current_y in enumerate(y_values)])
        k2 = []
        for function in self._functions:
            k2.append(function(k2_args))

        # y2 = c_y + 0.5 * k2 * h
        # k3 = self._function(t + 0.5 * h, y2)
        k3_args = tuple([self._t_values[t] + (h / 2.0)]
                      + [current_y + 0.5 * h*k2[i] for i, current_y in enumerate(y_values)])
        k3 = []
        for function in self._functions:
            k3.append(function(k3_args))

        # y3 = c_y + k3 * h
        # k4 = self._function(t + h, y3)
        k4_args = tuple([self._t_values[t] + h]
                      + [current_y + h*k3[i] for i, current_y in enumerate(y_values)])
        k4 = []
        for function in self._functions:
            k4.append(function(k4_args))

        # n_y = c_y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        an = []
        for i, current_y in enumerate(y_values):
            k_parts = k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]
            next_y = current_y + k_parts / 6.0
            an.append(next_y)

            if isinf(next_y):
                raise OverflowError(
                    "y{} reached infinity. Stopping generation at t={}".format(
                        i,
                        self._t_values[t]
                    )
                )

        an = np.swapaxes(np.array([an]), 0, 1)
        self._y_values = np.append(self._y_values, an, axis=1)
        self._t_values.append(self._t_values[t] + h)

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


def plot(objects, xscales=[], yscales=[], title=""):
    '''
    Plots current state of objects in subplots.
    Define xscales and yscales as dict of indexes.
    '''
    l = len(objects)
    first = round(l / 2)
    second = l / 2
    for i in range(0, l):
        plt.subplot(first, second, i + 1)
        if i in xscales:
            plt.xscale(xscales[i])
        if i in yscales:
            plt.yscale(yscales[i])
        fig = plt.gcf()
        fig.suptitle(title, fontsize="x-large")
        plt.plot(objects[i].get_t_values(), objects[i].get_y_values())

if __name__ == '__main__':
    '''
    Tests for Euler
    '''
    import matplotlib.pyplot as plt

    functions = [Euler, RungeKutta2, RungeKutta4]
    for function in functions:
        results = [
            function(lambda (t, x): 1, 0, 0),
            # function(lambda (t, x): x, 0, 0),
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
        plt.show()
        plt.close()

    '''
    Euler test with multiple functions
    '''
    euler6 = Euler([
        lambda (t, x, y): 0.5 * x,
        lambda (t, x, y): 0.5 * x - 1
    ], 0, [1, 2])
    euler6.generate_n(10)

    plt.title('Vector Euler')
    plt.plot(euler6.get_t_values(), euler6.get_y_values(0), 'r')
    plt.plot(euler6.get_t_values(), euler6.get_y_values(1), 'b')

    plt.show()
    plt.close()
