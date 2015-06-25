#!/usr/bin/python

import os
import sys
import time

from pexpect import pxssh as pxssh
import pexpect
import yaml

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

validated = 0
control_topic = 'default'
information_topic = 'default'
status_topic = 'default'
relay_topic = 'default'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('control/service/safety/smoke-alarm/2/power')
    client.subscribe(information_topic)

def on_message(client, userdata, msg):
    print (msg.topic)
    if (msg.topic == control_topic):
        print (msg.payload)
        client.unsubscribe(control_topic)
        #if (validated != 2):
        #    validated += 1
    elif (msg.topic == information_topic):
        print (msg.payload)
        client.unsubscribe(information_topic)
        #if (validated != 2):
        #    validated += 1
    else:
        print "Unknown topic received"

    #if (validated > 1):
    #    print "Message Topics validated"
        # client.loop_stop()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# containername='testpx'

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv[1])

if (str(sys.argv[1]) == 'desire.yaml'):
  print "Attempting to reach desired state"
  time.sleep(1)
  print "Attempt 1"

# YAML parsing

  print "Opening yaml file"
  f = open('desire.yaml')
  print "Parsing Yaml file"
  desire_dictionary = yaml.load(f)
  print "Closing YAML file"
  f.close()

  #with open("desire.yaml", 'r') as stream:
  #  print(yaml.load(stream))

# Variable Assignments

  has_host = ''.join(desire_dictionary['infrastructure']['host'][0])
  print "Assigning host to be:"
  print ''.join(desire_dictionary['infrastructure']['host'][0])

  containername = ''.join(desire_dictionary['container']['name'][0])
  print "Assgning container name to be:"
  print ''.join(desire_dictionary['container']['name'][0])

  codefolder = ''.join(desire_dictionary['code']['folder'][0])
  print "Assigning code folder to be:"
  print ''.join(desire_dictionary['code']['folder'][0])

  codesource = ''.join(desire_dictionary['code']['source'][0]) 
  print "Assigning code source file to be:"
  print ''.join(desire_dictionary['code']['source'][0])

  codecommand = ''.join(desire_dictionary['code']['command'][0])
  print "Assigning code interpreter to be:"
  print  ''.join(desire_dictionary['code']['command'][0])

  print "Assigning topics (MOM Interfaces)"

  control_topic = 'control/'.join(desire_dictionary['topic']['control'][0])
  information_topic = 'information/'.join(desire_dictionary['topic']['information'][0])
  
  #print 'control/'.join(desire_dictionary['topic']['control'][0])
  #print 'information/'.join(desire_dictionary['topic']['information'][0])

  relayed_topic = 'information/'.join(desire_dictionary['topic']['relay'][0])
  status_topic = 'information/'.join(desire_dictionary['topic']['status'][0])

# Concatenate environmental variable strings

  environmentals = ' -e '+ '"INFORMATION_TOPIC=' + information_topic + ' -e '+ '"STATUS_TOPIC=' + status_topic + ' -e '+ '"RELAYED_TOPIC=' + relayed_topic + ' -e '+ '"CONTROL_TOPIC=' + status_topic + ' '

  print environmentals

 #  os.system("expect ../bash/expect/expect.sh 10.37.85.223 root root ' -it --name firstexpect /mkugel/archmosqextpysensor /bin/bash'") 

# Remote Execution of Docker command using pexpect via ssh
  
  dockercommand = 'docker run -it --name '+containername+ environmentals+' -v '+codefolder+':/root/code/3rd-party mkugel/archmosqextpysensor '+codecommand+' /root/code/3rd-party/'+codesource

  print "The docker command executed on the remote host is:"
  print(dockercommand)

  # dockercommand = 'docker run -it --name '+containername+' mkugel/archmosqextpysensor /bin/bash'

  p = pxssh.pxssh()
  p.login(has_host, 'root', 'root')

  # p.sendline('docker run -it --name secondpx mkugel/archmosqextpysensor /bin/bash')

  p.sendline(dockercommand)

# Verification of container deployment
  
  time.sleep(1)
  print "Verifying desired state"
  time.sleep(1)
  p.sendline('docker ps')
  p.prompt()
  output = p.before
  if(containername in output):
    print "Confirmed"
  else:
    print "Could NOT confirm if "+containername+" was launched."

  print "Running Tests for container..."
  time.sleep(1)

  client.connect(has_host, 1883, 60)
  client.loop_start()
  msgs = [{'topic':control_topic, 'payload':"test"}, (information_topic, "test", 0, False)]
  publish.multiple(msgs, hostname=has_host)
  # if (validated > 1):
  print "ALOK - desire script terminated"

elif (str(sys.argv[1]) in ['-h', '--help', '?']):
  print "Author: mkugel"
  print "Help (-h)"
  print "Usage: python <this.py> <desire.conf>"

else:
  print "No arguments provided. Try -h for help"


