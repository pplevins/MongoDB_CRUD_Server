@REM Setting local MongoDB docker container for stage 1
docker run -d --name my-mongodb -p 27017:27017 mongo

@REM Building docker image of the api server code and pushing it to DockerHub
docker build -t pplevins/mongo_api_server:v1.0 .
docker push pplevins/mongo_api_server:v1.0
docker image tag pplevins/mongo_api_server:v1.0 pplevins/mongo_api_server:latest
docker push pplevins/mongo_api_server:latest

@REM Login to OpenShift
oc login --token=<my-api-token> --server=https://api.rm3.7wse.p1.openshiftapps.com:6443
oc apply -f mongo-secret.yaml
oc apply -f mongo-pvc.yaml
oc apply -f mongo-deployment.yaml
oc apply -f mongo-service.yaml

oc apply -f api-server-deployment.yaml
oc apply -f api-server-service.yaml
oc expose svc/mongo-server