import sys
import django
import os

sys.path.insert(0, '../')

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#sys.path.append(BASE_DIR)

#os.environ.setdefault('DJANGO_SETTINGS_MODULE','projectname.settings')
#django.setup()

from django.http import HttpResponse, JsonResponse
##from rest_framework.authtoken.models import Token
from .models import instructor,student, User
from .msg import *
import json

#ist = instructor(email="admin@jhu.edu", password="123456")
#ist.save()

try:
    ins = instructor.objects.create(name='Instructor', avatar='tiger', type=1, password='123456', email='admin@jhu.edu')
    ins.uid = ins.generate_key()
    ins.save()
except:
    pass