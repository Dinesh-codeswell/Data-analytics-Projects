import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Load pre-trained models
classifier_model = joblib.load(r'C:\Users\Acer\Documents\Projects\Expense Tracker\model\expense_classifier.pkl')
vectorizer = joblib.load(r'C:\Users\Acer\Documents\Projects\Expense Tracker\model\tfidf_vectorizer.pkl')

# Set custom page style
def set_page_style():
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(135deg, #6D3F91, #12C2E9);
        }
        .sidebar .sidebar-content {
            background-color: #0a043c;
            color: #ffffff;
        }
        h1 {
            color: #ffffff;
            font-family: 'Roboto', sans-serif;
            font-size: 48px;
            text-align: center;
            margin-bottom: 20px;
        }
        h2, h3 {
            color: #ffffff;
            font-family: 'Roboto', sans-serif;
        }
        .stButton>button {
            background-color: #3CB371;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            padding: 12px 30px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover {
            background-color: #2F8B55;
        }
        .footer {
            text-align: center;
            color: #95a5a6;
            margin-top: 30px;
            font-size: 14px;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Function to predict transaction category
def predict_category(description):
    """Predict the category of a transaction based on the description."""
    description_tfidf = vectorizer.transform([description])
    prediction = classifier_model.predict(description_tfidf)
    return prediction[0]

# Function to get a random money-saving quote
def get_random_quote():
    quotes = [
        "“Do not save what is left after spending, but spend what is left after saving.” – Warren Buffett",
        "“A penny saved is a penny earned.” – Benjamin Franklin",
        "“Beware of little expenses. A small leak will sink a great ship.” – Benjamin Franklin",
        "“The art is not in making money, but in keeping it.” – Proverb",
        "“An investment in knowledge pays the best interest.” – Benjamin Franklin",
        "“Saving is a great habit, but without investing it is just like saving for nothing.” – Anonymous"
    ]
    return random.choice(quotes)

# Function to display an inspirational image
def display_image():
    images = [
        "https://via.placeholder.com/800x400.png?text=Save+Money+Smartly",
        "https://via.placeholder.com/800x400.png?text=Track+Your+Spending+Wisely",
        "https://via.placeholder.com/800x400.png?text=Invest+in+Your+Future"
    ]
    selected_image = random.choice(images)
    st.image(selected_image, use_container_width=True)

# Main app function
def main():
    set_page_style()

    # Header
    st.title("💰 Expense Tracker with ML")
    st.markdown("### Analyze your spending patterns, predict categories, and gain insights into your financial habits.")

    # Display Random Quote and Image
    st.markdown("#### 💡 **Motivational Quote:**")
    st.info(get_random_quote())
    display_image()

    # Sidebar
    st.sidebar.header("🔍 Predict Transaction Category")
    st.sidebar.markdown("Use the AI-powered feature to categorize your transactions.")
    description_input = st.sidebar.text_area("Enter Transaction Description:", help="Provide a description of your expense.")
    if st.sidebar.button("Predict Category"):
        if description_input:
            category = predict_category(description_input)
            st.sidebar.success(f"**Predicted Category**: {category}")
        else:
            st.sidebar.warning("Please enter a transaction description.")

    # File upload and visualization section
    st.header("📊 Expense Data Visualization")
    st.markdown("Upload your expense data to uncover your spending trends and insights.")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("**Data Preview:**", df.head())

        # Spending by category - Animated Bar Chart
        st.subheader("💸 Total Spending by Category")
        spending_by_category = df.groupby('Category')['Amount'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x='Amount', y='Category', data=spending_by_category, palette="coolwarm", ax=ax)
        ax.set_title("Total Spending by Category", fontsize=16)
        st.pyplot(fig)

        # Daily spending trend - Line Chart
        st.subheader("📅 Daily Spending Trend")
        df['Date'] = pd.to_datetime(df['Date'])
        daily_spending = df.groupby(df['Date'].dt.date)['Amount'].sum().reset_index()
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.plot(daily_spending['Date'], daily_spending['Amount'], marker='o', color='#00C8D4')
        ax2.set_title("Daily Spending Trend", fontsize=16)
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Total Spending")
        ax2.set_xticklabels(daily_spending['Date'], rotation=45)
        st.pyplot(fig2)

    # Footer
    st.markdown("---")
    st.markdown("### 💡 Tips for Financial Success:")
    st.markdown("1. Track spending habits regularly.")
    st.markdown("2. Set a monthly budget for categories.")
    st.markdown("3. Always categorize expenses to get better insights.")
    st.markdown("4. Set reminders to avoid unnecessary purchases.")
    st.markdown("<div class='footer'>Powered by Streamlit | Designed with ❤️ by AI</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
