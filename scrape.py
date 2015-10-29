#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import requests
import json
import io
from datetime import datetime
from bs4 import BeautifulSoup

# Restaurant
restaurants = []

# domain url
domain = "http://www.ipeen.com.tw"
url = domain + "/taipei/channel/F?p=1&id=F&so=cdate&soway=d"

# html content
html = requests.get(url)

# bs Object
bsObj = BeautifulSoup(html.text, "html.parser")

# Find All Restaurant
firstObj = bsObj.findAll("div",{"class":"newcmm_cmm_main"})
for link in firstObj:
    temp = link.find(class_="cmm_read_title_area").find(class_="cmm_read_title_name").find("a")
    created_time = link.find(class_="cmm_read_time").text
    img_url = link.find(class_="cmm_read_pic").find("img")["src"]
    resObj = {"url": domain + temp["href"], "title": temp.text, "comment_id": temp["href"][9:], "created_time": created_time, "img_url": img_url}
    restaurants.append(resObj)

# create a new json to data/
data = ""
with io.open("data/"+(datetime.now()).strftime("%Y%m%d-%H:%M:%S")+".json", "w+", encoding="utf-8") as outfile:
    data = json.dumps(restaurants, ensure_ascii=False, indent=4)
    outfile.write(unicode(data))

# overwrite restaurant.json
with io.open("restaurant.json", "w+", encoding="utf-8") as outfile:
    outfile.write(unicode(data))

# Output Save all Restaurant with Url
print datetime.now()
for res in restaurants:
    print "Found Restaurant:(" + res["comment_id"] + ") " + res["title"]
