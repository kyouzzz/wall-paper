#encoding=utf8

import urllib2
import json
import os
from urllib2 import HTTPError, URLError

folder_path = "/Users/kyou/Pictures/background/";
bg_api = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
try:
    req = urllib2.Request(bg_api, None)
    response = urllib2.urlopen(req)
    result = json.loads(response.read())
    img_url = result['images'][0]['url'];
    # img_url = img_url.replace("1920x1080", "1920x1200");

    name = img_url.split('/')[-1];
    startdate = result['images'][0]['startdate'];
    new_name = startdate + "_" + name

    pic_req = urllib2.Request(img_url, None)
    pic_req = urllib2.urlopen(pic_req)


    os.system("find %s  -type f -exec mv {} /Users/kyou/Pictures/backups/ \; " % (folder_path))

    f = open(folder_path + new_name,'wb')  
    f.write(pic_req.read());
except urllib2.URLError, e:
    print e.reason
