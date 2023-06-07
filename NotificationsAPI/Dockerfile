# Diving into docker

FROM python:3.10-alpine

MAINTAINER Tiago Pedrosa

LABEL version="1.0"

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# COPY EmailSender.py /app/src

COPY EmailSenderAPI.py /app/EmailSenderAPI.py

EXPOSE 8010/tcp

CMD ["uvicorn", "EmailSenderAPI:app", "--host", "0.0.0.0", "--port", "8010"]
