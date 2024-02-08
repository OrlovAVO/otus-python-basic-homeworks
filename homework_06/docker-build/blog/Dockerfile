FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY blog /app

WORKDIR /app