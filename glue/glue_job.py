from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('SalesETL').getOrCreate()

# Read raw CSV
df = spark.read.option('header', 'true').csv('s3://raw-sales-data/sales_data.csv')

# Transform data
df = df.withColumn('total_amount', col('quantity').cast('int') * col('unit_price').cast('int'))

# Write transformed parquet
df.write.mode('overwrite').parquet('s3://processed-sales-data/sales_data/')

print('Glue ETL Job Completed')
