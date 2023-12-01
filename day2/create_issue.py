# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://bala-works.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0qRNhHb2czNTROwowd_ZFHwPaqUepV0-gokiIEl4r0FvRBG9875QFPFXU5kCmL466PQ2K2jx38uWIBEDXiUw7WskwtZ8EzCebjUPAp5AcBdTChEVqZBa_L_c_23_MEW16XelX1vb2sc8kLvQIuxeSm_4qO0etWt33wSddLYjHlRM=21D4377A"

auth = HTTPBasicAuth("balavignesh715@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "AUT"
    },
    "issuetype": {
      "id": "10001"
    },
    "summary": "second JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

