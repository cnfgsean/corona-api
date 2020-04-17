import requests
import json

def pp(d):
    print(json.dumps(d, indent=2))

api_url = "https://api.covid19api.com/"
response = requests.get(api_url)
r = response.json()
#pp(r)
#yeet

allCountries = requests.get(api_url + "countries").json()
#pp(allCountries)

summary = requests.get(api_url + "summary").json()
#pp(summary)

for x in summary["Countries"]:
    if x["CountryCode"] == "US":
        #print(x)
        pass

usInfo = requests.get(api_url + "/live/country/united-states/status/confirmed").json()
#print(usInfo)

print("Getting data from data file.")

with open('data.txt', 'r') as file:
     lastusInfo = file.readline()
     print("last info")
     print(lastusInfo)
print("got it.")

print("clearing past file")
# clear the file
open('data.txt', 'w').close()

with open('data.txt', 'w') as file:
     file.write(json.dumps(usInfo))
print("Wrote data to data.txt.")


