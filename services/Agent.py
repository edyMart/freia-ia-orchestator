import requests
import json
class Agent:
    def __init__(self):
        print("")
    
    def description(self, body):
        url = "https://freia.styrk.io/agent/api/v0/products/description"

        payload = json.dumps(body)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)


        return response.json()



