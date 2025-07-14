# 🛒 Walmart Retail Sales Data Analysis

This project demonstrates how data analytics and machine learning can be used to analyze and predict sales performance in a retail environment using Walmart data. It includes a trained model, an interactive Streamlit dashboard, and a Power BI report and time series forecasting notebook.

---

## 📌 Project Overview

This project includes:
- 🔍 **Exploratory Data Analysis** on Walmart retail sales
- 💡 **Sales prediction model** using Random Forest
- 📈 **Top-selling product analysis**
- 🚚 **Shipping delay insights**
- 🖥️ **Interactive dashboard** built using Streamlit
- 📊 **Power BI dashboard** 
- 📆 **SARIMA forecasting notebook** 

---

## 📂 Project Structure

Walmart-Retail-Sales-Data-Analysis/

1. streamlitapp.py # Streamlit web app
2. model_training.py # Python script to train ML model
3. sales_prediction_model.pkl # Trained model file
4.  walmart Retail Data.xlsx # Sales dataset
5. Power BI dashboard.pbix # Power BI file
6. Sarima_Forecast.ipynb #  SARIMA notebook
7. README.md # Project documentation



---

## 🚀 How to Run the App Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Walmart-Retail-Sales-Data-Analysis.git
   cd Walmart-Retail-Sales-Data-Analysis

    
Run the Streamlit app
   
-  streamlit run streamlitapp.py
   
🧠 Model Description

Algorithm: Random Forest Regressor

- Features used:
- Product Category (encoded)
- Discount
- Shipping Delay
- Previous Sales Value
- Target: Future Sales Value

Model is trained using model_training.py and saved as sales_prediction_model.pkl.


📊 Dashboard Features (Streamlit)

- Predict Sales  

- Top-Selling Products	

- Shipping Delay Analysis	



📈 Additional Analysis

1. SARIMA Forecasting
   
- Forecasts future sales using seasonal ARIMA time series modeling.
- Implemented in: Sarima_Forecasting.ipynb

2. Power BI Dashboard
   
- Rich interactive dashboard to visualize key KPIs, product performance, and shipping trends.
- File: Power BI dashboard.pbix

📦 Requirements
These are the Python packages needed :

- streamlit
- pandas
- numpy
- scikit-learn
- joblib
- openpyxl
- matplotlib
- seaborn
- statsmodels
- pmdarima


👩‍💻 Author
Sujithra B
Data Science & AI Enthusiast

🔗 LinkedIn - linkedin.com/in/sujithra-baskaran-825827237/
📧 sujithrabaskaran406@gmail.com
