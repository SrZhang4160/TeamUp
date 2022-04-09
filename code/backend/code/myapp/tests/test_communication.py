from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student, Profile, Project
from django.test.client import Client
from .test_utils import post_request
import json 
import pytest
from django.db import transaction

"""
python manage.py makemigrations
python manage.py migrate
"""
class test_communication(TestCase):   
    def setUp(self, enable=True):
        if enable:
            self.user = student(name="testname1", avatar= "test", email="test1@jhu.edu", password= "123321", uid="123")
            self.user.save()
            self.user = student(name="testname2", avatar= "test", email="test2@jhu.edu", password= "123321", uid="321")
            self.user.save()
            self.user = student(name="testname3", avatar= "test", email="test3@jhu.edu", password= "123321", uid="456")
            self.user.save()
            self.user = student(name="testname4", avatar= "test", email="test4@jhu.edu", password= "123321", uid="654")
            self.user.save()
            print( 80*"-" + "\nPass setUp")

    def test_create_student_api(self, json_data=None, enable=False):
        if enable:
            client = Client()
            if json_data is None:
                json_data = {
                            "name": "testname",
                            "avatar": "test",
                            "email": "test@jhu.edu",
                            "password": "123321"
                            }
            response_json = post_request(client, "create_student_api", json_data)
            return response_json
        else:
            pass

    @pytest.mark.django_db(transaction=True)
    def test_sent_msg(self, enable=True):
        if enable:
            client = Client()
            json_data = {
                        "email": "admin",
                        "password": "123456"
                        }
            response_json = post_request(client, "login-test", json_data)
    
            if "Successfully" not in response_json["msg"]:
                print(80*"-" + "\nCreate account")
                json_data = {
                            "name": "admin",
                            "avatar": "test",
                            "email": "test@jhu.edu",
                            "password": "123456"
                            }
                response_json = self.test_create_student_api(json_data, enable=True)

            print(80*"-" + "\nTest login with created account")
            json_data = {
                        "email": "test@jhu.edu",
                        "password": "123456"
                        }
            _response_json = post_request(client, "login-test", json_data)

            url = 'http://127.0.0.1:8000/send_message_api'
            self.client = Client()
 
            json_data = {
                        "HTTP_X_TOKEN": _response_json['token'],
                        "sendTo":"test1@jhu.edu",
                        "sendMessage":"HELLO…… best"
                        }
            self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json['msg'])

            test_url = 'http://127.0.0.1:8000/retrieve_contact_api'
            data = {
                        "HTTP_X_TOKEN": _response_json['token']
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json_0 = json.loads(self.response.content)
            print(return_json)
 
            test_url = 'http://127.0.0.1:8000/retrieve_message_api'
            data = {
                        "HTTP_X_TOKEN": _response_json['token'],
                        "email":"test1@jhu.edu",
                        "page":1,
                        "size":20
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json_0 = json.loads(self.response.content)
            print(return_json)

            json_data = {
                        "HTTP_X_TOKEN": _response_json['token'],
                        "sendTo":"test2@jhu.edu",
                        "sendMessage":"HELLO…… best"
                        }
            self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json['msg'])

