from dash_package import app
import dash_core_components as dcc
import dash_html_components as html


app.layout = html.Div(
    children=[
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(id='user', label='Recommendation by User',
            children=[
            # dcc.Graph(figure=
            # {'data': [1, 2 ,3],
            # 'layout': {}})
            ]
        ),
        dcc.Tab(id='artist', label='Artist Recommendation',
            children=[
            # dcc.Graph(figure=
            # {'data': [1, 2, 3],
            # 'layout': {}})
            ]
        ),
        dcc.Tab(id='analysis', label='Artist Analysis',
            children=[
            dcc.Graph(figure=
            {'data': [
            {'x': [1,2,3], 'y': [4,5,6], 'type': "line",'name': "Example"}],
            'layout': {}})
            ]
        )

        ])
    ]
)





# def listing_prices():
#     listing_titles = ['bk', 'queens', 'manhattan']
#     listing_prices = [4, 10, 20]
#     return {'x': listing_titles, 'y': listing_prices}
#
# def job_salaries():
#     listing_titles = ['engineer', 'data scientist', 'product manager']
#     listing_prices = [4, 55, 6]
#     return {'x': listing_titles, 'y': listing_prices}


# app.layout = html.Div(
#     children=[
#     dcc.Tabs(id="tabs", children=[
#         dcc.Tab(id='other', label='salaries',
#             children=[
#             dcc.Graph(figure=
#             {'data': [job_salaries()],
#             'layout': {}})
#             ]
#         ),
#         dcc.Tab(id='something', label='apartments',
#             children=[
#             dcc.Graph(figure=
#             {'data': [listing_prices()],
#             'layout': {}})
#             ]
#         )
#
#         ])
#     ]
# )
