#!/bin/sh
docker ps
docker start mosqbrokermain
docker start newsensor1
docker start newsensor6
docker start newsensor7
docker start sensor-gateway-1
docker exec mosqbrokermain su labadmin
docker exec mosqbrokermain mosquitto
docker exec newbroker3 su labadmin -c mosquitto
docker exec newsensor1 python ~/code/iot-home/iot-home-mqtt-sensor.py
docker exec newsensor6 python ~/code/iot-home/iot-home-mqtt-sensor.py
docker exec newsensor7 python ~/code/iot-home/iot-home-mqtt-sensor.py
