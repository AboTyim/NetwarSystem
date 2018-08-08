#!/usr/bin/python
import os, re
from simpleconfigparser import simpleconfigparser

config = simpleconfigparser()
config.read(os.environ['HOME'] +'/.twitter')

for root, dirs, files in os.walk(os.environ['HOME'] + "/" + config.API.homedir, topdown=True):
   for name in files:
      if re.search("consolidated", name):
	      print(os.path.join(root, name))

