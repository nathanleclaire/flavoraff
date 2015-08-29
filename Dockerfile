FROM alpine:latest
RUN apk add --update python py-pip python-dev postgresql-dev build-base && \
		rm -rf /var/cache/apk/*
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN python manage.py collectstatic --noinput
