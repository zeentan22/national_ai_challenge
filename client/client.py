# test client for http requests

import requests
import os

class Client:
    def __init__(self, base_url):
        self.base = base_url

    def get(self, endpoint):
        endpoint = os.path.join(self.base, endpoint)
        r = requests.get(endpoint)
        return r.json()

    def post(self, endpoint, data):
        endpoint = os.path.join(self.base, endpoint)
        r = requests.post(endpoint, json=data)
        return r.json()

if __name__ == "__main__":
    client = Client(base_url="http://127.0.0.1:8000/")
    resp = client.post("api/sentiment/", data={"user_input": "This is a sample input string!"})

    print(resp)
