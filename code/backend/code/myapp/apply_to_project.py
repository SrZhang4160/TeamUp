from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import student, User, Project
from .msg import *
import json

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()    

def apply_to_project(request):
    try:
        req = json.loads(request.body)
        print(req)
        
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
                user = student.objects.get(uid=HTTP_X_TOKEN)
                project = Project.objects.get(projectId=req['projectId'])


                if project.applied_stu is None:
                    project.applied_stu = []
                print(project.applied_stu)
                # project.applied_stu = []
                # project.save()
                    
                # --> check user status 
                print('!!!',user)
                if user.projectId: # user has a group
                    print('-1')
                    return_msg = "you are member/leader of other project, need to exit/terminate current project to join new project"
                elif {"name": user.name, "eml": user.email} in project.applied_stu: # user has applied for this project
                    return_msg = PROJECT_APPLY_REPEAT
                else:# user has no group
                    print('0')
                    return_msg = PROJECT_APPLY_SUCCESS
                print('1') 
                
                if return_msg == PROJECT_APPLY_SUCCESS: # only when APPLY_SUCCESS do the following:
                # "you are member/leader of other project, need to exit/terminate current project to join new project",
                    if {"name": user.name, "eml": user.email} not in project.applied_stu:
                        project.applied_stu.append({"name": user.name, "eml": user.email})
                    print(project.applied_stu)
                    if user.applied_project is None:
                        user.applied_project = []
                    # print(user.applied_project)
                    if req['projectId'] not in user.applied_project:
                        user.applied_project.append(req['projectId'])
                # print(user.applied_project)
                
                try:
                    user.save()
                except Exception as e:
                    print(e)
                print('4')
                project.save()
                data = PROJECT_MSG(code=1, msg=return_msg)
                return HttpResponse(json.dumps(data), content_type='application/json')
            except:
                data = PROJECT_MSG(msg=PROJECT_APPLY_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_APPLY_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')
