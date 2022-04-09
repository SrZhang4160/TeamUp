from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import student, User, Project
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
        print(req)
        all_projects = Project.objects.values()  
        try:
            print('req')
            project = Project.objects.get(projectId=req['projectId'])
            user = student.objects.get(uid=HTTP_X_TOKEN)
        except:
            try:
                user = student.objects.get(uid=HTTP_X_TOKEN)
                # print(user.profile.userProject)
                try:
                    if len(user.project.projectId) > 0 : 
                        project = user.project
                except:
                    project = Project.objects.get(projectId=user.profile.userProject['projectId'])
            except:
                data =  {
                    "code": 0,
                    "msg": "You have not join any project yet, please find a project team in the main lobby.",
                    "userRole": 0,
                    "project": {}}
                return HttpResponse(json.dumps(data), content_type='application/json')
 
        # --> check user status
        print(project.teamLeader.email)
        print(project.teamMemName)
        print('!!')
        print(user)
        print('!!')
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
        print('hh')

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
                    "teamLeaderName": project.teamLeader.name,
                    "teamMemName": project.teamMemName
                    }
            }
        print(data)
    except:
        data =  {
            "code": 0,
            "msg": PROJECT_RETRIEVE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')