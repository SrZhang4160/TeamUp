from django.http import HttpResponse, JsonResponse
import json


# 添加学生信息
def addstinfo(request):
    try:
        # 读取前端传递的参数
        req = json.loads(request.body)
        print(req)

        print("tokenHTTP:" + request.environ['HTTP_X_TOKEN'])


        # 读取name
        rename = req.get("rename")
        print("rename:"+rename)
        # 读取pwd
        sex = req.get("sex")
        print("sex:" + sex)
        birthday = req.get("birthday")
        print("birthday:" + birthday)
        agree = req.get("agree")
        # 布尔值无法直接打印
        print("agree:")

        hobby = req.get("hobby")
        # 多选框无法直接打印
        print("hobby:")
        grade = req.get("grade")
        print("grade:" + grade)
        remark = req.get("remark")
        print("remark:" + remark)

        data = {
            'code': 1,
            'msg': "创建成功."
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    except Exception as e:
        # 出现意外情况返回异常
        data = {
            'code': 0,
            'msg': "err."
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


# 获取学生信息
def getstinfo(request):
    print("tokenHTTP:" + request.environ['HTTP_X_TOKEN'])
    data = {
        'code': 1,
        'msg': "获取数据成功.",
        'rename': 'real nam',
        'sex': "1",
        'birthday': "2022-02-20T16:00:00.000Z",
        'agree': True,
        'hobby': ['ZZZ', 'YYY'],
        'grade': "c",
        'remark': "remark",
    }
    return HttpResponse(json.dumps(data), content_type='application/json')


# 更新学生信息
def updatestinfo(request):
    data = {
        'code': -1,
        'msg': "登录异常."
    }
    return HttpResponse(json.dumps(data), content_type='application/json')
