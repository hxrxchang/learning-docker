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

- run container
```
docker container run handson/tutorial1:latest
```

application is running http://localhost:8080/

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
