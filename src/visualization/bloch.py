import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def qubit_to_bloch(alpha, beta):
    """Convert qubit amplitudes to Bloch sphere coordinates (x, y, z)"""
    
    alpha = complex(alpha)
    beta = complex(beta)
    
    x = 2 * np.real(alpha * np.conjugate(beta))
    y = 2 * np.imag(alpha * np.conjugate(beta))
    z = abs(alpha)**2 - abs(beta)**2
    
    return x, y, z

def plot_bloch_vector(alpha, beta):
    """Plot the qubit state on the Bloch Sphere"""
    
    # Convert to (x, y, z)
    x, y, z = qubit_to_bloch(alpha, beta)
    
    # Create a 3D Plot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection="3d")
    
    # Draw Sphere
    u, v = np.linspace(0, 2 * np.pi, 50), np.linspace(0, np.pi, 50)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones_like(u), np.cos(v))
    
    ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.3)
    
    # Draw axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='red', linewidth=2)    # X-axis
    ax.quiver(0, 0, 0, 0, 1, 0, color='green', linewidth=2)  # Y-axis
    ax.quiver(0, 0, 0, 0, 0, 1, color='blue', linewidth=2)   # Z-axis
    
    # Plot qubit vector
    ax.quiver(0, 0, 0, x, y, z, color='black', linewidth=3)
    
    # Labels
    ax.set_title("Bloch Sphere Representation")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    
    plt.show()
