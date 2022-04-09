from django.http import HttpResponse, JsonResponse
from .models import student, User, Project
from .msg import *
import json
import re

def return_student_without_proj_num(request):
    try:
        try:
            all_students = student.objects.values()
            if len(all_students) == 0:
                data = STUDENT_PROJ_MSG(code=1, msg=STUDENT_PROJECT_NUM_QUERY_SUCCESS, numval=0) ####
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:

                student_with_projects = []
                for tmp_student in all_students:
                    if tmp_student['projectId'] is not None:
                        if tmp_student['is_leader'] is True:
                            student_with_projects.append(tmp_student['email'])

                all_projects = Project.objects.values()            
                for project in all_projects:
                    if project['teamMemName'] is not None:
                        for team_mem in project['teamMemName']:
                            if team_mem['eml'] not in student_with_projects:
                                student_with_projects.append(team_mem['eml'])
 
                student_without_projects = []
                for tmp_student in all_students:
                    if tmp_student['email'] not in student_with_projects and tmp_student['email'] not in student_without_projects:
                        student_without_projects.append(tmp_student['email'])
                data = STUDENT_PROJ_MSG(code=1, msg=STUDENT_PROJECT_NUM_QUERY_SUCCESS, numval=len(student_without_projects)) ####
                return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            data = PROJECT_MSG(msg=STUDENT_PROJECT_NUM_QUERY_FAIL) ####
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=STUDENT_PROJECT_NUM_QUERY_FAIL) ###
        return HttpResponse(json.dumps(data), content_type='application/json')


def return_student_with_proj_num(request):
    try:       
        try:
            all_students = student.objects.values()
            if len(all_students) == 0:
                data = STUDENT_PROJ_MSG(code=1, msg=STUDENT_PROJECT_NUM_QUERY_SUCCESS, numval=0) ####
                return HttpResponse(json.dumps(data), content_type='application/json')
            else:
                student_with_projects = []
                for tmp_student in all_students:
                    if tmp_student['projectId'] is not None:
                        if tmp_student['is_leader'] is True:
                            student_with_projects.append(tmp_student['email'])
                
                for project in Project.objects.values() :
                    if project['teamMemName'] is not None:
                        for team_mem in project['teamMemName']:
                            if team_mem['eml'] not in student_with_projects:
                                student_with_projects.append(team_mem['eml'])

                data = STUDENT_PROJ_MSG(code=1, msg=STUDENT_PROJECT_NUM_QUERY_SUCCESS, numval=len(student_with_projects)) ####
                return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            data = PROJECT_MSG(msg=STUDENT_PROJECT_NUM_QUERY_FAIL) ####
            return HttpResponse(json.dumps(data), content_type='application/json')
        
    except Exception as e:
        data = PROJECT_MSG(msg=STUDENT_PROJECT_NUM_QUERY_FAIL) ###
        return HttpResponse(json.dumps(data), content_type='application/json')