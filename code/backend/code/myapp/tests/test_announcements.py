from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student, Profile, Project
from django.test.client import Client
from .test_utils import post_request
import json 
import requests
import time
"""
python manage.py makemigrations
python manage.py migrate
"""
class test_annosProject(TestCase):   
    def setUp(self):
        self.user = student(name="testname", avatar= "test", email="test@jhu.edu", password= "123321", uid="-1")
        #self.user.uid = self.user.generate_key()
        self.user.save()
        print( 80*"-" + "\nPass setUp")
                 
    def test_annos(self):
        url = 'http://127.0.0.1:8000/annos_create_msg_api'
        self.client = Client()
        json_data = {
                        "name": "321",
                        "val": "projectName011 sdfsdfs projectName121"
                    }
        self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
        return_json = json.loads(self.response.content)
        time.sleep(1)
        url = 'http://127.0.0.1:8000/annos_create_msg_api'
        self.client = Client()
        json_data = {
                        "name": "321",
                        "val": "projectName001 projectName001 sdfsdf"
                    }
        self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
        return_json = json.loads(self.response.content)
        time.sleep(1)
        url = 'http://127.0.0.1:8000/annos_create_msg_api'
        self.client = Client()
        json_data = {
                        "name": "321",
                        "val": "dsdfsdf projectName001 projectName121"
                    }
        self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
        return_json = json.loads(self.response.content)
        time.sleep(1)
        url_queryProject = 'http://127.0.0.1:8000/annos_list_msg_api'
        json_data_queryProject = {
                        "HTTP_X_TOKEN": "-1",
                    }
        self.response = self.client.post(url_queryProject, json.dumps(json_data_queryProject), content_type="application/json")
        return_json = json.loads(self.response.content)

        url_queryProject = 'http://127.0.0.1:8000/annos_retrieve_msg_api'
        json_data_queryProject = {
                        "HTTP_X_TOKEN": return_json['announcements'][0]['id'],
                    }
        self.response = self.client.post(url_queryProject, json.dumps(json_data_queryProject), content_type="application/json")
        return_json = json.loads(self.response.content)