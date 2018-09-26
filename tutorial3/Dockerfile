FROM python:3

WORKDIR /app
ADD ./src/ /app

RUN pip install bottle
RUN pip install mysql-connector-python-rf

ENTRYPOINT ["python", "index.py"]
