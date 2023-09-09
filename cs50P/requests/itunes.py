"""cs50p 9/9/2023 the requests thrid party package that
allow us connect to API's"""
import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
# print(json.dumps(response.json(), indent=4))
o = response.json()
for result in o["results"]:
    print(result["trackName"])
