FROM python:3.8-alpine

WORKDIR /

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \ 
    && apk add --no-cache mariadb-dev \
    && apk add mariadb-connector-c-dev


ENV LD_LIBRARY_PATH /usr/lib/instantclient
                       
COPY init.sql /docker-entrypoint-initdb.d/init.sql
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .
