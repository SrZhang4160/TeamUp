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
        url = 'http://127.0.0.1:8000/create_project_api'
        print(80*"-" + "\nstart to create project")
        print(80*"-" + self.user.name)
        self.client = Client()
        json_data = {
                        "HTTP_X_TOKEN": "-1",
                        "projectName": "projectName",
                        "teamName" : "teamName",
                        "project_idea" : "project_idea",
                        "projectIntroduction" : "projectIntroduction",
                        "intendedLanguage" : ["c++", "java"],
                        "otherLanguage" : "otherLanguage",
                        "skillWanted": "skillWanted",
                        "keywords": "keywords"
                    }
        self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
        return_json = json.loads(self.response.content)
        print(return_json['msg'])

        url_queryProject = 'http://127.0.0.1:8000/recommend_project_api'
        print(80*"-" + "\nstart to recommend project")
        print(80*"-" + self.user.name)
        json_data_queryProject = {
                        "HTTP_X_TOKEN": "-1"
                    }
        self.response = self.client.get(url_queryProject, json.dumps(json_data_queryProject), content_type="application/json")
        return_json = json.loads(self.response.content)
        print(return_json)


