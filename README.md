# learning-docker
## tutorial1
- build
```
docker image build -t handson/tutorial1:latest .
```

check if image is built
```
docker images
```

application is running http://localhost:8080/

- run container
```
docker container run handson/tutorial1:latest
```

## tutorial2
- build
```
docker image build -t handson/tutorial2:latest .
```

- run
```
docker-compose up -d
```

application is running http://localhost:8080/
