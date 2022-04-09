from django.http import HttpResponse, JsonResponse
from .models import student, User, Project
from .msg import *
import json
import re

# Dummy return_all_project --> to be modified
def return_all_project(request):
    try:
        req = json.loads(request.body)
        
        # if request.environ.get('HTTP_X_TOKEN') is not None:
        try:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        except:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN'] 
        
        try:
            # current dummy search: with no inputword and selectword
            all_projects = Project.objects.values()  
                       
            if req['inputword'] == '' and req['selectword'] == []:
                dummpy_project0 = {
                                    "projectId":"aaa",
                                    "projectName":"bbb",
                                    "keywords":"CC",
                                    "type":["IOS","Android"],
                                    "skillWanted":"DDD"
                                    }
                dummpy_project1 = {
                                    "projectId":"AAA",
                                    "projectName":"BBB",
                                    "keywords":"CCCC",
                                    "type":["Web applocation"],
                                    "skillWanted":"DDD"
                                    }
                data = PROJECT_MSG_SEARCH_RETURN(code=1, msg=PROJECT_SEARCH_EMPTY_SUCCESS)
                for project in all_projects:
                    # return all projects
                    data["projectList"].append({"projectId": project['projectId'],
                                                "projectName": project['projectName'],
                                                "keywords": project['keywords'],
                                                "type": project['type'],
                                                "skillWanted": project['skillWanted']})
                append_dummy = False
                # append_dummpy is designed for situation (no project has been created)
                # default value: False
                if append_dummy:
                    data["projectList"].append(dummpy_project0)
                    data["projectList"].append(dummpy_project1)
            else:
                data = PROJECT_MSG_SEARCH_RETURN(code=1, msg=PROJECT_SEARCH_VALID_SUCCESS)
                if len(req['inputword']) > 0:
                    try:
                        search_domains = {"projectName": "projectName", 
                                        "skillWanted": "skillWanted", 
                                        "projectIntroduction": "projectIntroduction", 
                                        "keywords": "keywords"}
                        for project in all_projects:
                            for _key in search_domains.keys():
                                search_str = " ".join(project[search_domains[_key]]) if type( project[search_domains[_key]]) is list else project[search_domains[_key]]
                                if re.search(req['inputword'], search_str, re.IGNORECASE):
                                    # avoid duplicate project append
                                    if project not in data["projectList"]:
                                        data["projectList"].append(project)
                    except:
                        pass
                if len(req['selectword']) > 0:
                    try:
                        search_domains = {"type": "type", 
                                        "skillWanted": "skillWanted"}
                        for selected_word in req['selectword']:
                            for project in all_projects:
                                for _key in search_domains.keys(): 
                                    search_str = " ".join(project[search_domains[_key]]) if type( project[search_domains[_key]]) is list else project[search_domains[_key]]
                                    if re.search(selected_word, search_str, re.IGNORECASE):
                                        # avoid duplicate project append
                                        if project not in data["projectList"]:
                                            data["projectList"].append(project)
                    except:
                        pass
            return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            data = PROJECT_MSG(msg=PROJECT_RETURN_ALL_FAIL1) ####
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_RETURN_ALL_FAIL2) ###
        return HttpResponse(json.dumps(data), content_type='application/json')