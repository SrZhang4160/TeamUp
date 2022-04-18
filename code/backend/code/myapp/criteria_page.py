from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import instructor, student, User, Project, criteria
from .msg import *
import json

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
    import umap.umap_ as umap
    import hdbscan
    import sister
    import math
    import sklearn.cluster as cluster
    from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
    from sister.word_embedders import Word2VecEmbedding
    from k_means_constrained import KMeansConstrained
    sentence_embedder = sister.MeanEmbedding(lang="en")
except:
    print("Please install required packages")

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
                    "code": 0,
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
            user.group_selection = 0
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

def update_criteria_page_left(request):
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
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    use_dummpy = True
    visualize = True
    try:
        user = instructor.objects.get(uid=HTTP_X_TOKEN)
        if user.group_selection == 0:
            # all studnets
            if use_dummpy:
                num_members = 1000
                dumpy_user_profiles, domains = generate_random_student(num_members)
                domains_criteria = [random.randint(1, 10) for key in range(len(domains.keys()))]
                norm_domains_criteria= [tmp/sum(domains_criteria) for tmp in domains_criteria]
                user_profiles = dumpy_user_profiles
            else:
                all_students = student.objects.values()
                num_members = len(all_students)
                user_profiles = []
                for student in all_students:
                    user_profile = {"major": student.major,
                                    "grade": student.grade,
                                    "leadInt": student.leadInt,
                                    "fieldInt": student.fieldInt,
                                    "exep": student.exep,
                                    "prod": student.prod,
                                    "lang": student.lang,
                                    "mbti": student.mbti,
                                    "skillLevel": student.skillLevel,}
                    user_profiles.append(user_profile)
                
            user_all_embeds = []
            for idx in range(len(user_profiles)):
                domain_val_embds = []
                for domain in domains:
                    embd_vector = sentence_embedder(user_profiles[idx][domain])
                    domain_val_embds.append(embd_vector)
                weighted_embds = sum([domain_val_embd*norm_domain_criteria for domain_val_embd, norm_domain_criteria in zip(domain_val_embds, norm_domains_criteria)])
                user_all_embeds.append(weighted_embds)
            print("Finish feature extraction")   
            # kmeans_labels = cluster.KMeans(n_clusters=10).fit_predict(np.asarray(dummpy_use_all_embeds)) # This is the kmeans without constrain
            # 
            clf = KMeansConstrained(
                    n_clusters=int(math.ceil(len(user_profiles)/7)),
                    size_min=5,
                    size_max=7,
                    random_state=42
                    )
            clf.fit_predict(np.asarray(user_all_embeds))
            #print(clf.cluster_centers_)
            kmeans_labels = clf.labels_
            if visualize:
                standard_embedding = umap.UMAP(random_state=42).fit_transform(np.asarray(user_all_embeds))
                plt.scatter(standard_embedding[:, 0], standard_embedding[:, 1], c=kmeans_labels, s=1, cmap='Spectral');
                plt.savefig('grouping_cluster.png')

            if not use_dummpy:
                all_students = student.objects.values()
                num_members = len(all_students)
                user_profiles = []
                for student in all_students:
                    student.projectId = kmeans_labels[idx]

            group_distribution = {}
            for kmeans_label in kmeans_labels[:len(user_profile)]:
                if str(kmeans_label) not in group_distribution.keys():
                    group_distribution[str(kmeans_label)] = 1
                else:
                    group_distribution[str(kmeans_label)] += 1
        elif user.group_selection == 1:
            all_students = student.objects.values()
            num_members = len(all_students)
            user_profiles = []
            for student in all_students:
                if student.projectId == "":
                    user_profile = {"major": student.major,
                                    "grade": student.grade,
                                    "leadInt": student.leadInt,
                                    "fieldInt": student.fieldInt,
                                    "exep": student.exep,
                                    "prod": student.prod,
                                    "lang": student.lang,
                                    "mbti": student.mbti,
                                    "skillLevel": student.skillLevel,}
                    user_profiles.append(user_profile)
                
            user_all_embeds = []
            for idx in range(len(user_profiles)):
                domain_val_embds = []
                for domain in domains:
                    embd_vector = sentence_embedder(user_profiles[idx][domain])
                    domain_val_embds.append(embd_vector)
                weighted_embds = sum([domain_val_embd*norm_domain_criteria for domain_val_embd, norm_domain_criteria in zip(domain_val_embds, norm_domains_criteria)])
                user_all_embeds.append(weighted_embds)
            print("Finish feature extraction")   
            # kmeans_labels = cluster.KMeans(n_clusters=10).fit_predict(np.asarray(dummpy_use_all_embeds)) # This is the kmeans without constrain
            # 
            clf = KMeansConstrained(
                    n_clusters=int(math.ceil(len(user_profiles)/7)),
                    size_min=5,
                    size_max=7,
                    random_state=42
                    )
            clf.fit_predict(np.asarray(user_all_embeds))
            #print(clf.cluster_centers_)
            kmeans_labels = clf.labels_
            if visualize:
                standard_embedding = umap.UMAP(random_state=42).fit_transform(np.asarray(user_all_embeds))
                plt.scatter(standard_embedding[:, 0], standard_embedding[:, 1], c=kmeans_labels, s=1, cmap='Spectral');
                plt.savefig('grouping_cluster.png')

            if not use_dummpy:
                all_students = student.objects.values()
                num_members = len(all_students)
                user_profiles = []
                for student in all_students:
                    student.projectId = kmeans_labels[idx]

            group_distribution = {}
            for kmeans_label in kmeans_labels[:len(user_profile)]:
                if str(kmeans_label) not in group_distribution.keys():
                    group_distribution[str(kmeans_label)] = 1
                else:
                    group_distribution[str(kmeans_label)] += 1
        data = {"code": 1,
                "msg": "suc",
                "projectList": [{"groupNo": 1, "teamMemName":[{"name": "bbb","eml": "BBB@jhu.edu"}, 
                                                              {"name": "ccc","eml": "CCC@jhu.edu"}]},
                                {"groupNo": 2, "teamMemName":[{"name": "DD","eml": "DD@jhu.edu"}, 
                                                              {"name": "EE","eml": "EE@jhu.edu"}]}]
                }

        data = {
            "code": 1,
            "msg": CRITERIA_SUC
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": CRITERIA_PAGE_FAIL}
    return HttpResponse(json.dumps(data), content_type='application/json')