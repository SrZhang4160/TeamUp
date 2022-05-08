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

// 发送公告
export function sendnotice(data) {
  return request({
    url: 'annos_create_msg_api',
     // url: '/vue-admin-template/message/sendnotice',
    method: 'post',
    data
  })
}

// 公告列表
export function noticelist(data) {
  return request({
     url: 'annos_list_msg_api',
    //url: '/vue-admin-template/message/noticelist',
    method: 'post',
    data
  })
}
// 公告详情
export function noticedetail(data) {
  return request({
    url: 'annos_retrieve_msg_api',
    // url: '/vue-admin-template/message/noticedetail',
    method: 'post',
    data
  })
}
// echarts 饼图
export function piechart(data) {
  return request({
     url: 'project_lang_distribution_api',
    // url: '/vue-admin-template/message/piechart',
    method: 'post',
    data
  })
}
//柱状图
export function cylinderchart(data) {
  return request({
    url: 'student_interest_field_distribution_api',
    // url: '/vue-admin-template/message/cylinderchart',
    method: 'post',
    data
  })
}
// 本组人员
export function recommendation(data) {
  return request({
   url: 'retrieve_group_with_userID_page_api',
     // url: '/vue-admin-template/message/recommendation',
    method: 'post',
    data
  })
}

// saveword 定时保存
export function saveword(data) {
  return request({
    url: 'cache_message_api',
    // url: '/vue-admin-template/message/saveword',
    method: 'post',
    data
  })
}

// readingdata 读取保存数据
export function readingdata(data) {
  return request({
    url: 'retrieve_cache_message_api',
    // url: '/vue-admin-template/message/readingdata',
    method: 'post',
    data
  })
}
