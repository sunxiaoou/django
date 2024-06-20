import json
from pprint import pprint

import requests

from django.test import TestCase


class DrfTestCase(TestCase):
    base_url = "http://127.0.0.1:8000"
    csrf_token = None
    last_id = -1

    @classmethod
    def setUpTestData(cls) -> None:
        url = f"{cls.base_url}/login/"
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
        cls.csrf_token = response.json()['token']
        print("csrf_token(%s)" % cls.csrf_token)

        url = f"{cls.base_url}/books/api/"
        headers = {
            'x-csrftoken': cls.csrf_token
        }
        response = requests.request("GET", url, headers=headers, data={})
        response.raise_for_status()
        books = response.json()['data']
        cls.last_id = max([book['id'] for book in books])
        print("last_id(%d)" % cls.last_id)

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

    def test_add_book(self):
        print("Test - add book")
        url = f"{self.base_url}/books/api/"
        payload = json.dumps({
            "title": "镜之孤城",
            "price": "56.00",
            "pub_date": "2020-04-01"
        })
        headers = {
            'Content-Type': 'application/json',
            'x-csrftoken': self.csrf_token
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.text)

    def test_delete_book(self):
        print("Test - delete book")
        url = f"{self.base_url}/book/api/" + str(self.last_id)
        headers = {
            'x-csrftoken': self.csrf_token
        }
        response = requests.request("DELETE", url, headers=headers, data={})
        print(response.text)

    def test_modify_book(self):
        print("Test - modify book")
        url = f"{self.base_url}/book/api/3"
        payload = json.dumps({
            "title": "夜晚的潜水艇",
            "price": "52.00",
            "pub_date": "2020-09-09"
        })
        headers = {
            'Content-Type': 'application/json',
            'x-csrftoken': self.csrf_token
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        response.raise_for_status()
        print(response.text)
