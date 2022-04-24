from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import instructor, student, User, Project, criteria, prj_group
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
"""
pip uninstall umap
pip install umap-learn
pip install k-means-constrained
pip install numba==0.53
"""
try:
    #import umap.umap_ as umap
    import hdbscan
    import sister
    import math
    import sklearn.cluster as cluster
    from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
    from sister.word_embedders import Word2VecEmbedding
    from k_means_constrained import KMeansConstrained
    sentence_embedder = sister.MeanEmbedding(lang="en")
except:
    #print("Please install required packages")
    pass

def criteria_page(request):
    req = json.loads(request.body)
    print(req)
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']

    try:
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        try:
            if req["isTemp"] != '0':
                data = {
                    "code": 0,
                    "msg": CRITERIA_PAGE_FAIL,
                    "criteriaList": []
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            
            if user.criteriaList == []: # fail to create object : criteria() / criteria.objects.create(
                print('cri0')
                major = {"criteriaId":"001", "criteriaName":"major", "criteriaNum":0, "criteriaPption":"Similar"}
                grade = {"criteriaId":"002", "criteriaName":"grade", "criteriaNum":0, "criteriaPption":"Similar"}
                leadInt = {"criteriaId":"003", "criteriaName":"leadInt", "criteriaNum":0, "criteriaPption":"Similar"}
                fieldInt = {"criteriaId":"004", "criteriaName":"fieldInt", "criteriaNum":0, "criteriaPption":"Similar"}
                exep = {"criteriaId":"005", "criteriaName":"exep", "criteriaNum":0, "criteriaPption":"Similar"}
                prod = {"criteriaId":"006", "criteriaName":"prod", "criteriaNum":0, "criteriaPption":"Similar"}
                lang = {"criteriaId":"007", "criteriaName":"lang", "criteriaNum":0, "criteriaPption":"Similar"}
                mbti = {"criteriaId":"008", "criteriaName":"mbti", "criteriaNum":0, "criteriaPption":"Similar"}
                skillLevel = {"criteriaId":"009", "criteriaName":"skillLevel", "criteriaNum":0, "criteriaPption":"Similar"}

                # all_criteria = criteria.objects.values()

                for crit in [major,grade,leadInt,fieldInt,exep,prod,lang,mbti,skillLevel]:
                    user.criteriaList.append(crit)
                    # user.criteriaList.append({'criteriaId': criteria.criteriaId, 'criteriaName': criteria.criteriaName, 
                    #                           'criteriaNum': criteria.criteriaNum, 'criteriaPption': criteria.criteriaPption})
                print("first time")
                data = {
                    "code": 1,
                    "msg": CRITERIA_SUC,
                    "criteriaList": user.criteriaList
                }
            else:
                user.criteriaList = []
                major = {"criteriaId":"001", "criteriaName":"major", "criteriaNum":0, "criteriaPption":"Similar"}
                grade = {"criteriaId":"002", "criteriaName":"grade", "criteriaNum":0, "criteriaPption":"Similar"}
                leadInt = {"criteriaId":"003", "criteriaName":"leadInt", "criteriaNum":0, "criteriaPption":"Similar"}
                fieldInt = {"criteriaId":"004", "criteriaName":"fieldInt", "criteriaNum":0, "criteriaPption":"Similar"}
                exep = {"criteriaId":"005", "criteriaName":"exep", "criteriaNum":0, "criteriaPption":"Similar"}
                prod = {"criteriaId":"006", "criteriaName":"prod", "criteriaNum":0, "criteriaPption":"Similar"}
                lang = {"criteriaId":"007", "criteriaName":"lang", "criteriaNum":0, "criteriaPption":"Similar"}
                mbti = {"criteriaId":"008", "criteriaName":"mbti", "criteriaNum":0, "criteriaPption":"Similar"}
                skillLevel = {"criteriaId":"009", "criteriaName":"skillLevel", "criteriaNum":0, "criteriaPption":"Similar"}

                # all_criteria = criteria.objects.values()

                print('xxxx')
                for crit in [major,grade,leadInt,fieldInt,exep,prod,lang,mbti,skillLevel]:
                    user.criteriaList.append(crit)
                user.save()
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
            # print(req) {'criteriaList': '[{"criteriaId":"001","criteriaName":"major","criteriaNum":29,"criteriaPption":"Similar"},
            # if req["isTemp"] != 0:
            #     data = {
            #         "code": 0,
            #         "msg": CRITERIA_PAGE_FAIL,
            #         "criteriaList": []
            #     }
            #     return HttpResponse(json.dumps(data), content_type='application/json')
            # for tmp_criteria in req["criteriaList"]:
            #     tmp = criteria(criteriaId= tmp_criteria["criteriaId"], 
            #                    criteriaName= tmp_criteria["criteriaName"], 
            #                    criteriaNum= tmp_criteria["criteriaNum"], 
            #                    criteriaPption= tmp_criteria["criteriaPption"]) 
            #     tmp.save()
            user.group_selection = 0
            user.criteriaList = req["criteriaList"]
            user.save()
            print(user.criteriaList)
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
            if req["isTemp"] != 0:
                data = {
                    "code": 0,
                    "msg": CRITERIA_PAGE_FAIL,
                    "criteriaList": []
                }
                return HttpResponse(json.dumps(data), content_type='application/json')
            for tmp_criteria in req["criteriaList"]:
                tmp = criteria(criteriaId= tmp_criteria["criteriaId"], 
                               criteriaName= tmp_criteria["criteriaName"], 
                               criteriaNum= tmp_criteria["criteriaNum"], 
                               criteriaPption= tmp_criteria["criteriaPption"]) 
                tmp.save()
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
    print('try dummy')
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    try:
        all_students = student.objects.all()
        ct = 0
        grp_no = 1
        return_project_list = []
        teamMem = []
        for s in all_students:
            teamMem.append({"name": s.name, "eml": s.email})
            ct +=1
            if ct % 5 == 0:
                return_project_list.append({"groupNo": grp_no, "teamMemName": teamMem})
            teamMem = []
            grp_no += 1
        if teamMem != []:
            return_project_list.append({"groupNo": grp_no, "teamMemName": teamMem})
    # use_dummpy = True
    # visualize = True
    # now = datetime.now()
    # try:
    #     user = instructor.objects.get(uid=HTTP_X_TOKEN)
    #     filter_students = []
    #     if user.group_selection == 0:
    #         # all studnets
    #         if use_dummpy:
    #             num_members = 1000
    #             dumpy_user_profiles, domains = generate_random_student(num_members)
    #             domains_criteria = [random.randint(1, 10) for key in range(len(domains.keys()))]
    #             norm_domains_criteria= [tmp/sum(domains_criteria) for tmp in domains_criteria]
    #             user_profiles = dumpy_user_profiles
    #         else:
    #             all_students = student.objects.values()
    #             filter_students = all_students
    #             num_members = len(all_students)
    #             user_profiles = []
    #             for student in all_students:
    #                 user_profile = {"major": student.major,
    #                                 "grade": student.grade,
    #                                 "leadInt": student.leadInt,
    #                                 "fieldInt": student.fieldInt,
    #                                 "exep": student.exep,
    #                                 "prod": student.prod,
    #                                 "lang": student.lang,
    #                                 "mbti": student.mbti,
    #                                 "skillLevel": student.skillLevel,}
    #                 user_profiles.append(user_profile)
    #     elif user.group_selection == 1:
    #         all_students = student.objects.values()
    #         num_members = len(all_students)
    #         user_profiles = []
    #         for student in all_students:
    #             if student.projectId == "":
    #                 user_profile = {"major": student.major,
    #                                 "grade": student.grade,
    #                                 "leadInt": student.leadInt,
    #                                 "fieldInt": student.fieldInt,
    #                                 "exep": student.exep,
    #                                 "prod": student.prod,
    #                                 "lang": student.lang,
    #                                 "mbti": student.mbti,
    #                                 "skillLevel": student.skillLevel,}
    #                 user_profiles.append(user_profile)
    #                 filter_students.append(student)
                

    #     user_all_embeds = []
    #     for idx in range(len(user_profiles)):
    #         domain_val_embds = []
    #         for domain in domains:
    #             embd_vector = sentence_embedder(user_profiles[idx][domain])
    #             domain_val_embds.append(embd_vector)
    #             ## currently only similarity, diff --> 1 / domain_val_embd
    #         weighted_embds = sum([domain_val_embd*norm_domain_criteria for domain_val_embd, norm_domain_criteria in zip(domain_val_embds, norm_domains_criteria)])
    #         user_all_embeds.append(weighted_embds)
    #     print("Finish feature extraction")   
    #     # kmeans_labels = cluster.KMeans(n_clusters=10).fit_predict(np.asarray(dummpy_use_all_embeds)) # This is the kmeans without constrain
    #     # 
    #     clf = KMeansConstrained(
    #             n_clusters=int(math.ceil(len(user_profiles)/7)),
    #             size_min=5,
    #             size_max=7,
    #             random_state=42
    #             )
    #     clf.fit_predict(np.asarray(user_all_embeds))
    #     #print(clf.cluster_centers_)
    #     kmeans_labels = clf.labels_
    #     #if visualize:
    #         #standard_embedding = umap.UMAP(random_state=42).fit_transform(np.asarray(user_all_embeds))
    #         #plt.scatter(standard_embedding[:, 0], standard_embedding[:, 1], c=kmeans_labels, s=1, cmap='Spectral');
    #         #plt.savefig('grouping_cluster.png')

#         user_all_embeds = []
#         for idx in range(len(user_profiles)):
#             domain_val_embds = []
#             for domain in domains:
#                 embd_vector = sentence_embedder(user_profiles[idx][domain])
#                 domain_val_embds.append(embd_vector)
#                 ## currently only similarity, diff --> 1 / domain_val_embd
#             weighted_embds = sum([domain_val_embd*norm_domain_criteria for domain_val_embd, norm_domain_criteria in zip(domain_val_embds, norm_domains_criteria)])
#             user_all_embeds.append(weighted_embds)
#         print("Finish feature extraction")   
#         # kmeans_labels = cluster.KMeans(n_clusters=10).fit_predict(np.asarray(dummpy_use_all_embeds)) # This is the kmeans without constrain
#         # 
#         clf = KMeansConstrained(
#                 n_clusters=int(math.ceil(len(user_profiles)/7)),
#                 size_min=5,
#                 size_max=7,
#                 random_state=42
#                 )
#         clf.fit_predict(np.asarray(user_all_embeds))
#         #print(clf.cluster_centers_)
#         kmeans_labels = clf.labels_
#         if visualize:
#             standard_embedding = umap.UMAP(random_state=42).fit_transform(np.asarray(user_all_embeds))
#             plt.scatter(standard_embedding[:, 0], standard_embedding[:, 1], c=kmeans_labels, s=1, cmap='Spectral');
#             plt.savefig('grouping_cluster.png')

    #     if not use_dummpy:
    #         all_students = student.objects.values()
    #         num_members = len(all_students)
    #         user_profiles = []
    #         for student in all_students:
    #             student.projectId = kmeans_labels[idx]

    #     group_distribution = {}
    #     for kmeans_label in kmeans_labels:
    #         if str(kmeans_label) not in group_distribution.keys():
    #             group_distribution[str(kmeans_label)] = 1
    #         else:
    #             group_distribution[str(kmeans_label)] += 1
 
    #     return_groups = {}
    #     for kmeans_label_idx in range(len(kmeans_labels)):
    #         if kmeans_labels[kmeans_label_idx] not in  return_groups.keys():
    #             return_groups[kmeans_labels[kmeans_label_idx]] = []
    #         student = filter_students[kmeans_label_idx]
    #         if {"name": student.name,"eml": student.eml} not in return_groups[kmeans_labels[kmeans_label_idx]]:
    #             return_groups[kmeans_labels[kmeans_label_idx]].append({"name": student.name,"eml": student.eml})
    #     return_project_list = []
    #     for key in return_groups.keys():
    #         return_project_list.append({"groupNo": key, "teamMemName": return_groups[key]})

        grp = prj_group(groupTag=now.strftime("%Y-%m-%d %H:%M"), groupinfo=return_project_list)
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
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    try:
        all_grps = prj_group.objects.values()
        all_grps_with_time = []
        for grp in all_grps:
            if grp.groupTag != "current":
                all_grps_with_time.append({"time": grp.groupTag,
                                           "groupinfo": grp.groupinfo})

        sorted_grp = sorted(all_grps_with_time, key=lambda t: datetime.strptime(t['time'], "%Y-%m-%d %H:%M:%S"))
        grp_latest = sorted_grp[0]
        grp = prj_group(groupTag="current", groupinfo=grp_latest['groupinfo'])
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
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    try:
        grp = prj_group.objects.get(groupTag="current")
        data = {"code": 1,
                "msg": "suc",
                "projectList": grp.groupinfo
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')

def retrieve_group_with_userID_page(request):
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    try:
        user = student.objects.get(uid=HTTP_X_TOKEN)
        grp = prj_group.objects.get(groupTag="current")
        user_group_id = user.projectId
        userlist = []
        for temp_grp in  grp.groupinfo:
            if temp_grp["groupNo"] == user_group_id:
                for team_mem in temp_grp['teamMemName']:
                    if team_mem['eml'] != user.eml:
                        team_member = student.objects.get(eml=team_mem['eml'])
                        userlist.append({
                                        "userId":team_member.uid,
                                        "avatar":team_member.avatar.name,
                                        "showVal": " ,".join(team_member.name, team_member.grad, team_member.major),
                                        "email": team_member.eml
                                        })
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
