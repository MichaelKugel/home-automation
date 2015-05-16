import paho.mqtt.publish as publish
import time

msgs = [{'topic':"service/safety/smoke-alarm/status", 'payload':"IMOK"},
    ("service/safety/smoke-alarm/value", "FALSE", 0, False)]

while True:
    publish.multiple(msgs, hostname="10.37.85.223")
    time.sleep(10)


