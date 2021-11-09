# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

RUN apt-get update -y && apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /

EXPOSE 5000

ENV FLASK_ENV=development
ENV FLASK_APP=main
RUN  apt install -y curl 



CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
