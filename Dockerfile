FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /HavocOS_Web
WORKDIR /HavocOS_Web
COPY ./requirements.txt /HavocOS_Web
RUN pip install -r requirements.txt
COPY ./HavocOS_Web/ /HavocOS_Web/
RUN python /HavocOS_Web/manage.py makemigrations
RUN python /HavocOS_Web/manage.py migrate
RUN python /HavocOS_Web/manage.py loaddata /HavocOS_Web/device_maintainer.json
ENTRYPOINT DJANGO_APP=python /HavocOS_Web/manage.py runserver 8000
