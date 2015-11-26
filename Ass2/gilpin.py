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


result = RungeKutta4([
        lambda (t, x, y, z): x * (1 - 0.001 * x - 0.001 * y - 0.01 * z),
        lambda (t, x, y, z): y * (1 - 0.001 * y - 0.0015 * x - 0.001 * z),
        lambda (t, x, y, z): z * (0.005 * x + 0.0005 * y - 1)
    ], 0, [11, 49, 23], stepsize=0.05)

result.generate_n(20000)


title = 'Gilpin'
fig = plt.gcf()
fig.suptitle(title, fontsize="x-large")

values = result.get_y_values()
x, y = values.shape
print values
for j in range(x):
    plt.plot(result.get_t_values(), values[j, :])
plt.show()
plt.close()