import email
from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import student, User, Project
from .msg import *
import json
from datetime import datetime

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()

def send_message(request):
    try:
        req = json.loads(request.body)
        print(req)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN']
        
        sender = student.objects.get(uid=HTTP_X_TOKEN)
        receiver = student.objects.get(email=req['sendTo'])
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
        print(req)
        print(HTTP_X_TOKEN)
        
        if uid_exists(HTTP_X_TOKEN) is False:
            data = PROJECT_MSG(msg=PROJECT_CREATION_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            print('1')
            contact = student.objects.get(uid=HTTP_X_TOKEN)
            print('2')
            data = {
                "code":1,
                "msg":"Success",
                "projectList":contact.contactsList
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
            me = student.objects.get(uid=HTTP_X_TOKEN)
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