#!/usr/bin/python
import datetime, platform, getpass
import csv, json, pprint, os, random, re, sys, time, datetime
import redis, walrus, tweepy, configparser, ssl
import psutil, getpass, setproctitle, platform
from time import gmtime, strftime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch.connection import create_ssl_context
from urllib3.exceptions import ProtocolError
from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher
import squish2, requests

#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

config = configparser.ConfigParser()
config.read(os.environ['HOME'] +'/.twitter')

try:
	ssl_context = create_ssl_context(cafile='/home/root-ca.pem')
	ssl_context.check_hostname = False
	ssl_context.verify_mode = ssl.CERT_NONE
	client = Elasticsearch(config['STREAM']['elksg'], ssl_context=ssl_context, timeout=60, http_auth=(config['STREAM']['elksguser'], config['STREAM']['elksgpass']))
except:
	sys.exit()

lastweek = datetime.datetime.now() - datetime.timedelta(days=14)
lastweek.strftime("%a %b %d %X +0000 %Y")

s = Search(using=client, index="twbrexit").filter('range', created_at={"from": lastweek.strftime("%a %b %d %X +0000 %Y") }).query("match", text="Brexit")
results = s.execute()

#'quote_count', 'reply_count'
for hit in s.scan():
	if((hit.quote_count + hit.reply_count) > 0):
		print(str(hit.quote_count) + " " + str(hit.reply_count))
