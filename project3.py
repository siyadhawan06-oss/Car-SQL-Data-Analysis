import sqlite3
import pandas as pd

# Load dataset
df = pd.read_excel("Car_Data_Analysis.xlsx")

# Create database
conn = sqlite3.connect("cars.db")

# Store data in SQL table
df.to_sql("cars", conn, if_exists="replace", index=False)

# SQL Query
query = """
SELECT Brand, AVG(Price) AS Average_Price
FROM cars
GROUP BY Brand
"""

result = pd.read_sql_query(query, conn)

print(result)

conn.close()