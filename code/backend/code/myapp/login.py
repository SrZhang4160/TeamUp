import imp
from django.http import HttpResponse, JsonResponse
import json
from .models import student, User, Profile
from .models import instructor, student
from .msg import *

# Logout 
def logoutPage(request):
    try:
        data = LOGOUT_RETURN_MSG(code=1, msg=LOGOUT_SUCCESS)
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data = LOGOUT_RETURN_MSG(msg=LOGOUT_ERROR)
        return HttpResponse(json.dumps(data), content_type='application/json')

# Login
def loginPage(request):
    """
    * Create empty return json data
    Default HTTP_X_TOKEN: -1
    Default msg: "Login error",
    """
    try:
    # Read front-end parameter
        req = json.loads(request.body)
        try:
            #If the student account exists
            if student.objects.filter(email=req['email']).exists() is True:
                user = student.objects.get(email=req['email'])
                if user.password == req['password']:
                    data = LOGIN_RETURN_MSG(code=1, 
                                            msg=LOGIN_SUCCESS, 
                                            type=user.type, 
                                            token=user.uid, 
                                            email=user.email, 
                                            name=user.name)
                else:
                    data = LOGIN_RETURN_MSG(msg=LOGIN_PASSWD_WRONG)
                print(data)
                return HttpResponse(json.dumps(data), content_type='application/json')
            #If the instructor account exists
            else:
                if instructor.objects.filter(email=req['email']).exists() is True:
                    user = instructor.objects.get(email=req['email'])
                    if user.password == req['password']:
                        data = LOGIN_RETURN_MSG(code=1, 
                                            msg=LOGIN_SUCCESS, 
                                            type=user.type, 
                                            token=user.uid, 
                                            email=user.email, 
                                            name=user.name)
                    else:
                        data = LOGIN_RETURN_MSG(msg=LOGIN_PASSWD_WRONG)
                else: 
                    data = LOGIN_RETURN_MSG(msg=LOGIN_NOT_EXIST)
                #import pdb;pdb.set_trace()
                print(data)
                return HttpResponse(json.dumps(data), content_type='application/json') 
            #User dose not exists
        except:
            data = LOGIN_RETURN_MSG(msg=LOGIN_ERROR)
            return HttpResponse(json.dumps(data), content_type='application/json')    
    except:
        data = LOGIN_RETURN_MSG(msg=LOGIN_ERROR)
        return HttpResponse(json.dumps(data), content_type='application/json')
    


        