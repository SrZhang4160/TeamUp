import django
import binascii
import os
import json
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractUser, AbstractBaseUser
from django.contrib.postgres.fields.jsonb import JSONField
from django.db.models import JSONField as BuiltinJSONField
# from django.contrib.postgres.fields import ArrayField

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Create your models here.
class User(AbstractBaseUser):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length = 25)
    type = models.PositiveSmallIntegerField(default=1)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    objects = UserManager()
    is_leader = models.BooleanField(null = True)
    projectId = models.CharField(max_length=200, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','password']

class instructor(models.Model):
    uid = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length = 25, null=True)
    type = models.PositiveSmallIntegerField(default=1, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    criteriaList = BuiltinJSONField(unique=False, null=True, default=list)
    group_selection = models.CharField(max_length = 25, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    # mandatory
    uid = models.CharField(max_length=500, null=True)
    name = models.CharField(max_length=500, null=True)
    major = models.CharField(max_length=500, null=True)
    # skillLevel = models.CharField(max_length=500, null=True)
    leadInt = models.CharField(max_length=500, null=True)
    grade = models.CharField(max_length=500, null=True)
    # fieldInt = models.CharField(max_length=300, null=True)
    fieldInt = BuiltinJSONField(unique=False, null=True, default=list)
    prod = models.CharField(max_length=500, null=True)
    exep = models.CharField(max_length=300, null=True)
    #checkedLanguage = models.CharField(max_length=500, null=True)
    # optional
    #otherLanguage = models.CharField(max_length=500, null=True)
    prefer = models.CharField(max_length=500, null=True)
    preferNot = models.CharField(max_length=500, null=True)
    # 
    skillLevel = BuiltinJSONField(unique=False, null=True, default=list)
    mbti = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    userProject = BuiltinJSONField(unique=False, null=True, default=list)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.name

class announcements(models.Model):
    uid = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    val = models.CharField(max_length=5000, null=True)
    releaseTime = models.CharField(max_length=200, null=True)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()
        
class student(models.Model):
    uid = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length = 25, null=True)
    type = models.PositiveSmallIntegerField(default=1, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    is_leader = models.BooleanField(null = True)
    projectId = models.CharField(max_length=200, null=True, blank=True)
    #applied_project = ArrayField(base_field=models.CharField(max_length=200, null=True),null=True)
    # applied_project = models.CharField(max_length=200, null=True)
    applied_project = BuiltinJSONField(null=True)
    contactsList = BuiltinJSONField(unique=True, null=True)
    messageList = BuiltinJSONField(unique=True, null=True)
# """message --> {
#                                     "message":req['sendMessage'],
#                                     "sender": sender.email,
#                                     "receiver": receiver.email,
#                                     "sendTime": now.strftime("%Y-%m-%d %H:%M"),
#                                     "isme": 0,
#                                     "avatar": sender.avatar.name
#                                     }
# contact --> {
#                                             "userName":receiver.name,
#                                             "userId":receiver.uid,
#                                             "email":receiver.email,
#                                             "lastTime": now.strftime("%Y-%m-%d %H:%M"),
#                                             "unread":0
#                                             }
#                                     """

    def create_profile(self, uid,
                             name,
                             major,
                             skillLevel,
                             leadInt,
                             grade,
                             fieldInt,
                             prod,
                             exep,
                             email="",
                             mbti="",
                             prefer="",
                             preferNot=""):
        self.profile = Profile(uid=uid, 
                               name=name,
                               major=major,
                               skillLevel=skillLevel,
                               leadInt=leadInt,
                               grade=grade,
                               fieldInt=fieldInt,
                               prod=prod,
                               exep=exep,
                               email=email,
                               mbti=mbti,
                               prefer=prefer,
                               preferNot=preferNot)
        # Save the profile into the database.
        self.profile.save()
        return self.profile

    def create_project(self, 
                        projectName,
                        teamName,
                        projectIntroduction,
                        intendedLanguage,
                        otherLanguage,
                        type,
                        skillWanted,
                        keywords,
                        ):
        self.project = Project( projectName=projectName,
                                teamName=teamName,
                                projectIntroduction=projectIntroduction,
                                intendedLanguage=intendedLanguage,
                                otherLanguage=otherLanguage,
                                type=type,
                                skillWanted=skillWanted,
                                keywords=keywords)
        # Save the profile into the database.
        self.project.save()
        return self.project
    
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.name

class Project(models.Model):
    #projectId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    projectId = models.CharField(max_length=200, null=True)
    projectName = models.CharField(max_length=200, null=True)
    projectIntroduction = models.CharField(max_length=800, null=True)
    keywords = models.CharField(max_length=200, null=True)
    intendedLanguage = BuiltinJSONField(unique=False, null=True, default=list)
    otherLanguage = BuiltinJSONField(unique=False, null=True, default=list)
    type = BuiltinJSONField(unique=False, null=True, default=list) # prev name type is inappropriate
    skillWanted = models.CharField(max_length=200, null=True)

    teamName = models.CharField(max_length=200, null=True)
    teamLeader = models.OneToOneField(student, on_delete=models.SET_NULL, null=True)
    # project_idea = models.CharField(max_length=800, null=True)
    #teamMemName = ArrayField(base_field=models.EmailField(unique=True, null=True),null=True)
    # teamMemName = models.JsonField(unique=True, null=True) # 暂时用Json, 后面再研究
    teamMemName = BuiltinJSONField(unique=False, null=True, default=list) # 暂时用Json, 后面再研究
    #intendedLanguage = ArrayField(base_field=models.CharField(max_length=200, null=True),null=True)
    #skillWanted = ArrayField(base_field=models.CharField(max_length=200, null=True),null=True)
    #applied_stu = ArrayField(base_field=models.EmailField(unique=True, null=True),null=True)
    applied_stu = BuiltinJSONField(unique=False, null=True, default=list) # 暂时用Char, 后面再研究
    
    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.projectName
    
class criteria(models.Model):
    criteriaId = models.CharField(max_length=200, null=True)
    criteriaName = models.CharField(max_length=200, null=True)
    criteriaNum = models.SmallIntegerField(default=0, null=True)
    criteriaPption = models.CharField(max_length=200, null=True)
            
class prj_group(models.Model):
    groupTag = models.CharField(max_length=200, null=True)
    groupinfo = BuiltinJSONField(unique=False, null=True, default=list)

class contact(models.Model):
    contactTag = models.CharField(max_length=200, null=True)
    instructorName = models.CharField(max_length=200, null=True)
    instructorEmail = models.CharField(max_length=200, null=True)
    zoomLink = models.CharField(max_length=200, null=True)
    Ta = BuiltinJSONField(unique=False, null=True, default=list)
    officeHour  = BuiltinJSONField(unique=False, null=True, default=list)
    