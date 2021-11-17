FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .