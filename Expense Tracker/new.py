import pandas as pd
import random
from datetime import datetime, timedelta

# Define categories and sample data
categories = ['Stationery', 'Mobile Recharge', 'SSD Purchase', 'Laptop Repair', 'Food', 'Other']

# Generate sample transaction data
def generate_transaction_data(start_date, end_date, num_records):
    data = []
    current_date = start_date

    for _ in range(num_records):
        description = random.choice([
            'Notebook', 'Pen', 'Pencil', 'Ink', 'Mobile Recharge', 
            'SSD Purchase', 'Laptop Repair', 'Fruits', 'Outdoor Food', 'Groceries'
        ])
        amount = random.uniform(10, 500)  # Random expense amount
        category = random.choice(categories)
        current_date += timedelta(days=random.randint(0, 2))  # Random date increment
        transaction_date = current_date.strftime('%Y-%m-%d')
        
        # For laptop repair, make sure there are multiple occurrences
        if 'Laptop Repair' in description and category == 'Laptop Repair':
            amount = random.uniform(100, 400)  # Higher range for repairs

        data.append([transaction_date, description, amount, category])
        
    return data

# Set the start and end date for the records
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 2, 15)
num_records = 100  # Adjust the number of records as needed

# Generate data
transaction_data = generate_transaction_data(start_date, end_date, num_records)

# Create DataFrame
columns = ['Date', 'Description', 'Amount', 'Category']
df = pd.DataFrame(transaction_data, columns=columns)

# Save to CSV
output_path = r"C:\Users\Acer\Documents\Projects\Expense Tracker\data\transaction_history.csv"
df.to_csv(output_path, index=False)

print(f"CSV file generated at {output_path}")
