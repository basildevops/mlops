# pipeline.py

from kfp.dsl import pipeline
from kfp import compiler
from kfp.components import load_component_from_file

@pipeline(
    name="Simple Linear Regression Pipeline",
    description="Train a linear regression model using Kubeflow Pipelines."
)
def regression_pipeline():
    train_op = load_component_from_file("train_component.yaml")()
    
if __name__ == "__main__":
    compiler.Compiler().compile(
        pipeline_func=regression_pipeline,
        package_path="regression_pipeline.yaml"
    )
