import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define mathematical functions to visualize
def sphere(x, y):
    return np.sqrt(1 - x**2 - y**2)

def saddle(x, y):
    return x**2 - y**2

def ripple(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Generate data points
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# Evaluate mathematical functions at each point
Z_sphere = sphere(X, Y)
Z_saddle = saddle(X, Y)
Z_ripple = ripple(X, Y)

# Create 3D visualization
fig = plt.figure(figsize=(12, 6))

# Plot 3D surface plots
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, Z_sphere, cmap='viridis')
ax1.set_title('Sphere')

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, Z_saddle, cmap='plasma')
ax2.set_title('Saddle')

ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, Z_ripple, cmap='magma')
ax3.set_title('Ripple')

plt.show()
