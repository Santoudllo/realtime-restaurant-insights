from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

def run_kedro():
    subprocess.run(["kedro", "run"], check=True)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'kedro_pipeline_dag',
    default_args=default_args,
    description='Exécuter le pipeline Kedro toutes les 8 heures',
    schedule_interval='0 */8 * * *',
)

run_kedro_task = PythonOperator(
    task_id='run_kedro',
    python_callable=run_kedro,
    dag=dag,
)
