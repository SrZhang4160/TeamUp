from django.http import HttpResponse, JsonResponse
from .models import student, User
import json

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()    

# 获取用户详情
def userinfo(request):
    try:
        token = request.environ['HTTP_X_TOKEN']
        if uid_exists(token) is False:
            data = {
                'code': 0,
                'msg': "fail."
                }
            return HttpResponse(json.dumps(data), content_type='application/json') 
        else:
            user=student.objects.get(uid=token)
            isUnread = 0
            print(user.contactsList)
            if user.contactsList:
                for contact in user.contactsList:
                    isUnread += contact['unread']
            # user.type 2
            data = {
                'code': 1,
                'msg': "success.",
                'type': user.type,
                'token': token,
                'eml': user.email,
                'name': user.name,
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
