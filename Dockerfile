FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN pip install uwsgi

RUN mkdir /code

WORKDIR /code
