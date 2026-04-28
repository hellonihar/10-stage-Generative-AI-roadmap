# 🔍 Unsupervised Learning Demo

Welcome to the **Unsupervised Learning** demonstration module! Unlike supervised learning, unsupervised learning involves working with data that has **no labels**. The goal is to discover hidden patterns or structures within the data.

---

## 🚀 Demos Included

### 1. 📂 K-Means Clustering (`clustering_demo.py`)
This script demonstrates **Clustering**. It groups the Iris dataset into clusters based on physical similarities without knowing the actual species.
*   **Algorithm**: K-Means
*   **Goal**: Find natural groupings (clusters) in the data.
*   **Visualization**: Shows how data points are grouped and identifies the 'centroids' of each cluster.

### 2. 📉 PCA Dimensionality Reduction (`pca_demo.py`)
This script demonstrates **Dimensionality Reduction**. It reduces the 4-dimensional Iris dataset into 2 dimensions for easier visualization while preserving as much variance (information) as possible.
*   **Algorithm**: Principal Component Analysis (PCA)
*   **Goal**: Simplify data and identify the most important features.
*   **Visualization**: Shows the data projected onto the first two principal components.

---

## 🛠️ Setup and Installation

**1. Navigate to this directory:**
```bash
cd "Phase 1_Foundations/ML_Basics/Unsupervised_learning_demo"
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🏃 How to Run

### Run the Clustering Demo:
```bash
python clustering_demo.py
```

### Run the PCA Demo:
```bash
python pca_demo.py
```

---

## 🧠 Core Concepts

*   **No Labels**: The model learns from the structure of the data itself, not from pre-defined answers.
*   **Clustering**: Grouping similar data points together.
*   **Dimensionality Reduction**: Compressing data while keeping its essence. Useful for visualization and speeding up other ML algorithms.
*   **Pattern Discovery**: Finding hidden relationships in datasets.

---

## 📊 Requirements
*   `scikit-learn`: For ML models (KMeans, PCA).
*   `numpy`: For numerical operations.
*   `matplotlib`: For data visualization.
