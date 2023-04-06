# POC_ML_DAG

## Usage

### File setup

```
chmod +x file_setup.sh
./file_setup.sh 
```

### Docker container build

```
docker-compose up airflow-init
docker-compose up
```

### Usage
1. Go to `http://localhost:8080/`
2. Username/password: airflow
3. Find a DAG called ML_inference_DAG
4. Launch it. Result will be placed in `dags/outputs/prediction.csv`