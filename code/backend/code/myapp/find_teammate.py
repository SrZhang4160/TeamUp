from django.http import HttpResponse, JsonResponse
from .models import student, User, Project, Profile
from .msg import *
import json
import re

# Dummy return_all_project --> to be modified
def return_students(request):
    try:
        req = json.loads(request.body)
        # print(req)
        data = FIND_TEAMMATE_SEARCH_RETURN(code=1, msg=TEAMMATE_SEARCH_SUCCESS)
        try:
            data = FIND_TEAMMATE_SEARCH_RETURN(code=1, msg=TEAMMATE_SEARCH_SUCCESS)
            # current dummy search: with no inputword and selectword
            all_students = student.objects.all()
            # print(len(all_students))
                       
            if req['inputword'] == '':
                data = FIND_TEAMMATE_SEARCH_RETURN(code=1, msg=TEAMMATE_SEARCH_SUCCESS)
                for user in all_students:
                    try:
                        p = Profile.objects.get(uid= user.uid)
                        data["userlist"].append({  "userId":user.uid,
                        "avatar":user.avatar.name,
                        "showVal":p.name+' '+p.grade+' '+p.major,
                        "email":user.email})
                    except:
                        pass
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                data = FIND_TEAMMATE_SEARCH_RETURN(code=1, msg=TEAMMATE_SEARCH_SUCCESS)
                if len(req['inputword']) > 0:
                    try:
                        for user in all_students:
                            try: # some earliest users lack a profile (or other problems)!!
                                p = Profile.objects.get(uid= user.uid)
                                search_str = p.name+p.grade+p.major+p.prod+p.email+p.exep+p.mbti
                                search_str += "".join([s['skillName'] for s in p.skillLevel])
                                try:
                                    search_str += "".join(p.fieldInt) #[{'value': 'Education'}, {'value': 'Grocery', 'key': 1648750485048}]
                                except:
                                    search_str += "".join([s['value'] for s in p.fieldInt])
                                search_str = "".join([s for s in search_str if s!= ' ']) #
                                # print(search_str)
                                # search_str = " ".join(user[search_domains[_key]]) if type( user[search_domains[_key]]) is list else student[search_domains[_key]]
                                if re.search(req['inputword'], search_str, re.IGNORECASE):
                                    # avoid duplicate project append
                                    # print(user.uid)
                                    # print(user.avatar.name)
                                    # print(user.email)
                                    # print([u['userId'] for u in data["userlist"]])
                                    # print({  "userId":user.uid,
                                    #     "avatar":user.avatar.name,
                                    #     "showVal":p.name+' '+p.grade+' '+p.major,
                                    #     "email":user.email})
                                    if user.uid not in [u['userId'] for u in data["userlist"]]:
                                        data["userlist"].append({  "userId":user.uid,
                                        "avatar":user.avatar.name,
                                        "showVal":p.name+' '+p.grade+' '+p.major,
                                        "email":user.email})
                            except:
                                pass
                        return HttpResponse(json.dumps(data), content_type='application/json')
                    except:
                        data = TEAMMATE_MSG(msg=TEAMMATE_RETURN_ALL_FAIL3) ####
            return HttpResponse(json.dumps(data), content_type='application/json')

        except:
            data = TEAMMATE_MSG(msg=TEAMMATE_RETURN_ALL_FAIL1) ####
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = TEAMMATE_MSG(msg=TEAMMATE_RETURN_ALL_FAIL2) ###
        return HttpResponse(json.dumps(data), content_type='application/json')
