
import pandas as pd

# Read raw CSV file
df = pd.read_csv('data/raw/sales_data.csv')

print('Data Ingested Successfully')
print(df.head())
print(f'Total Records: {len(df)}')
