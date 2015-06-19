# HAS PAHO BRIDGE
# (C) 2015 mkugel

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

host_source = "192.168.1.110"
host_destination = "192.168.1.111"
topic = "information/service/security/intruder-alert"

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
    msgs = [{'topic':topic, 'payload':"bridged"},
    (topic, str(msg.payload), 0, False)]
    publish.multiple(msgs, host_destination)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host_source, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()

