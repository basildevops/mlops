# component.py

from kfp.dsl import component
import train_model

@component(
    base_image="python:3.9",
    packages_to_install=["pandas", "matplotlib", "scikit-learn", "joblib"]
)
def train_component():
    train_model.train_and_evaluate()
