import urllib3
import urllib
from bs4 import BeautifulSoup
import certifi
import csv
import json
# http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())


responses = {}
with open("TravelChannels3.json",'r') as fp:
       responses = json.load(fp)

#get descriptions from html scraped. titles are directly taken from the previous steps
ctr = 0
descriptions = []
for key in responses:
    l = responses[key]
    for item in l:
        try:
            videos = item["items"]
        except:
            continue
        for v in videos:
            try:
                description = {}
                videoid = v["id"]["videoId"]
                description["id"] = videoid
                urllib.request.urlretrieve('https://www.youtube.com/watch?v='+str(videoid),"vid.html")
                with open("vid.html") as fp:
                    soup = BeautifulSoup(fp,features='html5lib')
                    ptags = soup.find_all('p',{"id":"eow-description"})
                    for p in ptags:
                        description["description"] = p.text
                description["title"] = v["snippet"]["title"]
                print(description["title"])
                descriptions.append(description)
                ctr = ctr + 1
            except:
                continue
        d = {}
        d["desc"] = descriptions
        with open("TravelScraped2.json", 'w') as fp:
            json.dump(d,fp,indent=4)
        print(ctr)