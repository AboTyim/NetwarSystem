# Netwar System Twitter Recorder

This is the prime repository for our Twitter related code. There are four major functions that this system provides.

* Bulk capture of Twitter account timelines.
* Bulk capture of Twitter user profiles.
* Persistent tracking based on a user lists.
* Capture streaming of userids or search terms.

The following are infrastructure dependencies.

* Redis- provides shared Python objects, used for various work queues.
* Elasticsearch 6.5.4 - searchable archive of text data.
* Search Guard - Elasticsearch security package, needed for teams and/or public access.
* Neo4j - graph database for storing Twitter interactions, new as of 3/2019.
* Netdata - system monitor, which you will become familiar.

The following are the major Python dependencies:

* Walrus - provides a Python objects layer over Redis.
* Elasticsearch 6.3.1 for Python.
* Py2neo Neo4j client.
* Tweepy Twitter API access for Python.

Elasticsearch and Redis/Walrus were the first things implemented, then Search Guard, and we have barely scratched the surface with Neo4j. There are significant changes from Elasticsearch 6.5.4 to 6.7.0, and even more dramatic changes to 7.x. We have a ELK7 prototype, but it's nowhere near ready. We can not support this software on anything but 6.5.x at this time.

#System Requirements

When we first ran this system it was on a small desktop:

* intel i7-2820QM - cpumark 6640.
* 32 gig of ram.
* 120 gig SSD, 32 gig for OS, remainder for zfs caching.
* 500 gig spindle used for ZFS storage.

This machine is still around for testing, but is limited to four to eight accounts, which exercises it heavily. if you don't have room for two drives, you definitely need an SSD for this system, even at small scale. Sixteen gig would be enough for a handful of accounts.


Our current setup is a pair of machines with these specs:

* Dual Xeon E5-2680v1 eight core processors.
* 192 gig of ram.
* 500 gig SSD, half for OS, half for ZFS cache.
* Pairs of Seagate IronWolf 2tb NAS drives.

This configuration has supported sixty four accounts doing bulk collection of tweets or users, while simultaneously running 16 stream captures.

# Installation

* Do a git clone of this archive.
* Try pip install -r REQUIREMENTS.txt
* Look at pipfreeze.txt to see what was actually running on 13 Apr 2019.
* Install Elasticsearch.
* Install Redis.
* Install Neo4j.
* Install Netdata monitoring software.
* Look at example.conf to see how a client is configured. You MUST have your own Twitter API keys, we do not provide that.
* Look at crontab.txt to see how observer accounts, bulk tweets, and bulk userids are collected.
* Copy the copy code to /usr/local/bin, then chmod 755 so it's executable.

When configured and enabled you should find the following ports open. You can check this with netstat -lan | grep "LISTEN". If you are unsure what a given port does, try lsof -i :portnumber

* tcp/9200 - Elasticsearch clients.
* tcp/9300 - Elasticsearch cluster communications.
* tcp/6379 - Redis.
* tcp/7474 - Neo4j browser.
* tcp/7687 - Neo4j BOLT port.
* tcp/19999 - Netdata monitoring.

# Operation

