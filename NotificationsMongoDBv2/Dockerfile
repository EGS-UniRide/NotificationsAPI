# Diving into docker

FROM python:3.10-alpine

MAINTAINER Tiago Pedrosa

LABEL version="1.0"

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY NotificationsAPI.py /app/NotificationsAPI.py

COPY ./src /app/src

EXPOSE 8010/tcp

CMD ["uvicorn", "NotificationsAPI:app", "--host", "0.0.0.0", "--port", "8010"]