#!/bin/bash

docker ps
docker stop mosqbrokermain
docker rm mosqbrokermain
docker run -d --name mosqbrokermain -e "CONTAINER_NAME=mosqbrokermain" -h mosqbrokermain -p 1883:1883 -p 8883:8883 mkugel/arch-mosq-new-sensor /bin/bash -c 'su labadmin -c mosquitto'
