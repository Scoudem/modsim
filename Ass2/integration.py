'''
File: integration.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains Euler and second and fourth order Runge-Kutta integration methods.
'''

from math import isinf


'''
'''
class Euler:
    '''
    Constructor, takes a function, initial timestep, initial y value.
    Optional: stepsize
    '''
    def __init__(self, function, time, y0, stepsize=1):
        self._function = function
        self._timestep = time
        self._x_values = [0] * (time + 1)
        self._y_values = [0] * time + [y0]
        self._stepsize = stepsize

        print self


    '''
    Returns the current list of x values
    '''
    def getXValues(self):
        return self._x_values


    '''
    Returns the current list of y values
    '''
    def getYValues(self):
        return self._y_values


    '''
    Generates the next N values of the given function
    '''
    def generateN(self, N):
        for n in range(N):
            self.getNext()


    '''
    Generates the next value of the given function
    '''
    def getNext(self):
        An = self._function(self._x_values[self._timestep],
                            self._y_values[self._timestep])
        self._x_values.append(self._x_values[self._timestep] + self._stepsize)
        self._y_values.append(self._y_values[self._timestep] +
                              self._stepsize * An)

        if isinf(self._y_values[-1]):
            raise OverflowError(
                "y reached infinity. Stopping generation at {}".format(
                    self._timestep
                )
            )

        self._timestep += 1


    '''
    Returns a string containing all variables
    '''
    def __str__(self):
        return "Current timestep: {}.\nStepsize: {}.\nx: {}.\ny: {}.".format(
            self._timestep,
            self._stepsize,
            self._x_values,
            self._y_values
        )


'''
Tests
'''
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    euler1 = Euler(lambda x, y: 1, 0, 0)
    euler2 = Euler(lambda x, y: y, 0, 0)
    euler3 = Euler(lambda x, y: y, 0, 1)
    euler4 = Euler(lambda x, y: y * y, -1, 1)
    euler5 = Euler(lambda x, y: y * y, 1, 1)

    euler1.generateN(10)
    euler2.generateN(10)
    euler3.generateN(5)
    euler4.generateN(1)
    euler5.generateN(10)

    print euler1, euler2, euler3, euler4, euler5

    # ax = plt.gca()
    # ax.set_yscale("log")
    plt.subplot(231)
    plt.plot(euler1.getXValues(), euler1.getYValues())
    plt.subplot(232)
    plt.plot(euler2.getXValues(), euler2.getYValues())
    plt.subplot(233)
    plt.plot(euler3.getXValues(), euler3.getYValues())
    plt.subplot(234)
    plt.plot(euler4.getXValues(), euler4.getYValues())
    plt.subplot(235)
    plt.plot(euler5.getXValues(), euler5.getYValues())
    plt.show()
