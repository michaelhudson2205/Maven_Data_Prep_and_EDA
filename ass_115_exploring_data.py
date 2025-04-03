"""blah, blah, blah"""
import pandas as pd

df = pd.read_csv('data/happiness_survey_data.csv')
df.head()
df.shape
df.describe()

# Filter out any data before 2010 and after 2019
mask = (df['year'] >= 2010) & (df['year'] < 2020)
df[mask]
filtered_df = df[mask]
filtered_df.head()

# Group the data by country and calculate the maximum happiness score for each one
filtered_df.groupby('country_name')['happiness_score'].max()

# Sort the grouped countries by max happiness score and return the top five
filtered_df.groupby('country_name')['happiness_score'].max(
).sort_values(ascending=False).head(5)

# Group the data by country and calculate the average happiness score for each one
filtered_df.groupby('country_name')['happiness_score'].mean()

# Sort the grouped countries by mean happiness score and return the top five
filtered_df.groupby('country_name')['happiness_score'].mean(
).sort_values(ascending=False).head(5)

# Compare the two lists
