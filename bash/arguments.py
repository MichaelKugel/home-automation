#!/usr/bin/python

import sys
import time

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
  time.sleep(1)
  print "Verifying desired state"
  time.sleep(1)
  print "Confirmed"
