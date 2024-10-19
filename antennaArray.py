import numpy as np
import math
import matplotlib.pyplot as plt
import circle

freq = 915e6

wavelength = 3e8 / freq

# wavenumber
beta = 2*np.pi / wavelength

d = wavelength / 2

theta_degrees = np.linspace(0, 360, 1000)
theta = theta_degrees * (np.pi / 180)

steer_angle = np.deg2rad(0)
alpha = beta * d * np.cos(steer_angle)
# array_elems = [
#                     [2, 0, 0], [3, 0, 0],
#             [1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0],
#     [0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0], [4, 2, 0], [5, 2, 0],
#     [0, 3, 0], [1, 3, 0], [2, 3, 0], [3, 3, 0], [4, 3, 0], [5, 3, 0],
#     [0, 4, 0], [1, 4, 0], [2, 4, 0], [3, 4, 0], [4, 4, 0], [5, 4, 0],
#     [0, 5, 0], [1, 5, 0], [2, 5, 0], [3, 5, 0], [4, 5, 0], [5, 5, 0],
#     [0, 6, 0], [1, 6, 0], [2, 6, 0], [3, 6, 0], [4, 6, 0], [5, 6, 0],
#             [1, 7, 0], [2, 7, 0], [3, 7, 0], [4, 7, 0],
#                     [2, 8, 0], [3, 8, 0],
# ]
array_elems, array_elems_gain = circle.generate_circle_points_and_weights(32)
for i in range(len(array_elems)):
    array_elems[i][0] *= d
    array_elems[i][1] *= d

# array_elems_gain = [
#             0.25, 0.25,
#         0.25, 0.50, 0.50, 0.25,
#     0.25, 1.00, 1.00, 1.00, 1.00, 0.25,
#     0.25, 1.00, 1.00, 1.00, 1.00, 0.25,
#     0.50, 1.00, 1.00, 1.00, 1.00, 0.50,
#     0.25, 1.00, 1.00, 1.00, 1.00, 0.25,
#     0.25, 1.00, 1.00, 1.00, 1.00, 0.25,
#         0.25, 0.50, 0.50, 0.25,
#             0.25, 0.25,
# ]

# for i in range(len(array_elems_gain)):
#     array_elems_gain[i] = 1

af_arr = np.array([])
phi = np.deg2rad(90)
for t in theta:
    af = 0
    for e in range(len(array_elems)):
        # print(e)
        af += array_elems_gain[e] * (np.exp(-1j * (beta * np.dot(np.array([np.sin(t)*np.cos(phi), np.sin(t)*np.sin(phi), np.cos(t)]), np.array(array_elems[e]))) + alpha))
    af_arr = np.append(af_arr, 10*np.log10(np.square(np.abs(af))))
    # print(af)
# print(np.size(af_arr))

# psi = beta * d * np.cos(theta) + alpha

# r_hat = np.array((np.sin(theta) + np.sin(theta) + np.cos(theta))) * array_elems
# AF = np.exp(-1j * (beta * r_hat * array_elems))
sorted_af_arr = sorted(af_arr)
print(sorted_af_arr[-1] - sorted_af_arr[-2])
AF_norm = np.abs(af_arr) / np.max(af_arr)

linewidth_val = 3

fig, ax = plt.subplots(subplot_kw = {'projection' : 'polar'})
ax.plot(theta, np.absolute(af_arr), linewidth = linewidth_val)
# ax.set_rmax(1)
ax.grid(True)

plt.show()
