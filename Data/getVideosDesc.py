import requests
import json

url = "https://www.googleapis.com/youtube/v3/channels"
key ="AIzaSyBtIIMV0bKymmTAEjW9m7HWHKMx1jOGQjQ"

links = {}
with open("ChannelLinks.json", 'r') as fp:
    links = json.load(fp)
print(links)
d = {}

# get channel info from username and channel id
for l in links['urls']:
    if(l[0] == 'U'):
        querystring = {"key":key,"part":"snippet","id":l}
        response = requests.request("GET", url,params=querystring)
        d[l] = json.loads(response.text)
        continue
    querystring = {"key":key,"part":"snippet","forUsername":l}
    response = requests.request("GET", url,params=querystring)
    d[l] = json.loads(response.text)

with open("ChannelSnippets.json", 'w') as fp:
    json.dump(d,fp,indent=4)
d={}
with open("ChannelSnippets.json", 'r') as fp:
    d = json.load(fp)

# list all the videos in a particular channel
ctr = 0
channeltovideos = {}
videoResponse = {}
for k in d:
    print(d[k])
    url = "https://www.googleapis.com/youtube/v3/search"
    l = []
    responses = []
    item = d[k]["items"][0]
    id = item["id"]
    print(item["snippet"]["title"])
    querystring = {"order":"date","part":"snippet","channelId":id,"maxResults":"50","key":key}
    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    responses.append(response)

    try:
        while True:
            nextPageToken = response["nextPageToken"]
            querystring = {"order":"date","part":"snippet","channelId":id,"maxResults":"50","key":key,"pageToken":nextPageToken}
            response = requests.request("GET", url, params=querystring)
            response = json.loads(response.text)
            responses.append(response)
            print("Next Page")
    except Exception as e: 
        print(e)
    videoResponse[id] = responses
    with open("VideoSnippets.json",'w') as fp:
        json.dump(videoResponse,fp,indent=4)
    # # Get video info for each video. Couldnt do this since youtube's api limits requests to 10000.
    # for resp in responses:
    #     r = resp
    #     url = "https://www.googleapis.com/youtube/v3/videos"
    #     for item in r['items']:
    #         try:
    #             videoid = item['id']['videoId']
    #         except:
    #             continue
    #         querystring = {"part":"snippet","id":videoid,"key":key}
    #         response = requests.request("GET", url, params=querystring)
    #         j = json.loads(response.text)
    #         videodetails = j["items"][0]
    #         l.append(videodetails)    
    # channeltovideos[id] = l
    
    # with open("VideoSnippets"+str(ctr)+".json", 'w') as fp:
    #     json.dump(channeltovideos,fp,indent=4)
    # ctr = ctr + 1


