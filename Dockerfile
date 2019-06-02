FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Dependencies and scripts setup
RUN apk add --update --no-cache postgresql-client nginx jpeg-dev zlib-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc  libc-dev linux-headers postgresql-dev python3-dev 

COPY Pipfile .
COPY Pipfile.lock .
RUN pip install pipenv==2018.11.26 && \
  pipenv install --system

RUN apk del .tmp-build-deps

RUN adduser -D user

# Add code and directories
RUN mkdir /food_club
WORKDIR /food_club/
COPY ./django /food_club/django
COPY ./scripts /food_club/scripts

RUN mkdir -p /food_club/django/media_root \
  && mkdir -p /food_club/django/static_root \
  && chown -R user /food_club

# TODO: Bind volumes as non-root or change ownership of them to non-root user.
# USER user