#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
### DAG Tutorial Documentation
This DAG is demonstrating an Extract -> Transform -> Load pipeline
"""
from __future__ import annotations

# [START tutorial]
# [START import_module]
import json
from textwrap import dedent

import pendulum

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python import ExternalPythonOperator

# [END import_module]

# [START instantiate_dag]
with DAG(
    "ML_inference_DAG",
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={"retries": 2, 'provide_context': True},
    # [END default_args]
    description="DAG tutorial",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:
    # [END instantiate_dag]
    # [START documentation]
    dag.doc_md = __doc__
    # [END documentation]

    # [START extract_function]

    # [END extract_function]

    # [START transform_function]
    def predict(**kwargs):
        from sklearn.datasets import load_iris
        import pickle as pkl
        import pandas as pd

        
        with open('./dags/models/model.pkl', 'rb') as f:
            model = pkl.load(f)

        X = load_iris().data
        pred = model.predict(X)
        df = pd.DataFrame({'label': pred})
        df.to_csv('./dags/outputs/prediction.csv')


       

    # [END transform_function]

    # [START load_function]
    # [END load_function]

    # [START main_flow]
    # extract_task = ExternalPythonOperator(
    #     task_id="load",
    #     python='/opt/airflow/.venv/bin/python3',
    #     python_callable=load,
    # )
    # extract_task.doc_md = dedent(
    #     """\
    # #### Extract task
    # A simple Extract task to get data ready for the rest of the data pipeline.
    # In this case, getting data is simulated by reading from a hardcoded JSON string.
    # This data is then put into xcom, so that it can be processed by the next task.
    # """
    # )

    transform_task = ExternalPythonOperator(
        task_id="predict",
        python='/opt/airflow/.venv/bin/python3',
        python_callable=predict,
    )
    transform_task.doc_md = dedent(
        """\
    #### Transform task
    A simple Transform task which takes in the collection of order data from xcom
    and computes the total order value.
    This computed value is then put into xcom, so that it can be processed by the next task.
    """
    )

    # save_task = ExternalPythonOperator(
    #     task_id="save",
    #     python='/opt/airflow/.venv/bin/python3',
    #     python_callable=save,
    # )
    # save_task.doc_md = dedent(
    #     """\
    # #### Save task
    # Saves our prediction into a .csv file
    # """
    # )

    transform_task 

# [END main_flow]

# [END tutorial]