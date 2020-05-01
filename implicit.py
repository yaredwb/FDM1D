'''
@author: Yared W. Bekele
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab as py
import scipy.linalg as lin

py.rcParams['figure.figsize'] = 4.5, 6.5

# Soil layer properties
H = 1.0       # Depth of soiil layer in m
cv = 2e-6     # Coefficient of consolidation in m^2/s

# Spatial discretization
N = 160            # Number of elements of 1D mesh (N+1 nodes)
z = np.linspace(0, H, N+1)
dz = z[1] - z[0]  # Node spacing for a uniform discretization

# Temporal discretization
dt = 100

# Calculate \kappa = cv * dt / dz^2
k = cv * dt / dz**2

# Total time for simulation (t) and number of time steps (Nt)
t = 86400.0 * 2
Nt = int(t / dt) + 1

# Create array for storing pore pressures
u   = np.zeros(N+1)           # unknown u at new time level
u_1 = np.zeros(N+1)           # u at the previous time level

# Boundary conditions
u[0] = 0
u[N] = 0

# Coefficient matrix and RHS vector of linear system Ax = b
A = np.zeros((N-1,N-1))
b = np.zeros(N-1)
for i in range(0,N-1):
    A[i,i]   = 1 + 2*k

for i in range(0,N-2):
    A[i,i+1] = -k

for i in range(1,N-1):
    A[i,i-1] = -k

# Set initial condition
for i in range(0, N+1):
    u_1[i] = 50. 
# Compute the pore pressure for subsequent time steps
for n in range(0, Nt):
    # RHS vector b for inner unknown nodes
    for i in range(1,N):
        b[i-1] = u_1[i]

    # Insert boundary conditions to RHS vector
    b[0] += k * u[0]
    b[N-2] += k * u[N]

    # Solve linear system
    u[1:N] = lin.solve(A,b)

    # Update u_1 for next time step
    u_1[:] = u

    # Dimensionless time
    T = cv * n * dt / (H/2)**2

    # Plot results
    #if T >= 0.2 and T < 0.25 :
    if T > 0.0 and T % 0.1 == 0:
        plt.plot(u,z,label='T = ' + str(T))

plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()
plt.gca().set_xlabel('X LABEL')
plt.gca().xaxis.set_label_position('top')
plt.xlabel('$u$ [$\mathrm{kPa}$]')
plt.ylabel('$z$ [$\mathrm{m}$]')
plt.legend(loc='best')
plt.savefig('Implicit_1D_N-' + str(N) + '_dt-' + str(dt) + '.eps')
plt.show()
