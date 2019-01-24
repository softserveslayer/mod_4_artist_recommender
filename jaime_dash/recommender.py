# https://pythonprogramming.net/how-to-program-best-fit-line-machine-learning-tutorial/
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from recommender_queries import *

external_stylesheets = ['https://codepen.io/softserveslayer/pen/bzdoLL.css']

df = pd.read_csv('top_10_matrix.csv', low_memory=False).iloc[:,1:]
new_df = df.T
new_df.columns = new_df.iloc[0]
new_df = new_df.iloc[1:,:]
artists = list(df.Artist)
app = dash.Dash()


app.layout = html.Div(
    children=[
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(id='artist-to-artist',
        label='Artist-to-Artist Recommendation',
            children=[
                dcc.Dropdown(
                id = 'artist_dropdown',
                options=artist_dropdown,
                value= 'blink-182',
                style={'color': 'black', 'fontSize': 24}
            ),
            html.Div(
            html.P([html.P(artist) for artist in new_df['blink-182']],
            id = 'top_artists'),
            style={'color': 'navy', 'fontSize': 24}
            )
            ]
        ),
        dcc.Tab(id='EDA', label='Exploratory Data Analysis',
            children=[
html.P("Most artists get less than 150 people listening to them"),
                dcc.Graph(
        figure=go.Figure(
            data=[
                go.Histogram(
                x= artist_count,
                xbins=dict(
                    start=0,
                    end=200,
                    size= 'M2'),
                    autobinx = False
                )
            ],
            layout=go.Layout(
                title='Distribution of number of people listening per artist',
                margin=go.layout.Margin(l=40, r=0, t=40, b=60)
            )
        ),
        style={'height': 500},
        id='histogram'
    ),
    html.Br(),
    html.Br(),
                    dcc.Graph(
            figure=go.Figure(
                data=[
                    go.Histogram(
                    x= total_plays,
                    xbins=dict(
                        start=0,
                        end=5000,
                        size= 'M2'),
                        autobinx = False
                    )
                ],
                layout=go.Layout(
                    title='Distribution of total plays per artist',
                    margin=go.layout.Margin(l=40, r=0, t=40, b=60)
                )
            ),
            style={'height': 500},
            id='sum_histogram'
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        dcc.Graph(
figure=go.Figure(
    data=[
        go.Bar(
            x=list(top_20.index),
            y=list(top_20.plays),
            name='Top 20',
            marker=go.bar.Marker(
                color='rgb(55, 83, 109)'
            )
        )
    ],
    layout=go.Layout(
        title='Top 20 artists by total plays',
        showlegend=True,
        legend=go.layout.Legend(
            x=0,
            y=1.0
        ),
        margin=go.layout.Margin(l=40, r=0, t=40, b=60)
    )
),
style={'height': 500},
id='my-graph'
)
            ]
        )

        ])
    ]

)

@app.callback(
    Output(component_id='top_artists', component_property='children'),
    [Input(component_id='artist_dropdown', component_property='value')]
)
def update_output_div(input_value):
    return [html.P(artist) for artist in new_df[input_value]]

if __name__ == '__main__':
    app.run_server(debug=True)
