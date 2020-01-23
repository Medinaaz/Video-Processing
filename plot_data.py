import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('stat.csv')
"""fig = go.Figure(go.Scatter(x = df['PlayersTR'], y = df['PtsTR'],
                  name='Average Statistics FIBA'))

fig.update_layout(title='Average Statistics FIBA',
                   plot_bgcolor='rgb(229, 253, 255)',
                   showlegend=True)

fig.show()"""

fig = go.Figure(go.Scatter(x = df['PlayersUSA'], y = df['pts'],
                  name='Average Statistics FIBA'))

fig.update_layout(title='Average Statistics FIBA',
                   plot_bgcolor='rgb(229, 253, 255)',
                   showlegend=True)

fig.show()