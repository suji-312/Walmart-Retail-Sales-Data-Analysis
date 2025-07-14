import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load the extracted Excel file
file_path = r"C:\Users\kamal\Downloads\walmart Retail Data.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse('walmart Retail Data')

# Preprocess
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Shipping Delay'] = (df['Ship Date'] - df['Order Date']).dt.days
df = df.dropna(subset=['Product Category', 'Discount', 'Shipping Delay', 'Sales'])
df['Product Category Code'] = df['Product Category'].astype('category').cat.codes

# Features and target
X = df[['Product Category Code', 'Discount', 'Shipping Delay', 'Sales']]
y = df['Sales']

# Train/test split
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'sales_prediction_model.pkl')
print("✅ Model saved as sales_prediction_model.pkl")
