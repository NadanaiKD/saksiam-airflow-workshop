from airflow import DAG
from airflow.utils import timezone
from airflow.operators.dummy import DummyOperator


default_args = {
    "owner":"Nadanai",
    "start_date": timezone.datetime(2021, 9, 28)
}

with DAG(
    "day1_homework_1",
    schedule_interval="*/5 * * * * *",
    default_args=default_args,
    catchup=False,
    tags=["homework"],
) as dag:

    num1 = DummyOperator(task_id="1")

    num2 = DummyOperator(task_id="2")

    num3 = DummyOperator(task_id="3")

    num4 = DummyOperator(task_id="4")

    num5 = DummyOperator(task_id="5")

    num6 = DummyOperator(task_id="6")

    num7 = DummyOperator(task_id="7")

    num8 = DummyOperator(task_id="8")

    num9 = DummyOperator(task_id="9")

    num1 >> [num2,num5]
    num2 >> [num3,num6] >> num4 >> num9
    num5 >> [num6,num7] >> num8 >> num9  
