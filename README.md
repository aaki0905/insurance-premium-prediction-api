# Insurance Premium Prediction API

A machine learning project that predicts an insurance premium category based on user information.

The trained ML model is exposed through a REST API built using **FastAPI**.

## Features

- Machine learning-based insurance premium prediction
- FastAPI REST API
- Input validation using Pydantic
- Health-check endpoint
- Model version tracking
- Clean project structure with separate model, schema, and configuration modules

## Tech Stack

- Python
- FastAPI
- Pydantic
- Pandas
- Scikit-learn
- Pickle
- Uvicorn

## Project Structure

```text
insurance-premium-prediction-api/
│
├── config/
│
├── model/
│   ├── model.pkl
│   └── predict.py
│
├── schema/
│   └── user_input.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
