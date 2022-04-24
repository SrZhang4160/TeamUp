from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import instructor, student, User, Project, announcements
from .msg import *
import json
from datetime import datetime

def annos_create_msg(request):
    req = json.loads(request.body)
    try:
        # get project id and user email
        annos = announcements.objects.create(name=req['name'], val=req['val'])
        annos.uid = annos.generate_key()
        now = datetime.now()
        annos.releaseTime = now.strftime("%Y-%m-%d %H:%M:%S")
        annos.save()
        data = {"code":1,"msg":"suc"}
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {"code": 0, "msg": "fail"}
    return HttpResponse(json.dumps(data), content_type='application/json')

def annos_list_msg(request):
    req = json.loads(request.body)
    try:
        # get project id and user email
        all_anns = announcements.objects.values()  
        # print(all_anns)
        return_all_anns = []
        for anno in all_anns:
            retrun_anno = {}
            for anno_k in anno.keys():
                if anno_k == 'id':
                    pass
                if anno_k == 'uid':
                    retrun_anno['id'] = anno[anno_k]
                else:
                    retrun_anno[anno_k] = anno[anno_k]
            return_all_anns.append(retrun_anno)
        data = {"code":1,
                "msg":"suc",
                "announcements":return_all_anns[::-1]}
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {"code": 0, "msg": "fail"}
    return HttpResponse(json.dumps(data), content_type='application/json')

def annos_retrieve_msg(request):
    req = json.loads(request.body)
    try:
        annos = announcements.objects.get(uid=req['id'])
        print("announcements search is ok")
        data = {"code":1,"msg":"suc",
                "announcement":{"id":annos.uid,
                                "name":annos.name,
                                "val":annos.val,
                                "releaseTime":annos.releaseTime}
                                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {"code": 0, "msg": "fail"}
    return HttpResponse(json.dumps(data), content_type='application/json')

def annos_latest_msg(request):
    # data = {"code":1,
    #             "msg":"suc",
    #             "announcement":{'name': 'anc', 'val': 'anc is dead', 'releaseTime': '2022-04-22 02:47:32'}}
    # return HttpResponse(json.dumps(data), content_type='application/json')
    # req = json.loads(request.body)

    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']

    try:
        # get project id and user email
        all_anns = announcements.objects.values() 
        sorted_list = sorted(all_anns, key=lambda t: datetime.strptime(t['releaseTime'], "%Y-%m-%d %H:%M:%S"))
        anno_latest = sorted_list[-1]
        data = {"code":1,
                "msg":"suc",
                "announcement":{
                            "name":anno_latest['name'],
                            "val":anno_latest['val'],
                            "releaseTime": anno_latest['releaseTime']
                            }
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {"code": 0, "msg": "fail"}
    return HttpResponse(json.dumps(data), content_type='application/json')