from django.http import HttpResponse, JsonResponse
from .models import *
# from .models import Project as Projectt
from .models import student
from .msg import *
import json
from numpy import dot
import numpy as np
from numpy.linalg import norm

try:
    #import umap.umap_ as umap
    import numpy as np
    import math
    import random
    from k_means_constrained import KMeansConstrained
    print('kmeans')
    import gensim.downloader as api
    print('api')
    # wv_from_bin = np.zeros((50,100))
    wv_from_bin = api.load("glove-wiki-gigaword-50")
    # print(wv_from_bin['ios'])
except:
    print("NOT WORKING!")
    pass

def cos_sim(a, b):
    dot_product = np.dot(a, b) # x.y
    norm_a = np.linalg.norm(a) #|x|
    norm_b = np.linalg.norm(b) #|y|
    return dot_product / (norm_a * norm_b)
def recommend_project(request):
    # try:
    #         # current dummy recommend: no request body, just return whatever
    #     data = {"code":1,
    #     "msg":PROJECT_RECOMMEND_SUCCESS,
    #     "projectList":[{
    #       "projectId":"aaa",
    #       "projectName":"Jazz For All",
    #       "keywords":"Music",
    #       "type":["Android","IOS"],
    #       "skillWanted":"Python,Java"
    #      },{
    #       "projectId":"AAA",
    #       "projectName":"Project name",
    #       "keywords":"Keywords",
    #       "type":["Web","Android"],
    #       "skillWanted":"Skill Wanted"
    #      }]}
    #     return HttpResponse(json.dumps(data), content_type='application/json')
        
    # except Exception as e:
    #     data = PROJECT_MSG(msg=PROJECT_RECOMMEND_FAIL) ###
    #     return HttpResponse(json.dumps(data), content_type='application/json')

    # req = json.loads(request.body)
    ##########
    print('start')
    try:
        print('s1')
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    except:
        print('s2')
        # HTTP_X_TOKEN = req['HTTP_X_TOKEN']
    
    try:
        # print('???')
        user = student.objects.get(uid=HTTP_X_TOKEN)
        print(11)
        user_profile = {"name": user.name,
                        "eml": user.email,
                        "Field of Interest": ' '.join(user.profile.fieldInt),
                        "Type of End Product": user.profile.prod,
                        "Programming Language": ' '.join([i["skillName"] for i in user.profile.skillLevel if '#' not in i["skillName"]])}

        print(223)
        domain_val_embds = []
        for domain in ["Field of Interest","Type of End Product","Programming Language"]:
            try:
                embd_vector = sum([wv_from_bin[i.lower()] for i in user_profile[domain].split()])/len(user_profile[domain].split()) # 9*300
                domain_val_embds.append(embd_vector)
            except:
                pass
        stu = sum(domain_val_embds)

            ## currently only similarity, diff --> 1 / domain_val_embd       300 each

        # user = student.objects.get(uid=HTTP_X_TOKEN)
        # embd_student_fieldInt = sentence_embedder(" ".join(user.fieldInt))
        # embd_student_skillLevell = sentence_embedder(" ".join([item['skillName'] for item in user.skillLevel]))
        # embd_student = (embd_student_fieldInt + embd_student_skillLevell) / 2 # Norm
        try:
            all_projects = Project.objects.all()
            print('all_projects')
            print(all_projects)
        except:
            print('eel')

        all_profiles = []
        for proj in all_projects:
            print(proj.projectId)
            # print(proj['projectId'])
            all_profiles.append({"id": proj.projectId,
                            "projectName": proj.projectName,
                            "skillWanted": proj.skillWanted,
                            "Field of Interest": proj.keywords,
                            "Type of End Product": ' '.join(proj.type),
                            "Programming Language": ' '.join([i for i in proj.intendedLanguage if '#' not in i])})
        prj_all_embeds = []
        for idx in range(len(all_projects)):
    ### type, intendedLanguage: list(str); keywords: str
            domain_val_embds = []
            for domain in ["Field of Interest","Type of End Product","Programming Language"]:
                try:
                    embd_vector = sum([wv_from_bin[i.lower()] for i in all_profiles[idx][domain].split()])/len(all_profiles[idx][domain].split()) # 9*300
                    domain_val_embds.append(embd_vector)
                except:
                    pass
            domain_val_embds = sum(domain_val_embds)
            prj_all_embeds.append(domain_val_embds)


        print(33)
        cossim = [cos_sim(stu,p) for p in prj_all_embeds]
        print(cossim)
        top3_project_ids = np.argsort(cossim)[::-1][:min(3,len(cossim))]
        proj_infos = []
        for top3_project_id in top3_project_ids:
            proj_info = {"projectId": all_profiles[top3_project_id]["id"],
                         "projectName": all_profiles[top3_project_id]["projectName"],
                         "keywords": all_profiles[top3_project_id]["Field of Interest"],
                         "type": all_profiles[top3_project_id]["Type of End Product"],
                         "skillWanted": all_profiles[top3_project_id]["skillWanted"],}
            proj_infos.append(proj_info)
        data = {"code":1,
                "msg":PROJECT_RECOMMEND_SUCCESS,
                "projectList":proj_infos
                }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_RECOMMEND_FAIL) ###
        return HttpResponse(json.dumps(data), content_type='application/json')
