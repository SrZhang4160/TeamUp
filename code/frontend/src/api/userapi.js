import request from '@/utils/request'
// 登录
export function login(data) {
  return request({
     url: 'login-test',
   // url: '/vue-admin-template/user/login',
    method: 'post',
    data
  })
}

// 获取用户信息 方法实现
export function getInfo(token) {
  return request({
    url: 'userinfo',
     //url: '/vue-admin-template/user/info',
    method: 'get',
    params: { token }
  })
}
// 退出
export function logout(token) {
  return request({
     url: 'logout-test',
    //url: '/vue-admin-template/user/logout',
    method: 'post',
    params: { token }
  })
}
