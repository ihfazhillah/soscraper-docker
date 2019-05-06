FROM python:3.6

RUN mkdir /simplereq
COPY requirements.txt /simplereq
WORKDIR /simplereq

RUN pip install -r requirements.txt
