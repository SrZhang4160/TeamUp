import request from '@/utils/request'

// 打开联系人列表
export function getList(data) {
  return request({
    url: 'find_teammate_api',
    // url: '/vue-admin-template/message/list',
    method: 'post',
    data
  })
}
// 查看联系人详情
export function getDetail(data) {
  return request({
    url: 'query_profile_others_api',
    // url: 'return_all_project_api',
    // url: '/vue-admin-template/message/detail',
    method: 'post',
    data
  })
}
// 聊天列表
export function getMessageList(data) {
  return request({
    url: 'retrieve_contact_api',
    // url: '/vue-admin-template/message/messageList',
    method: 'post',
    data
  })
}
// 聊天记录
export function getMessagerecord(data) {
  return request({
    url: 'retrieve_message_api',
    // url: '/vue-admin-template/message/messageRecord',
    method: 'post',
    data
  })
}
// 发送信息
export function getSendMessage(data) {
  return request({
    url: 'send_message_api',
    // url: '/vue-admin-template/message/sendMessage',
    method: 'post',
    data
  })
}
