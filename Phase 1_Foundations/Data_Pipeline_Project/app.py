from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI(title="Customer Data API")

CLEANED_DATA_PATH = 'cleaned_customers.json'

def load_data():
    if not os.path.exists(CLEANED_DATA_PATH):
        return None
    return pd.read_json(CLEANED_DATA_PATH)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Customer Data API. Use /customers to see data."}

@app.get("/customers")
def get_customers():
    df = load_data()
    if df is None:
        raise HTTPException(status_code=404, detail="Data not found. Please run the pipeline first.")
    return df.to_dict(orient='records')

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    df = load_data()
    if df is None:
        raise HTTPException(status_code=404, detail="Data not found.")
    
    customer = df[df['id'] == customer_id]
    if customer.empty:
        raise HTTPException(status_code=404, detail="Customer not found.")
    
    return customer.iloc[0].to_dict()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
