FROM python:3.7.10-slim-buster

RUN apt-get update && apt-get install -y gcc

COPY /requirements/base.txt base.txt
RUN pip install -r base.txt

RUN mkdir /code/

WORKDIR /code/
