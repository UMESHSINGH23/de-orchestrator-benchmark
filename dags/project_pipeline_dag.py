# Airflow DAG file
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# ---------------------------
# Task functions
# ---------------------------

def extract_data():
    """
    Extract raw data from the source dataset.
    """
    print("Extracting data...")

def clean_data():
    """
    Perform data cleaning and preprocessing.
    """
    print("Cleaning data...")

def build_features():
    """
    Create features required for analysis and modeling.
    """
    print("Building features...")

def train_model():
    """
    Train a simple analytical or machine learning model.
    """
    print("Training model...")

def generate_figures():
    """
    Generate all required figures from the analysis.
    """
    print("Generating figures...")

def save_tables():
    """
    Save all generated tables to disk.
    """
    print("Saving tables...")


# ---------------------------
# DAG Definition
# ---------------------------

with DAG(
    dag_id="project_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    description="End-to-end data engineering pipeline DAG",
) as dag:

    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    clean_task = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
    )

    feature_task = PythonOperator(
        task_id="build_features",
        python_callable=build_features,
    )

    train_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )

    figure_task = PythonOperator(
        task_id="generate_figures",
        python_callable=generate_figures,
    )

    table_task = PythonOperator(
        task_id="save_tables",
        python_callable=save_tables,
    )

    # ---------------------------
    # Task Dependencies
    # ---------------------------

    extract_task >> clean_task >> feature_task >> train_task >> figure_task >> table_task