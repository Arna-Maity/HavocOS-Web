#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build ./HavocOS_Web/ -t $DOCKER_USERNAME/havocos-web
docker push $DOCKER_USERNAME/havocos-web