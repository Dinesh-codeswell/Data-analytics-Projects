# src/clustering.py
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def perform_clustering(df):
    """Cluster transactions based on amount and category."""
    # Prepare data: Using 'Amount' and category (encoded as integers)
    df['Category_encoded'] = pd.factorize(df['Category'])[0]
    X = df[['Amount', 'Category_encoded']]  # Features (amount, encoded category)
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)
    
    # Visualize the clusters
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Amount'], df['Category_encoded'], c=df['Cluster'], cmap='viridis', marker='o')
    plt.title('Clustering Spending Patterns')
    plt.xlabel('Amount')
    plt.ylabel('Category')
    plt.colorbar(label='Cluster')
    plt.show()
    
    return df, kmeans

if __name__ == "__main__":
    # Load and preprocess data
    df = pd.read_csv(r"C:\Users\Acer\Documents\Projects\Expense Tracker\data\processed_data.csv")
    df, kmeans = perform_clustering(df)
    
    # Save the clustering model
    import joblib
    joblib.dump(kmeans, r'C:\Users\Acer\Documents\Projects\Expense Tracker\model\spending_cluster_model.pkl')
