import paho.mqtt.publish as publish
import time

msgs = [{'topic':"service/broker/status", 'payload':"IMOK"},
    ("service/all/status", "ALOK", 0, False)]

while True:
    publish.multiple(msgs, hostname="10.37.85.223")
    time.sleep(10)

