import numpy as np
import pandas as pd
import plotly.express as px


def create_interactive_plotly(df):
    """
    Creates an interactive scatter plot using Plotly.

    Parameters:
    df (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    plot_df = df.copy()
    plot_df['point'] = np.arange(1, len(plot_df) + 1)       # point number, shown on hover
    plot_df['series'] = 'Data points'                       # a named group, so the legend appears

    fig = px.scatter(
        plot_df, x='x', y='y', color='series',
        color_discrete_map={'Data points': '#0072B2'},
        hover_data={'point': True, 'x': ':.3f', 'y': ':.3f', 'series': False},
        labels={'x': 'Variable x', 'y': 'Variable y', 'series': 'Legend'},
        title='Interactive scatter plot of x and y (hover, zoom and pan to explore)',
        template='plotly_white',
    )
    fig.update_traces(marker=dict(size=10, opacity=0.8, line=dict(width=1, color='white')))
    fig.update_layout(showlegend=True)

    # The function only builds the figure; showing it is left to the caller,
    # so the automated test does not try to open a browser.
    return fig

if __name__ == '__main__':
    # Example data
    df = pd.DataFrame({'x': np.random.rand(50), 'y': np.random.rand(50)})
    fig = create_interactive_plotly(df)
    fig.show()                                   # opens the interactive chart in the browser
    fig.write_html('interactive_scatter.html')   # also saves it as a web page
