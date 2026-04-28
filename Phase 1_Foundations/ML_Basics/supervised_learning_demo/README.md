# 🧠 Supervised Learning Demo

Welcome to the **Supervised Learning** demonstration module! This directory contains practical implementations of the two primary types of supervised learning: **Classification** and **Regression**.

Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs.

---

## 🚀 Demos Included

### 1. 🌸 Iris Species Classification (`demo.py`)
This script demonstrates **Classification**. It uses the famous Iris dataset to train a model that can predict the species of a flower based on its physical measurements.
*   **Algorithm**: K-Nearest Neighbors (KNN)
*   **Goal**: Predict one of 3 species (Setosa, Versicolor, Virginica).
*   **Key Metrics**: Accuracy Score.

### 2. 🏠 House Price Prediction (`house_price_prediction.py`)
This script demonstrates **Regression**. It generates synthetic data to model the relationship between house size (square footage) and its market price.
*   **Algorithm**: Linear Regression
*   **Goal**: Predict a continuous numerical value (Price).
*   **Key Metrics**: Mean Absolute Error (MAE) and Visual Plotting.

---

## 🛠️ Setup and Installation

Ensure you have Python installed, then follow these steps:

**1. Clone the repository (if not already done)**
**2. Navigate to this directory:**
```bash
cd "Phase 1_Foundations/ML_Basics/supervised_learning_demo"
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🏃 How to Run

### Run the Classification Demo:
```bash
python demo.py
```

### Run the Regression Demo:
```bash
python house_price_prediction.py
```

---

## 🧠 Core Machine Learning Concepts

This module covers several fundamental concepts essential for any AI engineer:

*   **Labled Data**: The "ground truth" used to train the model.
*   **Train/Test Split**: Dividing data into a **Training set** (to teach the model) and a **Test set** (to evaluate its performance on unseen data).
*   **Classification vs. Regression**: 
    *   *Classification* predicts a **category** (discrete).
    *   *Regression* predicts a **quantity** (continuous).
*   **Model Evaluation**: Using metrics like Accuracy and MAE to quantify how well the model is performing.

---

## 📊 Requirements
*   `scikit-learn`: For ML models and datasets.
*   `numpy`: For numerical operations.
*   `matplotlib`: For data visualization.