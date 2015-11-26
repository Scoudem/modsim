'''
File: lotka-volterra.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains a Lotka-Volterra Model which is simulated using the RK4 method.
'''
from integration import RungeKutta4
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

'''
Method that simulates a Lotka-Volterra Model using RK4 for the given
functions with a list containing sets of startvalues and a list of timesteps
This will show a window for each of the timesteps
'''
def lotke_volterra(functions, startvalues, dts, generations):
    for dt in dts:
        objects = []
        for startvalue in startvalues:
            objects.append(RungeKutta4(functions, 0, startvalue, stepsize=dt))

        for m in objects:
            m.generate_n(generations)

        fig = plt.gcf()
        fig.suptitle('Lotka-Volterra with dt:{} ({} timesteps)'.format(dt, generations), fontsize="x-large")
        olen = len(objects)

        ''' Make plots for each set of startvalues '''
        for i, m in enumerate(objects):
            ax = plt.subplot(2, olen, i + 1)
            x = startvalues[i][0]
            y = startvalues[i][1]
            ax.set_title("Startvalues: x:{} y:{}".format(x, y))

            ''' Plot values '''
            values = m.get_y_values()
            ax.plot(m.get_t_values(), values[0, :], label="x")
            ax.plot(m.get_t_values(), values[1, :], label="y")
            ax.legend(loc='best')

            ''' Make scatter plot '''
            ax = plt.subplot(2, olen, olen + i + 1)
            ax.scatter(values[0, :], values[1, :])
        plt.show()
        plt.close()


''' Main execution '''
if __name__ == '__main__':
    startvalues = [[11, 49], [1, 10], [15, 26]]
    dt = [1, 0.1, 0.05, 0.01, 0.005, 0.001]
    generations = 10000
    functions = [
        lambda (t, x, y): -0.5 * x + 0.01 * x * y,
        lambda (t, x, y): y - 0.1 * x * y
    ]
    lotke_volterra(functions, startvalues, dt, generations)


'''
Calculations for stable point:

x' = -a * x + c * d * x * y
y' = b * y - d * x * y
a = 0.5, b = 1,c = 0.1 and d = 0.1.

x' = -0.5 * x + 0.01 * x * y
y' = y - 0.1 * x * y

Stable:
x'=0 y'=0 x!=0 y!=0

-0.5 * x + 0.01 * x * y = 0
-0.5 + 0.01 * y = 0
0.01y = 0.5
y = 50

y - 0.1 * x * y = 0
1 - 0.1x = 0
0.1x = 1
x = 10
'''