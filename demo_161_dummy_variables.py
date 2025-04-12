# connect to a sql database
import sqlite3

import pandas as pd

conn = sqlite3.connect('data/online_shop.db')

# view the transactions table
transactions = pd.read_sql('SELECT * FROM transactions', conn)
transactions.head()

# view the items table
items = pd.read_sql('SELECT * FROM items', conn)
items.head()

conn.close()

# merge two tables together
df = transactions.merge(items, how='left', on='item_id')
df

# convert data types to datetime and numeric fields
df.purchase_date = pd.to_datetime(df.purchase_date)
df.price = pd.to_numeric(df.price.str.replace('$', ''))
df.rating = pd.to_numeric(df.rating)

# create a subset of april and may data
df_april_may = df[df.purchase_date.dt.month < 6]
df_april_may.head()

# create a subset of june data
df_june = df[df.purchase_date.dt.month == 6]
df_june.head()

# create a column of june dog food purchases
dog_food_rows = df_june[df_june.item_description == 'Dog Food']

june_dog_food_purchases = (dog_food_rows
                           .groupby('customer')['item_id']
                           .count()
                           .rename('june_dog_food_purchases'))

june_dog_food_purchases

# how much did each customer spend in april and may?
total_spend = df_april_may.groupby(
    'customer')['price'].sum().rename('total_spend')
total_spend

# each row now represents a customer
model_df = (pd.concat([june_dog_food_purchases, total_spend], axis=1)
            .fillna(0).reset_index()
            .rename(columns={'index': 'customer'}))

model_df
model_df.head()
df_april_may.head()

# specify a column to get dummy variables
category_dummies = pd.get_dummies(df_april_may['category'], dtype='int')
category_dummies

# combine with customer data
pd.concat([df_april_may['customer'], category_dummies], axis=1)

# group by customer so each row is a single customer
categories = pd.concat([df_april_may['customer'], category_dummies],
                       axis=1).groupby('customer').sum().reset_index()
categories.head()

# add categories to the model dataframe
model_df = model_df.merge(categories, how='left', on='customer')
model_df.head()
model_df.shape

# view the dataframe with april/may behaviour
df_april_may.head()
df_april_may.shape

# 163 DEMO Reparing DateTime Columns
# goal: add on a new column based on date (number of days since last purchase)

# find the last purchase date
last_purchase = df_april_may.groupby('customer')['purchase_date'].max()
last_purchase.head()

# note down today's date
today = pd.Series(pd.to_datetime('2023-06-01'), index=last_purchase.index)
today.head()

# find the number of days since the last purchase
days_between = (today - last_purchase).dt.days.rename('days_between')
days_between.head()

# add the column to the model_df dataframe
model_df = model_df.merge(days_between.reset_index(),
                          how='left', on='customer')
model_df.head()
