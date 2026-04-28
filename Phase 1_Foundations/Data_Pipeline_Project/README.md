# 🏗️ Mini Data Pipeline Project

This project demonstrates a full data lifecycle: from raw CSV ingestion to cleaning with Pandas and exposure via a REST API using FastAPI.

---

## 📂 Project Structure

*   `raw_customers.csv`: The initial messy dataset.
*   `pipeline.py`: A script to clean the data (handles missing values, date formatting).
*   `app.py`: A FastAPI application that serves the cleaned data.
*   `cleaned_customers.json`: The output of the pipeline (generated after running `pipeline.py`).

---

## 🚀 How to Run

**1. Navigate to this directory:**
```bash
cd "Phase 1_Foundations/Data_Pipeline_Project"
```

**2. Install Dependencies:**
```bash
pip install pandas fastapi uvicorn
```

**3. Run the Data Pipeline:**
This will process the raw CSV and create a cleaned JSON file.
```bash
python pipeline.py
```

**4. Start the API:**
```bash
python app.py
```

**5. Access the API:**
*   Main endpoint: [http://127.0.0.1:8000/customers](http://127.0.0.1:8000/customers)
*   Specific customer: [http://127.0.0.1:8000/customers/1](http://127.0.0.1:8000/customers/1)
*   API Docs (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧠 Learning Objectives

*   **Data Manipulation**: Using Pandas to handle missing data (`fillna`) and type conversion (`to_datetime`).
*   **API Development**: Creating endpoints with FastAPI and returning JSON responses.
*   **Workflow Integration**: Connecting a data processing script with a web service.
