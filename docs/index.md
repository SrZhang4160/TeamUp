# TeamUp!

In many courses, students need to find their partners without much information about each other. The method they use to form a group now is to group with people they know or post a message through Slack, which is inefficient and hard to create the team that best fits them. Therefore, we propose this app to gather information about all the students and provide team formation services considering multiple conditions. We aim to make your team formation much easier and more fun!


## User Manual

More detailed guide at 
* [User Manual](https://docs.google.com/document/d/1BIOBSlkrhK4A-KTrATP1yNt82MWt9KnO0kNrsbVQAWM/edit?usp=sharing)

If you are an instructor, contact the admin to create an instructor account. Log in to your account and choose a model for students to form teams. Choose or add criteria for team formation.

If you are a student, create an account and log in to your account first. When you first log in to your account, you have to fill out your profile to unlock other app functions. Don't hesitate to be a team leader if you have a good project idea! You can form your group and add or remove team members! If you only want to find teams based on your preferences, type in your criteria and search for the teas that fit you best!

## API Reference
```diff
+ == Iteration 1 ==
```

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/login-test   |   Post   |    TeamUp user login  |

```diff
Request parameters: 
```
> Raw parameter: login code \
> { \
> email: “email”, \
>  password: “password”, \
> } 

```diff
Response example:
```
> { \
> 'code': 1, \
>              'msg': "Login Successfully!", \
>              'toked': "token", \
>              'email':"email", \
>              'name': "name", \
>              'type': "0" or "1" or "2" \
>             }


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/fill_profile_api   |   Post   |    TeamUp student profile filling  |

```diff
Request parameters: 
```

> { \
 >“email”: “email”, \
 >“password”: “password”, \
 >"name": "admin", \
 >"major": "123456", \
 >"skillLevel": "expert", \
 >"LeadInt": "Yes", \
 >"grade" : "Graduate", \
 >"fieldInt" : "Yes", \
 >"prod" : "NA", \
 >"exep" : "NA", \
 >"checkedLanguage" : ["C++", "Jave", "Python"], \
 >"otherLanguage" : "Lua", \
 >"prefer" : "prefer@jhu.edu", \
 >"preferNot" : "preferNot@jhu.edu", \
 >"HTTP_X_TOKEN" : HTTP_X_TOKEN \
}

```diff
Response example:
```
>	{ \
> "code": 1, \
> "msg": "suc." \
>}


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/create_student_api   |   Post   |    TeamUp account creation  |

```diff
Request parameters: 
```

> { \
> “email”: “Email”, \
> “password”: “Password”, \
> "name": "User", \
> "avatar": "Avatar" \
>}

```diff
Response example:
```
>{ \
> "code":  1, \
> "msg": "Account create successfully" \
>}


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/create_project_api  |   Post   |    A student can create a project as the team leader  |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": "-1", \
>                        "project_name": "project_name", \
>                        "team_name" : "team_name", \
>                        "project_idea" : "project_idea", \
>                        "project_Intro" : "project_Intro", \
>                        "intended_langs" : ["c++", "java"], \
>                        "other_langs" : "other_langs", \
>                        "skills_wanted": "skills_wanted", \
>                        "keywords": "keywords" \
>}


```diff
Response example:
```
>{ \
> "code":  1, \
> "msg": "Create Project Successfully!" \
>}


```diff
+ == Iteration 2 ==
```


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/return_all_project_api |   Post   |    return and exhibit the list of projects that fit criteria |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> "inputword":"xxx", \
> "selectword":["IOS","JAVA"] \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> "projectList":[{ \
>  "projectId":"aaa", \
>  "projectName":"bbb", \
>  "keywords":"CC", \
>  "type":["IOS","Android"], \
>  "skillWanted":"DDD" \
> },{ \
>  "projectId":"AAA", \
>  "projectName":"BBB", \
>  "keywords":"CCCC", \
>  "type":["Web applocation"], \
>  "skillWanted":"DDD" \
> }] \
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/return_student_with_proj_num_api|   Post   |    return the number of students with a project |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> "numval":22 \
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/return_student_without_proj_num_api|   Post   |    return the number of students without a project |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> "numval":22 \
> }


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/recommend_project_api|   Post   |    recommends projects (<= 3) based on user's profile |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> "projectList":[{ \
>  "projectId":"aaa", \
>  "projectName":"bbb", \
>  "keywords":"CC", \
>  "type":["IOS","Android"], \
>  "skillWanted":"DDD" \
> },{ \
>  "projectId":"AAA", \
>  "projectName":"BBB", \
>  "keywords":"CCCC", \
>  "type":["Web applocation"], \
>  "skillWanted":"DDD" \
> }] \
> }




| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/create_project_api|   Post   |    a student can create a project (and automatically become team leader), filling in related info |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
>  "projectName":"BBB", \
>  "projectIntroduction": "I'm a bad guy", \
>  "teamName": "All the good girls go to hell", \
>  "keywords":"CCCC", \
>  "intendedLanguage": ["Python","JAVA"], \
>  "otherLanguage": ["Javascript"], \
>  "type":["Web applocation"], \
>  "skillWanted":"DDD", \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/project_page_api|   Post   |    view a project page, the project page will show differently base on the user role of that project. Also, this page can be look up by either project ID(from main lobby) or user ID(from "My Group") |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
>  "projectId":"aaa" \
> }

OR

>{ \
> "HTTP_X_TOKEN": xx, \
>  "UserId":"ffewf2432foiewfi234325" \
> }


```diff
Response example:
```
> {
> "code": 1,\
> "msg": "success",\
>  "userRole": 1,\
>  "project": {\
>  "projectId": "aaa",\
>  "projectName": "bbb",\
>  "projectIntroduction": "XX",\
>  "keywords": "CC",\
>  "intendedLanguage": ["JAVA", "OTHER"],\
>  "otherLanguage": "VUE",\
>  "type": ["IOS"],\
>  "skillWanted": "DDD",\
>  "teamName": "aa",\
>  "teamLeader": "AAA@jhu.edu",\
>  "teamLeaderName": "AAA",\
>  "teamMemName": [{\
>  "name": "bbb",\
>  "eml": "BBB@jhu.edu"\
>  }, {\
>  "name": "ccc",\
>  "eml": "CCC@jhu.edu"\
>  }]\
>  }\
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/apply_to_project_api|   Post   |    a student apply a project if not already in a project |

```diff
Request parameters: 
```
> { \
> "HTTP_X_TOKEN": xx, \
>  "projectId":"aaa" \
> }


```diff
Response example:
```
> { \
> "code":1, \
> "msg":"Success", \
> }


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/del_project_api|   Post   |    a team leader can terminate a project he/she owns|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
>  "projectId":"aaa" \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> }


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/project_page_view_api|   Post   |    Project edit view (different allowed actions to teamLeader/teamMember/others) |

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
>  "projectId":"aaa" \
> }


```diff
Response example:
```
>{\
>  "code": 1,\
>  "msg": "Success",\
>  "userRole": 1,\
>  "project": {\
>  "projectId": "aaa",\
>  "projectName": "bbb",\
>  "projectIntroduction": "XX",\
>  "keywords": "CC",\
>  "intendedLanguage": ["JAVA", "OTHER"],\
>  "otherLanguage": "VUE",\
>  "type": ["IOS"],\
>  "skillWanted": "DDD",\
>  "teamName": "aa",\
>  "teamLeader": "AAA@jhu.edu",\
>  "teamLeaderName": "AAA",\
>  "teamMemName": [{\
>  "name": "bbb",\
>  "eml": "BBB@jhu.edu"\
>  }, {\
>  "name": "ccc",\
>  "eml": "CCC@jhu.edu"\
>  }]\
>  }\
> }


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/project_page_edit_api|   Post   |    save the edited detail|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
>  "projectId":"aaa", \
>  "projectName":"bbb", \
>  "projectIntroduction":"CC", \
>  "keywords":"CC", \
>  "intendedLanguage":["JAVA","OTHER"], \
>  "otherLanguage":"VUE", \
>  "type":["IOS"], \
>  "skillWanted":"DDD", \
>  "teamName":"aa", \
> "teamMemName":[{ \
>  "name": "", \
>  "eml": "D@jhu.edu" \
>  }, { \
>  "name": "", \
>  "eml": "E@jhu.edu" \
>  }] \
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> }


```diff
+ == Iteration 3 ==
```


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/project_page_exit_api|   Post   |    allow team members to exit the current project|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> "projectId":"aaa"\
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> }


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/find_teammate_api|   Post   |    Allow users to view full list of students and search by keyword|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> "inputword":"Grad"\
> }


```diff
Response example:
```
>{\
> "code":1,\
> "msg":"success",\
> "userlist":[{\
>  "userId":"aaa",\
>  "avatar":"dragon",\
>  "showVal":"Yuting Zhang，Grad，Computer Science",\
>  "email":"XXXX@JHU.EDU"\
> },{\
>  "userId":"bbb",\
>  "avatar":"chicken",\
>  "showVal":"Akshay，Grad，Computer Science",\
>  "email":"YYY@JHU.EDU"\
> }]\
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/query_profile_others_api|   Post   |    view other student's profile|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> "email":"YYY@JHU.EDU"\
> }


```diff
Response example:
```
>{\
> "code":1,\
> "msg":"success",\
> "userDetails":{\
>  "name":"SAN ZHANG",\
>  "major":"COMPUTER SCIENCE",\
>  "grade":"GRAD",\
>  "skillLevel":[\
>  {"skillName":"JAVA","level":"LOW"},\
>  {"skillName":"C++","level":"HIGH"}\
>  ],\
>  "leadInt":"HIGH",\
>  "fieldInt":["XX","YY"],\
>  "prod":["IOS","WEB"], \
>  "exep":"intern",\
>  "mbti":"estj-T",\
>  "email":"YYY@JHU.EDU"\
> },\
> "userProject":{\
>  "projectId":"aaa",\
>  "projectName":"bbb"\
> }\
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/retrieve_contact_api|   Post   |    get contact list of current user, display by last message time|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> }


```diff
Response example:
```
>{\
> "code":1,\
> "msg":"success",\
> "contactsList":[{\
>  "userName":"aaa",\
>  "userId":"bbb",\
>  "email":"YYY@JHU.EDU",\
>  "lastTime":"2022-03-23 12:23",\
>  "unread":1\
> },{\
>  "userName":"CCC",\
>  "userId":"DDD",\
>  "email":"QWE@JHU.EDU",\
>  "lastTime":"2022-03-22 12:23",\
>  "unread":0\
> }]\
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/send_message_api|   Post   |    allow students to send message to other students via email address|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> "sendTo":"YYY@JHU.EDU",\
> "sendMessage":"HELLO…… best"\
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/retrieve_message_api|   Post   |    get message detail|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
>  "email":"YYY@JHU.EDU",\
> "page":1,\
> "size":20\
> }


```diff
Response example:
```
>{\
> "code":1,\
> "msg":"success",\
> "messageList":[{\
>  "message":"aaa",\
>  "sendTime":"2022-03-23 12:23",\
>  "isme":1,\
>  "avatar":"dragon"\
> },{\
>  "message":"aaa",\
>  "sendTime":"2022-03-23 12:23",\
>  "isme":1,\
>  "avatar":"hmbb"\
> }]\
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/query_profile_api|   Post   |    Page shows when user access "My Profile" page|

```diff
Request parameters: 
```

>{ \
> "HTTP_X_TOKEN": xx, \
> "projectId":"aaa"\
> }


```diff
Response example:
```
>{\
> "code":1,\
> "msg":"success",\
> "userDetails":{\
>  "name":"SAN ZHANG",\
>  "major":"COMPUTER SCIENCE",\
>  "grade":"GRAD",\
>  "skillLevel":[\
>  {"skillName":"JAVA","level":"LOW"},\
>  {"skillName":"C++","level":"HIGH"}\
>  ],\
>  "leadInt":"HIGH",\
>  "fieldInt":["XX","YY"],\
>  "prod":"WEB"\
>  "exep":"intern",\
>  "mbti":"estj-T",\
>  “prefer” : “aaa@jhu.edu”\
>  "preferNot" :  “aaa@jhu.edu”\
>  "email":"YYY@JHU.EDU"\
> },\
> "userProject":{\
>  "projectId":"aaa",\
>  "projectName":"bbb"\
> }\
> }

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/update_profile_api|   Post   |    Save the change user made to own profile|

```diff
Request parameters: 
```

>{\
> "userDetails":{\
>  "name":"SAN ZHANG",\
>  "major":"COMPUTER SCIENCE",\
>  "grade":"GRAD",\
>  "skillLevel":[\
>  {"skillName":"JAVA","level":"LOW"},\
>  {"skillName":"C++","level":"HIGH"}\
>  ],\
>  "leadInt":"HIGH",\
>  "fieldInt":["XX","YY"],\
>  "prod":"WEB"\
>  "exep":"intern",\
>  "mbti":"estj-T",\
>  “prefer” : “aaa@jhu.edu”\
>  "preferNot" :  “aaa@jhu.edu”\
>  "email":"YYY@JHU.EDU"\
> },\
> }


```diff
Response example:
```
>{ \
> "code":1, \
> "msg":"Success", \
> }

```diff
+ == Iteration 4 ==
```
| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/project_lang_distribution_api|   Post   |   Project Language stats |

```diff
Request parameters: 
```
>{ \
> "HTTP_X_TOKEN": xx, \
> }

```diff
Response example:
```
>{"code":1,"msg":"suc", \
> "projectsLanguages":[{ \
>  "name":"java", \
>  "percentage":30.55 \
> },{ \
>  "name":"Python", \
>  "percentage":69.45 \
> }]}


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/student_interest_field_distribution_api|   Post   |   Student Interest Field stats |
```diff
Request parameters: 
```
>{ \
> "HTTP_X_TOKEN": xx, \
> }

```diff
Response example:
```
>{"code":1,"msg":"suc", \
> "interestedFields":[ \
> {"name":"Books","num":130.55}, \
> {"name":"health","num":230.55}, \
> {"name":"Music","num":330.55}, \
> {"name":"Education","num":320.55}, \
> {"name":"Grocery","num":260.55}, \
> {"name":"Sports","num":120.55}, \
> {"name":"Travel","num":420.55}, \
> {"name":"Lifestyle","num":230.55}, \
> {"name":"Utilties","num":180.55}, \
> {"name":"Others","num":269.45} \
> ]}

| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/annos_create_msg_api|   Post   |   Instructor creates a new announcement |
```diff
Request parameters: 
```
>{ \
> "HTTP_X_TOKEN": xx, \
> "name":"AAAA", \
> "val":"CCCCC" \
> }

```diff
Response example:
```
>{"code":1,"msg":"suc", \
> }]}


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/annos_list_msg_api|   Post   |   Instructor gets a list of all previous announcements |
```diff
Request parameters: 
```
>{ \
> "HTTP_X_TOKEN": xx, \
> }

```diff
Response example:
```
>{"code":1,"msg":"suc", \
> "announcements":[{ \
> "id":"AAA","name":"AAA","val":"AAA", \
> "releaseTime":"2022-04-06 12:33"},{ \
>  "id":"BBB","name":"BBB","val":"BBB", \
> "releaseTime":"2022-04-08 12:33"}]}


| API address | Request method| Description |
| :----------- | :------------: | ------------: |
| http://47.253.99.242/annos_retrieve_msg_api|   Post   |   Instructor retrieves a particular announcement |
```diff
Request parameters: 
```
>{ \
> "HTTP_X_TOKEN": xx, \
> }

```diff
Response example:
```
>{"code":1,"msg":"suc", \
> "announcements":[{ \
> "id":"AAA","name":"AAA","val":"AAA", \
> "releaseTime":"2022-04-06 12:33"},{ \
>  "id":"BBB","name":"BBB","val":"BBB", \
> "releaseTime":"2022-04-08 12:33"}]} \



## About Us!

We are Four-Z-One-X.
