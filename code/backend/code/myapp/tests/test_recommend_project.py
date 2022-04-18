from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student, Profile, Project
from django.test.client import Client
from .test_utils import post_request
import json 
import requests


class test_recommendProject(TestCase):   
    def setUp(self):
        self.user = student(name="testname", avatar= "test", email="test@jhu.edu", password= "123321", uid="-1")
        #self.user.uid = self.user.generate_key()
        self.user.save()
        print( 80*"-" + "\nPass setUp")
                 
    def test_returnAllProject(self):
        url_queryProject = 'http://127.0.0.1:8000/recommend_project_api'
        client = Client()
        print(80*"-" + "\nTest login with created account")
        json_data = {
                    "HTTP_X_TOKEN" : "-1",
                    }
        response_json = post_request(client, "recommend_project_api", json_data)
        return response_json

