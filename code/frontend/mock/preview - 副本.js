const Mock = require('mockjs')

const data = Mock.mock({
    'list': {},
    "userlist": {},
    "saveList":{}
  }

)
module.exports = [{
    url: '/vue-admin-template/preview/list',
    type: 'post',
    response: config => {
      const items = data.list
      return {
        "code": 1,
        "msg": "suc",
        "projectList": [{
            "projectId": "aaa",
            "projectName": "bbb",
            "teamName": "aa",
            "teamLeader": "A@jhu.edu",
            "teamLeaderName": "AAA",
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu"
              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu"
              }
            ]
          },
          {
            "projectId": "BBB",
            "projectName": "CCC",
            "teamName": "CC",
            "teamLeader": "C@jhu.edu",
            "teamLeaderName": "C",
            "teamMemName": [{
                "name": "DD",
                "eml": "DD@jhu.edu"
              },
              {
                "name": "EE",
                "eml": "EE@jhu.edu"
              }
            ]
          },
          {
            "projectId": "aaa",
            "projectName": "bbb",
            "teamName": "aa",
            "teamLeader": "A@jhu.edu",
            "teamLeaderName": "AAA",
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu"
              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu"
              }
            ]
          },
          {
            "projectId": "BBB",
            "projectName": "CCC",
            "teamName": "CC",
            "teamLeader": "C@jhu.edu",
            "teamLeaderName": "C",
            "teamMemName": [{
                "name": "DD",
                "eml": "DD@jhu.edu"
              },
              {
                "name": "EE",
                "eml": "EE@jhu.edu"
              }
            ]
          }
        ]
      }
    }
  },
  {
    url: '/vue-admin-template/editpreview/list',
    type: 'post',
    response: config => {
      const items = data.userlist
      return {
        "code": 1,
        "msg": "suc",
        "criteriaList": [{
            "criteriaId": "aaa",
            "criteriaName": "Major",
            "criteriaNum": 33,
            "criteriaPption": "Similar"
          },
          {
            "criteriaId": "bbb",
            "criteriaName": "Grade",
            "criteriaNum": 33,
            "criteriaPption": "Similar"
          },
          {
            "criteriaId": "ccc",
            "criteriaName": "Leadership Interest",
            "criteriaNum": 33,
            "criteriaPption": "Different"
          },
          {
            "criteriaId": "ddd",
            "criteriaName": "Type of end product",
            "criteriaNum": 33,
            "criteriaPption": "Similar"
          },
          {
            "criteriaId": "eee",
            "criteriaName": "Related Experience",
            "criteriaNum": 33,
            "criteriaPption": "Similar"
          },
          {
            "criteriaId": "fff",
            "criteriaName": "Field of Interest",
            "criteriaNum": 33,
            "criteriaPption": "Similar"
          },
          {
            "criteriaId": "ggg",
            "criteriaName": "Programming Language",
            "criteriaNum": 59,
            "criteriaPption": "Different"
          }
        ]
      }
    }
  },
  {
    url: '/vue-admin-template/preview/save',
    type: 'post',
    response: config => {
      const items = data.saveList
      return {
        "code": 1,
        "msg": "提交成功"
      }
    }
  },
]
