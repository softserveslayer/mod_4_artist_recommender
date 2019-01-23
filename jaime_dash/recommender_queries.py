import numpy as np
import pandas as pd
import dash_html_components as html

df = pd.read_csv('top_10_matrix.csv', low_memory=False).iloc[:,1:]
artists = list(df.Artist)



artist_dropdown = []
for artist in artists:
    artist_dict = {'label': artist, 'value': artist}
    artist_dropdown.append(artist_dict)


new_df = df.T
new_df.columns = new_df.iloc[0]
new_df = new_df.iloc[1:,:]

def create_top_10(artist):
    return list(new_df[artist])


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
