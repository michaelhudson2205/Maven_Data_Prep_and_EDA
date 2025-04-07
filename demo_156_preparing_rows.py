"""blah, blah, blah"""
import sqlite3

import pandas as pd

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

# goal: predict which customers are most likely to buy dog food in June
# each row should contain data for one customer
# y: June dog food purchases
# x: aggregation based on April and May data

df
df.dtypes

# convert data types to datetime and numeric fields
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
df['price'] = pd.to_numeric(df['price'].str.replace('$', ''))
df['rating'] = pd.to_numeric(df['rating'])

# check updated data types
df.dtypes

# create a subset of april and may data
df_april_may = df[df['purchase_date'].dt.month < 6]
df_april_may.head()

# create a subset of june data
df_june = df[df['purchase_date'].dt.month == 6]
df_june.head()

# create a column of june dog food purchases
dog_food_rows = df_june[df_june['item_description'] == 'Dog Food']

df_june[df_june['item_description'] == 'Dog Food']

june_dog_food_purchases = (dog_food_rows
                           .groupby('customer')['item_id']
                           .count()
                           .rename('june_dog_food_purchases'))

june_dog_food_purchases

# how much did each customer spend in april and may?
total_spend = df_april_may.groupby(
    'customer')['price'].sum().rename('total_spend')
total_spend

# each row now represents a customer - can be merged
model_df = (pd.concat([june_dog_food_purchases, total_spend], axis=1)
            .fillna(0)
            .reset_index()
            .rename(columns={'index': 'customer'}))

model_df
