import paho.mqtt.client as mqtt
from flask import Flask
app = Flask(__name__)

teststring = "test"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mqtt/')
def my_mqtt():
    return 'Wasup ' + teststring

if __name__ == '__main__':
    app.run()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/")
    # client.subscribe("service/#")
    client.subscribe("service/#")

def do_something(msg):
    print(msg)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    print('Damnit')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# client.connect("10.37.85.223", 1883, 1)
client.connect("192.168.1.100", 1883, 1)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
