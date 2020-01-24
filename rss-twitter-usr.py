#!/usr/bin/env python3

import requests, json
import feedparser
from time import sleep

hook = ("Webhook URL") 

parse = feedparser.parse('https://twitrss.me/twitter_user_to_rss/?user=<username>') #for Twitter RSS feed of particular user
for i in parse.entries:
        l = (i.link)
        mess = {"text" : "{}".format(l)}
        response = requests.post(hook, headers={"Content-Type":"application/json"}, data= json.dumps(mess)) #posts to RockeChat Webhook
        
