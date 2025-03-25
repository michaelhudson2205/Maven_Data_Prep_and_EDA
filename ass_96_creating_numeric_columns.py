import numpy as np
import pandas as pd

pen_sales = pd.read_excel('data/Pen Sales Data.xlsx')
pen_sales.head()

pen_sales['Total Spend'] = pen_sales['Pen Cost'] + pen_sales['Shipping Cost']
pen_sales['Free Shipping'] = np.where(
    pen_sales['Shipping Cost'] == 0, "yes", 'no')
pen_sales

# ass_100_creating_datetime_columns
pen_sales['Delivery Time'] = pen_sales['Delivery Date'] - \
    pen_sales['Purchase Date']
pen_sales.head()

pen_sales['Delivery Time'].mean()
