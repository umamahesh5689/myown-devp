import requests
import json

response = requests.get("https://someapiurl.clom/api")
import json
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())
