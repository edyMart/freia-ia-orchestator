import requests
import json
from flask import Flask, jsonify


class BillingService:
    def __init__(self):
        self.url = "/billing/api/v0"

    def tokenVerify(self, token):
        url = self.url + "/create/billing"


        headers = {
            'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data={})
        status = response.status_code

        return status

