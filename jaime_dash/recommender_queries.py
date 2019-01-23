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


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

users = pd.DataFrame(np.array([i.strip().split("\t") for i in open('user_artists.dat', 'r', encoding='latin-1').readlines()]),
                       columns = ['userID', 'artistID', 'plays'])
users = users.drop(users.index[0])
users = users.apply(pd.to_numeric)
users.head()

#Reading 'artists' dataset, splitting the first column into three columns on the newline, turning artistid into int
artists = pd.DataFrame(open('artists.dat', 'r',  encoding='latin-1').readlines())
artists = pd.DataFrame(artists[0].str.split("\t").values.tolist(),columns = ['artistID', 'name', 'url', 'pictureURL'])
artists = artists.drop(artists.index[0])
artists = artists.drop(columns=['pictureURL'])
artists['artistID'] = artists['artistID'].apply(pd.to_numeric)
users_artists = pd.merge(users, artists, on='artistID', how='left')
# Create a utility matrix A by pivoting ratings.df
users_artists_piv = users_artists.pivot(index = 'userID', columns = 'name', values = 'plays').fillna(0)
users_artists_piv = users_artists_piv.loc[(users_artists_piv.sum(axis=1) > 1), (users_artists_piv.sum(axis=0) > 150)]
users_artists_piv=users_artists_piv.reset_index()
users_artists_piv=users_artists_piv.iloc[:,1:]
users_artists_piv.head()
play_counts = users_artists_piv.sum(axis = 0, skipna = True).sort_values(ascending = False)
play_counts = pd.DataFrame(play_counts, columns = ['plays'])
top_20 = pd.DataFrame(play_counts.nlargest(20, 'plays'))
