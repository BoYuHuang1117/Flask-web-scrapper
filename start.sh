#!/bin/bash

# name of the container
app="scrapy-be"

# build image template from Dockerfile in cd
docker build . -t ${app}

# create container exposed at port 5000
# and links cd to /var/www in the container

# -d means container in daemon mode (background mode)

# -p means binding port 5000 on server to 
# port 80 on the Docker container

# -v means Docker volume to mount
# here is entire project to /var/www
docker run -d -p 5000:80\
  --name=${app} \
  -v $PWD:/app ${app}
