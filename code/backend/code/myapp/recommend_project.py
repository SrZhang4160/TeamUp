from django.http import HttpResponse, JsonResponse
from .models import student, User, Project
from .msg import *
import json
import random
import binascii
import os
from numpy import dot
import numpy as np
from numpy.linalg import norm

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

def generate_random_project(num):
    domains = {"keywords": ['Computer Science','Cognitive Science','Robotics','Psychology', 'Electrical Engineering'],
               "type": ['Android','Web','Mobile','iOS'],
               "skillWanted": ['C++','Python','Jave','C#','Lua']
              }
    dummpy_prjs = []
    for i in range(num):
        dummpy_prj = {}
        dummpy_prj["keywords"] = random.sample(domains["keywords"], 2)
        dummpy_prj["type"] = random.sample(domains["type"], 2)
        dummpy_prj["skillWanted"] = random.choice(domains["skillWanted"])
        dummpy_prj["projectId"] = binascii.hexlify(os.urandom(20)).decode()
        dummpy_prj["projectName"] = binascii.hexlify(os.urandom(10)).decode()
        dummpy_prjs.append(dummpy_prj)
    print(80*"-"+"Generated Projects")
    return dummpy_prjs, domains.keys()

def recommend_project(request):
    req = json.loads(request.body)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    
    try:
        dummy_student = {
                        "name":"SAN ZHANG",
                        "major":"COMPUTER SCIENCE",
                        "grade":"GRAD",
                        "skillLevel":[
                            {"skillName":"JAVA","level":"LOW"},
                            {"skillName":"C++","level":"HIGH"}
                            ],
                        "leadInt":"HIGH",
                        "fieldInt":["XX","YY"],
                        "prod":"WEB",
                        "exep":"intern",
                        "mbti":"estj-T",
                        "prefer" : "aaa@jhu.edu",
                        "preferNot" :  "aaa@jhu.edu",
                        "email":"YYY@JHU.EDU"
                        }
        dummpy_projects, domains_keys = generate_random_project(10)

        all_projects = Project.objects.values()
        user = student.objects.get(uid=HTTP_X_TOKEN)
        embd_student_fieldInt = sentence_embedder(" ".join(user.fieldInt))
        embd_student_skillLevell = sentence_embedder(" ".join([item['skillName'] for item in user.skillLevel]))
        embd_student = (embd_student_fieldInt + embd_student_skillLevell) / 2 # Norm

        prj_all_embeds = []
        for idx in range(len(all_projects)):
            domain_val_embds = []
            domain_val_embds.append(sentence_embedder(" ".join(all_projects[idx].keywords)))
            domain_val_embds.append(sentence_embedder(" ".join(all_projects[idx].type)))
            domain_val_embds.append(sentence_embedder(" ".join(all_projects[idx].skillWanted)))
            avg_embds = sum([domain_val_embd*(1/3) for domain_val_embd in domain_val_embds])
            prj_all_embeds.append(avg_embds)

        cos_sim = dot(embd_student, np.transpose(np.asarray(prj_all_embeds)))/(norm(embd_student)*norm(np.transpose(np.asarray(prj_all_embeds))))
        top3_project_ids = np.argsort(cos_sim)[:3]
        proj_infos = []
        for top3_project_id in top3_project_ids:
            proj_info = {"projectId": all_projects[top3_project_id]["projectId"],
                         "projectName": all_projects[top3_project_id]["projectName"],
                         "keywords": all_projects[top3_project_id]["keywords"],
                         "type": all_projects[top3_project_id]["type"],
                         "skillWanted": all_projects[top3_project_id]["skillWanted"],}
            proj_infos.append(proj_info)
        data = {"code":1,
                "msg":PROJECT_RECOMMEND_SUCCESS,
                "projectList":proj_infos
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_RECOMMEND_FAIL) ###
        return HttpResponse(json.dumps(data), content_type='application/json')
