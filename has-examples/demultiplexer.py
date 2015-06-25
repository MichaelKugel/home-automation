# HAS PAHO DEMULTIPLEXER
# (C) 2015 mkugel

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

host = "10.37.85.223"
in_topic = "control/service/security/access/general"
out_topics = ["control/service/security/access/frontdoor", "control/service/security/access/backdoor", "control/service/security/access/sidedoor"]

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe(in_topic)

# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):

    for topic in out_topics:
        print topic
        msgs = [{'topic':topic, 'payload':"demultiplexed"}, (topic, str(msg.payload), 0, False)]
        publish.multiple(msgs, hostname=host)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()

