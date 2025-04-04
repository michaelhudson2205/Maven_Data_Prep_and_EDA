"""blah blah blah"""
import pandas as pd
import seaborn as sns

songs = pd.read_csv('data/spotify_songs.csv')
songs.head()
songs.shape

sns.pairplot(songs)

songs[songs['duration_ms'] > 300000]

sns.histplot(songs['tempo'], bins=10)
songs['tempo'].round(-1).value_counts().sort_index()

# 133 Correlations
songs.corr(numeric_only=True)

songs.sort_values(by='valence')
