import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

def train_text_classifier(df):
    """Train a text classification model to categorize expenses."""
    # Prepare the data
    X = df['Description']  # Features (text descriptions)
    y = df['Category']  # Target (categories)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Vectorize the text data using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    # Train a Logistic Regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_tfidf, y_train)

    # Predictions and evaluation
    y_pred = model.predict(X_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.2f}")
    print("Classification Report:\n", report)
    
    return model, vectorizer

if __name__ == "__main__":
    # Load and preprocess data
    df = pd.read_csv(r"C:\Users\Acer\Documents\Projects\Expense Tracker\data\processed_data.csv")
    model, vectorizer = train_text_classifier(df)
    
    # Ensure the 'model' directory exists
    model_dir = r'C:\Users\Acer\Documents\Projects\Expense Tracker\model'
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    
    # Save the model and vectorizer
    joblib.dump(model, os.path.join(model_dir, 'expense_classifier.pkl'))
    joblib.dump(vectorizer, os.path.join(model_dir, 'tfidf_vectorizer.pkl'))
