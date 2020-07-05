import os
import json
import sys
from datetime import datetime


if len(sys.argv) > 2:
    journeyJSONDirectory = sys.argv[1]
    tiddlerDirectory = sys.argv[2]
else:
    print("Usage: python3 %s journeyJSONDirectory tiddlerDirectory" % (sys.argv[0]))
    sys.exit()

def ordinal(num):
     ldig = num % 10
     l2dig = (num // 10) % 10
     if l2dig == 1:
         suffix = 'th'
     elif ldig == 1:
         suffix = 'st'
     elif ldig == 2:
         suffix = 'nd'
     elif ldig == 3:
         suffix = 'rd'
     else: 
         suffix = 'th'
     return '%d%s' % (num, suffix)

files = os.listdir(journeyJSONDirectory)

for f in files: # Read through each JSON file & gather relevant info
  if(f.lower().endswith(('.json'))):
    with open(journeyJSONDirectory + '/' + f) as x:
      journey = json.load(x)
      
      res = {
        "text":'',
        "title":'',
        "tags":"Journal",
        "modified":'', #20200705064525178 YYYYMMDDHHMMSSmm
        "created": ''  
      }

      dt = datetime.utcfromtimestamp(int(journey["date_journal"])/1000)
      day = str(dt.strftime('%d'))
      res["title"] = ordinal(int(day)) + dt.strftime(' %B %Y') # #5th July 2020
      res["text"] = journey["text"]
      res["modified"] = str(dt.strftime('%Y%m%d%H%M%S'+'000'))
      res["created"] = res["modified"] 

    with open(tiddlerDirectory + '/' + res["title"] + '.json', 'w') as outfile:
      json.dump(res, outfile)

print("ALL DONE!!!")

# https://tiddlywiki.com/static/How%2520to%2520build%2520a%2520TiddlyWiki5%2520from%2520individual%2520tiddlers.html TO BUILD THE RESULTING TIDDLERS