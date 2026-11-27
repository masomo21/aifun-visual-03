import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    # Seaborn's built-in style: clean background with light gridlines
    sns.set_theme(style='whitegrid')

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=data, x='x', y='y', ax=ax,
                    color='#0072B2', s=50, alpha=0.8, edgecolor='white')
    ax.set_xlabel('Variable x')
    ax.set_ylabel('Variable y')
    ax.set_title('Relationship between x and y')
    fig.tight_layout()

    return fig


if __name__ == '__main__':
    # Example data
    data = pd.DataFrame({
        'x': np.random.rand(50),
        'y': np.random.rand(50)
    })
    create_scatter_plot(data)
    plt.show()
