#!/usr/bin/python

import os
import sys
import time
from pexpect import pxssh as pxssh
import pexpect
import yaml

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

# Variable Assignments

  has_host = ''.join(desire_dictionary['infrastructure']['host'][0])
  print "Assigning host to be:"
  print(desire_dictionary['infrastructure']['host'][0])

  containername = ''.join(desire_dictionary['infrastructure']['host'][0])
  print "Assgning container name to be:"
  print(desire_dictionary['container']['name'][0])

  codefolder = ''.join(desire_dictionary['code']['folder'][0])
  print "Assigning code folder to be:"
  print(desire_dictionary['code']['folder'][0])

  codesource = ''.join(desire_dictionary['code']['source'][0])
  print "Assigning code source file to be:"
  print(desire_dictionary['code']['source'][0])

  codecommand = ''.join(desire_dictionary['code']['command'][0])
  print "Assigning code interpreter to be:"
  print(desire_dictionary['code']['command'][0])

  print "Assigning topics (MOM Interfaces - not implemented yet!)

# Remote Execution of Docker command using pexpect via ssh
  
  dockercommand = 'docker run -it --name '+containername+' -v '+codefolder+':/root/code/3rd-party mkugel/archmosqextpysensor '+codecommand+' /root/code/3rd-party/'+codesource

  print "The docker command executed on the remote host is:"
  print(dockercommand)

  # dockercommand = 'docker run -it --name '+containername+' mkugel/archmosqextpysensor /bin/bash'

  p = pxssh.pxssh()
  p.login(has_host, 'root', 'root')

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
  print "ALOK"

elif (str(sys.argv[1]) in ['-h', '--help', '?']):
  print "Author: mkugel"
  print "Help (-h)"
  print "Usage: python <this.py> <desire.conf>"

else:
  print "No arguments provided. Try -h for help"
