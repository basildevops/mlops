## Setup

```
git clone https://github.com/basildevops/mlops.git
cd mlops
sudo apt install python3.10-venv
python3.10 -m venv .venv
source .venv/bin/activate
python3.10 -m pip install numpy pandas scikit-learn joblib kfp
```


## Create the Pipeline YAML

```
python3 app/kubeflow/component.py
python3 app/kubeflow/pipeline.py
```
