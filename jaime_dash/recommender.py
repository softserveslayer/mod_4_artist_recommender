# https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from recommender_queries import *

df = pd.read_csv('top_10_matrix.csv', low_memory=False).iloc[:,1:]
new_df = df.T
new_df.columns = new_df.iloc[0]
new_df = new_df.iloc[1:,:]
artists = list(df.Artist)
app = dash.Dash()

# app.layout = dash_table.DataTable(
#     id='top_ten_table',
#     # columns=[{"name": i, "id": i} for i in new_df['The Glitch Mob']],
#     # columns=[{"name": i, "id": i} for i in new_df.iloc[:,5:6].columns],
#     columns = ['Artists'],
#     data=new_df['The Glitch Mob'].to_dict(),
#     # data=new_df.iloc[:,5:6].to_dict("rows"),
#
# )

app.layout = html.Div([
    dcc.Dropdown(
    id = 'artist_dropdown',
    options=artist_dropdown,
    value= 'test'
), html.Div(
list(new_df['Katy Perry'])
)
])



if __name__ == '__main__':
    app.run_server(debug=True)
