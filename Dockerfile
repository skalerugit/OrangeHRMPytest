FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1
COPY ./Requirements.txt /Requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r /Requirements.txt

RUN mkdir /pytest-container
ADD . /pytest-container
WORKDIR /pytest-container

