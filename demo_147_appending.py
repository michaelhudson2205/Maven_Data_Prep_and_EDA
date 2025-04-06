"""blah, blah, blah"""
import sqlite3

import pandas as pd

ca = pd.read_csv('data/happiness_data_ca.txt')
mx = pd.read_csv('data/happiness_data_mx.txt')
us = pd.read_csv('data/happiness_data_us.txt')
cr = pd.read_csv('data/happiness_data_cr.txt')

# canada data
ca.head(2)

# mexico data
mx.head(2)

# us data - missing last column
us.head(2)

# costa rica data - first column has different name
cr.head(2)

# append canada & mexico
pd.concat([ca, mx]).head()
pd.concat([ca, mx]).tail()

# append canada, mexico & united states
pd.concat([ca, mx, us]).head()
pd.concat([ca, mx, us]).tail()

# append canada, mexico, united states & costa rica
pd.concat([ca, mx, us, cr]).head()
pd.concat([ca, mx, us, cr]).tail()

# rename column before appending
pd.concat([ca, mx, us, cr.rename(
    columns={'nombre del país': 'country_name'})]).reset_index(drop=True)

# ===149. DEMO: Joining===
sales_may = pd.read_excel('data/Sales Tables.xlsx', sheet_name=0)
sales_june = pd.read_excel('data/Sales Tables.xlsx', sheet_name=1)
regions = pd.read_excel('data/Sales Tables.xlsx', sheet_name=2)

sales_may
sales_june
regions

# merge sales_may with regions
# inner join INCORRECT
sales_may.merge(regions)

# left join
sales_may.merge(regions, how='left')

# can be more specific
sales_may.merge(regions, how='left', left_on='store', right_on='store')

# be more concise
sales_may.merge(regions, how='left', on='store')

# ===151. DEMO: Types of Joins===
# only look at 2020's data
happy_scores = pd.concat([ca, mx, us, cr.rename(
    columns={'nombre del país': 'country_name'})]).reset_index(drop=True)
happy_scores = happy_scores[happy_scores['year'] > 2019]
happy_scores

# population by country in North America
pop = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)')[0]
pop = pop[pop['UN statistical subregion[1]'] == 'Northern America']
pop

# inner join (default)
happy_scores.merge(pop, how='inner', left_on='country_name',
                   right_on='Country or territory')
happy_scores.merge(pop, how='outer', left_on='country_name',
                   right_on='Country or territory')
happy_scores.merge(pop, how='left', left_on='country_name',
                   right_on='Country or territory')
happy_scores.merge(pop, how='right', left_on='country_name',
                   right_on='Country or territory')

# ===152. DEMO: Creating a Single Table
# connect to a sql database
conn = sqlite3.connect('data/online_shop.db')

# view the transactions table
transactions = pd.read_sql('SELECT * FROM transactions', conn)
transactions.head()

# view the items table
items = pd.read_sql('SELECT * FROM items', conn)
items.head()

# I believe it is good practice to close the connection
conn.close()

# merge the two table together
df = transactions.merge(items, how='left', on='item_id')
df
