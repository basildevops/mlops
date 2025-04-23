# component.py

from kfp.dsl import component
import train_model

@component(
    base_image="python:3.9",
    packages_to_install=["pandas", "matplotlib", "scikit-learn", "joblib"]
)
def train_component():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    import joblib
    import boto3
    from botocore.client import Config

    # Dataset
    data = {
        "Size (sq ft)": [500, 1000, 1500, 2000, 2500],
        "Price (in Lakhs)": [25, 50, 75, 100, 125]
    }
    df = pd.DataFrame(data)
    X = df[["Size (sq ft)"]]
    y = df["Price (in Lakhs)"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Model Coefficients: {model.coef_}")
    print(f"Model Intercept: {model.intercept_}")

    # Save model locally
    joblib.dump(model, "model.pkl")

    # Upload to MinIO (S3)
    s3 = boto3.client('s3',
                      endpoint_url='http://minio.kubeflow.svc.cluster.local:9000',  # MinIO internal URL in Kubeflow
                      aws_access_key_id='minio',
                      aws_secret_access_key='minio123',
                      config=Config(signature_version='s3v4'),
                      region_name='us-east-1')

    bucket_name = 'mlpipeline'
    object_name = 'model.pkl'

    # Ensure bucket exists (optional)
    s3.create_bucket(Bucket=bucket_name)
    # Upload
    s3.upload_file('model.pkl', bucket_name, object_name)
    print(f"Model uploaded to MinIO bucket '{bucket_name}' as '{object_name}'")
