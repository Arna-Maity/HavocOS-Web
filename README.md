# HavocOS-Web # 
![](https://api.travis-ci.org/Arna-Maity/HavocOS-Web.svg?branch=master)


The Havoc OS Website.

## Setting up the Development Environment ##
### Dependencies (optional): ###
`sudo apt install postgresql-11 pgadmin4 postgresql-server-dev-11 libpq-dev postgresql-client-11`

### Installing Python package dependencies ###
`pip install -r requirements.txt`

### Setting up Environment Variables in Linux ###
- export *variable-name*='*variable-value*

### Setting up Environment Variable in Windows ###
![](HavocOS_Web/docs/images/Env_Var_Setup.png)


 ![](HavocOS_Web/docs/images/Env_Var_Setup_2.png)

 For more info regarding setting up Environment Variables in Windows, go   through [this link](https://www.youtube.com/watch?v=IolxqkL7cD8).


### NOTE: For the following options, you will be requiring a Docker account and docker should also be installed on your system. For more information on setting up docker on your system, go through [this link](https://docs.docker.com/engine/install/).

## (Alternative-2) Run a Docker Image ##

 ### Creating a Docker image ###
 `sudo docker build ./HavocOS_Web/ -t <your-dockerID>/<name-of-the-image-to-create>`

 ### Running the Docker image ###
`sudo docker run -e SECRET_KEY='<your-secret-key>' --network=host <your-dockerID>/<name-of-image-you-created>` 

## (Alternative-3) Run a pre-built Docker Image from DockerHUB ##

This is the recommended option if anyone just wants to quickly test all the latest features and changes made to the web app without getting their hands dirty with setting up a development environment.

Once you have docker installed on your system, run the following command: 

`sudo docker run -e SECRET_KEY='<your-secret-key>' --network=host arnamaity/havocos-web`

