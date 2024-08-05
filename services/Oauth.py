import requests
import json
from flask import Flask, jsonify


class Oauth:
    def __init__(self):
        self.url = "https://freia.styrk.io"

    def tokenVerify(self, token):
        url = self.url + "/clients/api/v0/token/verify"


        headers = {
            'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data={})
        status = response.status_code

        return status

    def authorize(self, body):
        url = self.url + "/clients/api/v0/authorize"

        payload = json.dumps(body)

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def register(self, body):
        url = self.url + "/clients/api/v0/register"
        payload = json.dumps(body)

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()

    def verify(self, token):
        url = self.url + "/clients/api/v0/token/verify"

        payload = {}
        headers = {
            'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.json()


