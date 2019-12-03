FROM python:3.8.0-alpine

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE core.settings

MAINTAINER "Michael" <imichael@pm.me>

WORKDIR /app

RUN pip install --upgrade pip

ADD requirements_dev.txt .
RUN pip install -r requirements_dev.txt

ADD tests tests
ADD manage.py .