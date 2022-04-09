from django.http import HttpResponse, JsonResponse
from .models import student, User, Project
from .msg import *
import json

def recommend_project(request):
    try:
    #     req = json.loads(request.body)
        
    #     # if request.environ.get('HTTP_X_TOKEN') is not None:
    #     try:
    #         HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    #     except:
    #         HTTP_X_TOKEN = req['HTTP_X_TOKEN']

            # current dummy recommend: no request body, just return whatever
        data = {"code":1,
        "msg":PROJECT_RECOMMEND_SUCCESS,
        "projectList":[{
          "projectId":"aaa",
          "projectName":"bbb",
          "keywords":"CC",
          "type":["IOS","Android"],
          "skillWanted":"DDD"
         },{
          "projectId":"AAA",
          "projectName":"BBB",
          "keywords":"CCCC",
          "type":["Web applocation"],
          "skillWanted":"DDD"
         }]}
        return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_RECOMMEND_FAIL) ###
        return HttpResponse(json.dumps(data), content_type='application/json')
