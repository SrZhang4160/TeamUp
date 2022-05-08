import request from '@/utils/request'
// 注册用户
export function contact_edit(data) {
  return request({
    url: 'contact_edit_api',
    method: 'post',
    data
  })
}


export function contact_show() {
  return request({
    url: 'contact_show_api',
    method: 'post',
  })
}