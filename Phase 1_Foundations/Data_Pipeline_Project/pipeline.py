import pandas as pd
import os

def run_pipeline():
    print("🚀 Starting Data Pipeline...")
    
    # 1. Load Data
    raw_data_path = 'raw_customers.csv'
    if not os.path.exists(raw_data_path):
        print(f"❌ Error: {raw_data_path} not found.")
        return

    df = pd.read_csv(raw_data_path)
    print(f"📊 Loaded {len(df)} records.")

    # 2. Clean Data
    print("🧹 Cleaning data...")
    
    # Fill missing ages with the median age
    median_age = df['age'].median()
    df['age'] = df['age'].fillna(median_age)
    
    # Fill missing purchase amounts with 0
    df['purchase_amount'] = df['purchase_amount'].fillna(0)
    
    # Convert signup_date to datetime objects
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    
    # Add a 'total_points' column based on purchase amount (1 point per dollar)
    df['total_points'] = (df['purchase_amount'] * 1).astype(int)

    # 3. Save Cleaned Data
    cleaned_data_path = 'cleaned_customers.json'
    df.to_json(cleaned_data_path, orient='records', indent=4)
    print(f"✅ Cleaned data saved to {cleaned_data_path}")
    
    return df

if __name__ == "__main__":
    run_pipeline()
