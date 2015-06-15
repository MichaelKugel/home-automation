import paho.mqtt.publish as publish
import time

msgs = [{'topic':"information/service/safety/smoke-alarm/status", 'payload':"IMOK"},
    ("information/service/safety/smoke-alarm/value", "FALSE", 0, False)]

while True:
    publish.multiple(msgs, hostname="192.168.1.110")
    time.sleep(10)
