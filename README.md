# Netwar System Twitter Recorder

This is the prime repository for our Twitter related code. There are four major functions that this system provides.

* Bulk capture of Twitter account timelines.
* Bulk capture of Twitter user profiles.
* Persistent tracking based on a user's lists.
* Capture streaming of userids or search terms.

The following are infrastructure dependencies.

* Redis- provides shared Python objects, used for various work queues.
* Elasticsearch 6.5.4 - searchable archive of text data.
* Search Guard - Elasticsearch security, needed for teams and/or public access.
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

* Dual Xeon E5-2680v1 eight core processors - combined cpumark 25,000.
* 192 gig of ram.
* 500 gig SSD, half for OS, half for ZFS cache.
* Pairs of Seagate IronWolf 2tb NAS drives.

This configuration has supported sixty four accounts doing bulk collection of tweets or users, while simultaneously running 16 stream captures. Each machine runs three VMs that store the data. This requires a bit of hand waving to explain, but it sets us up to grow beyond two machines when we need to do so.

# Installation

* Do a git clone of this archive.
* Try pip install -r REQUIREMENTS.txt
* Look at pipfreeze.txt to see what was actually running on 13 Apr 2019.
* Clone TwitterUtils, which has some useful bits from our pre-Elastic software.
* Do a git clone of the ELKSG archive, which has Elastic setup/tuning stuff in it.
* Install Elasticsearch 6.5.4.
* Install Redis.
* Install Neo4j.
* Install Netdata monitoring software.
* Look at example.conf to see how a client is configured. You MUST have your own Twitter API keys, we do not provide that.
* Look at crontab.txt to see how observer accounts, bulk tweets, and bulk userids are collected.
* Copy the copy code to /usr/local/bin, then chmod 755 so it's executable.

When configured and enabled you should find the following ports open. You can check this with netstat -lan | grep "LISTEN". If you are unsure what a given port does, try lsof -i :portnumber

* tcp/9200 - Elasticsearch clients.
* tcp/9300 - Elasticsearch cluster communications.
* tcp/5601 - Elasticsearch Kibana graphical interface.
* tcp/6379 - Redis.
* tcp/7474 - Neo4j browser.
* tcp/7687 - Neo4j BOLT port.
* tcp/19999 - Netdata monitoring.

# Basic Operations

You'll need access to a Twitter developer account. Obtain the consumer key and consumer secret, place those in the tw-auth command. Run it, auth using a Twitter account, put the seven digit PIN in on the command line, and your first ~/.twitter file will be created.

The tw-myname script is a good way to check that your auth is done right.

tw-rates will show any API usage for the account in ~/.twitter. If you have multiple accounts you can feed this script a different file name via the command line and it'll check that one instead.

The TwitterUtils repository contains some small scripts that were part of our prior generation of software, when we still had a great deal of flat text file usage. This is not so necessary any more, but they'll work with the ~/.twitter file and they perform some interesting functions. If you're wanting to learn Python as part of exploring this software, this is definitely a good thing to examine.

# Prepping Elasticsearch

Elasticsearch is an Absolute Unit to operate and scale up. There are about four dozen bash/curl scripts in our repo that do various things. These need to be updated so they use ~/.twitter for their auth, or to detect that you're running just Elaticsearch and do not have Search Guard.

If you are the technology person for your group, you're probably going to have to order Elasticsearch: The Definitive Guide by Clinton Gormley and Zachary Tong. It's 690 pages and it provides a solid reference to Elasticsearch _prior to version 7_. The platform is going to change dramatically in the next release; forewarned is forearmed. They'll update the book, but it won't be available immediately.

If you're going to collect a lot of data - 32 million user profiles are about 19 gig, 10 million tweets fill about 35 gig of disk space - you are going to get familiar with ZFS. The best resource on ZFS is FreeBSD Mastery: ZFS, with the **STRONG** caveat that device names and disk labels for Linux are **VERY** different. We'll publish some of our configs to help you get started.

# Collecting Some Tweets

tw-quser2work <file> - put a few Twitter account names in a file, this loads them to the Redis work queue.

tw-idu3elk - run from the command line, you'll see it fetch an account and store tweets in tw [index]

bonus - it'll also grab userids and put them in tu [index]

# Collecting Some User IDs

tw-quser2usertest <file> - put some Twitter account names in a file, this loads them to the right queue in Redis.

tw-queue2usertest - run from command line, it'll check its queue, then start processing accounts it finds there.

tw-1name <screen_name> will look up an account.

tw-tumsearch and tw-tnamesearch are used to audit big collections of account names or numeric IDs.

tw-follow2usertest will grab the numeric IDs of every follower of an account and place them in the Redis queue for processing.

# Explore Your Results With Kibana

Elasticsearch's default graphical front end is Kibana. This app runs on port tcp/5601 but all you need is to point a browser at it. There really aren't any good books on Kibana - we've looked and looked. Search YouTube for videos if you need hints. We've produced a few of our own ... but where are they? Link? Anyone? Bueller ... Bueller?

# Explore The Neo4j Data

You can point a browser at tcp/7474 and you'll find the Neo4j graph database. 