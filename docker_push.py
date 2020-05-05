import os

DOCKER_USERNAME = os.environ['DOCKER_USERNAME']
DOCKER_PASSWORD = os.environ['DOCKER_PASSWORD']

login = "echo \"" + DOCKER_PASSWORD + "\" | docker login -u \"" + DOCKER_USERNAME + "\" --password-stdin"
img = 'docker build ./HavocOS_Web/ -t ' + DOCKER_USERNAME + '/havocos-web'
push = 'docker push ' + DOCKER_USERNAME + '/havocos-web'
print(login)
print("Logging into Docker ...")
os.system(login)
print(img) 
print("Building Docker image ...")
os.system(img)
print(push)
print("Pushing Docker image to dockerHUB ...")
os.system(push)