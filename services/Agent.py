import requests
import json
class Agent:
    def __init__(self):
        self.url = "https://freia.styrk.io/agent/api/v0"
    def description(self, body):
        url = self.url + "/products/description"

        payload = json.dumps(body)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)


        return response.json()

    def regionalize(self, body):
        url = self.url + "/regionalize"

        payload = json.dumps(body)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def spellcheck(self, body):
        url = self.url + "/spellcheck"

        payload = json.dumps(body)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def images_description(self, body):
        url = self.url + "/images/description"

        payload = json.dumps(body)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def products_img(self, body):
        url = self.url + "/products/img"
        
        payload = json.dumps(body)
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()