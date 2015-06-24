#!/usr/bin/python

import os
import sys
import time
from pexpect import pxssh as pxssh
import pexpect

containername='fourthpx'

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv[1])
if (str(sys.argv[1]) in ['-h', '--help', '?']):
  print "Author: mkugel"
  print "Help (-h)"
  print "Usage: python <this.py> <desire.conf>"
if (str(sys.argv[1]) == 'desire.yaml'):
  print "Attempting to reach desired state"
  time.sleep(1)
  print "Attempt 1"
 #  os.system("expect ../bash/expect/expect.sh 10.37.85.223 root root ' -it --name firstexpect /mkugel/archmosqextpysensor /bin/bash'") 
  
  dockercommand = 'docker run -it --name '+containername+' mkugel/archmosqextpysensor /bin/bash'
  p = pxssh.pxssh()
  p.login('10.37.85.223', 'root', 'root')
  # p.sendline('docker run -it --name secondpx mkugel/archmosqextpysensor /bin/bash')
  p.sendline(dockercommand)
  
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
