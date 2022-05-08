import email
from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from wordfreq import CACHE_SIZE
from .models import instructor, student, User, Project
from .msg import *
import json
from datetime import datetime

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists() or instructor.objects.filter(uid=uid).exists()

def send_message(request):
    try:
        req = json.loads(request.body)
        print(req)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']
        
        ### now both sender and receiver could be instructor
        try:
            sender = student.objects.get(uid=HTTP_X_TOKEN)
        except:
            sender = instructor.objects.get(uid=HTTP_X_TOKEN)
        try:
            receiver = student.objects.get(email=req['sendTo'])
        except:
            receiver = instructor.objects.get(email=req['sendTo'])

        if receiver.messageList is None: receiver.messageList = []
        now = datetime.now()
        # Receiver : add this message
        print('1')
        receiver.messageList.append({
                                    "message":req['sendMessage'],
                                    "sender": sender.email,
                                    "receiver": receiver.email,
                                    "sendTime": now.strftime("%Y-%m-%d %H:%M"),
                                    "isme": 0,
                                    "avatar": sender.avatar.name
                                    })
        # Receiver : add/update this contact
        print('2')
        if receiver.contactsList is None: receiver.contactsList = []
        contacted = False
        for i,contact in enumerate(receiver.contactsList):
            if sender.name == contact["userName"]:
                receiver.contactsList[i]["lastTime"] = now.strftime("%Y-%m-%d %H:%M")
                receiver.contactsList[i]["unread"] += 1
                contacted = True
        if contacted is False:
                receiver.contactsList.append({
                                            "userName":sender.name,
                                            "userId":sender.uid,
                                            "email":sender.email,
                                            "lastTime": now.strftime("%Y-%m-%d %H:%M"),
                                            "unread":1
                                            })
        receiver.save()
        # Sender : add this message
        print('3')
        if sender.messageList is None: sender.messageList = []
        sender.messageList.append({
                                    "message":req['sendMessage'],
                                    "sender": sender.email,
                                    "receiver": receiver.email,
                                    "sendTime": now.strftime("%Y-%m-%d %H:%M"),
                                    "isme": 1,
                                    "avatar": sender.avatar.name
                                    })
        # Sender : add/update this contact
        print('4')
        if sender.contactsList is None: sender.contactsList = []
        contacted = False
        for i,contact in enumerate(sender.contactsList):
            if receiver.name == contact["userName"]:
                sender.contactsList[i]["lastTime"] = now.strftime("%Y-%m-%d %H:%M")
                # sender.contactsList["unread"] += 1 # message sent by oneself will not add unread
                contacted = True
        if contacted is False:
                sender.contactsList.append({
                                            "userName":receiver.name,
                                            "userId":receiver.uid,
                                            "email":receiver.email,
                                            "lastTime": now.strftime("%Y-%m-%d %H:%M"),
                                            "unread":0
                                            })
        sender.save()
        data = {"code":1, "msg":"success"}
        return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = {"code":1, "msg":"fail"}
        return HttpResponse(json.dumps(data), content_type='application/json')

def retrieve_contact(request):
    try:
        req = json.loads(request.body)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN'] 
        # print(req)
        # print(HTTP_X_TOKEN)
        
        if uid_exists(HTTP_X_TOKEN) is False:
            data = PROJECT_MSG(msg=PROJECT_CREATION_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            print('1')
            try:
                contact = student.objects.get(uid=HTTP_X_TOKEN)
            except:
                contact = instructor.objects.get(uid=HTTP_X_TOKEN)
            print('2')
            data = {
                "code":1,
                "msg":"Success",
                "projectList":[i for i in contact.contactsList if i['email']!='CACHE'] if contact.contactsList else []
            }
            print(data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_EDIT_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

def retrieve_message(request):
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
                me = student.objects.get(uid=HTTP_X_TOKEN)
            except:
                me = instructor.objects.get(uid=HTTP_X_TOKEN)
            email_other = req['email']
            return_msg = []
            for msg in me.messageList:
                if (msg['sender'] == me.email and msg['receiver'] == email_other) or (msg['sender'] == email_other and msg['receiver'] == me.email):
                    return_msg.append(msg)
            data ={
                "code":1,
                "msg":"Success",
                "messageList":return_msg
                }
            for i,contact in enumerate(me.contactsList):
                if email_other == contact['email']:
                    me.contactsList[i]["unread"] = 0
            me.save()
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_EDIT_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

def cache_message(request):
    try:
        req = json.loads(request.body)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']
        
        ### now both sender and receiver could be instructor
        try:
            cacher = student.objects.get(uid=HTTP_X_TOKEN)
        except:
            cacher = instructor.objects.get(uid=HTTP_X_TOKEN)

        if cacher.contactsList is None: cacher.contactsList = []
        now = datetime.now()
        cached = False
        for i,contact in enumerate(cacher.contactsList):
            if 'CACHE' == contact["email"]:
                cacher.contactsList[i]["lastTime"] = now.strftime("%Y-%m-%d %H:%M")
                cacher.contactsList[i]["userName"] = req['sendTo']
                cacher.contactsList[i]["userId"] = req['sendMessage']
                contacted = True
        if cached is False:
                cacher.contactsList.append({
                                            "userName":req['sendTo'],
                                            "userId":req['sendMessage'],
                                            "email":'CACHE',
                                            "lastTime": now.strftime("%Y-%m-%d %H:%M"),
                                            "unread":0
                                            })
        cacher.save()

        data = {"code":1, "msg":"success"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = COMMUNICATION_MSG(msg="cache_message fail")
        return HttpResponse(json.dumps(data), content_type='application/json')
# {
#  "sendTo":"YYY@JHU.EDU",
#  "sendMessage":"HELLO…… best"
#  }

# {
#  "code":1,
#  "msg":"获取成功",
# }
def retrieve_cache_message(request):
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
                me = student.objects.get(uid=HTTP_X_TOKEN)
            except:
                me = instructor.objects.get(uid=HTTP_X_TOKEN)
            for i,contact in enumerate(me.contactsList):
                if 'CACHE' == contact['email']:
                    data = {"code":1, "msg":"success", "sendTo":contact["userName"], "sendMessage":contact['userId']}
        return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = {"code":1, "msg":"no msg", "sendTo":"", "sendMessage":""}
        return HttpResponse(json.dumps(data), content_type='application/json')

# {
#  "code":1,
#  "msg":"获取成功",
#  "sendTo":"YYY@JHU.EDU",
#  "sendMessage":"HELLO…… best"
#  }