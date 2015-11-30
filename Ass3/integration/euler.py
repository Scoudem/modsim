'''
File: euler.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains Euler integration
'''


from integration import IntegrationTechnique
from math import isinf
import numpy as np


class Euler(IntegrationTechnique):
    '''
    Basic Euler integration
    '''
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
