
FROM apache/airflow:2.5.3
ENV PIP_USER=false
RUN python3 -m venv .venv
COPY  requirements.txt .
RUN /opt/airflow/.venv/bin/pip install -r requirements.txt
ENV PIP_USER=true

