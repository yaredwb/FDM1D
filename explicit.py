'''
@author: Yared W. Bekele
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab as py

py.rcParams['figure.figsize'] = 4.5, 6.5

# Soil layer properties
H = 1.0       # Depth of soiil layer in m
cv = 2e-6     # Coefficient of consolidation in m^2/s

# Spatial discretization
N = 80            # Number of elements of 1D mesh (N+1 nodes)
z = np.linspace(0, H, N+1)
dz = z[1] - z[0]  # Node spacing for a uniform discretization

# Temporal discretization (explicit method)
dt_max = dz**2 / 2.0 / cv
#print('Time step should be less than or equal to %'), dt_max
dt = 1.0 * dt_max

# Calculate \kappa = cv * dt / dz^2
k = cv * dt / dz**2

# Total time for simulation (t) and number of time steps (Nt)
t = 86400.0 * 2
Nt = int(t / dt) + 1

# Create array for storing pore pressures
u   = np.zeros(N+1)           # unknown u at new time level
u_1 = np.zeros(N+1)           # u at the previous time level

# Set initial condition
for i in range(0, N+1):
    u_1[i] = 50.0

# Compute the pore pressure for subsequent time steps
for n in range(0, Nt):
  # Compute pore pressure at inner nodes
  for i in range(1,N):
    u[i] = u_1[i] + k * (u_1[i-1] - 2 * u_1[i] + u_1[i+1])

    # Insert boundary conditions
    u[0] = 0.0
    #u[N] = 0.0

  # Update u_1 for next time step
  u_1[:] = u

  # Dimensionless time
  T = cv * n * dt / (H/2)**2

  # Plot results
  #if n > 0 and n % (N/2) == 0:
  if T > 0.0 and T % 0.1 == 0:
    plt.plot(u,z,label='T = ' + str(T))

plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.gca().set_xlabel('X LABEL')
plt.gca().xaxis.set_label_position('top')
plt.xlabel('$u$ [$\mathrm{kPa}$]')
plt.ylabel('$z$ [$\mathrm{m}$]')
plt.legend(loc='best')
plt.savefig('Explicit_1D_N-' + str(N) + '.eps')
plt.show()
