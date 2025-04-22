# component.py

from kfp.components import create_component_from_func
import train_model

def train_component():
    train_model.train_and_evaluate()

if __name__ == "__main__":
    component = create_component_from_func(
        train_component,
        base_image="python:3.9",
        packages_to_install=["pandas", "matplotlib", "scikit-learn", "joblib"]
    )
    component.save("train_component.yaml")
