import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib

def train_model(data):
    features = ['Age', 'BMI', 'Children', 'Sex', 'Smoker', 'Region']
    target = 'Charges'

    X = data[features]
    y = data[target]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"Root Mean Squared Error (RMSE): {rmse}")

    joblib.dump(model, 'insurance_model.pkl')
    joblib.dump(scaler, 'insurance_scaler.pkl')

    return model, scaler

if __name__ == "__main__":
    data = pd.read_csv("cleaned_insurance_data.csv")
    train_model(data)
