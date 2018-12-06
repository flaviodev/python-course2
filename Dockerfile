FROM python:alpine

RUN echo 'http://dl-3.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

RUN apk upgrade --update

RUN apk add mongodb

RUN mkdir -p /data/db

RUN mkdir -p /data/code

RUN python -m pip install pymongo

RUN python -m pip install mongoengine

WORKDIR /usr/src
