#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build ./HavocOS_Web/ -t arnamaity/havocos-web
docker push arnamaity/havocos-web