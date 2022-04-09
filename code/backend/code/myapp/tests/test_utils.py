from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student,Profile
from django.contrib.auth import authenticate, login, logout
from django.test.client import Client
import json 
import os 
import requests

base_url = "http://127.0.0.1:8000"
 
def post_request(client, request_url, data):
    access_url = os.path.join(base_url, request_url)
    response = client.post(access_url, json.dumps(data), content_type="application/json")
    response_json = json.loads(response.content)
    print(80*"-" + "\n" + response_json['msg'])
    if "error" in response_json['msg']:
        print(80*"-" + "\n  FAIL")
    return response_json