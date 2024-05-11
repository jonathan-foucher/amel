import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams['figure.autolayout'] = True

# big curve
t = np.linspace(0, 2 * np.pi, 1000)
x, y = 16 * np.sin(t) ** 3, 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
fig, ax = plt.subplots()
ax.plot(2 * x, 2 * y, 'r')

# small curve
ax.plot(0.5 * x, 0.5 * y - 14, 'r')

# letters
# A
t = np.linspace(-25, -20, 500)
a1 = 3 * t + 70
ax.plot(t, a1, 'black')

t = np.linspace(-20, -15, 500)
a2 = -3 * t - 50
ax.plot(t, a2, 'black')

plt.hlines(0, -23.5, -16.5, 'black')

# M
plt.vlines(-13, -5, 10,'black')

t = np.linspace(-13, -8, 500)
m1 = - 1.5 * t - 9.5
ax.plot(t, m1, 'black')

t = np.linspace(-8, -3, 500)
m2 = 1.5 * t + 14.5
ax.plot(t, m2, 'black')

plt.vlines(-3, -5, 10,'black')

# E
plt.vlines(3, -5, 10,'black')

plt.hlines(10, 3, 13,'black')

plt.hlines(2.5, 3, 13,'black')

plt.hlines(-5, 3, 13,'black')

# L
plt.vlines(16, -5, 10,'black')

plt.hlines(-5, 16, 25,'black')

# print the result
plt.show()
