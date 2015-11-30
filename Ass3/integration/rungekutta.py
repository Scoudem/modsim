'''
File: rungekutta.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains second and fourth order Runge-Kutta methods.
'''


from integration import IntegrationTechnique
from math import isinf
import numpy as np


class RungeKutta2(IntegrationTechnique):
    '''
    The second order Runge-Kutta method
    '''

    def get_next(self):
        '''
        Generates the next value for each of the functions
        '''

        t = self._timestep
        h = self._stepsize
        y_values = self._y_values[:, t].tolist()

        k1_args = tuple(
            [self._t_values[t]] + y_values
        )
        k1 = []

        for function in self._functions:
            k1.append(h * function(k1_args))

        k2_args = tuple(
            [self._t_values[t] + (h / 2.0)] +
            [current_y + 0.5 * k1[i] for i, current_y in enumerate(y_values)])
        k2 = []

        for function in self._functions:
            k2.append(h * function(k2_args))

        an = []
        for i, current_y in enumerate(y_values):
            next_y = current_y + k2[i]
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


class RungeKutta4(IntegrationTechnique):
    '''
    The classical Runge-Kutta method
    '''

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

        k2_args = tuple([self._t_values[t] + (h / 2.0)]
                        + [current_y + 0.5 * h * k1[i]
                        for i, current_y in enumerate(y_values)])
        k2 = []
        for function in self._functions:
            k2.append(function(k2_args))

        k3_args = tuple([self._t_values[t] + (h / 2.0)]
                        + [current_y + 0.5 * h * k2[i]
                        for i, current_y in enumerate(y_values)])
        k3 = []
        for function in self._functions:
            k3.append(function(k3_args))

        k4_args = tuple([self._t_values[t] + h]
                        + [current_y + h * k3[i]
                        for i, current_y in enumerate(y_values)])
        k4 = []
        for function in self._functions:
            k4.append(function(k4_args))

        an = []
        for i, current_y in enumerate(y_values):
            k_parts = k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]
            next_y = current_y + k_parts / 6.0 * h
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
