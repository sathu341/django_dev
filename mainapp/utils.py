import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib

# Define the exchange rate
EXCHANGE_RATE = 83

# Load dataset
data = pd.read_csv('C:/waiterproject/tips.csv')

# Convert monetary values to INR
data['total_bill'] *= EXCHANGE_RATE
data['tip'] *= EXCHANGE_RATE

# Prepare features and target
X = data.drop(columns=['tip'])
y = data['tip']

categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['number']).columns

# One-hot encode categorical columns
encoder = OneHotEncoder(sparse_output=False, drop='first')
X_encoded = pd.DataFrame(encoder.fit_transform(X[categorical_cols]))
X_encoded.columns = encoder.get_feature_names_out(categorical_cols)

# Combine features
X_final = pd.concat([X[numerical_cols].reset_index(drop=True), X_encoded.reset_index(drop=True)], axis=1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and encoder
joblib.dump(model, 'tip_predictor_model.pkl')
joblib.dump(encoder, 'tip_encoder.pkl')

# Load the model and encoder
def load_model():
    model = joblib.load('tip_predictor_model.pkl')
    encoder = joblib.load('tip_encoder.pkl')
    return model, encoder

# Function to make predictions
def predict_tip(data):
    model, encoder = load_model()
    sample_data = pd.DataFrame(data)
    sample_data = sample_data.reindex(columns=X_final.columns, fill_value=0)
    predicted_tip = model.predict(sample_data)[0]
    return predicted_tip
