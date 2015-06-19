# HAS PAHO RELAY
# (C) 2015 mkugel

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

information_topic = "information/service/safety/smoke-alarm"
control_topic = "control/service/safety/smoke-alarm"
relayed_topic = "information/service/safety/smoke-alarm/relayed"

relay = "ON"
host = "10.37.85.223"

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.

    client.subscribe(control_topic)

    # Based on the state of relay, subscribe to the information topic or not.

    if (relay == "ON"):
        client.subscribe(information_topic)

# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):

# Relay switches based on ON/OFF message sent to control topic.

    print msg.topic
    if (msg.topic == control_topic):
        print msg.payload
        if (msg.payload == "OFF"):
            relay == "OFF"
            client.unsubscribe(information_topic)
        if (msg.payload == "ON"):
            relay == "ON"
            client.subscribe(information_topic)

    # Based on the state of relay, publish to the information topic or not.

    if (relay == "ON"):
        msgs = [{'topic':relayed_topic, 'payload':"relayed"}, (relayed_topic, str(msg.payload), 0, False)]
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

