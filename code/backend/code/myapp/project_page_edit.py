from turtle import pd
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from .models import student, User, Project
from .msg import *
import json

def uid_exists(uid):
    return student.objects.filter(uid=uid).exists()  

def project_page_exit(request):
    try:
        req = json.loads(request.body)
        print(req)
        
        if request.environ.get('HTTP_X_TOKEN') is not None:
            HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
        else:
            HTTP_X_TOKEN = req['HTTP_X_TOKEN'] 
        
        ###### TODO IF TEAMLEADER EXIT, ALL WILL HAVE NO PROFILE GROUP + PROJECT ID
        if uid_exists(HTTP_X_TOKEN) is False:
            PROJECT_MSG(msg=PROJECT_CREATION_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            try:
                user = student.objects.get(uid=HTTP_X_TOKEN)
                try:
                    project = Project.objects.get(projectId=req['projectId'])
                except:
                    user = student.objects.get(uid=HTTP_X_TOKEN)
                    try:
                        if len(user.project.projectId) > 0 : 
                            project = user.project
                    except:
                        project = Project.objects.get(projectId=user.profile.userProject['projectId'])
                user.projectId = ""
                user.project = None
                user.profile.userProject = []
                new_teamMemName = []
                for team_mem in project.teamMemName:
                    if team_mem['eml'] != user.email:
                        new_teamMemName.append(team_mem)
                project.teamMemName = new_teamMemName
                user.profile.save()
                user.project.save()
                user.save()
                project.save()
                data = PROJECT_MSG(code=1, msg=PROJECT_EXIT_SUCCESS)
                print(data)
            except:
                data = PROJECT_MSG(msg=PROJECT_EDIT_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_EDIT_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

def project_page_edit(request):
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
                # create student profile and change student status to have already filled in profile info
                # student and profile have the same uid
                #user=student.objects.get(uid=HTTP_X_TOKEN)
                try:
                    project = Project.objects.get(projectId=req['projectId'])
                    user = student.objects.get(uid=HTTP_X_TOKEN)
                except:
                    user = student.objects.get(uid=HTTP_X_TOKEN)
                    try:
                        if len(user.project.projectId) > 0 : 
                            project = user.project
                    except:
                        project = Project.objects.get(projectId=user.profile.userProject['projectId'])
                project.projectIntroduction = req['projectIntroduction']
                project.keywords = req['keywords']
                project.intendedLanguage = req['intendedLanguage']
                project.otherLanguage = req['otherLanguage']
                project.type = req['type']
                project.skillWanted = req['skillWanted']
                project.teamName = req['teamName']
                project.teamMemName = []
                #import pdb; pdb.set_trace()
                for teamMemName in req['teamMemName']:
                    mem_eml = ""
                    for covercome_email_error_key in ["eml", "email"]:
                        if covercome_email_error_key in teamMemName.keys():
                            if len(teamMemName[covercome_email_error_key]) > 0:
                                mem_eml = teamMemName[covercome_email_error_key]
                    #import pdb; pdb.set_trace()
                    try:
                        _tmp_user = student.objects.get(email=mem_eml)
                        #import pdb; pdb.set_trace()
                        if _tmp_user.projectId is not None:
                            if len(_tmp_user.projectId) > 0:
                                if project.projectId != _tmp_user.projectId:
                                    data = PROJECT_MSG(msg=_tmp_user.name + " has belong to other project !")
                                    return HttpResponse(json.dumps(data), content_type='application/json')
                        _tmp_user_name = _tmp_user.name
                        _tmp_user.projectId = project.projectId
                        #### If ADD TEAM MEMBER, need to update team member's project
                        print('DEAD')
                        _tmp_user.project = Project.objects.get(projectId=project.projectId)
                        print('DEAD1')
                        # UPDATE PERSONAL INFO
                        _tmp_user.project.save()
                        print(_tmp_user.project)
                        _tmp_user.profile.userProject = {'projectId':_tmp_user.project.projectId, 'projectName':_tmp_user.project.projectName}
                        print('DEAD3')
                        _tmp_user.profile.save()
                        print('DEAD4')
                        _tmp_user.save()
                        print('DEAD5')
                    except:
                        _tmp_user_name = ""
                    _tmp_member = {"name": _tmp_user_name,
                                   "eml": mem_eml}
                    if _tmp_member not in project.teamMemName:
                        project.teamMemName.append(_tmp_member)
                filter_teamMemName = [mem for mem in project.teamMemName if (len(mem["name"])>0 and len(mem['eml'])>0) ]
                if len(filter_teamMemName) < 6:
                    filter_teamMemName = filter_teamMemName + [{"name": "", "eml": ""}] * (6 - len(filter_teamMemName))
                print(project.projectId)
                print(project.projectName)
                user.profile.userProject = {'projectId':project.projectId, 'projectName':project.projectName}
                user.profile.save()
                print('DEAD7')
                project.teamMemName = filter_teamMemName
                print('DEAD8')
                project.save()
                data = PROJECT_MSG(code=1, msg=PROJECT_EDIT_SUCCESS)
                
            except:
                data = PROJECT_MSG(msg=PROJECT_EDIT_FAIL)
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=PROJECT_EDIT_FAIL)
        return HttpResponse(json.dumps(data), content_type='application/json')

def project_page_view(request):
    req = json.loads(request.body)
    print(req)
    
    if request.environ.get('HTTP_X_TOKEN') is not None:
        HTTP_X_TOKEN = request.environ.get('HTTP_X_TOKEN')
    else:
        HTTP_X_TOKEN = req['HTTP_X_TOKEN']

    try:
        if uid_exists(HTTP_X_TOKEN) is False:
            PROJECT_MSG(msg=PROJECT_CREATION_NO_USER)
            return HttpResponse(json.dumps(data), content_type='application/json')
        else:
            # get project id and user email
            try:
                project = Project.objects.get(projectId=req['projectId'])
                user = student.objects.get(uid=HTTP_X_TOKEN)
            except:
                try:
                    user = student.objects.get(uid=HTTP_X_TOKEN)
                    try:
                        if len(user.project.projectId) > 0 : 
                            project = user.project
                    except:
                        project = Project.objects.get(projectId=user.profile.userProject['projectId'])
                except:
                    data =  {
                        "code": 0,
                        "msg": "You have not join any project yet, please find a project team in the main lobby.",
                        "userRole": 0,
                        "project": {}}
                    return HttpResponse(json.dumps(data), content_type='application/json')

            # --> check user status
            if project.teamLeader.email == user.email: # team leader
                userRole = 1 
            elif project.teamMemName is not None:
                if user.email in [mem['eml'] for mem in project.teamMemName]: # team member
                    userRole = 2
            elif user.projectId: # user has a group
                userRole = 4
            else: # user has no group
                userRole = 3
            
            try:
                if len(project.teamMemName) > 0:
                    data =  {
                        "code": 1,
                        "msg": PROJECT_RETRIEVE_SUCCESS,
                        "userRole": userRole,
                        "project": {
                                "projectId": project.projectId,
                                "projectName": project.projectName,
                                "projectIntroduction": project.projectIntroduction,
                                "keywords": project.keywords,
                                "intendedLanguage": project.intendedLanguage,
                                "otherLanguage": project.otherLanguage,
                                "type": project.type,
                                "skillWanted": project.skillWanted,
                                "teamName": project.teamName,
                                "teamLeader": project.teamLeader.email,
                                "teamLeaderName": project.teamLeader.name,
                                "teamMemName": project.teamMemName + [{"name": "", "eml": ""}] * (6 - len(project.teamMemName)) ,
                                "appliedList": project.applied_stu,
                                },
                                    }
                else:
                    data =  {
                        "code": 1,
                        "msg": PROJECT_RETRIEVE_SUCCESS,
                        "userRole": userRole,
                        "project": {
                                "projectId": project.projectId,
                                "projectName": project.projectName,
                                "projectIntroduction": project.projectIntroduction,
                                "keywords": project.keywords,
                                "intendedLanguage": project.intendedLanguage,
                                "otherLanguage": project.otherLanguage,
                                "type":  project.type,
                                "skillWanted": project.skillWanted,
                                "teamName": project.teamName,
                                "teamLeader": project.teamLeader.email,
                                "teamLeaderName": project.teamLeader.name,
                                "teamMemName": [{"name": "", "eml": ""} for i in range(6)],
                                "appliedList": project.applied_stu,
                                },
                        }
                    print(data)
                return HttpResponse(json.dumps(data), content_type='application/json')
            except:
                data =  {
                    "code": 0,
                    "msg": PROJECT_RETRIEVE_FAIL,
                    "userRole": 0,
                    "project": {}}
            return HttpResponse(json.dumps(data), content_type='application/json')
    except:
        data =  {
            "code": 0,
            "msg": PROJECT_RETRIEVE_FAIL,
            "userRole": 0,
            "project": {}}
    return HttpResponse(json.dumps(data), content_type='application/json')