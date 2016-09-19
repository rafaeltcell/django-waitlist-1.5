FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install vim

RUN mkdir /code

WORKDIR /code

#ADD requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

#RUN useradd -m tcelluser && echo "tcelluser:tcelluser" | chpasswd && adduser tcelluser sudo

#USER tcelluser
#CMD /bin/bash

#RUN chown -R tcelluser /code
#RUN chgrp -R tcelluser /code
