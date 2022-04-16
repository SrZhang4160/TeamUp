from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import student, User, Project
from .msg import *
import json

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()    

def create_project(request):
    try:
        req = json.loads(request.body)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN'] 
        
        if uid_exists(HTTP_X_TOKEN) is False:
            PROJECT_MSG(msg=PROJECT_CREATION_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            try:
                # create student profile and change student status to have already filled in profile info
                # student nad profile have the same uid
                user=student.objects.get(uid=HTTP_X_TOKEN)
                print(req)
                user.create_project(
                    projectName = req['projectName'],
                    projectIntroduction = req['projectIntroduction'],
                    teamName = req['teamName'],
                    keywords = req['keywords'],
                    intendedLanguage = req['intendedLanguage'].split(",")  if "," in req['intendedLanguage'] else req['intendedLanguage'],
                    otherLanguage = req['otherLanguage'].split(",") if "," in req['otherLanguage'] else req['otherLanguage'],
                    type = req['type'].split(",") if "," in req['type'] else req['type'],
                    skillWanted = req['skillWanted'],
                )
                print("Project info received")
                user.project.teamLeader = user
                user.project.projectId = user.project.generate_key()
                user.projectId = user.project.projectId
                # for PERSONAL INFO
                user.profile.userProject = {'projectId':user.projectId, 'projectName':user.project.projectName}
                print(user.projectId)
                user.is_leader = True
                user.save()
                user.profile.save()
                user.project.save()
                
                data = PROJECT_MSG(code=1, msg=PROJECT_FILL_SUCCESS)
            except:
                data = PROJECT_MSG(msg=PROJECT_FILL_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_CREATION_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')
