import paho.mqtt.publish as publish
import time

msgs = [{'topic':"service/climate/interior/temperature/status", 'payload':"IMOK"},
    ("service/climate/interior/temperature/value", "22", 0, False)]

while True:
    publish.multiple(msgs, hostname="10.37.85.223")
    time.sleep(10)


