
import pandas as pd

# Read raw data
df = pd.read_csv('data/raw/sales_data.csv')

# Create total amount column
df['total_amount'] = df['quantity'] * df['unit_price']

# Convert date column
df['order_date'] = pd.to_datetime(df['order_date'])

# Save transformed data
df.to_parquet('data/processed/sales_data.parquet', index=False)

print('Data Transformation Completed')
print(df.head())
