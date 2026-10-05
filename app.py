from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import InsuranceData
from model.predict import model, MODEL_VERSION, predict_insurance_category
from schema.prediction_response import PredictionResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}

@app.get("/health")
def health_check():
    return {"status": "healthy",
             "model_version": MODEL_VERSION,
             "model_loaded": True if model else False}

@app.post("/predict", response_model=PredictionResponse)
def predict_insurance(data: InsuranceData):

    user_input = {  
        "age": data.age,
        "weight": data.weight,
        "height": data.height,
        "income_lpa": data.income_lpa,
        "smoker": int(data.smoker),
        "city_tier": data.city_tier,
        "occupation": data.occupation,
        "bmi": data.bmi,
        "lifestyle_risk": data.lifestyle_risk,
        "age_group": data.age_group
    }

    try:
        prediction = predict_insurance_category(user_input)
        return JSONResponse(status_code=200, content={"response": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    