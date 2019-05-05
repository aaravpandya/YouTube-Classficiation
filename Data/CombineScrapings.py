import json
import csv
l = []
d = {}
with open("HistoryScraped.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    tempList = []
    tempList.append(i["id"])
    tempList.append(i["title"])
    tempList.append(i["description"])
    tempList.append("History")
    l.append(tempList)

ctr = 0
for i in range(0,4):
    hdict = {}
    with open("VideoSnippets" + str(i)+".json","r") as fp:
        hdict = json.load(fp)
    for k in hdict:
        for innerDict in hdict[k]:
            tempList = []
            
            tempList.append(innerDict["id"].encode('ascii','ignore').decode("ascii"))
            
            title = innerDict["snippet"]["title"].encode('ascii','ignore').decode("ascii")
            if("game" in title):
                continue
            tempList.append(title)
            desc = innerDict["snippet"]["description"].encode('ascii','ignore').decode("ascii")
            if("game" in desc):
                continue
            tempList.append(desc)
            tempList.append("History")
            l.append(tempList)
    
with open("MusicScraped.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:

        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Music")
        l.append(tempList)
    except:
        continue
with open("MusicScraped2.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Music")
        l.append(tempList)
    except:
        continue

with open("FoodScraped.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Cooking")
        l.append(tempList)
    except:
        continue
with open("CookingScraped2.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Cooking")
        l.append(tempList)
    except:
        continue

with open("ManufacturingScraped.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Manufacturing")
        l.append(tempList)
    except:
        continue

with open("TechScraped.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Tech")
        l.append(tempList)
    except:
        continue


with open("TechScraped2.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Tech")
        l.append(tempList)
    except:
        continue

with open("TravelScraped.json", 'r') as fp:
    d = json.load(fp)
m = d["desc"]
for i in m:
    try:
        tempList = []
        tempList.append(i["id"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["title"].encode('ascii','ignore').decode('ascii'))
        tempList.append(i["description"].encode('ascii','ignore').decode('ascii'))
        tempList.append("Travel")
        l.append(tempList)
    except:
        continue


with open("output2.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(l)

