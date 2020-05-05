import os

DOCKER_USERNAME = os.environ['DOCKER_USERNAME']
DOCKER_PASSWORD = os.environ['DOCKER_PASSWORD']

login = "echo \"" + DOCKER_PASSWORD = "\" | docker login -u "$DOCKER_USERNAME" --password-stdin
img = 'docker build ./HavocOS_Web/ -t ' + DOCKER_USERNAME + '/havocos'
push = 'docker push ' + DOCKER_USERNAME + '/havocos'
print(img) 
os.system(img)
print(push)
os.system(push)