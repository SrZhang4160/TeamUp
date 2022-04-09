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
class test_project_page_view_edit(TestCase):   
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
    
    @pytest.mark.django_db(transaction=True)
    def test_queryProject(self, enable=True):
        if enable:
            url = 'http://127.0.0.1:8000/create_project_api'
            print(80*"-" + "\nstart to create project")
            print(80*"-" + self.user.name)
            self.client = Client()
 
            json_data = {
                            "HTTP_X_TOKEN": "321",
                            "projectName": "projectName001",
                            "teamName" : "team1",
                            "teamMemName": "",
                            "projectIntroduction" : "projectIntroduction xxx",
                            "intendedLanguage" : ["c++", "java"],
                            "otherLanguage" : "otherLanguage",
                            "skillWanted": "skillWanted",
                            "type": ["iOS","Android"],
                            "keywords": "keywords1"
                        }
            self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json['msg'])

            test_url = 'http://127.0.0.1:8000/return_all_project_api'
            data = {
                            "HTTP_X_TOKEN": "-1",
                            "inputword": "",
                            "selectword":[]
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json_0 = json.loads(self.response.content)
            print(return_json)

            test_url = 'http://127.0.0.1:8000/apply_to_project_api'
            data = {
                            "HTTP_X_TOKEN": "123",
                            "projectId": return_json_0['projectList'][-1]['projectId']
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            test_url = 'http://127.0.0.1:8000/project_page_view_api'
            data = {
                            "HTTP_X_TOKEN": "321",
                            "projectId": return_json_0['projectList'][-1]['projectId']
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            test_url = 'http://127.0.0.1:8000/project_page_api'
            data = {
                            "HTTP_X_TOKEN": "321"
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            test_url = 'http://127.0.0.1:8000/project_page_api'
            data = {
                            "HTTP_X_TOKEN": "321",
                            "projectId": return_json_0['projectList'][-1]['projectId']
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            test_url = 'http://127.0.0.1:8000/project_page_edit_api'
            data = {
                    "HTTP_X_TOKEN": "321",
                    "projectId": return_json_0['projectList'][-1]['projectId'],
                    "projectName": return_json_0['projectList'][-1]['projectName'],
                    "projectIntroduction":"CC",
                    "keywords":"CC",
                    "intendedLanguage":["JAVA","OTHER"],
                    "otherLanguage":"VUE",
                    "type":["IOS"],
                    "skillWanted":"DDD",
                    "teamName":"aa",
                    "teamMemName":[{
                                    "name": "",
                                    "eml": "D@jhu.edu"
                                    }, 
                                    {
                                    "name": "",
                                    "eml": "E@jhu.edu"
                                    }]
                    
                    }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            test_url = 'http://127.0.0.1:8000/project_page_exit_api'
            data = {
                            "HTTP_X_TOKEN": "321",
                            "projectId": return_json_0['projectList'][-1]['projectId']
                        }
            self.response = self.client.post(test_url, json.dumps(data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)


