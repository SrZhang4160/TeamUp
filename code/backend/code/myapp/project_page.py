from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import instructor, student, User, Project
from .msg import *
import json

def project_page(request):
    req = json.loads(request.body)

    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']

    try:
        # get project id and user email
        all_projects = Project.objects.values()  
        Is_Instructor = False
        try:
            project = Project.objects.get(projectId=req['projectId'])

            try: # student
                user = student.objects.get(uid=HTTP_X_TOKEN)
            except: # instructor
                Is_Instructor = True
        except:
            try:
                user = student.objects.get(uid=HTTP_X_TOKEN)
                try:
                    if len(user.project.projectId) > 0 : 
                        project = user.project
                except:
                    project = Project.objects.get(projectId=user.profile.userProject['projectId'])
            except:
                data =  {
                    "code": 1,
                    "userRole": 0,
                    "project": {}}
                return HttpResponse(json.dumps(data), content_type='application/json')
 
        # --> check user status
        if Is_Instructor is True:
            userRole = 0
        else:
            if project.teamLeader.email == user.email: # team leader
                userRole = 1 
            elif project.teamMemName is not None:
                if user.email in [mem['eml'] for mem in project.teamMemName]: # team member
                    userRole = 2
                else:
                    userRole = 4
            elif user.projectId: # user has a group
                userRole = 4
            else: # user has no group
                userRole = 3

        data =  {
            "code": 1,
            "msg": PROJECT_RETRIEVE_SUCCESS,
            "userRole": userRole,
            "project": {
                    "projectId": project.projectId,
                    "projectName": project.projectName,
                    "projectIntroduction": project.projectIntroduction,
                    "keywords": project.keywords,
                    "intendedLanguage": project.intendedLanguage,
                    "otherLanguage": project.otherLanguage,
                    "type": project.type,
                    "skillWanted": project.skillWanted,
                    "teamName": project.teamName,
                    "teamLeader": project.teamLeader.email,
                    "teamLeaderName": project.teamLeader.profile.name,
                    "teamMemName": project.teamMemName
                    }
            }
        # print(data)
    except:
        data =  {
            "code": 0,
            "msg": PROJECT_RETRIEVE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')
