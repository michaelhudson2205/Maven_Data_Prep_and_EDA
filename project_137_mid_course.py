# ===Video 138. SOLUTION: Exploring Data===

"""blah, blah, blah"""
import numpy as np
import pandas as pd
import seaborn as sns

movies = pd.read_csv('data/Rotten Tomatoes Movies.csv')
movies.head(3)

movies = movies[['movie_title', 'rating', 'genre', 'in_theaters_date', 'runtime_in_minutes',
                 'tomatometer_rating', 'tomatometer_count', 'audience_rating', 'audience_count']]
movies.head()

movies.shape
movies['in_theaters_date'].dt.year
movies.dtypes

# convert the in_theaters_date to a datetime field
movies['in_theaters_date'] = pd.to_datetime(movies['in_theaters_date'])
movies.dtypes

# filter on only movies from the 2010's and newer
movies = movies[movies['in_theaters_date'].dt.year >= 2010]
movies.shape

# highest rated movies by critics
movies.sort_values('tomatometer_rating', ascending=False).head()

# highest rated movies by the audience
movies.sort_values('audience_rating', ascending=False).head()

# filter movies data set to only include 100k+ audience ratings
movies_popular = movies[movies['audience_count'] > 100000]
movies_popular.shape

# highest rated popular movies by critics
movies_popular.sort_values('tomatometer_rating', ascending=False).head()

# highest rated popular movies by the audience
movies_popular.sort_values('audience_rating', ascending=False).head()

# how many movies fall under each type of rating?
movies_popular['rating'].value_counts()

# average audience rating for each movie rating type
movies_popular.groupby('rating')['audience_rating'].mean()

# ===Video 139. SOLUTION: Creating New Columns===
# create a column for animation
movies_popular['Animation'] = np.where(
    movies_popular['genre'].str.contains('Animation'), 1, 0)

# copy to avoid the warning
movies_popular = movies[movies['audience_count'] > 100000].copy()
movies_popular['Animation'] = np.where(
    movies_popular['genre'].str.contains('Animation'), 1, 0)
movies_popular['Action & Adventure'] = np.where(
    movies_popular['genre'].str.contains('Action & Adventure'), 1, 0)
movies_popular['Comedy'] = np.where(
    movies_popular['genre'].str.contains('Comedy'), 1, 0)

# Create summary table
movies_popular.groupby('rating')[
    ['Animation', 'Action & Adventure', 'Comedy']].sum()

# Average critic rating vs audience rating
movies_popular.groupby('Animation')[
    ['tomatometer_rating', 'audience_rating']].mean()
movies_popular.groupby('Action & Adventure')[
    ['tomatometer_rating', 'audience_rating']].mean()
movies_popular.groupby('Comedy')[
    ['tomatometer_rating', 'audience_rating']].mean()

# ===Video 140. SOLUTION: Visualizing Data===
# exclude the newly created columns from the pair plot
sns.pairplot(movies_popular.iloc[:, :-3])

# find the outlier in the audience_count
movies_popular[movies_popular['audience_count'] > 2000000]
