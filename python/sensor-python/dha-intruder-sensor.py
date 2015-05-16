import paho.mqtt.publish as publish
import time

msgs = [{'topic':"service/security/intruder-alarm/status", 'payload':"IMOK"},
    ("service/security/intruder-alarm/value", "FALSE", 0, False)]

while True:
    publish.multiple(msgs, hostname="10.37.85.223")
    time.sleep(10)


