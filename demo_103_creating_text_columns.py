import numpy as np
import pandas as pd

groceries = pd.read_excel('data/Groceries.xlsx')
groceries.head()

groceries.Price_Dollars + 2
groceries.info()

groceries['Price_Dollars'] + 3

groceries['New Column'] = round(groceries['Price_Dollars'] * 1.05, 2)
groceries

total_inventory = groceries['Inventory'].sum()
total_inventory
groceries['Percent Inventory'] = round(
    groceries['Inventory'] / total_inventory * 100, 2)
groceries.head()

groceries['Low Inventory'] = np.where(
    groceries['Inventory'] < 50, "low Inventory", '')
groceries

# Demo

groceries.head()

groceries['Product_ID_Num'] = groceries['Product_ID'].str[1:]
groceries.head()
groceries.dtypes
groceries['Product_ID_Num'] = groceries['Product_ID_Num'].astype('int')
groceries.dtypes

groceries['Category'].value_counts()

groceries['Category'].str.split(':')

pd.DataFrame(groceries['Category'].str.split(':').to_list())
groceries[['Category', 'Subcategory']] = pd.DataFrame(
    groceries['Category'].str.split(':').to_list())
groceries.head()

groceries['Organic'] = groceries['Item'].str.lower().str.contains('organic')
groceries.head()

# Back demo 99 to create date time columns
groceries['Last_Updated_Time'] = groceries['Last_Updated'].dt.time

groceries['Shipment_Date_DOW'] = groceries['Next_Scheduled_Shipment'].dt.day_of_week
groceries.head()
dow_mapping = {0: 'Monday',
               1: 'Tuesday',
               2: 'Wednesday',
               3: 'Thursday',
               4: 'Friday',
               5: 'Saturday',
               6: 'Sunday'}

groceries['Shipment_Date_DOW'] = groceries['Shipment_Date_DOW'].map(
    dow_mapping)

groceries.head()

groceries['New_Shipment_Date'] = groceries['Next_Scheduled_Shipment'] + \
    pd.to_timedelta(1, 'D')

groceries['New_Shipment_Date'] = np.where(groceries['Subcategory'] == ' Fruit',
                                          groceries['Next_Scheduled_Shipment'] +
                                          pd.to_timedelta(1, 'D'),
                                          groceries['Next_Scheduled_Shipment'])

groceries

# reorder columns
groceries_with_new_columns = groceries[['Product_ID', 'Product_ID_Num', 'Category', 'Subcategory', 'Item', 'Organic', 'Price_Dollars',
                                        'Inventory', 'Percent Inventory', 'Low Inventory', 'Last_Updated', 'Last_Updated_Time', 'Next_Scheduled_Shipment', 'Shipment_Date_DOW']]
groceries_with_new_columns.head()

groceries_with_new_columns.to_pickle('data/groceries_with_new_columns.pkl')
