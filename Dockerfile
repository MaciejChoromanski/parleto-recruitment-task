FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install virtualenv \
    && virtualenv venv \
    && source venv/bin/activate
RUN pip install -r requirements.txt