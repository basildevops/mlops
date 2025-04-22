# train_model.py

def train_and_evaluate():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    import joblib

    data = {
        "Size (sq ft)": [500, 1000, 1500, 2000, 2500],
        "Price (in Lakhs)": [25, 50, 75, 100, 125]
    }

    df = pd.DataFrame(data)
    X = df[["Size (sq ft)"]]
    y = df["Price (in Lakhs)"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Model Coefficients: {model.coef_}")
    print(f"Model Intercept: {model.intercept_}")

    joblib.dump(model, "model.pkl")
