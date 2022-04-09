const Mock = require('mockjs')

const data = Mock.mock({
    'list': {},
    'detail': {},
    "messageList":{},
    "sendMessage":{}
  }

)
module.exports = [
    {
        url: '/vue-admin-template/message/list',
        type: 'post',
        response: config => {
          const items = data.list
          return {
                code:1,
                msg:"获取成功",
                userlist:[{
                userId:"aaa",
                avatar:"dragon",
                showVal:"Yuting Zhang，Grad，Computer Science",
                email:"XXXX@JHU.EDU"
                },{
                userId:"bbb",
                avatar:"chicken",
                showVal:"Akshay，Grad，Computer Science",
                email:"YYY@JHU.EDU"
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
            code:1,
            msg:"查询成功",
            userDetails:{
              name:"SAN ZHANG",
              major:"COMPUTER SCIENCE",
              grade:"GRAD",
              skillLevel:[
                {skillName:"JAVA","level":"LOW"},
                {skillName:"C++","level":"HIGH"}
              ],
              leadInt:"HIGH",
              fieldInt:["XX","YY"],
              prod:["IOS","WEB"], 
              expe:"intern",
              mbti:"estj-T",
              email:"YYY@JHU.EDU"
            },
            userProject:{
              projectId:"aaa",
              projectName:"bbb"
            }
            }
        }
      },
      {
        url: '/vue-admin-template/message/messageList',
        type: 'post',
        response: config => {
          const items = data.projectList
          return{
            code:1,
            msg:"获取成功",
            projectList:[{
              userName:"aaa",
              userId:"bbb",
              email:"YYY@JHU.EDU",
              lastTime:"2022-03-23 12:23",
              unread:1
            },{
              userName:"CCC",
              userId:"DDD",
              email:"QWE@JHU.EDU",
              lastTime:"2022-03-22 12:23",
              unread:0
            }]
            }
        }
      },
      {
        url: '/vue-admin-template/message/messageRecord',
        type: 'post',
        response: config => {
          const items = data.messageList
          return{
            code:1,
            msg:"获取成功",
            page:1,
            size:10,
            messageList:[{
              message:"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
              sendTime:"2022-03-23 12:23",
              isme:0,
              avatar:"dragon"
            },{
             message:"aaa",
              sendTime:"2022-03-23 12:23",
              isme:1,
              avatar:"hmbb"
            },
            {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:0,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:1,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:0,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:1,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:0,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:1,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:0,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:1,
               avatar:"hmbb"
             },
             {
              message:"aaa",
               sendTime:"2022-03-23 12:23",
               isme:0,
               avatar:"hmbb"
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
          return{
            code:1,
            msg:"处理成功"
            }
        }
      }

]