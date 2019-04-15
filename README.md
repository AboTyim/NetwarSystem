# Netwar System Twitter Recorder

This is the prime repository for our Twitter related code. There are four major functions that this system provides.

* Bulk capture of Twitter account timelines.
* Bulk capture of Twitter user profiles.
* Persistent tracking based on a user's lists.
* Capture streams based on userids or search terms.

The following are the major Python dependencies:

* This software requires Python 3.
* [Walrus](https://walrus.readthedocs.io/en/latest/) - provides a Python objects layer over Redis.
* Elasticsearch 6.3.1 for Python (yes, 6.3.1 of this software, not 6.5.4)
* Py2neo Neo4j client.
* [Tweepy](http://www.tweepy.org/) Twitter API access for Python.

The following are infrastructure dependencies.

* [Redis](http://redis.io) - provides shared Python objects, used for various work queues.
* [Elasticsearch](http://elastic.co) 6.5.4 - searchable archive of text data.
* [Search Guard](http://search-guard.com) - Elasticsearch security, needed for teams and/or public access.
* [Neo4j](http://neo4j.com) - graph database for storing Twitter interactions, new as of 3/2019.
* [Netdata](https://github.com/netdata/netdata) - system monitor, which with you will become familiar.

Elasticsearch and Redis/Walrus were the first things implemented, then Search Guard, and we have barely scratched the surface with Neo4j. There are significant changes from Elasticsearch 6.5.4 to 6.7.0, and even more dramatic changes to 7.x. We have a ELK7 prototype, but it's nowhere near ready. We can not support this software on anything but 6.5.x at this time.

# System Requirements

When we first successfully ran this system it was on a small desktop:

* intel i7-2820QM - cpumark 6640.
* 32 gig of ram.
* 120 gig SSD, 32 gig for OS, remainder for zfs caching.
* 500 gig spindle used for ZFS storage.

This machine is still around for testing, but is limited to four to eight accounts, which exercises it heavily. if you don't have room for two drives, you definitely need an SSD for this system, even at small scale. Sixteen gig would be enough for a handful of accounts.


Our current setup is a pair of machines with these specs:

* Dual Xeon E5-2680v1 eight core processors - combined cpumark 25,000 on each.
* 192 gig of ram.
* 500 gig SSD, half for OS, half for ZFS cache.
* Pairs of Seagate IronWolf 2TB NAS drives.

This configuration has supported sixty four accounts doing bulk collection of tweets or users, while simultaneously running 16 stream captures. Each machine runs three VMs that store the data. This requires a bit of hand waving to explain, but it positions us to grow beyond two physical machines when we need to do so.

Note the qualifier 'successfully' up there. We had a couple of VPS environments and what we've found is that Elasticsearch will always find a way to misbehave unless you have positive control over drive channel tuning. Our VM configuration works because we don't oversubscribe memory or processors, and we have a rockin' disk subsystem. If you post a question about performance troubles in a cloud implementation, we're just going to thank you for confirming our early experiences.

# Installation

* Do a git clone of this archive.
* Try pip install -r REQUIREMENTS.txt
* Look at pipfreeze.txt to see what was actually running on 13 Apr 2019.
* Clone [TwitterUtils](https://github.com/NetwarSystem/TwitterUtils, which has some useful bits from our pre-Elastic software.
* Do a git clone of the [ELKSG](https://github.com/NetwarSystem/ELKSG) archive, which has Elastic setup/tuning stuff in it.
* Install Elasticsearch 6.5.4.
* Install Redis.
* Install Neo4j.
* Install Netdata monitoring software.
* Look at example.conf to see how a client is configured. You MUST have your own Twitter API keys.
* Look at crontab.txt to see how observer accounts, bulk tweets, and bulk userids are collected.
* Copy the code to /usr/local/bin, then chmod 755 so it's executable.

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

If you're going to collect a lot of data - 32 million user profiles are about 19 gig, 10 million tweets fill about 35 gig of disk space - you are going to get familiar with ZFS. The best resource on ZFS is [FreeBSD Mastery: ZFS](https://www.amazon.com/FreeBSD-Mastery-ZFS-Book-ebook/dp/B00Y32OHNM/ref=sr_1_1), with the **STRONG** caveat that device names and disk labels for Linux are **VERY** different. We'll publish some of our configs to help you get started.

# Collecting Some Tweets

tw-quser2work <file> - put a few Twitter account names in a file, this loads them to the Redis work queue.

tw-idu3elk - run from the command line, you'll see it fetch an account and store tweets in tw {index}

bonus - it'll also grab userids and put them in tu {index}

# Collecting Some User IDs

tw-quser2usertest file.txt - put some Twitter account names in a file, this loads them to the right queue in Redis.

tw-queue2usertest - run from command line, it'll check its queue, then start processing accounts it finds there.

tw-1name screen_name will look up an account.

tw-tumsearch and tw-tnamesearch are used to audit big collections of account names or numeric IDs.

tw-follow2usertest will grab the numeric IDs of every follower of an account and place them in the Redis queue for processing.

# Explore Your Results With Kibana

Elasticsearch's default graphical front end is Kibana. This app runs on port tcp/5601 but all you need is to point a browser at it. There really aren't any good books on Kibana - we've looked and looked. Search YouTube for videos if you need hints. We've produced a few videos of our own ... but where are they? Link? Anyone? Bueller ... Bueller?

# Explore The Neo4j Data

You can point a browser at tcp/7474 and you'll find the Neo4j graph database.

I've you've never touched a graph database before, [Learning Neo4j 3.x](https://www.amazon.com/Learning-Neo4j-3-x-performance-visualization/dp/1786466147/ref=sr_1_fkmrnull_1_sspa) by Jerome Baton & Rik Van Bruggen was a pretty good read. The O'Reilly [Graph Databases](https://www.amazon.com/Graph-Databases-Opportunities-Connected-Data-ebook/dp/B00ZGRS4VY/ref=sr_1_3) book by Ian Robinson, Jim Webber, and Emil Eifrem speaks to a higher level of mastery - assuming the reader has SQL experience and needs to make a transition to using Neo4j.

We looked at a variety of tools for visualizing graph data, and we are amazed and pleased with [Graphileon](http://graphileon.com), which has a free community edition, good instructional videos, and as a bonus it has some support for Elasticsearch, too.

# Errata & Obscura

* [Redis](https://redis.io/) is doing its own work and it's also handling some of [RabbitMQ](https://rabbitmq.com)'s natural tasks as well. [RabbitMQ In Depth](https://www.amazon.com/RabbitMQ-Depth-Gavin-M-Roy/dp/1617291005/ref=sr_1_fkmrnull_1) by Gavin M. Roy is on order and that package should become part of the system over Q2 of 2019.

* Some of this software still gets run under the [tmux](https://github.com/tmux/tmux) terminal multiplexer utility. We add the logging plugin and use it to capture output.

* The perflog index is a general purpose logging feature that is not very mature, mostly because tmux is expedient.

* Cron was a fantastic idea when it first came out, but bell bottoms were in style, too. We have been at the reading stage of evaluating new software and [supervisord](http://supervisord.org) seems to be the best choice for an upgrade.

* We have used the [Gephi](http://gephi.org) data visualization package for a long time and our older flat file software automatically produced outputs for it. We do some ad hoc tool chaining to produce similar files now. This has to be maintained since Gephi is the only _gratis_ package available to do this kind of work.


# Support 

* If it should run but doesn't, post an [issue](https://github.com/NetwarSystem/TwitterRecorder/issues), bonus points awarded for logs, stack traces, etc.

* If you think it should run, but you aren't precisely sure, the [NetwarSystem](http://netwarsystem.slack.com) Slack server is the best route

