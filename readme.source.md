```aura width=800 height=280
<div style={{
  width: '100%',
  height: '100%',
  background: '#050508',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  padding: '0 56px',
  fontFamily: 'Inter, sans-serif',
  position: 'relative',
  overflow: 'hidden',
}}>
  <style>{`
    @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.4;transform:scale(1.6)} }
    @keyframes scanline { 0%{transform:translateY(-100%)} 100%{transform:translateY(1000%)} }
    @keyframes fadeIn1 { 0%{opacity:0;transform:translateX(-20px)} 100%{opacity:1;transform:translateX(0)} }
    @keyframes fadeIn2 { 0%{opacity:0;transform:translateX(-20px)} 100%{opacity:1;transform:translateX(0)} }
    @keyframes fadeIn3 { 0%{opacity:0;transform:translateX(-20px)} 100%{opacity:1;transform:translateX(0)} }
    @keyframes fadeIn4 { 0%{opacity:0;transform:translateX(-20px)} 100%{opacity:1;transform:translateX(0)} }
    @keyframes orbFloat { 0%,100%{transform:translate(0,0)} 33%{transform:translate(12px,-18px)} 66%{transform:translate(-8px,10px)} }
  `}</style>

  <div id="orb1" style={{
    position:'absolute', right:'60px', top:'20px',
    width:'240px', height:'240px', borderRadius:'50%',
    background:'radial-gradient(circle at 40% 40%, #ff2d2d33, transparent 70%)',
    animation:'orbFloat 7s ease-in-out infinite',
  }} />
  <div id="orb2" style={{
    position:'absolute', right:'180px', bottom:'10px',
    width:'130px', height:'130px', borderRadius:'50%',
    background:'radial-gradient(circle, #ff6b6b18, transparent 70%)',
    animation:'orbFloat 9s ease-in-out infinite reverse',
  }} />
  <div id="scan" style={{
    position:'absolute', left:0, right:0, top:0, height:'2px',
    background:'linear-gradient(90deg, transparent, #ff2d2d22, transparent)',
    animation:'scanline 5s linear infinite',
  }} />

  <div id="badge" style={{
    display:'flex', alignItems:'center', gap:'8px', marginBottom:'16px',
    animation:'fadeIn1 0.7s ease both',
  }}>
    <div id="dot" style={{
      width:'8px', height:'8px', borderRadius:'50%', background:'#ff2d2d',
      animation:'pulse 2s ease-in-out infinite',
    }} />
    <span style={{fontSize:'11px',color:'#ff2d2d',letterSpacing:'4px',textTransform:'uppercase',fontWeight:'700'}}>
      Medical AI · Breast Cancer Detection
    </span>
  </div>

  <div id="title" style={{animation:'fadeIn2 0.7s 0.15s ease both', opacity:0}}>
    <span style={{fontSize:'64px',fontWeight:'800',color:'#ffffff',letterSpacing:'-2px',lineHeight:'1',display:'block'}}>
      CancerScan <span style={{color:'#ff2d2d'}}>AI</span>
    </span>
  </div>

  <div id="sub" style={{marginTop:'14px', animation:'fadeIn3 0.7s 0.3s ease both', opacity:0}}>
    <span style={{fontSize:'14px',color:'#555',lineHeight:'1.6',display:'block'}}>
      Random Forest · SHAP Explainability · FastAPI · Deployed on Render
    </span>
  </div>

  <div style={{marginTop:'24px', display:'flex', gap:'10px', animation:'fadeIn4 0.7s 0.45s ease both', opacity:0}}>
    {['97.2% Accuracy','5-Fold CV','SHAP Explained'].map(tag => (
      <div key={tag} style={{
        padding:'5px 14px', border:'1px solid #1d1d22', borderRadius:'999px',
        fontSize:'11px', color:'#555', background:'#0b0b0f', fontWeight:'600', letterSpacing:'0.5px',
      }}>{tag}</div>
    ))}
  </div>
</div>
```

<p align="center">
  <a href="https://cancer-app-p6wz.onrender.com/app"><img src="https://img.shields.io/badge/Live%20Demo-FF2D2D?style=for-the-badge&logo=render&logoColor=white" /></a>&nbsp;
  <a href="https://www.kaggle.com/aliiakbarkhan"><img src="https://img.shields.io/badge/Kaggle%20Notebook-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" /></a>&nbsp;
  <a href="https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset"><img src="https://img.shields.io/badge/Dataset-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" /></a>
</p>

---

## What it does

Takes **5 tumor measurements** as input → predicts **Benign or Malignant** → explains *why* using SHAP feature attribution. The prediction is never a black box.

---

## Results

```aura width=800 height=160
<div style={{
  width:'100%', height:'100%',
  background:'#080809',
  display:'flex', alignItems:'center', justifyContent:'space-around',
  padding:'0 40px',
  fontFamily:'Inter, sans-serif',
  position:'relative', overflow:'hidden',
}}>
  <style>{`
    @keyframes countUp { 0%{opacity:0;transform:translateY(14px)} 100%{opacity:1;transform:translateY(0)} }
    @keyframes lineGrow { 0%{transform:scaleX(0);opacity:0} 100%{transform:scaleX(1);opacity:1} }
  `}</style>
  <div style={{position:'absolute',bottom:0,left:0,right:0,height:'1px',background:'linear-gradient(90deg,transparent,#ff2d2d22,transparent)'}} />
  {[
    {label:'Accuracy', value:'97.2%', color:'#ff2d2d', delay:'0s'},
    {label:'Precision', value:'96%', color:'#ff6b35', delay:'0.1s'},
    {label:'Recall', value:'97%', color:'#ffd60a', delay:'0.2s'},
    {label:'F1 Score', value:'97%', color:'#06d6a0', delay:'0.3s'},
    {label:'False Neg.', value:'3/114', color:'#4cc9f0', delay:'0.4s'},
  ].map(m => (
    <div key={m.label} style={{
      display:'flex', flexDirection:'column', alignItems:'center', gap:'8px',
      animation:`countUp 0.6s ${m.delay} ease both`, opacity:0,
    }}>
      <div id={`bar-${m.label}`} style={{
        width:'36px', height:'3px', borderRadius:'2px',
        background:`linear-gradient(90deg, ${m.color}, ${m.color}44)`,
        transformOrigin:'left',
        animation:`lineGrow 0.6s ${m.delay} ease both`,
        transform:'scaleX(0)',
      }} />
      <span style={{fontSize:'38px',fontWeight:'800',color:m.color,letterSpacing:'-1.5px',lineHeight:'1',fontVariantNumeric:'tabular-nums'}}>
        {m.value}
      </span>
      <span style={{fontSize:'10px',color:'#333',letterSpacing:'2.5px',textTransform:'uppercase',fontWeight:'700'}}>
        {m.label}
      </span>
    </div>
  ))}
</div>
```

> Evaluated via **5-fold stratified cross-validation** — not a single train/test split.

---

## Stack

```aura width=800 height=96
<div style={{
  width:'100%', height:'100%',
  background:'#080809',
  display:'flex', alignItems:'center', justifyContent:'space-around',
  padding:'0 48px',
  fontFamily:'Inter, sans-serif',
}}>
  <style>{`
    @keyframes slideUp { 0%{opacity:0;transform:translateY(10px)} 100%{opacity:1;transform:translateY(0)} }
  `}</style>
  {[
    {layer:'Model', tech:'Random Forest', color:'#ff2d2d'},
    {layer:'Explainability', tech:'SHAP TreeExplainer', color:'#ff6b35'},
    {layer:'Backend', tech:'FastAPI + Uvicorn', color:'#ffd60a'},
    {layer:'Frontend', tech:'HTML · CSS · JS', color:'#06d6a0'},
    {layer:'Hosting', tech:'Render', color:'#4cc9f0'},
  ].map((s, i) => (
    <div key={s.layer} style={{
      display:'flex', flexDirection:'column', alignItems:'center', gap:'5px',
      animation:`slideUp 0.5s ${i*0.09}s ease both`, opacity:0,
    }}>
      <div style={{width:'24px',height:'2px',borderRadius:'1px',background:s.color}} />
      <span style={{fontSize:'10px',color:'#333',letterSpacing:'2px',textTransform:'uppercase',fontWeight:'700'}}>{s.layer}</span>
      <span style={{fontSize:'12px',color:'#bbb',fontWeight:'600',textAlign:'center'}}>{s.tech}</span>
    </div>
  ))}
</div>
```

---

## ML Pipeline

```aura width=800 height=220
<div style={{
  width:'100%', height:'100%',
  background:'#080809',
  display:'flex', alignItems:'stretch',
  fontFamily:'Inter, sans-serif',
  position:'relative', overflow:'hidden',
}}>
  <style>{`
    @keyframes stepIn { 0%{opacity:0;transform:translateY(18px)} 100%{opacity:1;transform:translateY(0)} }
    @keyframes topBarGrow { 0%{transform:scaleX(0)} 100%{transform:scaleX(1)} }
  `}</style>
  {[
    {n:'01', title:'Data\nCleaning', desc:'Removed id col. Label encoded diagnosis: B→0, M→1.', color:'#ff2d2d'},
    {n:'02', title:'Class\nBalance', desc:'class_weight="balanced" prevents majority class bias.', color:'#ff6b35'},
    {n:'03', title:'Feature\nSelect', desc:'Top 15 of 30 features ranked by RF importance.', color:'#ffd60a'},
    {n:'04', title:'Evaluation', desc:'5-fold stratified CV. Minimised false negatives.', color:'#06d6a0'},
    {n:'05', title:'SHAP\nExplain', desc:'TreeExplainer gives per-prediction attribution.', color:'#4cc9f0'},
  ].map((s, i) => (
    <div key={s.n} style={{
      flex:1,
      display:'flex', flexDirection:'column',
      padding:'28px 16px 22px',
      borderRight: i < 4 ? '1px solid #0f0f10' : 'none',
      position:'relative',
      animation:`stepIn 0.6s ${i*0.1}s ease both`, opacity:0,
    }}>
      <div id={`topbar${i}`} style={{
        position:'absolute', top:0, left:0, right:0, height:'3px',
        background:s.color, transformOrigin:'left',
        animation:`topBarGrow 0.6s ${i*0.1+0.2}s ease both`,
        transform:'scaleX(0)',
      }} />
      <span style={{fontSize:'10px',color:s.color,letterSpacing:'3px',fontWeight:'800',marginBottom:'10px'}}>{s.n}</span>
      <span style={{fontSize:'13px',color:'#fff',fontWeight:'700',lineHeight:'1.35',whiteSpace:'pre-line',marginBottom:'10px'}}>{s.title}</span>
      <span style={{fontSize:'11px',color:'#444',lineHeight:'1.6'}}>{s.desc}</span>
    </div>
  ))}
</div>
```

---

## Project structure

```
cancer-app/
├── main.py               # FastAPI backend — /predict and /features
├── index.html            # Frontend — sliders, results, SHAP bar chart
├── model.pkl             # Trained Random Forest model
├── X_train.pkl           # Training data for SHAP background
├── feature_names.json    # Top 5 + all 15 feature names
├── requirements.txt
└── notebook/
    └── breast-cancer-prediction.ipynb
```

---

## API

**`GET /features`** — returns min, max, mean for the top 5 features (populates slider ranges in the frontend).

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

## Test cases

```aura width=800 height=220
<div style={{
  width:'100%', height:'100%',
  background:'#080809',
  fontFamily:'Inter, sans-serif',
  display:'flex', flexDirection:'column',
  overflow:'hidden',
}}>
  <style>{`
    @keyframes rowIn { 0%{opacity:0;transform:translateX(-14px)} 100%{opacity:1;transform:translateX(0)} }
  `}</style>
  <div style={{display:'flex',padding:'16px 32px 12px',borderBottom:'1px solid #0f0f10'}}>
    <span style={{flex:2,fontSize:'10px',color:'#2a2a2e',letterSpacing:'2.5px',textTransform:'uppercase',fontWeight:'700'}}>Feature</span>
    <span style={{flex:1,fontSize:'10px',color:'#06d6a0',letterSpacing:'2.5px',textTransform:'uppercase',fontWeight:'700',textAlign:'right'}}>Benign</span>
    <span style={{flex:1,fontSize:'10px',color:'#ff2d2d',letterSpacing:'2.5px',textTransform:'uppercase',fontWeight:'700',textAlign:'right'}}>Malignant</span>
  </div>
  {[
    {f:'Concave points worst', b:'0.053', m:'0.261'},
    {f:'Perimeter worst', b:'78.3', m:'197.4'},
    {f:'Concave points mean', b:'0.020', m:'0.147'},
    {f:'Radius worst', b:'12.1', m:'29.8'},
    {f:'Area worst', b:'422.0', m:'2501.0'},
  ].map((row, i) => (
    <div key={row.f} style={{
      display:'flex', alignItems:'center',
      padding:'10px 32px',
      borderBottom: i < 4 ? '1px solid #0c0c0e' : 'none',
      animation:`rowIn 0.5s ${i*0.08}s ease both`, opacity:0,
    }}>
      <span style={{flex:2,fontSize:'12px',color:'#555'}}>{row.f}</span>
      <span style={{flex:1,fontSize:'14px',color:'#06d6a0',fontWeight:'700',textAlign:'right',fontVariantNumeric:'tabular-nums'}}>{row.b}</span>
      <span style={{flex:1,fontSize:'14px',color:'#ff2d2d',fontWeight:'700',textAlign:'right',fontVariantNumeric:'tabular-nums'}}>{row.m}</span>
    </div>
  ))}
</div>
```

---

## Run locally

```bash
git clone https://github.com/aliiakbarkhan/cancer-app.git
cd cancer-app
pip install -r requirements.txt
uvicorn main:app --reload
# open http://localhost:8000/app
```

---

> ⚠️ This tool is for **research and educational purposes only**. It is not a substitute for professional medical diagnosis.

---

```aura width=800 height=72 link="https://github.com/aliiakbarkhan"
<div style={{
  width:'100%', height:'100%',
  background:'#050508',
  display:'flex', alignItems:'center', justifyContent:'space-between',
  padding:'0 48px',
  fontFamily:'Inter, sans-serif',
  borderTop:'1px solid #0f0f11',
}}>
  <style>{`
    @keyframes footerFade { 0%{opacity:0} 100%{opacity:1} }
  `}</style>
  <div style={{display:'flex',alignItems:'center',gap:'10px',animation:'footerFade 1s ease both'}}>
    <div style={{width:'6px',height:'6px',borderRadius:'50%',background:'#ff2d2d'}} />
    <span style={{fontSize:'15px',fontWeight:'700',color:'#fff',letterSpacing:'-0.5px'}}>Ali Akbar Khan</span>
  </div>
  <div style={{display:'flex',gap:'28px',animation:'footerFade 1s 0.2s ease both',opacity:0}}>
    {['Kaggle','GitHub','Live Demo'].map(l => (
      <span key={l} style={{fontSize:'12px',color:'#333',fontWeight:'600',letterSpacing:'1px'}}>
        <span style={{color:'#ff2d2d',marginRight:'5px'}}>→</span>{l}
      </span>
    ))}
  </div>
</div>
```