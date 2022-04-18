from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import instructor, student, User, Project, criteria, prj_group, contact
from .msg import *
import json

def contact_edit(request):
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    try:
        ctc = contact.objects.get(contactTag="current",
                                  instructorName=req["instructorName"],
                                  instructorEmail=req["instructorEmail"],
                                  zoomLink=req["zoomLink"],
                                  Ta=req["Ta"],
                                  officeHour=req["officeHour"])
        ctc.save()
        data = {"code": 1,
                "msg": "suc",
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')

def contact_show(request):
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    try:
        ctc = contact.objects.get(contactTag="current")
        data = {
                "code":1,
                "msg":"suc",
                "contactDetails": {"instructorName": ctc.instructorName,
                                   "instructorEmai": ctc.instructorEmail,
                                   "zoomLink": ctc.zoomLink,
                                   "Ta": ctc.Ta,
                                   "officeHour": ctc.officeHour
                                }
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')