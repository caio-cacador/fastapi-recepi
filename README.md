# FastAPI Recepi
API Recipe using FastAPI, PyDantic, Python Decoupe and MongoEngine


## Instructions for running the application

1. First, make sure you are at the root of the project.

2. Then, use the Docker Compose to start the MongoDB:

```sh
docker-compose up -d
```

3. Install the requirements:
```sh
pip install -r requirements.txt
```

4. Then, run the uvicorn:

```sh
uvicorn main:app
```
or 
```sh
uvicorn main:app --reload
```

5. Access the application through the link http://127.0.0.1:8000/

## Instructions for accessing the documentation

1. First, make sure you have run the application
2. Then, go to the link:

http://127.0.0.1:8000/docs

or

http://127.0.0.1:8000/redoc/



## To install Docker and Docker Compose use the links

#### Docker
https://docs.docker.com/engine/install/

#### Docker Compose
https://docs.docker.com/compose/install/
