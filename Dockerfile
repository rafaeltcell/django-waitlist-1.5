FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN pip install uwsgi

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
