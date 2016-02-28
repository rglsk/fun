FROM python:2.7-onbuild

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install -e .