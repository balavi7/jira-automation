# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://bala-works.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0qRNhHb2czNTROwowd_ZFHwPaqUepV0-gokiIEl4r0FvRBG9875QFPFXU5kCmL466PQ2K2jx38uWIBEDXiUw7WskwtZ8EzCebjUPAp5AcBdTChEVqZBa_L_c_23_MEW16XelX1vb2sc8kLvQIuxeSm_4qO0etWt33wSddLYjHlRM=21D4377A"

auth = HTTPBasicAuth("balavignesh715@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)

name = output[0]["name"]

print(name)