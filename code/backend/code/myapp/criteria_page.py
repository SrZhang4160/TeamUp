from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import instructor, student, User, Project, criteria
from .msg import *
import json

def criteria_page(request):
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']

    try:
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        try:
            if req["isTemp"] != 0:
                data = {
                    "code": 1,
                    "msg": CRITERIA_PAGE_FAIL,
                    "criteriaList": []
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            
            if user.criteriaList == []:
                major = criteria(criteriaId= "001", criteriaName = "major")
                major.save()
                grade = criteria(criteriaId= "002", criteriaName = "grade")
                grade.save()
                leadInt = criteria(criteriaId= "003", criteriaName = "leadInt")
                leadInt.save()
                fieldInt = criteria(criteriaId= "004", criteriaName = "fieldInt")
                fieldInt.save()
                exep = criteria(criteriaId= "005", criteriaName = "exep")
                exep.save()
                prod = criteria(criteriaId= "006", criteriaName = "prod")
                prod.save()
                lang = criteria(criteriaId= "007", criteriaName = "lang")
                lang.save()
                mbti = criteria(criteriaId= "008", criteriaName = "mbti")
                mbti.save()
                skillLevel = criteria(criteriaId= "009", criteriaName = "skillLevel")
                skillLevel.save()
                all_criteria = criteria.objects.values()
                for criteria in all_criteria:
                    user.criteriaList.append({'criteriaId': criteria.criteriaId, 'criteriaName': criteria.criteriaName, 
                                              'criteriaNum': criteria.criteriaNum, 'criteriaPption': criteria.criteriaPption})
                    print('for loop ok')
                print("first time")
                data = {
                    "code": 1,
                    "msg": CRITERIA_SUC,
                    "criteriaList": instructor.criteriaList
                }
            else:
                data = {
                    "code": 1,
                    "msg": CRITERIA_SUC,
                    "criteriaList": instructor.criteriaList
                }
        except:
            data =  {
            "code": 0,
            "msg": CRITERIA_SEARCH_INSTRUCTOR_FAIL,
            "userRole": 0,
            "project": {}}
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')
    
