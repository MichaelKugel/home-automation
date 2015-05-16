#!/bin/bash

docker run -i -td -p 1883:1883 -p 8883:8883 --name mqttbroker1 -v /root/code/broker-python:/python-code michaelk1/archmosqextpy
docker exec mqttbroker1 su labadmin -c mosquitto
docker exec mqttbroker1 python ~/python-code/dha-broker.py

