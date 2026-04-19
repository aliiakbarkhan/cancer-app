from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import shap
import numpy as np
import pandas as pd
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")
X_train = joblib.load("X_train.pkl")

with open("feature_names.json") as f:
    features = json.load(f)

all_features = features["all_features"]
top5 = features["top5"]
train_means = pd.DataFrame(X_train)[all_features].mean().to_dict()
explainer = shap.TreeExplainer(model, X_train)

class PredictRequest(BaseModel):
    inputs: dict

@app.get("/")
def root():
    return {"status": "CancerScan AI is running"}

@app.get("/features")
def get_features():
    mins = pd.DataFrame(X_train)[top5].min().to_dict()
    maxs = pd.DataFrame(X_train)[top5].max().to_dict()
    means = pd.DataFrame(X_train)[top5].mean().to_dict()
    return {"top5": top5, "mins": mins, "maxs": maxs, "means": means}

@app.post("/predict")
def predict(req: PredictRequest):
    row = train_means.copy()
    row.update(req.inputs)
    input_df = pd.DataFrame([row])[all_features]

    prediction = int(model.predict(input_df)[0])
    probability = model.predict_proba(input_df)[0].tolist()
    confidence = round(probability[prediction] * 100, 1)

    shap_values = explainer.shap_values(input_df)
    ev = explainer.expected_value
    base_val = float(ev[1]) if hasattr(ev, '__len__') else float(ev)

    if isinstance(shap_values, list):
        sv = shap_values[1][0].tolist()
    else:
        sv = input_df.shape[1] and shap_values[0, :, 1].tolist()

    shap_data = [
        {"name": all_features[i], "value": round(sv[i], 4)}
        for i in range(len(all_features))
    ]
    shap_data.sort(key=lambda x: abs(x["value"]), reverse=True)

    return {
        "prediction": prediction,
        "label": "Malignant" if prediction == 1 else "Benign",
        "confidence": confidence,
        "shap_values": shap_data,
        "shap_base": base_val,
    }