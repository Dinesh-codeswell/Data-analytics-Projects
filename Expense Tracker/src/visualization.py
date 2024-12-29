# src/visualization.py
import pandas as pd
import plotly.express as px

def visualize_data(df):
    """Generate interactive plots for spending trends."""
    # Plot total spending by category
    spending_by_category = df.groupby('Category')['Amount'].sum().reset_index()
    fig = px.bar(spending_by_category, x='Category', y='Amount', title="Total Spending by Category")
    fig.show()

    # Spending trends over time (daily)
    df['Date'] = pd.to_datetime(df['Date'])
    daily_spending = df.groupby(df['Date'].dt.date)['Amount'].sum().reset_index()
    fig = px.line(daily_spending, x='Date', y='Amount', title="Daily Spending Trend")
    fig.show()

if __name__ == "__main__":
    # Load and preprocess data
    df = pd.read_csv(r"C:\Users\Acer\Desktop\Expense Tracker\data\processed_data.csv")
    visualize_data(df)
