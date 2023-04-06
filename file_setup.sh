#!/usr/bin/env bash
pip install -r requirements.txt
python script.py
mkdir dags/models
mkdir dags/outputs
mv model.pkl dags/models/