## Create a Secret for kserve to access minio

```
kubectl create secret generic minio-creds \
  --from-literal=AWS_ACCESS_KEY_ID=YOUR_ACCESSKEY \
  --from-literal=AWS_SECRET_ACCESS_KEY=YOUR_SECRETKEY \
  -n kubeflow
```

Please make sure that you replace YOUR_ACCESSKEY and YOUR_SECRETKEY with actual values.

## Deploy to Kubernetes

```
kubectl apply -f .
```
