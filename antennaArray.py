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

psi = beta * d * np.cos(theta) + alpha

AF = np.exp(1j * 0 * psi) + \
     np.exp(1j * 1 * psi) + \
     np.exp(1j * 2 * psi) + \
     np.exp(1j * 3 * psi) + \
     np.exp(1j * 4 * psi) + \
     np.exp(1j * 5 * psi)

AF_norm = np.abs(AF) / np.max(AF)

linewidth_val = 3

fig, ax = plt.subplots(subplot_kw = {'projection' : 'polar'})
ax.plot(theta, np.absolute(AF_norm), linewidth = linewidth_val)
ax.set_rmax(1)
ax.grid(True)

plt.show()
