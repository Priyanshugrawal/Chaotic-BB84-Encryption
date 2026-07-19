# Lorenz System Time Series (Final)
# Initial Conditions:
# x = 0.1
# y = 0.2
# z = 0.3
#
# Parameters:
# sigma = 10
# rho = 5
# beta = 8/3

import matplotlib.pyplot as plt

# -----------------------------
# Parameters
# -----------------------------
sigma = 10
rho = 5
beta = 8 / 3

# -----------------------------
# Initial Conditions
# -----------------------------
x = 0.1
y = 0.2
z = 0.3

# -----------------------------
# Simulation Settings
# -----------------------------
dt = 0.01
iterations = 1000

# -----------------------------
# Lists to store data
# -----------------------------
time = []
x_values = []
y_values = []
z_values = []

# -----------------------------
# Euler Method
# -----------------------------
for i in range(iterations):

    time.append(i + 1)      # Iteration number

    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    x = x + dx * dt
    y = y + dy * dt
    z = z + dz * dt

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(12,9))

# X vs Time
plt.subplot(3,1,1)
plt.plot(time, x_values,
         color='blue',
         linewidth=1.5)
plt.title("Lorenz System: X vs Time")
plt.ylabel("X")
plt.xlim(1,1000)
plt.xticks(range(0,1001,100))
plt.grid(True)

# Y vs Time
plt.subplot(3,1,2)
plt.plot(time, y_values,
         color='red',
         linewidth=1.5)
plt.title("Lorenz System: Y vs Time")
plt.ylabel("Y")
plt.xlim(1,1000)
plt.xticks(range(0,1001,100))
plt.grid(True)

# Z vs Time
plt.subplot(3,1,3)
plt.plot(time, z_values,
         color='green',
         linewidth=1.5)
plt.title("Lorenz System: Z vs Time")
plt.xlabel("Iteration")
plt.ylabel("Z")
plt.xlim(1,1000)
plt.xticks(range(0,1001,100))
plt.grid(True)

plt.tight_layout()
plt.show()