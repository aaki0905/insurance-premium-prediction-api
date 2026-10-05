import pickle
import pandas as pd

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

## ML flow
MODEL_VERSION = "1.0.0"

## get class level prediction
class_labels = model.classes_.tolist()

def predict_insurance_category(InsuranceData : dict):
    input_df = pd.DataFrame([InsuranceData])
    prediction = model.predict(input_df)[0]

    # Get the predicted class label
    probabilities = model.predict_proba(input_df)[0]
    confidence = max(probabilities)
    class_probabilities = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))

    return {
        "predicted_category": str(prediction),
        "confidence": float(confidence),
        "class_probabilities": class_probabilities
    }