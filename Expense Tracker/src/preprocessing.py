# src/preprocessing.py
import pandas as pd
import re

def load_data(filepath):
    """Load dataset from a CSV file."""
    try:
        # Use on_bad_lines='skip' to skip lines with too many fields
        df = pd.read_csv(filepath, on_bad_lines='skip')  
        print(f"Data loaded successfully. Rows: {len(df)}")
        return df
    except Exception as e:
        print(f"Error loading the CSV file: {e}")
        return None

def clean_description(text):
    """Clean transaction description."""
    text = text.lower()  # Convert text to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    return text

def preprocess_data(df):
    """Preprocess the dataset."""
    if df is not None:
        # Clean 'Description' column
        df['Description'] = df['Description'].apply(clean_description)  # Clean text
        
        # Handle missing values (if any)
        df = df.dropna()  # Drop rows with missing values
        
        # Ensure 'Amount' is a numeric type
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')  # Convert to numeric and handle errors
        
        # Drop rows with invalid 'Amount' (e.g., NaN after coercion)
        df = df.dropna(subset=['Amount'])
        
        # Optional: Filter out data if needed, e.g., by category or specific range of amounts
        # df = df[df['Amount'] > 0]  # Filter out negative or zero amounts

        return df
    else:
        print("Dataframe is empty, unable to preprocess.")
        return None

if __name__ == "__main__":
    # Load data from the provided path
    df = load_data(r"C:\Users\Acer\Documents\Projects\Expense Tracker\data\transaction_history.csv")
    
    if df is not None:
        # Preprocess the data
        df = preprocess_data(df)
        
        if df is not None:
            # Save the preprocessed data
            df.to_csv(r"C:\Users\Acer\Documents\Projects\Expense Tracker\data\processed_data.csv", index=False)  # Save cleaned data
            print("Data cleaned and saved successfully.")
        else:
            print("Data preprocessing failed.")
    else:
        print("Failed to load the dataset.")
