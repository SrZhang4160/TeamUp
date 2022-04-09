import request from '@/utils/request'

// 打开列表
export function getList(data) {
  return request({
    url: 'return_all_project_api',
    // url: '/vue-admin-template/project/list',
    method: 'post',
    data
  })
}
// 获取数字1
export function HaveTeamNumber() {
  return request({
    url: 'return_student_with_proj_num_api',
   // url: '/vue-admin-template/project/HaveTeamNumber',
    method: 'post'
  })
}
// 获取数字2
export function noTeamNumber() {
  return request({
    url: 'return_student_without_proj_num_api',
   //  url: '/vue-admin-template/project/noTeamNumber',
    method: 'post'
  })
}
// 推荐项目
export function recommendList() {
  return request({
    url: 'recommend_project_api',
    // url: '/vue-admin-template/project/recommendList',
    method: 'post'
  })
}
// 项目详情查看
export function projectDetails(data) {
  return request({
    url: 'project_page_api',
    // url: '/vue-admin-template/project/projectDetails',
    method: 'post',
    data
  })
}
// 项目JOIN
export function joinProject(data) {
  return request({
    url: 'apply_to_project_api',
    // url: '/vue-admin-template/project/joinProject',
    method: 'post',
    data
  })
}
// 项目leaveProject
export function leaveProject(data) {
  return request({
    url: 'project_page_exit_api',
    // url: '/XXXX',
    method: 'post',
    data
  })
}
// 项目解散
export function erminateProject(data) {
  return request({
    url: 'del_project_api',
    // url: '/vue-admin-template/project/erminateProject',
    method: 'post',
    data
  })
}
// 项目详情 编辑版
export function projectEdit(data) {
  return request({
    url: 'project_page_view_api',
    // url: '/vue-admin-template/project/projectEdit',
    method: 'post',
    data
  })
}
// 项目详情 编辑保存
export function saveEditProject(data) {
  return request({
    url: 'project_page_edit_api',
    // url: '/vue-admin-template/project/saveEditProject',
    method: 'post',
    data
  })
}
export function create_project_api(data) {
  // console.log("test cre22")
  return request({
    url: 'create_project_api',
    // url: '',
    method: 'post',
    data
  })
}
