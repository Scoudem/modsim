'''
File: gilpin.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains Gilpin's Model which is simulated using the RK4 method.

x' = x(1 - 0.001x - 0.001y - 0.01z)
y' = y(1 - 0.001y - 0.0015x - 0.001z)
z' = z(0.005x + 0.0005y - 1)
'''
from integration import RungeKutta4, Euler
import matplotlib.pyplot as plt

'''
Method that simulates Gilpin's Model using RK4 for the given
functions with a list containing sets of startvalues and a given timestep
This will show a window containing the graphs for all startvalues
'''
def gilpin(functions, startvalues, dt, generations):
    objects = []
    for startvalue in startvalues:
        result = RungeKutta4(functions, 0, startvalue, stepsize=dt)
        result.generate_n(generations)
        objects.append(result)

    title = 'Gilpins model for dt={} ({} timesteps)'.format(dt, generations)
    fig = plt.gcf()
    fig.suptitle(title, fontsize="x-large")
    olen = len(objects)

    ''' Make plots for each set of startvalues '''
    for i, m in enumerate(objects):
        ax = plt.subplot(4, olen, i + 1)
        x = startvalues[i][0]
        y = startvalues[i][1]
        z = startvalues[i][2]
        ax.set_title("Startvalues: x:{} y:{}, z:{}".format(x, y, z))

        ''' Plot values '''
        values = m.get_y_values()
        ax.plot(m.get_t_values(), values[0, :], label="x")
        ax.plot(m.get_t_values(), values[1, :], label="y")
        ax.plot(m.get_t_values(), values[2, :], label="z")
        ax.legend(loc='best')

        ''' Make scatter plots '''
        ax = plt.subplot(4, olen, olen + i + 1)
        ax.set_title('Scatter x and y')
        ax.scatter(values[0, :], values[1, :])

        ''' Make scatter plots '''
        ax = plt.subplot(4, olen, olen * 2 + i + 1)
        ax.set_title('Scatter x and z')
        ax.scatter(values[0, :], values[2, :])

        ''' Make scatter plots '''
        ax = plt.subplot(4, olen, olen * 3 + i + 1)
        ax.set_title('Scatter y and z')
        ax.scatter(values[1, :], values[2, :])
    plt.show()
    plt.close()

''' Main execution '''
if __name__ == '__main__':
    functions = [
        lambda (t, x, y, z): x * (1 - 0.001 * x - 0.001 * y - 0.01 * z),
        lambda (t, x, y, z): y * (1 - 0.001 * y - 0.0015 * x - 0.001 * z),
        lambda (t, x, y, z): z * (0.005 * x + 0.0005 * y - 1)
    ]
    dt = 0.05
    generations = 20000
    startvalues = [[11, 49, 23], [20, 20, 20], [40, 40, 40]]
    gilpin(functions, startvalues, dt, generations)