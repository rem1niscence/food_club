FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN adduser -D user

# Dependencies and scripts setup
RUN apk add --update --no-cache postgresql-client nginx jpeg-dev zlib-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc  libc-dev linux-headers postgresql-dev python3-dev 
ENV LIBRARY_PATH=/lib:/usr/lib

# COPY ./requirements.txt /requirements.txt

COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv==2018.11.26 && \
  pipenv install --system

RUN apk del .tmp-build-deps

# Add code and directories
RUN mkdir /food_club
WORKDIR /food_club/
COPY ./django /food_club/django
COPY ./scripts /food_club/scripts

RUN chown -R user /food_club

USER user