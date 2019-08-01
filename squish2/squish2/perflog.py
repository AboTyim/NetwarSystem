import datetime, platform, getpass
def perflog(client, scname,mesg):
	mydate = str(datetime.datetime.utcnow())
	ebod = "{ \"index\" : { \"_index\" : \"perflog\" + platform.node(), \"_type\" : \"perfdata\"} }\n"
	ebod = ebod + "{\"host\" : \"" + platform.node() + "\", \"shell\" : \"" + getpass.getuser() + "\", \"screen_name\" : \""
	ebod = ebod + scname + "\", \"event\" : \"" + mesg + "\" , \"date\" : \"" + mydate + "\"}\n"
	#print(ebod)
	try:
		client.bulk(body=ebod)
	except(RuntimeError, TypeError, NameError):
		print("can't get to client")
		pass

