FROM python:3.11.0

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update

EXPOSE 5000