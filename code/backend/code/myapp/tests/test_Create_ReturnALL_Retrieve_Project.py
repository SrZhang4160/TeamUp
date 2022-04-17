from django.test import TestCase
from django.test.client import RequestFactory
from myapp.models import User, student, Profile, Project
from django.test.client import Client
from .test_utils import post_request
import json 
import requests

class test_Create_ReturnALL_Retrieve_Project(TestCase):   
    def setUp(self, enable=True):
        if enable:
            self.user = student(name="testname", avatar= "test", email="test1@jhu.edu", password= "123321", uid="123")
            self.user.save()
            self.user = student(name="testname", avatar= "test", email="test3@jhu.edu", password= "123321", uid="321")
            self.user.save()
            print( 80*"-" + "\nPass setUp")
                    
    """
    Test project query
    
    Args
        input: {
                "projectId":"AAA"
                }
        outputs:
        {
            "code": 1,
            "msg": "获取成功",
            "userRole": 1,
            "project": {
                        "projectId": "aaa",
                        "projectName": "bbb",
                        "projectIntroduction": "XX",
                        "keywords": "CC",
                        "intendedLanguage": ["JAVA", "OTHER"],
                        "otherLanguage": "VUE",
                        "type": ["IOS"],
                        "skillWanted": "DDD",
                        "teamName": "aa",
                        "teamLeader": "AAA@jhu.edu",
                        "teamLeaderName": "AAA",
                        "teamMemName": [{
                                        "name": "bbb",
                                        "eml": "BBB@jhu.edu"
                                        },
                                        {
                                        "name": "ccc",
                                        "eml": "CCC@jhu.edu"
                                        }
                                        ]
                        }
        }
    """
    def test_queryProject(self, enable=True):
        if enable:
            url = 'http://127.0.0.1:8000/create_project_api'
            print(80*"-" + "\nstart to create project")
            print(80*"-" + self.user.name)
            self.client = Client()
            """Create test project 1"""
            json_data = {
                            "HTTP_X_TOKEN": "321",
                            "projectName": "projectName001",
                            "teamName" : "team1",
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
            """Create test project 2"""
            json_data = {
                            "HTTP_X_TOKEN": "123",
                            "projectName": "projectName002",
                            "teamName" : "team1",
                            "projectIntroduction" : "projectIntroduction xxx",
                            "intendedLanguage" : ["c++", "python"],
                            "otherLanguage" : "otherLanguage",
                            "skillWanted": "skillWanted",
                            "type": ["iOS","Web application"],
                            "keywords": "keywords2"
                        }
            self.response = self.client.post(url, json.dumps(json_data), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json['msg'])

            url_queryProject = 'http://127.0.0.1:8000/return_all_project_api'
            print(80*"-" + "\nstart to search project")
            print(80*"-" + self.user.name)
            json_data_queryProject = {
                            "HTTP_X_TOKEN": "-1",
                            "inputword": "",
                            "selectword":[]
                        }
            self.response = self.client.post(url_queryProject, json.dumps(json_data_queryProject), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            url_queryProject = 'http://127.0.0.1:8000/project_lang_distribution_api'
            print(80*"-" + "\nstart to search project")
            print(80*"-" + self.user.name)
            json_data_queryProject = {
                            "HTTP_X_TOKEN": "-1",
                        }
            self.response = self.client.post(url_queryProject, json.dumps(json_data_queryProject), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            """Test"""
            url_queryProject = 'http://127.0.0.1:8000/return_all_project_api'
            print(80*"-" + "\nstart to search project")
            print(80*"-" + self.user.name)
            json_data_queryProject = {
                            "HTTP_X_TOKEN": "-1",
                            "inputword": "keywords1",
                            "selectword":["iOS"]
                        }
            self.response = self.client.post(url_queryProject, json.dumps(json_data_queryProject), content_type="application/json")
            return_json = json.loads(self.response.content)
            print(return_json)

            """Test project query"""
            url_queryProject = 'http://127.0.0.1:8000/project_page_api'
            print(80*"-" + "\nstart to search project")
            print(80*"-" + self.user.name)
            for project in return_json['projectList']:
                json_data = {
                                "HTTP_X_TOKEN": "321",
                                "projectId": project['projectId']
                            }
                self.response = self.client.post(url_queryProject, json.dumps(json_data), content_type="application/json")
                return_json = json.loads(self.response.content)
                print(return_json)