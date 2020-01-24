#!/usr/bin/env python3

import requests, json
import feedparser
from time import sleep

hook = ("Webhook URL") 

'''
If you created a feed for a user, it will look like this: https://twitrss.me/twitter_user_to_rss/?user=[USERNAME]

And if the feed is for a keyword / phrase or hash, it will look like this: http://twitrss.me/twitter_search_to_rss/?term=[SEARCH TERM]
http://twitrss.me/twitter_search_to_rss/?term=[SEARCH TERM]
'''


parse = feedparser.parse('https://twitrss.me/twitter_user_to_rss/?user=<username>') #for Twitter RSS feed of particular user
for i in parse.entries:
        l = (i.link)
        mess = {"text" : "{}".format(l)}
        response = requests.post(hook, headers={"Content-Type":"application/json"}, data= json.dumps(mess)) #posts to RockeChat Webhook
        
