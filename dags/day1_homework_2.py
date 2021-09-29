import logging
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


def _say_hello():
    logging.info("Hello")

def _print_log_message():
    logging.info("Hi")

default_args = {
    "owner":"Nadanai",
    "start_date": timezone.datetime(2021, 9, 28),
}

with DAG(
    "day1_homework_2",
    schedule_interval="*/30 * * * *",
    default_args=default_args,
    catchup=False,
    tags=["homework"]
) as dag:

    start = DummyOperator(task_id="1")

    echo_hello = BashOperator(
        task_id="2",
        bash_command="echo 'hello'",
    )

    say_hello = PythonOperator(
        task_id="3",
        python_callable=_say_hello
    )

    print_log_message = PythonOperator(
        task_id="4",
        python_callable=_print_log_message
    )

    end = DummyOperator(task_id="5")

    start >> echo_hello >> say_hello >> print_log_message >> end
