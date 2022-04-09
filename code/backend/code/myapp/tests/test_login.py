from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student
from django.contrib.auth import authenticate, login, logout
from django.test.client import Client

from .test_utils import post_request

class SigninTest(TestCase):
    def setUp(self, enable=False):
        if enable:
            user = student(name="testname", avatar= "test", email="test@jhu.edu", password= "123321")
            user.uid = user.generate_key()
            user.save()        
        
    def test_login_logout(self):
        client = Client()
        json_data = {
                    "email": "test@jhu.edu",
                    "password": "123321"
                    }
        response_json = post_request(client, "login-test", json_data)
 
        if "Successfully" not in response_json["msg"]:
            print(80*"-" + "\nCreate account")
            self.setUp(enable=True)

        print(80*"-" + "\nTest login with created account")
        json_data = {
                    "email": "test@jhu.edu",
                    "password": "123321"
                    }
        response_json = post_request(client, "login-test", json_data)
 
        json_data = {
                    "email": "test1@jhu.edu",
                    "password": "2222"
                    }
        response_json = post_request(client, "login-test", json_data)
        
        json_data = {
                    "name": "testname",
                    "token": "111111111111111",
                    }
        response_json = post_request(client, "logout-test", json_data)

