from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import student, User, Project
from .msg import *
import json

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()    

def del_project(request):
    try:
        req = json.loads(request.body)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN'] 
        
        try:
            try:
                project = Project.objects.get(projectId=req['projectId'])
                user = student.objects.get(uid=HTTP_X_TOKEN)
            except:
                user = student.objects.get(uid=HTTP_X_TOKEN)
                if len(user.project.projectId) > 0 : 
                    project = user.project
            all_students = student.objects.values()
            for tmp_student in all_students:
                if tmp_student['projectId'] is not None:
                    if tmp_student['projectId'] == project.projectId:
                        user=student.objects.get(email=tmp_student['email'])
                        user.projectId = None
                        user.save()
            user.profile.userProject = []
            user.profile.save()
            project.delete()
            data = PROJECT_MSG(code=1, msg=PROJECT_DEL_SUCCESS)
        except:
            data = PROJECT_MSG(msg=PROJECT_DEL_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_DEL_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')
