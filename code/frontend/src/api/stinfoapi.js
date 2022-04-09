import request from '@/utils/request'
// 注册用户
export function create_student_api(data) {
  return request({
    url: 'create_student_api',
    method: 'post',
    data
  })
}
// 填写用户信息
export function addstinfo_api(data) {
  return request({
    url: 'fill_profile_api',
    method: 'post',
    data
  })
}

export function getstinfo_api() {
  return request({
    url: 'getstinfo_api',
    method: 'get'
  })
}

export function updatestinfo_api(data) {
  return request({
    url: 'update_profile_api',
    method: 'post',
    data
  })
}

export function query_profile_api() {
  return request({
    url: 'query_profile_api',
    method: 'get'
  })
}