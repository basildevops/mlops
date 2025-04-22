# pipeline.py

from kfp import compiler
from kfp.dsl import pipeline
from component import train_component  # directly import decorated function

@pipeline(
    name="Simple Linear Regression Pipeline",
    description="Train a linear regression model using Kubeflow Pipelines."
)
def regression_pipeline():
    train_component()  # call the component directly

if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=regression_pipeline,
        package_path="regression_pipeline.yaml"
    )
