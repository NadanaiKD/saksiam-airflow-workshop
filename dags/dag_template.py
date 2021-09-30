import logging
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator



default_args = {
    "owner": "Nadanai",
    "start_date": timezone.datetime(2021, 9, 27)
}
with DAG(
    "covid_case_api_data_processing",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    tags=['"saksiam'],
) as dag:

    start = DummyOperator(task_id="start")

    end = DummyOperator(task_id="end")

    start >>  end
