import paho.mqtt.publish as publish
import time

msgs = [{'topic':"service/safety/co2/status", 'payload':"IMOK"},
    ("service/safety/co2/value", "0.0", 0, False)]

while True:
    publish.multiple(msgs, hostname="10.37.85.223")
    time.sleep(10)


