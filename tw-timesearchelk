#!/usr/bin/python
import datetime

# Python strftime reference
# http://strftime.org/
#
# Elasticsearch Twitter timestamp mapping as a single line of JSON
# "created_at" : {"type" : "date",  "format" : "EEE MMM dd HH:mm:ss Z YYYY"},
#
# Example timestamp: Sun Mar 24 05:20:06 +0000 2019

# Twitter timestamp of the now
now = datetime.datetime.now()
print(now.strftime("%a %b %d %X +0000 %Y"))

# 24 hours ago
last24 = now - datetime.timedelta(days=1)
print(last24.strftime("%a %b %d %X +0000 %Y"))

# This specific query works against Twitter data
#s = Search(using=client, index="twbrexit").filter('range', created_at={"from": last24.strftime("%a %b %d %X +0000 %Y") }).query("match", text="Brexit")
