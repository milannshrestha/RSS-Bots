#!/usr/bin/env python3

import requests, json
import feedparser
from time import sleep

hook = ("Webhook URL") #cort
parse = feedparser.parse('https://www.reddit.com/r/<subreddit>.rss')
for i in parse.entries:
        l = (i.link)
        mess = {"text" : "{}".format(l)}
        response = requests.post(hook, headers={"Content-Type":"application/json"}, data= json.dumps(mess)) #RSS feed for Sub Reddit



