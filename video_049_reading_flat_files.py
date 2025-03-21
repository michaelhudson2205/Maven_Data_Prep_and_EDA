"""This file is for blah blah blah"""
import pandas as pd
import pyodbc

pd.read_csv("data/course_offerings.csv")

pd.read_excel("data/Course Offerings.xlsx", sheet_name=1)

# A digression into connecting to SQL Server
DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'MikeXPS15'
DATABASE_NAME = 'Red30Tech'

connection_string = f"""

    DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

conn = pyodbc.connect(connection_string)
print(conn)

pd.read_sql("SELECT * FROM Customers WHERE City = 'Detroit'", conn)

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM Customers WHERE City = 'Amarillo'")
# row = cursor.fetchone()

# while row:
#     print(row)
#     row = cursor.fetchone()

conn.close()

# The end of the little excursion into SQL

df = pd.read_csv("data/course_offerings.csv")
df

df.head(2)
df.tail(2)

df.shape
df.count()
df.describe()
df.info()
