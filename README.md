# Stellar Analytics – Exoplanet Detection

This project builds an end-to-end machine learning pipeline for exoplanet discovery using the Kepler Objects of Interest (KOI) dataset.

## Tasks

1. Classification
Predict whether a signal corresponds to a confirmed exoplanet or a false positive.

Target column:
koi_disposition

Evaluation metrics:
F1 Score
ROC-AUC

2. Regression
Predict planetary radius in Earth radii.

Target column:
koi_prad

Evaluation metrics:
MAE
RMSE

## Pipeline

1. Data preprocessing
- Removed candidate labels
- Missing value imputation

2. Feature Engineering
- Transit parameters
- Stellar characteristics

3. Models
RandomForestClassifier
RandomForestRegressor

## Results

Classification
F1 Score: 0.89
ROC-AUC: 0.98

Regression
MAE: ~0.5
RMSE: ~1.0

## Running the App

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py
