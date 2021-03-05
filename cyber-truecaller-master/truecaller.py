# Check how the app works (i.e truecaller) and start sending request until it crashes, making it maybe possible to exploit the phone. 
# This example is how truecaller app works, website may be different code
#!/usr/bin/python3
import requests
import json

phone = input("Enter Phone Number:")

url = "https://search5-noneu.truecaller.com/v2/search"

headers = {
        "User-Agent":"Insert User ID here"
	"Authorization":"Insert Authorization Here"
}

params = {
	"q":phone,
	"type": 4,
	"placement": "SEARCHRESULTS,HISTORY,DETAILS",
	"adId": "Insert ID here",
	"encoding": "json"
}

res = requests.get(url, params=params, headers=headers)
print(res.text)
jres = json.load(res.text)
print(jres['data'][0]['name'])
