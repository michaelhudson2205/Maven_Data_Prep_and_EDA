"""blah, blah, blah"""
import pandas as pd

# =====================================================
# Get the data for the assignment
# Same code as used in demo 156

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

df.head()

# =====================================================

# Create June Purchases
june_purchases = (june.groupby('Customer ID')['Book']
                  .count()
                  .rename('June Purchases')
                  .to_frame()
                  .reset_index())

june_purchases.head()

# create 'Total Spend' for all books puchased in April and May
df_april_may = df[df['Purchase Date'].dt.month < 6]
df_april_may.tail()

total_spend = (df_april_may.groupby('Customer ID')['Price']
               .sum()
               .rename('Total Spend')
               .to_frame()
               .reset_index())

total_spend.head()

# combine 'June Puchases' and 'Total Spend' into single DataFrame
model_df = total_spend.merge(june_purchases, how='left').fillna(0)
model_df.head()
