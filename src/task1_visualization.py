import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    # Count how many times each category appears, sorted by category name
    counts = collections.Counter(data)
    categories = sorted(counts)
    frequencies = [counts[c] for c in categories]

    # Distinct, colour-blind-friendly colours (Okabe-Ito palette)
    colours = ['#0072B2', '#E69F00', '#009E73', '#D55E00', '#CC79A7', '#56B4E9']

    fig, ax = plt.subplots(figsize=(6, 4))
    bars = ax.bar(categories, frequencies,
                  color=[colours[i % len(colours)] for i in range(len(categories))])
    ax.bar_label(bars, padding=3)                 # exact count above each bar
    ax.set_ylim(0, max(frequencies) * 1.15)       # zero baseline, room for labels
    ax.set_xlabel('Category')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of each category')
    fig.tight_layout()

    return fig

if __name__ == '__main__':
    # Example data
    data = np.random.choice(['A', 'B', 'C'], size=100)
    plot_distribution(data)
    plt.show()
