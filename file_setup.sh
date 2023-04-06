#!/usr/bin/env bash
pip install -r requirements.txt
mkdir dags/models
mkdir dags/outputs
mv model.pkl dags/models/