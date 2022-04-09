LOGIN_SUCCESS="Login Successfully!"
LOGIN_ERROR="Login error"
LOGIN_PASSWD_WRONG="Wrong Password!"
LOGIN_NOT_EXIST="User does not exist."

LOGOUT_SUCCESS="Logout Successfully!"
LOGOUT_ERROR="Logout error"

USER_DICT = {0: "NonFilledStudent", 1: "Instructor", 2:"FilledStudent"}

PROFILE_CREATE_USER_SUCCESS="success ! account has been created."
PROFILE_CREATE_USER_EMAIL_HAS_REGISTERED="email has been registered."
PROFILE_CREATE_USER_ERROR="error."

PROFILE_UPDATE_NO_USER="error, no user!"
PROFILE_UPDATE_SUCCESS="suc."
PROFILE_UPDATE_FAIL="fail."
PROFILE_UPDATE_DUMMPY_INPUT="At least one of the mandatory fields are empty!!"

PROFILE_FILL_NO_USER="error, no user!"
PROFILE_FILL_SUCCESS="suc."
PROFILE_FILL_FAIL="fail."

PROFILE_QUERY_NO_USER="error, no user!"
PROFILE_QUERY_SUCCESS="suc."
PROFILE_QUERY_FAIL="fail."

PROJECT_APPLY_SUCCESS="Apply success"
PROJECT_APPLY_FAIL="Apply fail"
PROJECT_EDIT_SUCCESS="Edit success"
PROJECT_EDIT_FAIL="Edit fail"
PROJECT_DEL_SUCCESS="Del success"
PROJECT_DEL_FAIL="Del fail"


STUDENT_PROJECT_NUM_QUERY_SUCCESS="Student project num query success"
STUDENT_PROJECT_NUM_QUERY_FAIL="Student project num query fail"

PROJECT_CREATION_FAIL = "Project creation failed!"
PROJECT_CREATION_NO_USER = "Student does not exist"
PROJECT_FILL_FAIL = "Project fill failed!"
PROJECT_FILL_SUCCESS = "Create Project Successfully!"
PROJECT_SEARCH_EMPTY_SUCCESS = "Success Search Projects with empty criteria"
PROJECT_SEARCH_VALID_SUCCESS = "Success Search Projects with valid criteria"
PROJECT_RETRIEVE_SUCCESS = "Success retrieving project page."
PROJECT_RETRIEVE_FAIL = "Failure retrieving project page!!"
PROJECT_RECOMMEND_FAIL = "Cannot recommend project!"
PROJECT_RECOMMEND_SUCCESS = "Success recommend dummy Projects with no algorithm whatsoever"
PROJECT_RETURN_ALL_FAIL1 = "Cannot return all projects: inputword/selectword problem!"
PROJECT_RETURN_ALL_FAIL2 = "Cannot return all projects: HTTP_X_TOKEN or request body problem!"

TEAMMATE_SEARCH_SUCCESS = "Success Search Students with valid criteria"
TEAMMATE_RETURN_ALL_FAIL1 = "Cannot return all students: inputword problem!"
TEAMMATE_RETURN_ALL_FAIL2 = "Cannot return all students: HTTP_X_TOKEN or request body problem!"
TEAMMATE_RETURN_ALL_FAIL3 = "???!"

def CREATE_USER_MSG(code=0, msg=""):
    return {"code": code,
            "msg": msg}

def PROFILE_MSG(code=0, msg=""):
    return {"code": code,
            "msg": msg}

def LOGIN_RETURN_MSG(code=0, msg="", type=-1, token="", email="", name="", uid="", HTTP_X_TOKEN=""):  
    return {"code": code,
            "msg": msg,
            "type": type,
            "token": token,
            "email": email,
            "name": name,
            }

def LOGOUT_RETURN_MSG(code=0, msg=""):  
    return {"code": code,
            "msg": msg,      
            }

def PROJECT_MSG(code=0, msg=""):
    return {"code": code,
            "msg": msg}

def PROJECT_MSG_SEARCH_RETURN(code=0, msg=""):
    return {
            "code":code,
            "msg":msg,
            "projectList":[]
            }

def STUDENT_PROJ_MSG(code=0, msg="", numval=-1):
    return {"code": code,
            "msg": msg,
            "numval": numval}
    
def FIND_TEAMMATE_SEARCH_RETURN(code=1, msg=""):
    return {
            "code":code,
            "msg":msg,
            "userlist":[]
            }

def TEAMMATE_MSG(code=0, msg=""):
    return {"code": code,
            "msg": msg}