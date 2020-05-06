FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /HavocOS_Web
WORKDIR /HavocOS_Web
COPY ./requirements.txt /HavocOS_Web
RUN pip install -r requirements.txt
COPY ./HavocOS_Web/ /HavocOS_Web/
ENTRYPOINT DJANGO_APP=python /HavocOS_Web/manage.py runserver 8000
