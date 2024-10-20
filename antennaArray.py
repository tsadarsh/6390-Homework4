import numpy as np
import matplotlib.pyplot as plt
import circle

freq = 915e6

wavelength = 3e8 / freq

# wavenumber
beta = 2*np.pi / wavelength

d = wavelength / 2

theta_degrees = np.linspace(-90, 90, 1000)
theta = theta_degrees * (np.pi / 180)
r_ticks = np.linspace(0, 100, 1)

steer_angle = np.deg2rad(0)
alpha = beta * d * np.cos(steer_angle)

array_elems, array_elems_gain = circle.generate_circle_points_and_weights(16)
x, y, w = [], [], []

for i in range(len(array_elems)):
    x.append(array_elems[i][0])
    y.append(array_elems[i][1])
    w.append(array_elems_gain[i])
    array_elems[i][0] *= d
    array_elems[i][1] *= d

af_arr = np.array([])
phi = np.deg2rad(90)
for t in theta:
    af = 0
    for e in range(len(array_elems)):
        af += array_elems_gain[e] * (np.exp(-1j * (beta * np.dot(np.array([np.sin(t)*np.cos(phi), np.sin(t)*np.sin(phi), np.cos(t)]), np.array(array_elems[e]))) + alpha))
    af_arr = np.append(af_arr, 10*np.log10(np.square(np.abs(af))))

sorted_af_arr = sorted(af_arr)
print(sorted_af_arr[-1] - sorted_af_arr[-2])
AF_norm = np.abs(af_arr) / np.max(af_arr)

ax = plt.subplot(1, 2, 1)
plt.scatter(x, y, c=w, marker="s", s=250)
plt.colorbar()

ax = plt.subplot(1, 2, 2, projection='polar')
plt.plot(np.deg2rad(np.linspace(0, 180, 1000)), np.absolute(af_arr), linewidth = 3)
ax.set_rticks(np.arange(0, max(af_arr)+10, 5))
ax.set_thetagrids(np.arange(0, 360, 30))
# ax.grid(True)

plt.show()
