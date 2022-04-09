from django.http import HttpResponse, JsonResponse
##from rest_framework.authtoken.models import Token
from .models import student, User
from .msg import *
import json

# check if student account with a certain email exists
def email_exists(email):
    return student.objects.filter(email=email).exists()

# check if student account with a certain uid exists
def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()    

# create student account after checking email hasn't been registered
def create_student(request):
    req = json.loads(request.body)
 
    try:
        if email_exists(req['email']) is False:
            user = student.objects.create(name=req['name'], avatar=req['avatar'], type=0, password=req['password'], email=req['email'])
            user.uid = user.generate_key()
            user.save()
            data = CREATE_USER_MSG(code=1, msg=PROFILE_CREATE_USER_SUCCESS)
        else:
            data = CREATE_USER_MSG(msg=PROFILE_CREATE_USER_EMAIL_HAS_REGISTERED)
    except:
        data = CREATE_USER_MSG(msg=PROFILE_CREATE_USER_ERROR)
    return HttpResponse(json.dumps(data), content_type='application/json') 

def query_profile(request):
    try:
        # read request body from front end
        # req = json.loads(request.body)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']           
 
        if uid_exists(HTTP_X_TOKEN) is False:
            PROFILE_MSG(msg=PROFILE_FILL_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            try:
                # create student profile and change student status to have already filled in profile info
                # student and profile have the same uid
                # otherLanguage is not empty
                user=student.objects.get(uid=HTTP_X_TOKEN)
 
                data = {
                "code":1,
                "msg":PROFILE_QUERY_SUCCESS,
                "userDetails":{
                                "name":user.profile.name,
                                "major":user.profile.major,
                                "grade":user.profile.grade,
                                "skillLevel":user.profile.skillLevel,
                                "leadInt":user.profile.leadInt,
                                "fieldInt":user.profile.fieldInt,
                                "prod":user.profile.prod,
                                "exep":user.profile.exep,
                                "mbti":user.profile.mbti,
                                "prefer": user.profile.prefer,
                                "preferNot" : user.profile.preferNot,
                                "email":user.profile.email
                                },
                "userProject":user.profile.userProject
                }
                # print(data)
            except:
                data = PROFILE_MSG(msg=PROFILE_QUERY_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = PROFILE_MSG(msg=PROFILE_QUERY_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

def query_profile_others(request):
    try:
        # read request body from front end
        req = json.loads(request.body)
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']           
 
        if uid_exists(HTTP_X_TOKEN) is False:
            PROFILE_MSG(msg=PROFILE_FILL_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            try:
                # create student profile and change student status to have already filled in profile info
                # student and profile have the same uid
                # otherLanguage is not empty
                user=student.objects.get(email=req['email'])
 
                data = {
                "code":1,
                "msg":PROFILE_QUERY_SUCCESS,
                "userDetails":{
                                "name":user.profile.name,
                                "major":user.profile.major,
                                "grade":user.profile.grade,
                                "skillLevel":user.profile.skillLevel,
                                "leadInt":user.profile.leadInt,
                                "fieldInt":user.profile.fieldInt,
                                "prod":user.profile.prod,
                                "expe":user.profile.exep,
                                "mbti":user.profile.mbti,
                                "email":user.profile.email
                                },
                "userProject":user.profile.userProject
                }
                print(data)
            except:
                data = PROFILE_MSG(msg=PROFILE_QUERY_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = PROFILE_MSG(msg=PROFILE_QUERY_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

# fill in profile for a Student
def update_profile(request):
    try:
        # read request body from front end
        req = json.loads(request.body)
        print(req)
        # student should surely be already registered to able to create profile
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']           
 
        if uid_exists(HTTP_X_TOKEN) is False:
            PROFILE_MSG(msg=PROFILE_UPDATE_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            try:
                # create student profile and change student status to have already filled in profile info
                # student and profile have the same uid
                # otherLanguage is not empty
                
                user=student.objects.get(uid=HTTP_X_TOKEN)
                mandatory_fields_keys = ["name", "major", "skillLevel", "leadInt", "grade", "fieldInt", "prod", "exep"]
                mandatory_fields = [req["userDetails"][key] for key in mandatory_fields_keys]
                
                if '' not in mandatory_fields and [] not in mandatory_fields:
                    
                    user.profile.name =  req["userDetails"]["name"]
                    user.profile.major =  req["userDetails"]["major"]
                    user.profile.skillLevel =  req["userDetails"]["skillLevel"]
                    user.profile.leadInt =  req["userDetails"]["leadInt"]
                    user.profile.grade =  req["userDetails"]["grade"]
                    user.profile.fieldInt =  req["userDetails"]["fieldInt"]
                    user.profile.prod =  req["userDetails"]["prod"]
                    user.profile.exep =  req["userDetails"]["exep"]
                    user.profile.prefer =  req["userDetails"]["prefer"]
                    user.profile.preferNot =  req["userDetails"]["preferNot"]
                    # user.profile.email =  req["userDetails"]["email"]
                    user.profile.mbti =  req["userDetails"]["mbti"]
                    user.save()
                    user.profile.save()
                    data = PROFILE_MSG(code=1, msg=PROFILE_UPDATE_SUCCESS)
                else:

                    data = PROFILE_MSG(msg=PROFILE_UPDATE_DUMMPY_INPUT)
            except:
                data = PROFILE_MSG(msg=PROFILE_UPDATE_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = PROFILE_MSG(msg=PROFILE_UPDATE_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

def fill_profile(request):
    try:
        # read request body from front end
        req = json.loads(request.body)
        # student should surely be already registered to able to create profile
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']           
 
        if uid_exists(HTTP_X_TOKEN) is False:
            PROFILE_MSG(msg=PROFILE_FILL_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            try:
                # print(req)
                # create student profile and change student status to have already filled in profile info
                # student and profile have the same uid
                # otherLanguage is not empty
                user=student.objects.get(uid=HTTP_X_TOKEN)
                mandatory_fields_keys = ["name", "major", "skillLevel", "leadInt", "grade", "fieldInt", "prod", "exep"]
                mandatory_fields = [req[key] for key in mandatory_fields_keys]

                if '' not in mandatory_fields and [] not in mandatory_fields:
                    user.create_profile(
                        uid=HTTP_X_TOKEN,
                        name=req["name"],
                        major=req["major"],
                        skillLevel=req["skillLevel"],
                        leadInt=req["leadInt"],
                        grade=req["grade"],
                        fieldInt=req["fieldInt"],
                        prod=req["prod"],
                        exep=req["exep"],
                        prefer=req["prefer"],
                        preferNot=req["preferNot"],
                        mbti=req["mbti"],
                        email=user.email
                    )
                    user.type = 2
                    user.save()
                    user.profile.save()
                    data = PROFILE_MSG(code=1, msg=PROFILE_FILL_SUCCESS)
                else:
                    data = PROFILE_MSG(msg="At least one of the mandatory fields are empty!!")
            except:
                data = PROFILE_MSG(msg=PROFILE_FILL_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = PROFILE_MSG(msg=PROFILE_FILL_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')