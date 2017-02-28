FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/chat/
WORKDIR /opt/chat/

ADD . /opt/chat/
RUN pip install -r requirements.txt
