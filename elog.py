#!/usr/bin/python
# example of creating a single line to bulk load data to Elastic
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import datetime

#{ "index" : { "_index" : "test", "_type" : "type1", "_id" : "1" } }
#{ "field1" : "value1" }
client = Elasticsearch()

def elog(acct, mesg):
	mydate = str(datetime.datetime.utcnow())
	print(str(mydate))
	bod = "{ \"index\" : { \"_index\" : \"perflog\", \"_type\" : \"perfdata\"} }\n"
	bod = bod + "{\"name\" : \"" + acct + "\", \"event\" : \"" + mesg + "\" , \"date\" : \"" + mydate + "\"}\n"
	try:
		client.bulk(body=bod)
	except(RuntimeError, TypeError, NameError):
		pass

#client.bulk(index="tmptwitter",doc_type="twusers",body=bod)

elog("newname","some random message")




