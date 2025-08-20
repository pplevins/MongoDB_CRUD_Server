@REM Setting local MongoDB docker container for stage 1
docker run -d --name my-mongodb -p 27017:27017 mongo

@REM Building docker image of the api server code and pushing it to DockerHub
docker build -t pplevins/mongo_api_server:v1.0 .
docker push pplevins/mongo_api_server:v1.0