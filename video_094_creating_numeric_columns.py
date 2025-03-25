import numpy as np
import pandas as pd

data = {
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Vegetable', 'Vegetable'],
    'Item': ['Apple', 'Banana', 'Grapes', 'Carrots', 'Celery'],
    'Price': [1.29, 0.40, 3.99, 1.50, 1.99],
}

shopping_list = pd.DataFrame(data)
print(shopping_list)

# calculate the total amount spent
shopping_list['Total Spend'] = shopping_list['Price'].sum()
shopping_list

# calculate the percent spent
shopping_list['Percent Spend'] = shopping_list['Price'] / \
    shopping_list['Total Spend'] * 100
shopping_list

# demo groceries dataset
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
