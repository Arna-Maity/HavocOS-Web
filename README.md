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


## (Alternative) Run a Docker Image ##
 ### Creating a Docker image ###
 `sudo docker build ./HavocOS_Web/ -t <your-dockerID>/<name-of-the-image-to-create>`

 ### Running the Docker image ###
`sudo docker run -e SECRET_KEY='<your-secret-key>' --network=host <your-dockerID>/<name-of-image-you-created>` 