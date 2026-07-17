from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'manish',
    'start_date': datetime(2026, 7, 1),
}

dag = DAG(
    'sales_data_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
)

def start_pipeline():
    print('Starting Sales Data Pipeline')

start_task = PythonOperator(
    task_id='start_pipeline',
    python_callable=start_pipeline,
    dag=dag
)
