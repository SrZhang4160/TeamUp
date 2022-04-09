from django.contrib import admin

# Register your models here.
from .models import User, student, instructor, Profile

admin.site.register(User)
admin.site.register(student)
admin.site.register(instructor)
admin.site.register(Profile)