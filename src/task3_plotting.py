import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_1d(data):
    """1D data: a line plot of a sequence of values against their position."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(np.arange(len(data)), data, color='#0072B2', linewidth=2)
    ax.set_xlabel('Index (position in the sequence)')
    ax.set_ylabel('Value')
    ax.set_title('1D data: line plot of a sequence of values')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def plot_2d(x, y):
    """2D data: a scatter plot of two variables."""
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x, y, color='#E69F00', s=25, alpha=0.8, edgecolor='white')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('2D data: scatter plot of y against x')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return fig


def plot_3d(x, y, z):
    """3D data: a scatter plot of points in three-dimensional space."""
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(projection='3d')        # creates an Axes3D object
    points = ax.scatter(x, y, z, c=z, cmap='viridis', s=25)
    fig.colorbar(points, ax=ax, shrink=0.6, pad=0.1, label='z value')
    ax.set_xlabel('x (first dimension)')
    ax.set_ylabel('y (second dimension)')
    ax.set_zlabel('z (third dimension)')
    ax.set_title('3D data: scatter plot of (x, y, z) points')
    return fig

if __name__ == '__main__':
    # Example data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x)

    plot_1d(x)
    plot_2d(x, y)
    plot_3d(x, y, z)
    plt.show()
