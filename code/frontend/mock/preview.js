const Mock = require('mockjs')

const data = Mock.mock({
    'list': {},
    "userlist": {},
    "saveList": {}
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
            "groupNo": 1,
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu",
                "backgroundcolor": "#FEF6E0"

              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E8EBED"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              },
              {
                "name": "eee",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E7F6F8"
              }
            ]
          },
          {
            "groupNo": 2,
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu",
                "backgroundcolor": "#FEF6E0"

              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E8EBED"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              },
              {
                "name": "eee",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E7F6F8"
              }
            ]
          },
          {
            "groupNo": 3,
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu",
                "backgroundcolor": "#FEF6E0"

              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E8EBED"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              }
            ]
          },
          {
            "groupNo": 4,
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu",
                "backgroundcolor": "#FEF6E0"

              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E8EBED"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              },

            ]
          },
          {
            "groupNo": 5,
            "teamMemName": [{
                "name": "bbb",
                "eml": "BBB@jhu.edu",
                "backgroundcolor": "#FEF6E0"

              },
              {
                "name": "ccc",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#E8EBED"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              },
              {
                "name": "ddd",
                "eml": "CCC@jhu.edu",
                "backgroundcolor": "#F0ECF9"
              },

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
        "msg": "suc"
      }
    }
  },
]
