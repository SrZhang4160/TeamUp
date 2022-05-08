const Mock = require('mockjs')

const data = Mock.mock({
    'list': {},
    'detail': {},
    "messageList": {},
    "sendMessage": {},
    "noticelist": [],
    "sendnotice": {},
    "noticedetails": {},
    "cylinderchart": [],
    "piechart": [],
    "userlist":[],
    "saveword":{},
    "readingdata":{}
  }

)
module.exports = [{
    url: '/vue-admin-template/message/list',
    type: 'post',
    response: config => {
      const items = data.list
      return {
        code: 1,
        msg: "获取成功",
        userlist: [{
          userId: "aaa",
          avatar: "dragon",
          showVal: "Yuting Zhang，Grad，Computer Science",
          email: "XXXX@JHU.EDU"
        }, {
          userId: "bbb",
          avatar: "chicken",
          showVal: "Akshay，Grad，Computer Science",
          email: "YYY@JHU.EDU"
        }]
      }
    }
  },
  {
    url: '/vue-admin-template/message/detail',
    type: 'post',
    response: config => {
      const items = data.userDetails
      return {
        code: 1,
        msg: "查询成功",
        userDetails: {
          name: "SAN ZHANG",
          major: "COMPUTER SCIENCE",
          grade: "GRAD",
          skillLevel: [{
              skillName: "JAVA",
              "level": "LOW"
            },
            {
              skillName: "C++",
              "level": "HIGH"
            }
          ],
          leadInt: "HIGH",
          fieldInt: ["XX", "YY"],
          prod: ["IOS", "WEB"],
          expe: "intern",
          mbti: "estj-T",
          email: "YYY@JHU.EDU"
        },
        userProject: {
          projectId: "aaa",
          projectName: "bbb"
        }
      }
    }
  },
  {
    url: '/vue-admin-template/message/messageList',
    type: 'post',
    response: config => {
      const items = data.projectList
      return {
        code: 1,
        msg: "获取成功",
        projectList: [{
          userName: "aaa",
          userId: "bbb",
          email: "YYY@JHU.EDU",
          lastTime: "2022-03-23 12:23",
          unread: 1
        }, {
          userName: "CCC",
          userId: "DDD",
          email: "QWE@JHU.EDU",
          lastTime: "2022-03-22 12:23",
          unread: 0
        }]
      }
    }
  },
  {
    url: '/vue-admin-template/message/messageRecord',
    type: 'post',
    response: config => {
      const items = data.messageList
      return {
        code: 1,
        msg: "获取成功",
        page: 1,
        size: 10,
        messageList: [{
            message: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            sendTime: "2022-03-23 12:23",
            isme: 0,
            avatar: "dragon"
          }, {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 1,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 0,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 1,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 0,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 1,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 0,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 1,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 0,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 1,
            avatar: "hmbb"
          },
          {
            message: "aaa",
            sendTime: "2022-03-23 12:23",
            isme: 0,
            avatar: "hmbb"
          },
        ]
      }
    }
  },
  {
    url: '/vue-admin-template/message/sendMessage',
    type: 'post',
    response: config => {
      const items = data
      return {
        code: 1,
        msg: "处理成功"
      }
    }
  },
  {
    url: '/vue-admin-template/message/sendnotice',
    type: 'post',
    response: config => {
      const items = data.sendnotice
      return {
        code: 1,
        msg: "处理成功"
      }
    }
  },
  {
    url: '/vue-admin-template/message/noticelist',
    type: 'post',
    response: config => {
      const items = data.noticelist
      return {
        "code": 1,
        "msg": "suc",
        "announcements": [{
          "id": "AAA",
          "name": "AAA",
          "val": "AAA",
          "releaseTime": "2022-04-06 12:33"
        }, {
          "id": "BBB",
          "name": "BBB",
          "val": "BBB",
          "releaseTime": "2022-04-08 12:33"
        }]
      }
    }
  },
  {
    url: '/vue-admin-template/message/noticedetail',
    type: 'post',
    response: config => {
      const items = data.noticedetails
      return {
        "code": 1,
        "msg": "suc",
        "announcement": {
          "id": "AAA",
          "name": "AAA",
          "val": "AAA",
          "releaseTime": "2022-04-06 12:33"
        }
      }
    }
  },
  {
    url: '/vue-admin-template/message/piechart',
    type: 'post',
    response: config => {
      const items = data.piechart
      return {
        "code": 1,
        "msg": "suc",
        "projectsLanguages": [{
          "name": "java",
          "percentage": 30.55
        }, {
          "name": "Python",
          "percentage": 69.45
        }]
      }
    }
  },
  {
    url: '/vue-admin-template/message/cylinderchart',
    type: 'post',
    response: config => {
      const items = data.cylinderchart
      return {
        "code": 1,
        "msg": "suc",
        "interestedFields": [{
            "name": "Books",
            "num": 130.55
          },
          {
            "name": "health",
            "num": 230.55
          },
          {
            "name": "Music",
            "num": 330.55
          },
          {
            "name": "Education",
            "num": 320.55
          },
          {
            "name": "Grocery",
            "num": 260.55
          },
          {
            "name": "Sports",
            "num": 120.55
          },
          {
            "name": "Travel",
            "num": 420.55
          },
          {
            "name": "Lifestyle",
            "num": 230.55
          },
          {
            "name": "Utilties",
            "num": 180.55
          },
          {
            "name": "Others",
            "num": 269.45
          }
        ]
      }
    }
  },
  {
    url: '/vue-admin-template/message/recommendation',
    type: 'post',
    response: config => {
      const items = data.userlist
      return {
        "code":1,
        "msg":"suc",
        "userlist":[{
          "userId":"aaa",
          "avatar":"dragon",
          "showVal":"Yuting Zhang，Grad，Computer Science",
          "email":"XXXX@JHU.EDU"
        },{
          "userId":"bbb",
          "avatar":"chicken",
          "showVal":"Akshay，Grad，Computer Science",
          "email":"YYY@JHU.EDU"
        }]
        }
    }
  },
  {
    url: '/vue-admin-template/message/saveword',
    type: 'post',
    response: config => {
      const items = data.saveword
      return {
        "code": 1,
        "msg": "处理成功"
      }
    }
  },
  {
    url: '/vue-admin-template/message/readingdata',
    type: 'post',
    response: config => {
      const items = data.readingdata
      return {
        "code":1,
        "msg":"获取成功",
        "sendTo":"YYY@JHU.EDU",
        "sendMessage":"HELLO…… best"
        }
    }
  },
]
