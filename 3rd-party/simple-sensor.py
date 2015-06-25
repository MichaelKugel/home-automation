import paho.mqtt.publish as publish
import time
host = "10.37.85.223"

msgs = [{'topic':"information/service/safety/smoke-alarm/1/status", 'payload':"IMOK"},
    ("information/service/safety/smoke-alarm/1/value", "FALSE", 0, False)]

while True:
    publish.multiple(msgs, hostname=host)
    time.sleep(10)
