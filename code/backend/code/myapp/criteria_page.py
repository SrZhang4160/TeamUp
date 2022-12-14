from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import *
from .models import instructor, Profile
from .models import prj_group as Prj_group
from .models import student as Student
from .msg import *
import json
from datetime import datetime
#
import random
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
# Dimension reduction and clustering libraries
try:
    import numpy as np
    import math
    import random
    from k_means_constrained import KMeansConstrained
    import gensim.downloader as api
    wv_from_bin = api.load("glove-wiki-gigaword-50")
except:
    print("NOT WORKING!")
    pass

def criteria_page(request):
    req = json.loads(request.body)
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']

    try:
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        try:
            if req["isTemp"] != '0' and (req["isTemp"] != 0 and req["isTemp"] != 1):
                data = {
                    "code": 0,
                    "msg": CRITERIA_PAGE_FAIL,
                    "criteriaList": []
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            
            if user.criteriaList == []: # fail to create object : criteria() / criteria.objects.create(
                print('cri0')
                major = {"criteriaId":"001", "criteriaName":"Major", "criteriaNum":0, "criteriaPption":"Similar"}
                grade = {"criteriaId":"002", "criteriaName":"Grade", "criteriaNum":0, "criteriaPption":"Similar"}
                leadInt = {"criteriaId":"003", "criteriaName":"Leadership Interest", "criteriaNum":0, "criteriaPption":"Similar"}
                fieldInt = {"criteriaId":"004", "criteriaName":"Field of Interest", "criteriaNum":0, "criteriaPption":"Similar"}
                exep = {"criteriaId":"005", "criteriaName":"Related Experience", "criteriaNum":0, "criteriaPption":"Similar"}
                prod = {"criteriaId":"006", "criteriaName":"Type of End Product", "criteriaNum":0, "criteriaPption":"Similar"}
                lang = {"criteriaId":"007", "criteriaName":"Programming Language", "criteriaNum":0, "criteriaPption":"Similar"}
                mbti = {"criteriaId":"008", "criteriaName":"MBTI", "criteriaNum":0, "criteriaPption":"Similar"}
                skillLevel = {"criteriaId":"009", "criteriaName":"Skill Level", "criteriaNum":0, "criteriaPption":"Similar"}

                for crit in [major,grade,leadInt,fieldInt,exep,prod,lang,mbti,skillLevel]:
                    user.criteriaList.append(crit)
                user.save()
                data = {
                    "code": 1,
                    "msg": CRITERIA_SUC,
                    "criteriaList": user.criteriaList
                }
            else:
                user = instructor.objects.get(uid=HTTP_X_TOKEN)
                data = {
                    "code": 1,
                    "msg": CRITERIA_SUC,
                    "criteriaList": user.criteriaList
                }
            return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            data =  {
            "code": 0,
            "msg": CRITERIA_SEARCH_INSTRUCTOR_FAIL,
            "userRole": 0,
            "project": {}}
            return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')

def update_criteria_page(request):
    req = json.loads(request.body)

    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    now = datetime.now()
    try:
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        try:
            user.group_selection = 0
            user.criteriaList = req["criteriaList"]
            print(type(req["criteriaList"]))
            user.save()
            data = {
                "code": 1,
                "msg": CRITERIA_SUC
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            data =  {
            "code": 0,
            "msg": CRITERIA_SEARCH_INSTRUCTOR_FAIL,
            "userRole": 0,
            "project": {}}
            return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')

def update_criteria_page_left(request):
    req = json.loads(request.body)

    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    now = datetime.now()
    try:
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        try:
            user.group_selection = 1
            user.criteriaList = req["criteriaList"]
            user.save()
            data = {
                "code": 1,
                "msg": CRITERIA_SUC
            }
            return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            data =  {
            "code": 0,
            "msg": CRITERIA_SEARCH_INSTRUCTOR_FAIL,
            "userRole": 0,
            "project": {}}
            return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')

def generate_random_student(num):
    domains = {"major": ['Computer Science','Cognitive Science','Robotics','Psychology', 'Electrical Engineering'],
             "grade": ['Undergraduate','Graduate'],
             "leadInt": ['Low','Medium','High'],
             "fieldInt": ['Books','Health','Business','Music','Education','Entertainment','Academic','Social Networking'],
             "exep": ['None','Class Project','Internship','Work Experience'],
             "mbti": ['Android','Web','Mobile','iOS']
            }
    dummpy_students = []
    for i in range(num):
        dummpy_student = {}
        for domain_key in domains.keys():
            dummpy_student[domain_key] = random.choice(domains[domain_key])
        dummpy_students.append(dummpy_student)
    print(80*"-"+"Generated Students")
    return dummpy_students, domains
    
def criteria_group_page(request):
    # req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        pass
    try:
        #### Get criteria
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        ret_crit = user.criteriaList
        print(ret_crit)
        now = datetime.now()
    #### Get profiles ###
        try:
            if user.group_selection == '0':
                all_students=Student.objects.all()
            else:
                all_students=[s for s in Student.objects.all() if (not s.projectId)]
        except:
            print('why')

        profiles = []
        for student in all_students:
            try:
                user_profile = {"name": student.name,
                                "eml": student.email,
                                "Major": student.profile.major,
                                "Grade": student.profile.grade,
                                "Leadership Interest": student.profile.leadInt,
                                "Field of Interest": ' '.join(student.profile.fieldInt),
                                "Related Experience": student.profile.exep,
                                "Type of End Product": student.profile.prod,
                                "Programming Language": ' '.join([i["skillName"] for i in student.profile.skillLevel if '#' not in i["skillName"]]),
                                "MBTI": ' '.join([i for i in student.profile.mbti if i.isalnum()]) if student.profile.mbti != '' else 'xxxxx',
                                "Skill Level": ' '.join([i["level"] for i in student.profile.skillLevel])}
                profiles.append(user_profile)
            except:
                pass
        domains_criteria = [c['criteriaNum'] for c in ret_crit]
        norm_domains_criteria= [tmp/sum(domains_criteria) for tmp in domains_criteria]
        user_all_embeds = []
        for idx in range(len(profiles)):
            domain_val_embds = []
            for i,domain in enumerate([c['criteriaName'] for c in ret_crit]):
                # embd_vector = sentence_embedding(profiles[idx][domain]) # 9*300
                try:
                    embd_vector = sum([wv_from_bin[i.lower()] for i in profiles[idx][domain].split()])/len(profiles[idx][domain].split()) # 9*300
                except:
                    embd_vector = sum([wv_from_bin[i.lower()] for i in ['is']]) # 9*300
                domain_val_embds.append(embd_vector)
            user_all_embeds.append(domain_val_embds)

# change embeddings to random sample from all students if that category is DIFFERENT
        for i,domain in enumerate([c['criteriaPption'] for c in ret_crit]):
            if 'Different' == domain:
                all_types = [u[i] for u in user_all_embeds]
                for j in range(len(user_all_embeds)):
                    user_all_embeds[j][i] = random.choice(all_types)
        user_all_embeds = [sum([domain_val_embd*norm_domain_criteria for domain_val_embd, norm_domain_criteria in zip(domain_val_embds, norm_domains_criteria)]) for domain_val_embds in user_all_embeds]
        try:
            clf = KMeansConstrained(
                    n_clusters=int(math.ceil(len(profiles)/7)),
                    size_min=5,
                    size_max=7,
                    random_state=42
                    )
            clf.fit_predict(np.asarray(user_all_embeds))
        except:
            try:
                clf = KMeansConstrained(
                        n_clusters=int(math.ceil(len(profiles)/6.5)),
                        size_min=4,
                        size_max=7,
                        random_state=42
                        )
                clf.fit_predict(np.asarray(user_all_embeds))
            except:
                clf = KMeansConstrained(
                        n_clusters=int(math.ceil(len(profiles)/6.5)),
                        size_min=4,
                        size_max=8,
                        random_state=42
                        )
                clf.fit_predict(np.asarray(user_all_embeds))
        kmeans_labels = clf.labels_
        return_project_list = [{"groupNo": i+1 ,"teamMemName":[]} for i in range(np.max(kmeans_labels) + 1)]
        for i,label in enumerate(kmeans_labels):
            return_project_list[label]["teamMemName"].append({"name": profiles[i]['name'],"eml": profiles[i]['eml']})

        Prj_group.objects.all().delete()
        grp = Prj_group(groupTag=now.strftime("%Y-%m-%d %H:%M"), groupinfo=return_project_list)
        grp.save()

        data = {"code": 1,
                "msg": "suc",
                "projectList":return_project_list
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')


def criteria_group_save_page(request):
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        pass
    try:
        all_grps = Prj_group.objects.values()
        all_grps_with_time = []
        for grp in all_grps:
            if grp['groupTag'] != "current":
                all_grps_with_time.append({"time": grp['groupTag'],
                                           "groupinfo": grp['groupinfo']})
        sorted_grp = sorted(all_grps_with_time, key=lambda t: t['time']) #datetime.strptime(t['time'], "%Y-%m-%d %H:%M:%S")
        grp_latest = sorted_grp[0]
        grp = Prj_group(groupTag="current", groupinfo=grp_latest['groupinfo'])
        grp.save()
        data = {"code": 1,
                "msg": "suc"
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')

def criteria_group_show_page(request):
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        pass
    try:
        grp = Prj_group.objects.values()
        for i in grp:
            group = i
        data = {"code": 1,
                "msg": "suc",
                "projectList": group['groupinfo']
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')

def retrieve_group_with_userID_page(request):
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        pass
    try:
        user = Student.objects.get(uid=HTTP_X_TOKEN)
        group = Prj_group.objects.values()
        for i in group:
            grp = i
# [{"groupNo": 1, "teamMemName": [{"name": "jo111111111", "eml": "jo1@jhu.edu"},.....]},...]
        userlist = []
        for temp_grp in  grp['groupinfo']:
            if user.email in [i["eml"] for i in temp_grp['teamMemName']]:
                for team_mem in temp_grp['teamMemName']:
                    if team_mem['eml'] != user.email and team_mem['eml'] != user.profile.preferNot:
                        team_member = Student.objects.get(email=team_mem['eml'])
                        p = Profile.objects.get(uid= team_member.uid)
                        userlist.append({  "userId":team_member.uid,
                        "avatar":team_member.avatar.name,
                        "showVal":p.name+' '+p.grade+' '+p.major,
                        "email":team_member.email})
        data = {
                "code":1,
                "msg":"suc",
                "userlist": userlist
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')
