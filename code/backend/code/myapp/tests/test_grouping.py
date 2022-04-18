from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student,Profile
from django.contrib.auth import authenticate, login, logout
from django.test.client import Client

from .test_utils import post_request


class UserTest(TestCase):
    def setUp(self, enable=False):
        if enable:
            self.user = student(name="testname", avatar= "test", email="test@jhu.edu", password= "123321",uid ='-1')
            print(self.user.profile)
            self.user.save()
            self.user = student(name="testname", avatar= "test", email="test@jhu.edu", password= "123321",uid ='-1')
            self.user = student(name="testname", avatar= "test", email="test@jhu.edu", password= "123321",uid ='-1')

    def test_new_user(self):
        client = Client()
        json_data = {
            "name": "testname",
            "avatar": "test",
            "email": "test@jhu.edu",
            "password": "123321"
        }
        response_json = post_request(client, "create_student_api", json_data)
        return response_json

class ProfileTest(TestCase):
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

    def test_create_login_fill_group(self, return_json=None, enable=True):
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
            json_data = {
                        "name": "admin",
                        "major": "123456", 
                        "skillLevel": [{"skillName":"JAVA","level":"LOW"}, {"skillName":"C++","level":"HIGH"}],
                        "leadInt": "Yes",
                        "grade" : "Graduate",
                        "fieldInt" : ["XX","YY"],
                        "prod" : "NA",
                        "exep" : "NA",
                        "mbti": "NA",
                        "prefer" : "prefer@jhu.edu",
                        "preferNot" : "preferNot@jhu.edu",
                        "HTTP_X_TOKEN" : _response_json['token'] #frond end saved user.uid and will send this uid every time when send data to back end
                        }
            response_json = post_request(client, "fill_profile_api", json_data)

            json_data = {
                        "HTTP_X_TOKEN" : _response_json['token'] #frond end saved user.uid and will send this uid every time when send data to back end
                        }
            response_json = post_request(client, "query_profile_api", json_data)

            json_data = {
                        "userDetails":{
                                        "name":"SAN ZHANG",
                                        "major":"COMPUTER SCIENCE",
                                        "grade":"GRAD",
                                        "skillLevel":[
                                                        {"skillName":"JAVA","level":"LOW"},
                                                        {"skillName":"C++","level":"HIGH"}
                                                        ],
                                        "leadInt":"HIGH",
                                        "fieldInt":["XX","YY"],
                                        "prod":"WEB",
                                        "exep":"intern",
                                        "mbti":"estj-T",
                                        "prefer" : "aaa@jhu.edu",
                                        "preferNot" :  "aaa@jhu.edu",
                                        "email":"YYY@JHU.EDU"
                                        },
                        "HTTP_X_TOKEN" : _response_json['token']
                        }
            response_json = post_request(client, "update_profile_api", json_data)

            print(80*"-" + "\nTest login with created account")
            json_data = {
                        "HTTP_X_TOKEN" : "-1",
                        }
            response_json = post_request(client, "criteria_group_page_api", json_data)
            return response_json