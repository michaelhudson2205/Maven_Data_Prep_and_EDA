"""blah, blah, blah"""
import pandas as pd

april = pd.read_excel('data/Book_Sales_April.xlsx')
may = pd.read_excel('data/Book_Sales_May.xlsx')
june = pd.read_excel('data/Book_Sales_June.xlsx')
customers = pd.read_csv('data/Book_Customers.csv')

# check dataframes
april.head()
may.head()
june.head()

sales = pd.concat([april, may, june]).reset_index(drop=True)
sales.head()

customers.head()

# join
df = sales.merge(customers, how='left', on='Customer ID')
