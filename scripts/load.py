import pandas as pd

# Load transformed parquet file
df = pd.read_parquet('data/processed/sales_data.parquet')

print('Processed Data Loaded Successfully')
print(df.head())
print(f'Total Records: {len(df)}')
