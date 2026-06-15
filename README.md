# 🌿 EcoPredict AI — Vehicle CO₂ Emissions Prediction

🏆 XGBoost achieved an **R² score of 0.9962** and an **RMSE of 3.81 g/km** on the test set.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20App-green)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

Predict vehicle CO₂ emissions (g/km) using Machine Learning models trained on a large-scale dataset built from multiple international automotive and environmental data sources.

---

## 🎯 Overview

EcoPredict AI is an end-to-end Data Science project that estimates vehicle CO₂ emissions based on technical and environmental characteristics.

The project covers the complete Machine Learning workflow:

- Multi-source data collection and integration
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model training and evaluation
- Interactive Flask web application deployment

The final dataset was constructed by consolidating and harmonizing more than **92,000 vehicle records** collected from multiple public datasets.

---

## ✨ Features

- 📊 Large-scale vehicle emissions dataset
- 🔍 Exploratory Data Analysis (EDA)
- 🏗️ Feature Engineering pipeline
- 🤖 Multiple Machine Learning models
- 📈 Model comparison dashboard
- 🌐 Interactive Flask web application
- ⚡ Real-time CO₂ prediction
- 🔄 Ensemble prediction based on multiple models

---

## 🏗️ Project Architecture

```text
Raw Datasets
      │
      ▼
Data Integration & Harmonization
      │
      ▼
EDA & Feature Engineering
      │
      ▼
Final Dataset Construction
      │
      ▼
┌──────────────────────────────┐
│      Machine Learning        │
│                              │
│   • Random Forest            │
│   • XGBoost                  │
│   • MLP Neural Network       │
└──────────────────────────────┘
      │
      ▼
Model Evaluation Dashboard
      │
      ▼
Flask Web Application
      │
      ▼
CO₂ Emissions Prediction
```

---

## 📊 Dataset

The dataset was built by combining multiple sources:

- Kaggle Vehicle Emissions Datasets
- ADEME (France)
- Government of Canada Open Data
- EPA (United States)
- Additional automotive data collected from public sources

After preprocessing and harmonization, the final dataset contains:

- **92,000+ vehicle records**
- Technical vehicle specifications
- Fuel consumption information
- Vehicle category information
- CO₂ emissions measurements

---

## 🤖 Models Trained

The following regression models were trained and evaluated:

- Decision Tree
- Random Forest
- XGBoost
- Multi-Layer Perceptron (MLP)

---

## 📈 Model Performance

### Test Set Results

| Model | RMSE | MAE | R² |
|---------|---------|---------|---------|
| XGBoost | **3.81** | **1.65** | **0.9962** |
| Random Forest | 7.74 | 4.63 | 0.9842 |
| MLP Neural Network | 7.51 | 3.92 | 0.9852 |
| Decision Tree | 12.25 | 6.92 | 0.9605 |

🏆 **Best Model: XGBoost**

- RMSE: **3.81 g/km**
- MAE: **1.65 g/km**
- R²: **0.9962**

### Dashboard Visualization

The project includes an interactive dashboard for comparing model performance across multiple evaluation metrics.

<p align="center">
  <img src="images/dashboard_comparison.png" width="900">
</p>

---

## 🌐 Web Application

The application allows users to estimate vehicle CO₂ emissions through a simple and intuitive interface.

### ⚠️ Smart Business Logic

#### Electric Vehicles

When **Electric** is selected:

- Urban Consumption = 0
- Highway Consumption = 0

#### Hybrid Vehicles

When **Hybrid = Yes**:

- Consumption fields are automatically adjusted.

This ensures coherent inputs and more reliable predictions.

---

## 📂 Project Structure

```text
EcoPredict-AI/
│
├── dashboard/                 # Model comparison dashboard
│
├── models/                    # Trained models (.pkl)
│   ├── xgboost.pkl
│   ├── random_forest.pkl
│   └── mlp.pkl
│
├── static/                    # CSS, images, assets
│
├── templates/                 # HTML templates
│
├── dataset_final.csv          # Final processed dataset
│
├── Entrainement_modeles.ipynb # EDA, feature engineering & training
│
├── app.py                     # Flask application
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/OumaymaIddouche/EcoPredict-AI.git

cd EcoPredict-AI

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🛠️ Tech Stack

**Data Science:** Pandas, NumPy, Scikit-Learn, XGBoost

**Visualization:** Matplotlib, Seaborn, Plotly Dash

**Backend:** Flask, Pickle

**Frontend:** HTML, CSS, JavaScript

---

## 👩‍💻 Author

**Oumayma Iddouche**  
Data Science & AI Engineering Student — ENSIASD

[GitHub](https://github.com/OumaymaIddouche) • [LinkedIn](https://linkedin.com)

---

## 📄 License

This project is licensed under the MIT License.
