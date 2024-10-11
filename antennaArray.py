import numpy as np
import math
import matplotlib.pyplot as plt

freq = 915e6

wavelength = 3e8 / freq

# wavenumber
beta = 2*np.pi / wavelength

d = wavelength / 2

theta_degrees = np.linspace(0, 360, 1000)
theta = theta_degrees * (np.pi / 180)

steer_angle = np.deg2rad(90)
alpha = beta * d * np.cos(steer_angle)
array_elems = [
    [2, 0, 0], [3, 0, 0],
    [1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0],
    [0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0], [4, 2, 0], [5, 2, 0],
    [0, 3, 0], [1, 3, 0], [2, 3, 0], [3, 3, 0], [4, 3, 0], [5, 3, 0],
    [0, 4, 0], [1, 4, 0], [2, 4, 0], [3, 4, 0], [4, 4, 0], [5, 4, 0],
    [0, 5, 0], [1, 5, 0], [2, 5, 0], [3, 5, 0], [4, 5, 0], [5, 5, 0],
    [0, 6, 0], [1, 6, 0], [2, 6, 0], [3, 6, 0], [4, 6, 0], [5, 6, 0],
    [1, 7, 0], [2, 7, 0], [3, 7, 0], [4, 7, 0],
    [2, 8, 0], [3, 8, 0],
    ]
array_elems_gain = [
    0.25, 0.25,
    0.25, 0.5, 0.5, 0.25,
    0.25, 1, 1, 1, 1, 0.25,
    0.25, 1, 1, 1, 1, 0.25,
    0.5, 1, 1, 1, 1, 0.5,
    0.25, 1, 1, 1, 1, 0.25,
    0.25, 1, 1, 1, 1, 0.25,
    0.25, 0.5, 0.5, 0.25,
    0.25, 0.25,
]
# r_hat = np.array([])
af_arr = np.array([])
for t in theta:
    af = 0
    for e in range(len(array_elems)):
        # print(e)
        af += array_elems_gain[e] * (np.exp(-1j * (beta * np.dot(np.array([np.sin(t), np.sin(t), np.cos(t)]), np.array(array_elems[e])))))
    af_arr = np.append(af_arr, af)
    # print(af)
# print(np.size(af_arr))

# psi = beta * d * np.cos(theta) + alpha

# r_hat = np.array((np.sin(theta) + np.sin(theta) + np.cos(theta))) * array_elems
# AF = np.exp(-1j * (beta * r_hat * array_elems))

AF_norm = np.abs(af_arr) / np.max(af_arr)

linewidth_val = 3

fig, ax = plt.subplots(subplot_kw = {'projection' : 'polar'})
ax.plot(theta, np.absolute(AF_norm), linewidth = linewidth_val)
# ax.set_rmax(1)
ax.grid(True)

plt.show()
