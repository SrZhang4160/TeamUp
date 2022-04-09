const Mock = require('mockjs')

const data = Mock.mock({
    'list': {},
    'HaveTeamNumber': {

    },
    'noTeamNumber': {

    },
    'recommendList': {},
    'projectDetails': {},
    'erminateProject': {
      code: 1,
      msg: "处理成功"
    },
    'joinProject': {
      code: 1,
      msg: "处理成功"
    },
    'projectEdit': {},
    'saveEditProject': {
      code: 1,
      msg: '接口查询说明'
    }
  }

)

module.exports = [{
    // url: '/aa',
    url: '/vue-admin-template/project/list',
    type: 'post',
    response: config => {
      const items = data.list
      return {
        code: 1,
        msg: "获取成功",
        projectList: [{
            projectId: "aaa",
            projectName: "bbb",
            keywords: "CC",
            type: ["IOS", "Android"],
            skillWanted: "DDD"
          }, {
            projectId: "AAA",
            projectName: "BBB",
            keywords: "CCCC",
            type: ["Web applocation"],
            skillWanted: "DDD"
          },
          {
            projectId: "AAA",
            projectName: "BBB",
            keywords: "CCCC",
            type: ["Web applocation"],
            skillWanted: "DDD"
          },
          {
            projectId: "AAA",
            projectName: "BBB",
            keywords: "CCCC",
            type: ["Web applocation"],
            skillWanted: "DDD"
          },
          {
            projectId: "AAA",
            projectName: "BBB",
            keywords: "CCCC",
            type: ["Web applocation"],
            skillWanted: "DDD"
          },
          {
            projectId: "AAA",
            projectName: "BBB",
            keywords: "CCCC",
            type: ["Web applocation"],
            skillWanted: "DDD"
          }
        ]

      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/HaveTeamNumber',
    type: 'post',
    response: config => {
      const items = data.HaveTeamNumber
      return {
        code: 1,
        msg: "查询成功",
        numval: 33
      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/noTeamNumber',
    type: 'post',
    response: config => {
      const items = data.noTeamNumber
      return {
        code: 1,
        msg: "查询成功",
        numval: 22
      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/recommendList',
    type: 'post',
    response: config => {
      const items = data.recommendList
      return {
        code: 1,
        msg: "获取成功",
        projectList: [{
          projectId: "aaa",
          projectName: "bbb",
          keywords: "CC",
          type: ["IOS", "Android"],
          skillWanted: "DDD"
        }, {
          projectId: "AAA",
          projectName: "BBB",
          keywords: "CCCC",
          type: ["IOS", "Android"],
          skillWanted: "DDD"
        }, {
          projectId: "aaa",
          projectName: "bbb",
          keywords: "CC",
          type: ["IOS", "Android"],
          skillWanted: "DDD"
        }]
      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/projectDetails',
    type: 'post',
    response: config => {
      const items = data.projectDetails
      return {
        code: 1,
        msg: "获取成功",
        userRole: 1,
        project: {
          projectId: "aaa",
          projectName: "bbb",
          projectIntroduction: "CC",
          keywords: "CC",
          intendedLanguage: ["JAVA", "OTHER"],
          otherLanguage: "VUE",
          type: ["IOS"],
          skillWanted: "DDD",
          teamName: "aa",
          teamLeader: "AAA@jhu.edu",
          teamLeaderName: "AAA",
          teamMemName: [{
            name: "bbb",
            eml: "BBB@jhu.edu"
          }, {
            name: "ccc",
            eml: "CCC@jhu.edu"
          }],
          appliedList: [{
            name: "d",
            eml: "D@jhu.edu"
          }, {
            name: "e",
            eml: "E@jhu.edu"
          }]
        }
      }
    }
  },

  {
    // url: '/aa',
    url: '/vue-admin-template/project/erminateProject',
    type: 'post',
    response: config => {
      const items = data.erminateProject
      return {
        code: 1,
        msg: "处理成功"
      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/joinProject',
    type: 'post',
    response: config => {
      const items = data.joinProject
      return {
        code: 1,
        msg: "处理成功"
      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/projectEdit',
    type: 'post',
    response: config => {
      const items = data.projectEdit
      return {
        code: 1,
        msg: "获取成功",
        userRole: 1,
        project: {
          projectId: "aaa",
          projectName: "bbb",
          projectIntroduction: "CC",
          keywords: "CC",
          intendedLanguage: ["JAVA", "OTHER"],
          otherLanguage: "VUE",
          type: ["IOS"],
          skillWanted: "DDD",
          teamName: "aa",
          teamLeader: "AAA@jhu.edu",
          teamLeaderName: "AAA",
          teamMemName: [{
            name: "bbb",
            eml: "BBB@jhu.edu"
          }, {
            name: "ccc",
            eml: "CCC@jhu.edu"
          }],
          appliedList: [{
            name: "d",
            eml: "D@jhu.edu"
          }, {
            name: "e",
            eml: "E@jhu.edu"
          }]
        }
      }
    }
  },
  {
    // url: '/aa',
    url: '/vue-admin-template/project/saveEditProject',
    type: 'post',
    response: config => {
      const items = data.saveEditProject
      return {
        code: 1,
        msg: "处理成功"
      }
    }
  },

]
