from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'daniel',
    'depends_on_past': False,
    'start_date': datetime(2025, 7, 24),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'train_model',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
)

train_task = BashOperator(
    task_id='train_model_task',
    bash_command='python /opt/airflow/pipeline/train_model.py',
    dag=dag,
)
