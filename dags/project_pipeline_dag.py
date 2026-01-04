# Airflow DAG file
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.data_ingestion.ingest_data import ingest_data
from src.data_cleaning.clean_data import clean_data
from src.feature_engineering.build_features import build_features
from src.modeling.train_model import train_model
from src.evaluation.generate_outputs import generate_outputs

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="project_pipeline_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest = PythonOperator(
        task_id="data_ingestion",
        python_callable=ingest_data
    )

    clean = PythonOperator(
        task_id="data_cleaning",
        python_callable=clean_data
    )

    features = PythonOperator(
        task_id="feature_engineering",
        python_callable=build_features
    )

    train = PythonOperator(
        task_id="model_training",
        python_callable=train_model
    )

    evaluate = PythonOperator(
        task_id="model_evaluation",
        python_callable=generate_outputs
    )

    ingest >> clean >> features >> train >> evaluate
