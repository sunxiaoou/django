import json
from pprint import pprint

import requests

from django.test import TestCase


# Create your tests here.
class DrfTestCase(TestCase):
    def setUp(self) -> None:
        self.base_url = "http://127.0.0.1:8000"
        url = f"{self.base_url}/login/"
        payload = json.dumps({
            "username": "sun_xo",
            "password": "sun_xo"
        })
        headers = {
            'X-CSRFtoken': 'pNkL6P7qNlUAI6gkMm0VW92zduIpQhR7KIHzLc9MmZ74eODHRTw6BNSqi60e6dcA',
            'Content-Type': 'application/json',
            'Cookie': 'csrftoken=Kh2Zco1ifK5PjYC7jk1f6Qi1r7bWvh2t'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        self.csrf_token = response.json()['token']
        print("csrf_token(%s)" % self.csrf_token)

    def test_list_books(self):
        print("Test - list books")
        url = f"{self.base_url}/books/api/"
        headers = {
            'x-csrftoken': self.csrf_token
        }
        response = requests.request("GET", url, headers=headers, data={})
        response.raise_for_status()
        pprint(response.json()['data'])

    def test_show_book_info(self):
        print("Test - show book info")
        url = f"{self.base_url}/book/api/1"
        headers = {
            'x-csrftoken': self.csrf_token
        }
        response = requests.request("GET", url, headers=headers, data={})
        response.raise_for_status()
        print(response.json()['data'])

