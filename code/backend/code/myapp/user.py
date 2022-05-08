from django.http import HttpResponse, JsonResponse
from .models import student, User, instructor
import json

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()    

def iid_exists(uid):
    return instructor.objects.filter(uid=uid).exists()   

# 获取用户详情
def userinfo(request):
    try:
        token = request.environ['HTTP_X_TOKEN']

        if uid_exists(token) is False and iid_exists(token) is False:
            data = {
                'code': 0,
                'msg': "fail."
                }
            return HttpResponse(json.dumps(data), content_type='application/json') 
        else:
            
            if student.objects.filter(uid=token).exists() is True:
                user=student.objects.get(uid=token)
            elif instructor.objects.filter(uid=token).exists() is True:
                user=instructor.objects.get(uid=token)

            isUnread = 0
            # print(user.contactsList)
            if user.contactsList:
                for contact in user.contactsList:
                    isUnread += contact['unread']
            # user.type 2 student # user.type 1 instructor
            data = {
                'code': 1,
                'msg': "success.",
                'type': user.type,
                'token': token,
                'eml': user.email,
                'name': user.name if user.type == 1 else user.profile.name.split()[0],
                'avatar': user.avatar.name,
                'isUnread': isUnread,
                }

            return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        # 出现意外情况返回异常
        data = {
            'code': -1,
            'msg': "系统异常."
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
