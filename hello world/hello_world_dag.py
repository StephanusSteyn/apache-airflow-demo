from airflow import DAG
from datetime import datetime

dag = DAG(
    dag_id = "hello_world",
    start_date = datetime(2026,1,30),
    schedule = @daily,
    catchup = True
)
