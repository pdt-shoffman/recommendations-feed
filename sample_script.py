#Here is a sample pythong script to trigger change events
import requests
import json
from datetime import datetime
from pytz import timezone



url = "https://events.pagerduty.com/v2/change/enqueue"
events_url = "https://events.pagerduty.com/v2/enqueue"



#today = datetime.now()
today = datetime.now(timezone('UTC'))
timestamp = today.isoformat()
print(timestamp)

payload = { 
  "routing_key": "KEY",
  "payload": {
    "summary": "valramirez pushed branch master from recommendations-engine",
    "source": "GitHub",
      "timestamp": timestamp,
    "custom_details": {
      
    }
  }
}


payload2 = { 
  "routing_key": "KEY",
  "payload": {
    "summary": "Puppet run for master-srf03-sfprod",
    "timestamp": timestamp,
    "source": "puppet",
    "custom_details": {
    }
  }
}


payload3 = { 
  "routing_key": "KEY",
  "payload": {
    "summary": "Build Successful: Merge pull request #42 from recommendations-feed",
    "timestamp": timestamp,
    "source": "buildkite",
    "custom_details": {
    }
  }
}

feed_payload = { 
  "routing_key": "KEY",
  "event_action": "trigger",
  "payload": {
    "summary": "High number of feed requests timing out",
    "source": "Sumo",
    "severity": "critical",
    "custom_details": {
      "service": "Recommendations feed"
    }
  }
}



headers = {
    'accept': "application/vnd.pagerduty+json;version=2",
    'content-type': "application/json",
    'authorization': "Token token=LtVEG3-y34vuh64pCvW2"
    }

response = requests.request("POST", url, headers=headers,data=json.dumps(payload))
response2 = requests.request("POST", url, headers=headers,data=json.dumps(payload2))
response2 = requests.request("POST", url, headers=headers,data=json.dumps(payload3))
response3 = requests.request("POST", events_url, headers=headers,data=json.dumps(feed_payload))


