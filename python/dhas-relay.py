import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")
    client.subscribe("service/safety/smoke-alarm")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msgs = [{'topic':"service/safety/gateway-1", 'payload':"relayed"},
    ("service/safety/gateway-1", str(msg.payload), 0, False)]
    publish.multiple(msgs, hostname="192.168.1.100")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.37.85.223", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

