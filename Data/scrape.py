import urllib3
import urllib
from bs4 import BeautifulSoup
import certifi
import csv
import json
import requests
# http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

# r = http.request('GET', 'https://www.youtube.com/channels/music')
# r = requests.get("https://www.youtube.com/channels/music")
# with open("MusicChannels.html","w") as fp:
#     fp.write(r.text)

# urllib.request.urlretrieve('https://www.youtube.com/user/TFhistory/videos?view=0&sort=dd&shelf_id=0',"data.html")
# d = {}
# l = []
# l.append("https://www.youtube.com/user/TFhistory/videos")
# l.append("https://www.youtube.com/user/BlastfromthePast/videos")
# l.append("https://www.youtube.com/user/Zztoph/videos")


urllib.request.urlretrieve('https://www.youtube.com/results?search_query=vevo&sp=EgIQAg%253D%253D&pbjreload=10',"MusicChannelsVevo.html")

with open("MusicChannelsVevo.html") as fp:
    soup = BeautifulSoup(fp,'html5lib')
    links = soup.find_all('a',{'dir':'ltr'})
    l = []
    for link in links:
        l.append(link['href'])
        print(link['href'])
    d={}
    d['urls'] = l
    with open("MusicChannelLinks.json","w") as fp:
        json.dump(d,fp,indent=4)

## Fetches video urls from channels
# with open("data.html", 'r') as fp:

#     soup = BeautifulSoup(fp,features="html5lib")
#     links = soup.find_all('a',{'dir':'ltr'})
#     l = []
#     for link in links:
#         l.append(link['href'])
#         print(link['href'])
#     d={}
#     d['urls'] = l
#     with open("links.json","w") as fp:
#         json.dump(d,fp,indent=4)