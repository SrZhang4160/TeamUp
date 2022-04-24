from django.contrib import admin
from django.urls import path

from myapp import views as myapp_views
from myapp import login as myapp_login
from myapp import user as myapp_user
from myapp import stinfo as myapp_stinfo
from myapp import profile as myapp_profile
from myapp import create_project as myapp_create_project
from myapp import return_all_project as myapp_return_all_project
from myapp import recommend_project as myapp_recommend_project
from myapp import project_page as myapp_project_page
from myapp import apply_to_project as myapp_apply_to_project_page
from myapp import project_page_edit as myapp_project_page_edit
from myapp import return_student_num as myapp_return_student_num
from myapp import del_project as myapp_del_project
from myapp import find_teammate as myapp_find_teammate
from myapp import communication as myapp_communication
#from myapp import mygroup as myapp_mygroup_project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vue-test', myapp_views.vue_test),
    # Login Logout登录 退出
    path('login-test', myapp_login.loginPage),
    path('logout-test', myapp_login.logoutPage),
    # 获取用户信息
    path('userinfo', myapp_user.userinfo),
    # 添加、查看、修改学生信息
    path('addstinfo_api', myapp_stinfo.addstinfo),
    path('getstinfo_api', myapp_stinfo.getstinfo),
    path('updatestinfo_api', myapp_stinfo.updatestinfo),
    # fill in Profile
    path('create_student_api', myapp_profile.create_student),
    path('fill_profile_api', myapp_profile.fill_profile),

    path('create_project_api', myapp_create_project.create_project),
    path('return_all_project_api', myapp_return_all_project.return_all_project),
    path('recommend_project_api', myapp_recommend_project.recommend_project),
    path('project_page_api', myapp_project_page.project_page),
    path('apply_to_project_api', myapp_apply_to_project_page.apply_to_project),
    # view and edit project
    path('project_page_view_api', myapp_project_page_edit.project_page_view),
    path('project_page_edit_api', myapp_project_page_edit.project_page_edit),
    path('project_page_exit_api', myapp_project_page_edit.project_page_exit),
    # return student num
    path('return_student_with_proj_num_api', myapp_return_student_num.return_student_with_proj_num),
    path('return_student_without_proj_num_api', myapp_return_student_num.return_student_without_proj_num),
    # del project
    path('del_project_api', myapp_del_project.del_project),
    # My group
    # path('mygroup_page_api', myapp_mygroup_project.del_project),
    # 1.1 find teammate
    path('find_teammate_api', myapp_find_teammate.return_students),
    #.
    
    #3.2 retrieve contact
    path('retrieve_contact_api', myapp_communication.retrieve_contact),
    #3.3 send message
    path('send_message_api', myapp_communication.send_message),
    #3.4 retrieve message
    path('retrieve_message_api', myapp_communication.retrieve_message),
        # 4.1 query profile 
    path('query_profile_api', myapp_profile.query_profile),
    # 2.1 query profile (by other student)
    path('query_profile_others_api', myapp_profile.query_profile_others),
    #4.2 edit_profile
    path('update_profile_api', myapp_profile.update_profile)
]