from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, instructor, student, Profile, Project, criteria
from django.test.client import Client
from .test_utils import post_request
import json 
import requests
import pytest
from django.db import transaction

class test_criteria(TestCase):   
    def setUp(self, enable=True):
        if enable:
            self.user = instructor(name="testname", avatar= "test", email="test@jhu.edu", password= "123321", uid="-1")
            #self.user.uid = self.user.generate_key()
            self.user.save()
            print( 80*"-" + "\nPass setUp")
    
    @pytest.mark.django_db(transaction=True)            
    def criteria_page(self, enable=True):
        if enable:
            url = 'http://127.0.0.1:8000/criteria_page_api'
            print(80*"-" + "\ncriteria page first time")
            print(80*"-" + self.user.name)
            self.client = Client()
            json_data = {
                            "HTTP_X_TOKEN": "-1",
                            "isTemp": 0
                        }
            self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json['msg'])
            
            url = 'http://127.0.0.1:8000/criteria_page_api'
            print(80*"-" + "\ncriteria page second time")
            print(80*"-" + self.user.name)
            json_data = {
                            "HTTP_X_TOKEN": "-1",
                            "isTemp": 0
                        }
            self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json['msg'])

        