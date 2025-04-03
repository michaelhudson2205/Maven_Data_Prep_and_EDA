"""blah blah blah"""
import pandas as pd

groceries = pd.read_pickle('data/groceries_with_new_columns.pkl')
groceries

groceries.loc[groceries['Low Inventory'] ==
              'low Inventory', ['Price_Dollars', 'Inventory']]

groceries[groceries['Low Inventory'] == 'low Inventory']
groceries

groceries[groceries['Subcategory'] == ' Snacks']

groceries['Subcategory'] = groceries['Subcategory'].str.strip()

groceries[groceries['Subcategory'] == 'Snacks']

mask = (groceries['Low Inventory'] == 'low Inventory') & (
    groceries['Subcategory'] == 'Snacks')

groceries[mask]

groceries.loc[mask, ['Subcategory', 'Item', 'Inventory']]

# 112 DEMO Sorting
groceries.sort_values('Price_Dollars', ascending=False)

groceries.sort_values(['Subcategory', 'Price_Dollars'])

groceries[groceries['Low Inventory'] ==
          'low Inventory'].sort_values('Price_Dollars')

# 114 DEMO Grouping
groceries.head()

groceries.groupby('Category')['Inventory'].sum()
groceries.groupby('Category')['Inventory'].count()
groceries.groupby(['Category', 'Subcategory'])[
    'Inventory'].count().reset_index()

(groceries.groupby(['Category', 'Subcategory'])['Inventory']
          .agg(['sum', 'count'])
          .reset_index())

groceries.head()
groceries.groupby('Category')['Price_Dollars'].max()

# INCORRECT
groceries.groupby('Category')[['Item', 'Price_Dollars']].max()

# The correct way
(groceries[['Category', 'Item', 'Price_Dollars']]
 .sort_values('Price_Dollars', ascending=False)
 .groupby('Category')
 .head(1))
