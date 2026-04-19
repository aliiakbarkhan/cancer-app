# CancerScan AI

A breast cancer prediction system built with Random Forest and SHAP explainability, deployed as a full-stack web application.

**[Live Demo](https://cancer-app-p6wz.onrender.com/app)** · **[Kaggle Notebook](https://www.kaggle.com/aliiakbarkhan)** · **[Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)**

---

## What it does

Takes 5 tumor measurements as input and predicts whether a tumor is benign or malignant — then explains *why* using SHAP feature attribution, so the prediction is never just a black box.

---

## Results

| Metric | Score |
|--------|-------|
| Accuracy | 97.2% |
| Precision | 96% |
| Recall | 97% |
| F1 | 97% |
| False negatives | 3 / 114 test cases |

Evaluated using 5-fold stratified cross-validation, not a single train/test split.

---

## Stack

| Layer | Technology |
|-------|-----------|
| Model | scikit-learn Random Forest |
| Explainability | SHAP (TreeExplainer) |
| Backend | FastAPI + Uvicorn |
| Frontend | Vanilla HTML/CSS/JS |
| Hosting | Render (backend) |

---

## Project structure

```
cancer-app/
├── main.py               # FastAPI backend — /predict and /features endpoints
├── index.html            # Frontend — sliders, results, SHAP bar chart
├── model.pkl             # Trained Random Forest model
├── X_train.pkl           # Training data for SHAP background
├── feature_names.json    # Top 5 + all 15 feature names
├── requirements.txt      # Python dependencies
└── notebook/
└── breast-cancer-prediction.ipynb

```

---

## ML approach

**Data cleaning**
- Removed the `id` column (row identifier, not a medical feature)
- Label encoded diagnosis: B → 0, M → 1

**Class imbalance**
- Used `class_weight='balanced'` in Random Forest to prevent the model from being biased toward the majority benign class

**Feature selection**
- Ranked all 30 features by Random Forest importance
- Kept top 15 to remove redundant correlated columns (mean/se/worst versions of the same measure)

**Evaluation**
- 5-fold stratified cross-validation for reliable, stable metrics
- Confusion matrix analysis with focus on minimizing false negatives (missed malignant cases)

**Explainability**
- SHAP TreeExplainer generates per-prediction feature attribution
- Every prediction shows which measurements drove the result and by how much

---

## API

**`GET /features`**
Returns min, max and mean values for the top 5 features — used to populate slider ranges in the frontend.

**`POST /predict`**
```json
{
  "inputs": {
    "concave points_worst": 0.14,
    "perimeter_worst": 120.0,
    "concave points_mean": 0.07,
    "radius_worst": 16.0,
    "area_worst": 900.0
  }
}
```
Returns:
```json
{
  "prediction": 1,
  "label": "Malignant",
  "confidence": 94.2,
  "shap_values": [...],
  "shap_base": 0.37
}
```

---

## Run locally

```bash
git clone https://github.com/aliiakbarkhan/cancer-app.git
cd cancer-app
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open `http://localhost:8000/app`

---

## Test cases

| Feature | Benign case | Malignant case |
|---------|-------------|----------------|
| Concave points worst | 0.053 | 0.261 |
| Perimeter worst | 78.3 | 197.4 |
| Concave points mean | 0.020 | 0.147 |
| Radius worst | 12.1 | 29.8 |
| Area worst | 422.0 | 2501.0 |

---

## Disclaimer

This tool is for research and educational purposes only. It is not a substitute for professional medical diagnosis.

---

**Ali Akbar Khan** · [Kaggle](https://www.kaggle.com/aliiakbarkhan) · [GitHub](https://github.com/aliiakbarkhan)
