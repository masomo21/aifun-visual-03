import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def perform_eda(df):
    """
    Performs EDA including descriptive statistics, outlier detection,
    and correlation analysis.

    Parameters:
    df (DataFrame): A DataFrame containing data for EDA.
    """
    numeric = df.select_dtypes(include='number')

    # ---------- Step 1: descriptive statistics, as a table ----------
    stats = pd.DataFrame({
        'mean': numeric.mean(),
        'median': numeric.median(),
        'mode': numeric.mode().iloc[0],      # first mode if several values tie
        'variance': numeric.var(),
        'std': numeric.std(),
        'min': numeric.min(),
        'max': numeric.max(),
    }).round(3)
    print('Step 1. Descriptive statistics:')
    print(stats.to_string())
    print('Findings: compare mean and median for each column. A mean far above the median '
          'suggests right skew; variance shows how spread out each column is '
          '(columns on larger scales naturally have larger variance).\n')

    # ---------- Step 2: outlier detection with box plots ----------
    q1, q3 = numeric.quantile(0.25), numeric.quantile(0.75)
    iqr = q3 - q1
    outliers = ((numeric < q1 - 1.5 * iqr) | (numeric > q3 + 1.5 * iqr)).sum()

    fig_box, axes = plt.subplots(1, len(numeric.columns), figsize=(4 * len(numeric.columns), 4))
    axes = np.atleast_1d(axes)
    for ax, column in zip(axes, numeric.columns):
        # one panel per column, because the columns can have very different scales
        sns.boxplot(y=numeric[column], ax=ax, color='#56B4E9')
        ax.set_title(f'{column}: {outliers[column]} potential outlier(s)')
        ax.set_ylabel(column)
    fig_box.suptitle('Box plots: distribution and potential outliers (beyond 1.5 × IQR)')
    fig_box.tight_layout()

    print('Step 2. Potential outliers per column (1.5 × IQR rule):')
    print(outliers.to_string())
    print('Findings: points beyond the whiskers are potential outliers. They should be '
          'investigated before removal, because they may be genuine values.\n')

    # ---------- Step 3: correlation matrix and annotated heatmap ----------
    corr = numeric.corr()
    fig_heat, ax_heat = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', vmin=-1, vmax=1, square=True,
                cbar_kws={'label': 'Pearson correlation'}, ax=ax_heat)
    ax_heat.set_title('Correlation matrix of numeric variables')
    fig_heat.tight_layout()

    pairs = corr.where(np.triu(np.ones(corr.shape, dtype=bool), k=1)).stack()
    print('Step 3. Correlation matrix:')
    print(corr.round(2).to_string())
    if not pairs.empty:
        strongest = pairs.abs().idxmax()
        print(f'Findings: the strongest relationship is between {strongest[0]} and {strongest[1]} '
              f'(r = {pairs[strongest]:.2f}). Values near 0 mean no linear relationship; '
              'correlation does not imply causation.')

    return {'statistics': stats, 'outliers': outliers, 'correlation': corr,
            'boxplot_figure': fig_box, 'heatmap_figure': fig_heat}

if __name__ == '__main__':
    # Example data
    df = pd.DataFrame({
        'A': np.random.rand(50),
        'B': np.random.rand(50) * 10,
        'C': np.random.rand(50) * 100
    })
    perform_eda(df)
    plt.show()
