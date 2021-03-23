FROM python:3

RUN pip3 install flask

USER root

COPY . /app

CMD python3 /app/example.py