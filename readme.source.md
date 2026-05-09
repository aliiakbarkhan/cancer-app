```aura width=800 height=200
<div style={{
  width: '100%',
  height: '100%',
  background: '#0a0a0a',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'flex-start',
  padding: '0 48px',
  fontFamily: 'Inter, sans-serif',
  position: 'relative',
}}>
  <div style={{
    position: 'absolute',
    top: 0,
    right: 0,
    width: '320px',
    height: '100%',
    background: 'linear-gradient(135deg, #1a0000 0%, #0a0a0a 60%)',
    opacity: 0.8,
  }} />
  <div style={{
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    marginBottom: '10px',
    zIndex: 1,
  }}>
    <div style={{
      width: '10px',
      height: '10px',
      borderRadius: '50%',
      background: '#ef4444',
      boxShadow: '0 0 12px #ef4444',
    }} />
    <span style={{
      fontSize: '12px',
      color: '#ef4444',
      letterSpacing: '3px',
      textTransform: 'uppercase',
      fontWeight: 600,
    }}>Medical AI Research</span>
  </div>
  <h1 style={{
    fontSize: '52px',
    fontWeight: 800,
    color: '#ffffff',
    margin: 0,
    letterSpacing: '-1px',
    zIndex: 1,
    lineHeight: 1,
  }}>CancerScan <span style={{ color: '#ef4444' }}>AI</span></h1>
  <p style={{
    fontSize: '15px',
    color: '#888',
    margin: '10px 0 0',
    zIndex: 1,
    maxWidth: '480px',
    lineHeight: 1.5,
  }}>Breast cancer prediction with Random Forest + SHAP explainability — deployed as a full-stack web app</p>
</div>
```

**[Live Demo](https://cancer-app-p6wz.onrender.com/app)** · **[Kaggle Notebook](https://www.kaggle.com/aliiakbarkhan)** · **[Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)**

---

## What it does

Takes 5 tumor measurements as input and predicts whether a tumor is benign or malignant — then explains *why* using SHAP feature attribution, so the prediction is never just a black box.

---

## Results

```aura width=800 height=140
<div style={{
  width: '100%',
  height: '100%',
  background: '#0f0f0f',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-around',
  padding: '0 32px',
  fontFamily: 'Inter, sans-serif',
}}>
  {[
    { label: 'Accuracy', value: '97.2%', accent: '#ef4444' },
    { label: 'Precision', value: '96%', accent: '#f97316' },
    { label: 'Recall', value: '97%', accent: '#eab308' },
    { label: 'F1 Score', value: '97%', accent: '#22c55e' },
    { label: 'False Negatives', value: '3 / 114', accent: '#3b82f6' },
  ].map(m => (
    <div key={m.label} style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '6px',
    }}>
      <span style={{
        fontSize: '34px',
        fontWeight: 800,
        color: m.accent,
        letterSpacing: '-1px',
        lineHeight: 1,
      }}>{m.value}</span>
      <span style={{
        fontSize: '11px',
        color: '#666',
        letterSpacing: '1.5px',
        textTransform: 'uppercase',
        fontWeight: 600,
      }}>{m.label}</span>
    </div>
  ))}
</div>
```

Evaluated using **5-fold stratified cross-validation**, not a single train/test split.

---

## Stack

```aura width=800 height=120
<div style={{
  width: '100%',
  height: '100%',
  background: '#0f0f0f',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-around',
  padding: '0 40px',
  fontFamily: 'Inter, sans-serif',
}}>
  {[
    { layer: 'Model', tech: 'scikit-learn Random Forest', icon: '🌲' },
    { layer: 'Explainability', tech: 'SHAP TreeExplainer', icon: '📊' },
    { layer: 'Backend', tech: 'FastAPI + Uvicorn', icon: '⚡' },
    { layer: 'Frontend', tech: 'HTML / CSS / JS', icon: '🌐' },
    { layer: 'Hosting', tech: 'Render', icon: '☁️' },
  ].map(s => (
    <div key={s.layer} style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '6px',
    }}>
      <span style={{ fontSize: '26px' }}>{s.icon}</span>
      <span style={{ fontSize: '11px', color: '#666', letterSpacing: '1.5px', textTransform: 'uppercase', fontWeight: 600 }}>{s.layer}</span>
      <span style={{ fontSize: '12px', color: '#ccc', fontWeight: 500, textAlign: 'center', maxWidth: '110px', lineHeight: 1.3 }}>{s.tech}</span>
    </div>
  ))}
</div>
```

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

```aura width=800 height=200
<div style={{
  width: '100%',
  height: '100%',
  background: '#0f0f0f',
  display: 'flex',
  alignItems: 'stretch',
  fontFamily: 'Inter, sans-serif',
  gap: '1px',
}}>
  {[
    {
      step: '01',
      title: 'Data Cleaning',
      desc: 'Removed id column. Label-encoded diagnosis: B→0, M→1.',
      color: '#ef4444',
    },
    {
      step: '02',
      title: 'Class Balance',
      desc: 'class_weight="balanced" to avoid bias toward majority benign class.',
      color: '#f97316',
    },
    {
      step: '03',
      title: 'Feature Selection',
      desc: 'Ranked all 30 features by importance. Kept top 15, removing redundant correlated columns.',
      color: '#eab308',
    },
    {
      step: '04',
      title: 'Evaluation',
      desc: '5-fold stratified CV. Confusion matrix focused on minimizing false negatives.',
      color: '#22c55e',
    },
    {
      step: '05',
      title: 'Explainability',
      desc: 'SHAP TreeExplainer generates per-prediction feature attribution for every result.',
      color: '#3b82f6',
    },
  ].map(s => (
    <div key={s.step} style={{
      flex: 1,
      background: '#141414',
      display: 'flex',
      flexDirection: 'column',
      padding: '24px 20px',
      borderTop: `3px solid ${s.color}`,
      gap: '8px',
    }}>
      <span style={{ fontSize: '11px', color: s.color, fontWeight: 700, letterSpacing: '2px' }}>{s.step}</span>
      <span style={{ fontSize: '13px', color: '#fff', fontWeight: 700, lineHeight: 1.2 }}>{s.title}</span>
      <span style={{ fontSize: '11px', color: '#777', lineHeight: 1.5 }}>{s.desc}</span>
    </div>
  ))}
</div>
```

---

## API

**`GET /features`** — returns min, max, and mean values for the top 5 features (used to populate slider ranges in the frontend).

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

```aura width=800 height=200
<div style={{
  width: '100%',
  height: '100%',
  background: '#0f0f0f',
  fontFamily: 'Inter, sans-serif',
  display: 'flex',
  flexDirection: 'column',
  padding: '24px 32px',
  gap: '0px',
}}>
  <div style={{ display: 'flex', borderBottom: '1px solid #222', paddingBottom: '8px', marginBottom: '4px' }}>
    <span style={{ flex: 2, fontSize: '11px', color: '#555', letterSpacing: '1.5px', textTransform: 'uppercase', fontWeight: 600 }}>Feature</span>
    <span style={{ flex: 1, fontSize: '11px', color: '#22c55e', letterSpacing: '1.5px', textTransform: 'uppercase', fontWeight: 600, textAlign: 'right' }}>Benign</span>
    <span style={{ flex: 1, fontSize: '11px', color: '#ef4444', letterSpacing: '1.5px', textTransform: 'uppercase', fontWeight: 600, textAlign: 'right' }}>Malignant</span>
  </div>
  {[
    { feature: 'Concave points worst', benign: '0.053', malignant: '0.261' },
    { feature: 'Perimeter worst', benign: '78.3', malignant: '197.4' },
    { feature: 'Concave points mean', benign: '0.020', malignant: '0.147' },
    { feature: 'Radius worst', benign: '12.1', malignant: '29.8' },
    { feature: 'Area worst', benign: '422.0', malignant: '2501.0' },
  ].map((row, i) => (
    <div key={row.feature} style={{
      display: 'flex',
      padding: '10px 0',
      borderBottom: '1px solid #1a1a1a',
      alignItems: 'center',
    }}>
      <span style={{ flex: 2, fontSize: '13px', color: '#bbb' }}>{row.feature}</span>
      <span style={{ flex: 1, fontSize: '14px', color: '#22c55e', fontWeight: 700, textAlign: 'right', fontVariantNumeric: 'tabular-nums' }}>{row.benign}</span>
      <span style={{ flex: 1, fontSize: '14px', color: '#ef4444', fontWeight: 700, textAlign: 'right', fontVariantNumeric: 'tabular-nums' }}>{row.malignant}</span>
    </div>
  ))}
</div>
```

---

## Disclaimer

This tool is for **research and educational purposes only**. It is not a substitute for professional medical diagnosis.

---

```aura width=800 height=80 link="https://github.com/aliiakbarkhan"
<div style={{
  width: '100%',
  height: '100%',
  background: '#0a0a0a',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
  padding: '0 48px',
  fontFamily: 'Inter, sans-serif',
}}>
  <span style={{ fontSize: '16px', fontWeight: 700, color: '#fff', letterSpacing: '-0.5px' }}>Ali Akbar Khan</span>
  <div style={{ display: 'flex', gap: '24px' }}>
    {[
      { label: 'Kaggle', url: 'kaggle.com/aliiakbarkhan' },
      { label: 'GitHub', url: 'github.com/aliiakbarkhan' },
    ].map(l => (
      <span key={l.label} style={{ fontSize: '13px', color: '#555', fontWeight: 500 }}>
        <span style={{ color: '#ef4444', marginRight: '6px' }}>→</span>{l.label}
      </span>
    ))}
  </div>
</div>
```