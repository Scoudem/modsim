'''
File: lotka-volterra.py
Authors:
 - Sjoerd Wenker, 10617558
 - Tristan van Vaalen, 10551832

Contains a Lotka-Volterra Model which is simulated using the RK4 method.
'''
from integration import RungeKutta4
import matplotlib.pyplot as plt

startvalues = [[11.0, 49.0], [1.0, 20.0]]
#startvalues = [[1, 20]]
objects = []

for i,startvalue in enumerate(startvalues):
    objects.append(RungeKutta4([
        lambda (t, x, y): -0.5 * x + 0.01 * x * y,
        lambda (t, x, y): y - 0.1 * x * y
    ], 0, startvalue, stepsize=0.1))

for i, result in enumerate(objects):
    result.generate_n(1200)

fig = plt.gcf()
fig.suptitle('Lotka-Volterra', fontsize="x-large")

for i, result in enumerate(objects):
    plt.subplot(len(objects), 1, i + 1)
    values = result.get_y_values()
    x, y = values.shape
    print values
    for j in range(x):
        plt.plot(result.get_t_values(), values[j, :])
plt.show()
plt.close()

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